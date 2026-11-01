"""Import the checked Faded Page HTML ZIP, without changing translated segments.

The download stays outside the repository. No network or translation is used.
"""
import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import source_text


def sha(value):
    return hashlib.sha256(value).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path, help='Faded Page 20180126-h.zip, outside repository')
    parser.add_argument('--date', default=date.today().isoformat(), help='Actual import date, YYYY-MM-DD')
    parser.add_argument('--write', action='store_true', help='Write validated chapter source_text and images')
    parser.add_argument('--report', type=Path, help='Write a JSON provenance report')
    args = parser.parse_args()
    date.fromisoformat(args.date)
    paths = sorted((ROOT / 'manuscript/chapters').glob('*.json'))
    chapters = [json.loads(p.read_text(encoding='utf-8')) for p in paths]
    archive = args.archive.read_bytes()
    with zipfile.ZipFile(args.archive) as book:
        # Read only the known book member and referenced images, never extractall.
        raw = book.read('20180126.html')
        html = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')
        imported = source_text.extract_chapters(html, chapters, imported=args.date)
        names = sorted({name for item in imported.values() for name in item['assets']})
        assets = {name: book.read('images/' + name) for name in names}
    # Validate every chapter before writing any manuscript.
    for chapter in chapters:
        errors = source_text.validate_source(imported[chapter['id']], chapter)
        if errors:
            raise ValueError(chapter['id'] + ': ' + '; '.join(errors))
    coverage = []
    for chapter in sorted(chapters, key=lambda c: c['pages'][0]):
        item = imported[chapter['id']]
        tree = ET.fromstring('<div>' + item['html'] + '</div>')
        coverage.append({
            'chapter': chapter['id'], 'pages': item['pages'],
            'page_count': len(item['pages']), 'html_sha256': item['html_sha256'],
            'text_sha256': item['text_sha256'], 'assets': item['assets'],
            'image_occurrences': len(list(tree.iter('img'))),
            'author_footnotes': sum(n.get('class') == 'footnote' for n in tree.iter()),
            'sidenotes': sum(n.get('class') in {'sl', 'sr'} for n in tree.iter()),
        })
    report = {
        'date': args.date, 'source_id': 'joyce-fp',
        'edition': 'Viking Press, 1958, eighth printing, incorporating author corrections',
        'catalog_url': 'https://www.fadedpage.com/showbook.php?pid=20180126',
        'download_url': 'https://www.fadedpage.com/link.php?file=20180126-h.zip',
        'download_note': 'Normal book-page session and Referer required; an HTTP 200 landing page is not the book.',
        'archive_bytes': len(archive), 'archive_sha256': sha(archive),
        'html_member': '20180126.html', 'html_bytes': len(raw), 'html_sha256': sha(raw),
        'method': 'Cut at printed page markers; normalize HTML to restricted XHTML; compare Unicode text after removing whitespace. Preserve original image bytes, local anchors, author footnotes and sidenotes.',
        'limits': 'Mechanical text and page coverage checks, not full manual collation, semantic review or Chinese translation. Page markers do not establish new line coordinates. Existing translated segments and checkpoints are unchanged.',
        'chapters': coverage, 'chapter_count': len(coverage),
        'body_page_count': sum(c['page_count'] for c in coverage),
        'assets': [{'file': name, 'bytes': len(value), 'sha256': sha(value)} for name, value in assets.items()],
    }
    if args.write:
        asset_dir = ROOT / 'manuscript/source-assets'
        asset_dir.mkdir(exist_ok=True)
        for name, value in assets.items():
            (asset_dir / name).write_bytes(value)
        for path, chapter in zip(paths, chapters):
            chapter['source_text'] = imported[chapter['id']]
            path.write_text(json.dumps(chapter, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'write': args.write, 'chapters': len(coverage),
                      'pages': report['body_page_count'], 'assets': len(assets)}))


if __name__ == '__main__':
    main()
