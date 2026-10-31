#!/usr/bin/env python3
"""Capture retrieval facts and compare a bounded external text witness. Stdlib only.

An anchor match proves retrieval of that string, not source identity, reading,
independence, interpretation, or permission to publish. Keep those judgments in
the research ledger. Full response bodies are hashed in memory, never saved.
"""
import argparse
from datetime import datetime, timezone
import difflib
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen, HTTPRedirectHandler, build_opener


def digest(data):
    return hashlib.sha256(data).hexdigest()


def normalize(text):
    return ' '.join(text.split())


class VisibleText(HTMLParser):
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.frames, self.title_parts = [], [], []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        hidden = (bool(self.frames and self.frames[-1][1])
                  or tag in ('script', 'style', 'template')
                  or any(key == 'hidden' for key, _ in attrs))
        if tag not in self.VOID:
            self.frames.append((tag, hidden))
        if tag == 'title':
            self.in_title = True

    def handle_endtag(self, tag):
        for i in range(len(self.frames) - 1, -1, -1):
            if self.frames[i][0] == tag:
                del self.frames[i:]
                break
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if not self.frames or not self.frames[-1][1]:
            self.parts.append(data)
            if self.in_title:
                self.title_parts.append(data)


def capture(*, body, status, requested_url, effective_url, content_type, needles):
    """Return retrieval facts; ok requires all anchors in a successful text body."""
    r = dict(schema_version=1, captured_at=datetime.now(timezone.utc).isoformat(),
             requested_url=requested_url, effective_url=effective_url,
             http_status=status, content_type=content_type, bytes=len(body),
             sha256=digest(body), title=None, anchors=[], errors=[])
    if not 200 <= status < 300:
        r['errors'].append('http_not_successful')
    media_type = content_type.split(';', 1)[0].strip().lower()
    if body.startswith(b'%PDF-') or media_type not in ('text/html', 'application/xhtml+xml', 'text/plain'):
        r['errors'].append('not_supported_text; inspect PDF/image pages separately')
        r['ok'] = False
        return r
    charset = 'utf-8'
    for part in content_type.split(';')[1:]:
        if part.strip().lower().startswith('charset='):
            charset = part.split('=', 1)[1].strip(' "\'')
    try:
        text = body.decode(charset, errors='strict')
    except (UnicodeError, LookupError):
        r['errors'].append('decode_failed; determine encoding explicitly')
        r['ok'] = False
        return r
    if media_type != 'text/plain':
        parser = VisibleText(); parser.feed(text)
        text = ' '.join(parser.parts)
        r['title'] = normalize(' '.join(parser.title_parts))[:500] or None
    text = normalize(text)
    r['normalized_text_sha256'] = digest(text.encode())
    for needle in needles:
        needle = normalize(needle)
        count = text.count(needle) if needle else 0
        r['anchors'].append(dict(text=needle, count=count))
        if not count:
            r['errors'].append('anchor_missing: ' + needle)
    r['ok'] = bool(needles) and not r['errors']
    r['limit'] = 'Response text retrieval only; browser CSS/JS visibility, identity, edition, page and reading need separate inspection.'
    return r


def select_span(text, start, end):
    """Scope by unique verbatim anchors; never silently choose another occurrence."""
    text, start, end = normalize(text), normalize(start), normalize(end)
    if not start or not end or text.count(start) != 1 or text.count(end) != 1:
        raise ValueError('scope anchors must each occur exactly once')
    a, b = text.index(start), text.index(end) + len(end)
    if b < a + len(start):
        raise ValueError('scope end precedes start')
    return text[a:b]


