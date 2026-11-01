"""Import the existing Faded Page witness without inventing Chinese segments.

Only the body between printed page markers is imported. Markup is restricted
to book typography; scripts, external resources and event handlers are errors.
"""
import hashlib
from html import escape
from html.parser import HTMLParser
from pathlib import PurePosixPath
import re
import xml.etree.ElementTree as ET


PAGE = re.compile(r'<(?:div|span)\b[^>]*class=[\'\"][^\'\"]*pagenumber[^\'\"]*[\'\"][^>]*>\s*----- (\d+) -----\s*</(?:div|span)>')
TAGS = {'p', 'div', 'span', 'br', 'aside', 'a', 'img', 'table', 'tbody',
        'tr', 'td', 'th', 'caption', 'b', 'i', 'em', 'strong', 'sub', 'sup', 'hr', 'h1'}
VOID = {'br', 'img', 'hr'}
BLOCK = {'p', 'div', 'aside', 'table', 'h1', 'hr'}
STYLE = {'margin-top', 'margin-bottom', 'font-size', 'text-align',
         'vertical-align', 'width', 'font-family'}


def fingerprint(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, value):
        self.parts.append(value)


def text_content(html):
    parser = Text()
    parser.feed(html)
    return ''.join(parser.parts)


def text_fingerprint(html):
    return fingerprint(''.join(text_content(html).split()))


def asset_name(src):
    path = PurePosixPath(src)
    if (len(path.parts) != 2 or path.parts[0] != 'images'
            or not re.fullmatch(r'[A-Za-z0-9_-]+\.(?:jpg|png)', path.name)):
        raise ValueError('source image must be a local images/name.jpg or .png')
    return path.name


