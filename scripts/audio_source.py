"""Prepare speech jobs from canonical English without Chinese placeholder segments."""
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from scripts import source_text

ROOT = Path(__file__).resolve().parents[1]
ROLES = ('main', 'left', 'right', 'footnotes')
ORDER = 'page: main, left margin, right margin, footnotes'


def page_tracks(chapter):
    source = chapter['source_text']
    if source_text.fingerprint(source['html']) != source.get('html_sha256'):
        raise ValueError('source HTML fingerprint changed: ' + chapter['id'])
    tree = ET.fromstring('<div>' + source['html'] + '</div>')
    page = None
    seen = []
    tracks = {}
    figures = []

    def append(text, role):
        if not text:
            return
        if page is None:
            if text.strip():
                raise ValueError('source text before first page')
            return
        tracks.setdefault((page, role), []).append(text)

    def visit(node, inherited='main'):
        nonlocal page
        classes = set(node.get('class', '').split())
        if classes & {'pagenumber', 'chap_pagenumber'}:
            page = int(node.get('id').rsplit('-', 1)[-1])
            seen.append(page)
            append(node.tail, inherited)
            return
        role = ('footnotes' if 'footnote' in classes else 'left' if 'sl' in classes
                else 'right' if 'sr' in classes else inherited)
        # Omit inline navigation numbers; retain each footnote's own number.
        if 'fnanchor' in classes and role != 'footnotes':
            append(node.tail, inherited)
            return
        if node.tag == 'img':
            figures.append({'chapter': chapter['id'], 'page': page,
                            'asset': source_text.asset_name(node.get('src', '')),
                            'alt': node.get('alt', ''), 'spoken': False})
        elif node.tag == 'br':
            append(' ', role)
        else:
            append(node.text, role)
            for child in node:
                visit(child, role)
            if node.tag in {'p', 'div', 'aside', 'tr', 'td', 'th', 'h1'}:
                append('\n', role)
        append(node.tail, inherited)

    visit(tree)
    if seen != source['pages'] or seen != list(range(chapter['pages'][0], chapter['pages'][1] + 1)):
        raise ValueError('source pages missing or reordered: ' + chapter['id'])
    result = []
    for number in seen:
        for role in ROLES:
            text = ' '.join(''.join(tracks.get((number, role), [])).split())
            if text:
                result.append({'page': number, 'role': role, 'text': text})
    return result, figures


def prepare_queue(chapters, book, max_words=600):
    if book not in {'II', 'III', 'IV'} or type(max_words) is not int or not 1 <= max_words <= 2000:
        raise ValueError('invalid source book or chunk size')
    selected = sorted((c for c in chapters if c['book'] == book), key=lambda c: c['pages'][0])
    if not selected:
        raise ValueError('no source chapters for book ' + book)
    sources, items, figures = {}, [], []
    page_count = word_count = 0
    for chapter in selected:
        source = chapter['source_text']
        sources[chapter['id']] = {'source_id': source['source_id'],
                                 'html_sha256': source['html_sha256'],
                                 'pages': source['pages']}
        parts, images = page_tracks(chapter)
        figures.extend(images)
        page_count += len(source['pages'])
        for part in parts:
            words = list(re.finditer(r'\S+', part['text']))
            word_count += len(words)
            for offset in range(0, len(words), max_words):
                first, last = words[offset], words[min(offset + max_words, len(words)) - 1]
                original = part['text'][first.start():last.end()]
                cid = chapter['id'].lower().replace('.', '')
                identifier = f'fw-source-{cid}-{part["page"]:03d}-{part["role"]}-{offset // max_words + 1:03d}'
                items.append({'id': identifier, 'chapter': chapter['id'], 'page': part['page'],
                              'role': part['role'], 'start': first.start(), 'end': last.end(),
                              'word_count': min(max_words, len(words) - offset),
                              'original_sha256': source_text.fingerprint(original)})
    return {'schema_version': 1, 'kind': 'full_english_audio', 'book': book,
            'reading_order': ORDER, 'max_words': max_words, 'sources': sources,
            'items': items, 'non_spoken_figures': figures,
            'statistics': {'chapters': len(selected), 'pages': page_count,
                           'items': len(items), 'words': word_count}}


def load_source_segments(queue_path, root=ROOT):
    queue = json.loads(Path(queue_path).read_text(encoding='utf-8'))
    chapters = [json.loads(p.read_text(encoding='utf-8'))
                for p in (Path(root) / 'manuscript/chapters').glob('*.json')]
    # Rebuild metadata from current canonical text. Missing/reordered jobs,
    # changed offsets and a dropped chapter cannot masquerade as full coverage.
    expected = prepare_queue(chapters, queue.get('book'), queue.get('max_words'))
    if queue != expected:
        raise ValueError('source queue or canonical source changed; prepare a new queue')
    by_id = {c['id']: c for c in chapters}
    tracks = {}
    for cid in queue['sources']:
        parts, _ = page_tracks(by_id[cid])
        tracks[cid] = {(p['page'], p['role']): p['text'] for p in parts}
    result = []
    for item in queue['items']:
        text = tracks[item['chapter']][(item['page'], item['role'])]
        original = text[item['start']:item['end']]
        result.append({'id': item['id'], 'chapter': item['chapter'],
                       'locator': f'FW {item["page"]:03d} · {item["role"]}',
                       'original': original,
                       'source_binding': {'kind': queue['kind'], 'book': queue['book'],
                                          **item, **queue['sources'][item['chapter']]}})
    return result