def compare(candidate, witness):
    """Compare text only. A false provenance declaration cannot be detected here."""
    required = ('text', 'source_id', 'url', 'edition', 'locator', 'capture_method')
    errors = [f'missing_witness_{k}' for k in required if not witness.get(k)]
    if witness.get('basis') != 'external_witness':
        errors.append('witness_must_come_from_external_source')
    if witness.get('capture_method') not in (
            'web_tool_cached_transcription', 'downloaded_transcription', 'manual_scan_transcription'):
        errors.append('unsupported_or_unverified_capture_method')
    if errors:
        return dict(ok=False, verdict='provenance_incomplete', errors=errors)
    a, b = normalize(candidate), normalize(witness['text'])
    ok = a == b
    diff = '\n'.join(difflib.unified_diff(b.split(), a.split(),
                    fromfile='external-witness', tofile='candidate', lineterm=''))
    return dict(schema_version=1, ok=ok, verdict='text_equal' if ok else 'text_mismatch',
                locator=witness['locator'], source_id=witness['source_id'],
                witness_sha256=digest(b.encode()), candidate_sha256=digest(a.encode()),
                normalization='Unicode whitespace only; punctuation and accents retained',
                diff=diff, errors=[],
                limit='Bounded text comparison only; provenance and non-text elements require human inspection.')


class CheckedRedirect(HTTPRedirectHandler):
    def __init__(self, allow_http):
        self.allow_http = allow_http

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_url(newurl, self.allow_http)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def check_url(url, allow_http):
    u = urlsplit(url)
    if u.scheme not in ('https', 'http') or not u.netloc or u.username or u.password:
        raise ValueError('use a public HTTP(S) URL without credentials')
    if u.scheme == 'http' and not allow_http:
        raise ValueError('HTTP needs explicit --allow-http; TLS is never disabled')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    c = sub.add_parser('capture', help='record HTTP and string retrieval facts, not reading')
    c.add_argument('--url', required=True)
    c.add_argument('--needle', action='append', required=True)
    c.add_argument('--allow-http', action='store_true')
    c.add_argument('--timeout', type=int, default=25)
    c.add_argument('--out', type=Path, required=True)
    v = sub.add_parser('compare', help='compare a candidate span with a provenance-bearing witness JSON')
    v.add_argument('--candidate', type=Path, required=True)
    v.add_argument('--segment-id')
    v.add_argument('--witness', type=Path, required=True)
    v.add_argument('--start', required=True)
    v.add_argument('--end', required=True)
    v.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == 'capture':
            if sum(len(n) for n in args.needle) > 500:
                raise ValueError('keep anchor strings brief; max 500 characters combined')
            check_url(args.url, args.allow_http)
            req = Request(args.url, headers={'User-Agent': 'FinnegansWakeResearch/1.0'})
            opener = build_opener(CheckedRedirect(args.allow_http))
            try:
                response = opener.open(req, timeout=args.timeout)
            except HTTPError as e:
                response = e
            with response:
                body = response.read(5 * 1024 * 1024 + 1)
                if len(body) > 5 * 1024 * 1024:
                    raise ValueError('response exceeds 5 MiB; capture a bounded text resource')
                result = capture(body=body, status=response.code,
                    requested_url=args.url, effective_url=response.geturl(),
                    content_type=response.headers.get('Content-Type', ''), needles=args.needle)
        else:
            if args.candidate.resolve() == args.witness.resolve():
                raise ValueError('candidate file cannot also serve as external witness')
            data = json.loads(args.candidate.read_text())
            if args.segment_id:
                data = next(s for s in data['segments'] if s['id'] == args.segment_id)
            original = select_span(data['original'], args.start, args.end)
            witness = json.loads(args.witness.read_text())
            result = compare(original, witness)
            result['candidate_file'] = str(args.candidate)
            result['candidate_file_sha256'] = digest(args.candidate.read_bytes())
            result['witness_file_sha256'] = digest(args.witness.read_bytes())
            result['scope'] = dict(start=args.start, end=args.end, segment_id=args.segment_id)
    except (ValueError, OSError, URLError, KeyError, StopIteration) as e:
        result = dict(ok=False, errors=[f'{type(e).__name__}: {e}'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(('PASS' if result['ok'] else 'FAIL') + ': ' + str(args.out))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
