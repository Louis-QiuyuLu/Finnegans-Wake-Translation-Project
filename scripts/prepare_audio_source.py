#!/usr/bin/env python3
"""Freeze speech queues for books II–IV from the canonical English witness."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.audio_source import prepare_queue, load_source_segments


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--books', nargs='+', choices=['II', 'III', 'IV'], default=['II', 'III', 'IV'])
    parser.add_argument('--max-words', type=int, default=600)
    parser.add_argument('--output', type=Path, default=ROOT / 'audio/source-queues')
    args = parser.parse_args()
    chapters = [json.loads(p.read_text(encoding='utf-8')) for p in (ROOT / 'manuscript/chapters').glob('*.json')]
    queues = [prepare_queue(chapters, book, args.max_words) for book in args.books]
    args.output.mkdir(parents=True, exist_ok=True)
    for queue in queues:
        path = args.output / (queue['book'] + '.json')
        path.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        segments = load_source_segments(path)
        print(json.dumps({'book': queue['book'], **queue['statistics'], 'verified_items': len(segments)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