class Witness(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = ET.Element('div')
        self.stack = [self.root]

    def close_to(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                self.stack = self.stack[:i]
                return

    def handle_starttag(self, tag, pairs):
        if tag not in TAGS:
            raise ValueError('unsupported source tag: ' + tag)
        # Faded Page contains omitted paragraph end tags. Close them using
        # HTML block rules before serializing well-formed XHTML.
        if tag in BLOCK:
            self.close_to('p')
        if tag == 'tr':
            self.close_to('tr')
        if tag in {'td', 'th'}:
            self.close_to('td')
            self.close_to('th')
        attrs = {}
        for key, value in pairs:
            if key not in {'class', 'id', 'name', 'href', 'src', 'alt', 'style', 'width', 'height'}:
                raise ValueError('unsupported source attribute: ' + key)
            value = value or ''
            if key == 'name':
                if not any(k == 'id' for k, _ in pairs):
                    attrs['id'] = value if value.startswith('source-') else 'source-' + value
            elif key == 'id':
                if not re.fullmatch(r'[A-Za-z0-9_-]+', value):
                    raise ValueError('invalid source anchor')
                attrs[key] = value if value.startswith('source-') else 'source-' + value
            elif key == 'href':
                if not re.fullmatch(r'#[A-Za-z0-9_-]+', value):
                    raise ValueError('source links must be local fragment anchors')
                attrs[key] = value if value.startswith('#source-') else '#source-' + value[1:]
            elif key == 'src':
                asset_name(value)
                attrs[key] = value
            elif key in {'width', 'height'}:
                if not value.isdigit() or not 0 < int(value) <= 2000:
                    raise ValueError('invalid source image dimension')
                attrs[key] = value
            elif key == 'style':
                declarations = []
                for declaration in value.split(';'):
                    if not declaration.strip():
                        continue
                    prop, sep, val = declaration.partition(':')
                    prop, val = prop.strip(), val.strip()
                    if not sep or prop not in STYLE or not re.fullmatch(r'[A-Za-z0-9. %_-]+', val):
                        raise ValueError('unsupported source style')
                    declarations.append(prop + ':' + val)
                if declarations:
                    attrs[key] = ';'.join(declarations)
            elif key == 'class':
                if not re.fullmatch(r'[A-Za-z0-9_ -]*', value):
                    raise ValueError('invalid source class')
                attrs[key] = value
            else:
                attrs[key] = value
        if tag == 'img' and ('src' not in attrs or 'alt' not in attrs):
            raise ValueError('source image needs src and alt')
        element = ET.SubElement(self.stack[-1], tag, attrs)
        if tag not in VOID:
            self.stack.append(element)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag not in TAGS:
            raise ValueError('unsupported source closing tag: ' + tag)
        if tag not in VOID:
            self.close_to(tag)

    def handle_data(self, value):
        node = self.stack[-1]
        if len(node):
            node[-1].tail = (node[-1].tail or '') + value
        else:
            node.text = (node.text or '') + value


def sanitize_fragment(fragment):
    parser = Witness()
    parser.feed(fragment)
    parser.close()
    for node in parser.root.iter():
        if 'pagenumber' in node.get('class', ''):
            match = re.fullmatch(r'\s*----- (\d+) -----\s*', ''.join(node.itertext()))
            if not match:
                raise ValueError('malformed source page marker')
            node.set('id', 'source-page-' + match[1].zfill(3))
    html = escape(parser.root.text or '') + ''.join(ET.tostring(n, encoding='unicode') for n in parser.root)
    if text_fingerprint(fragment) != text_fingerprint(html):
        raise ValueError('source text changed during HTML normalization')
    return html


def extract_chapters(html, chapters, source_id='joyce-fp', imported='2026-11-01'):
    markers = list(PAGE.finditer(html))
    positions = {int(m[1]): m for m in markers}
    if len(positions) != len(markers):
        raise ValueError('duplicate source page marker')
    result = {}
    for chapter in chapters:
        first, last = chapter['pages']
        expected = list(range(first, last + 1))
        missing = [p for p in expected if p not in positions]
        if missing:
            raise ValueError('missing source pages: ' + ', '.join(map(str, missing)))
        next_marker = next((m for m in markers if int(m[1]) > last), None)
        end = next_marker.start() if next_marker else html.index('</body>')
        raw = html[positions[first].start():end]
        fragment = sanitize_fragment(raw)
        tree = ET.fromstring('<div>' + fragment + '</div>')
        assets = sorted({asset_name(img.get('src', '')) for img in tree.iter('img')})
        result[chapter['id']] = {'status': 'imported', 'source_id': source_id,
            'pages': expected, 'imported': imported, 'html': fragment,
            'html_sha256': fingerprint(fragment), 'text_sha256': text_fingerprint(fragment),
            'assets': assets}
    return result


def validate_source(source, chapter):
    errors = []
    try:
        if source.get('status') != 'imported':
            errors.append('status must be imported')
        if source.get('pages') != list(range(chapter['pages'][0], chapter['pages'][1] + 1)):
            errors.append('page coverage does not match chapter')
        fragment = source.get('html', '')
        if not isinstance(fragment, str) or not fragment.strip():
            return errors + ['empty source HTML']
        sanitize_fragment(fragment)
        tree = ET.fromstring('<div>' + fragment + '</div>')
        if fingerprint(fragment) != source.get('html_sha256') or text_fingerprint(fragment) != source.get('text_sha256'):
            errors.append('source hash mismatch')
        ids = [n.get('id') for n in tree.iter() if n.get('id')]
        if len(ids) != len(set(ids)):
            errors.append('duplicate source anchor')
        pages = [int(i.removeprefix('source-page-')) for i in ids if i.startswith('source-page-')]
        if pages != source.get('pages'):
            errors.append('source page anchors incomplete or unordered')
        if any(n.get('href', '')[1:] not in ids for n in tree.iter('a') if n.get('href')):
            errors.append('unresolved source footnote link')
        assets = sorted({asset_name(n.get('src', '')) for n in tree.iter('img')})
        if source.get('assets') != assets:
            errors.append('source assets disagree with HTML')
    except (ValueError, TypeError, ET.ParseError) as exc:
        errors.append(str(exc))
    return errors


def rendered_html(source, asset_prefix):
    tree = ET.fromstring('<div>' + source['html'] + '</div>')
    for image in tree.iter('img'):
        image.set('src', asset_prefix + asset_name(image.get('src', '')))
    return escape(tree.text or '') + ''.join(ET.tostring(n, encoding='unicode') for n in tree)


def markdown(source):
    tree = ET.fromstring('<div>' + source['html'] + '</div>')

    def visit(node):
        if 'pagenumber' in node.get('class', ''):
            page = int(node.get('id').rsplit('-', 1)[1])
            return f'\n\n## FW {page:03d} {{#source-page-{page:03d}}}\n\n' + (node.tail or '')
        if node.tag == 'img':
            alt = node.get('alt', '').replace(']', '\\]')
            return '![' + alt + '](../manuscript/source-assets/' + asset_name(node.get('src', '')) + ')' + (node.tail or '')
        if node.tag == 'br':
            return '\n' + (node.tail or '')
        value = (node.text or '') + ''.join(visit(n) for n in node)
        if node.tag in {'p', 'div', 'aside', 'tr', 'table'}:
            value += '\n\n'
        return value + (node.tail or '')

    return re.sub(r'\n{3,}', '\n\n', visit(tree)).strip() + '\n'
