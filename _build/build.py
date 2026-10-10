#!/usr/bin/env python3
"""Build the generated guide pages from _build/pages/*.py and _build/data/*.json.

    python3 _build/build.py           write the pages
    python3 _build/build.py --check   fail if any committed page differs from a fresh build
"""
import difflib
import importlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.dirname(ROOT)
sys.path.insert(0, ROOT)

import lib  # noqa: E402


def main():
    check = '--check' in sys.argv
    data = {'vans': lib.load('vans.json')['vans'], 'zones': lib.load('zones.json')}
    stale = []
    for name in sorted(os.listdir(os.path.join(ROOT, 'pages'))):
        if not name.endswith('.py') or name.startswith('_'):
            continue
        mod = importlib.import_module('pages.' + name[:-3])
        slug, html = mod.build(data)
        path = os.path.join(SITE_ROOT, slug, 'index.html')
        old = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
        if check:
            if old != html:
                stale.append(slug)
                diff = difflib.unified_diff(old.splitlines(), html.splitlines(), f'{slug} (committed)', f'{slug} (built)', lineterm='', n=0)
                print('\n'.join(list(diff)[:20]))
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(('updated ' if old != html else 'unchanged ') + slug)
    if check:
        if stale:
            print('Out of date: ' + ', '.join(stale) + '. Run python3 _build/build.py')
            sys.exit(1)
        print('All generated pages match a fresh build.')


if __name__ == '__main__':
    main()
