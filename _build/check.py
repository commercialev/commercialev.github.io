#!/usr/bin/env python3
"""Site-wide checks for every page, generated or hand-written.

    python3 _build/check.py

Checks: JSON-LD parses; internal links, anchors and assets exist; citations
match the sources list and are numbered in order; tables are wrapped; every
page uses the current stylesheet version and the same navigation; every
indexable page is in sitemap.xml; titles are 60 characters or fewer; generated
pages match a fresh build.
"""
import glob
import html
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.dirname(ROOT)
sys.path.insert(0, ROOT)
import lib  # noqa: E402

os.chdir(SITE_ROOT)
pages = ['index.html', '404.html'] + sorted(p for p in glob.glob('*/index.html') if not p.startswith('_'))
ids = {p: set(re.findall(r'id="([^"]+)"', open(p, encoding='utf-8').read())) for p in pages}
sitemap = open('sitemap.xml', encoding='utf-8').read()
NOT_INDEXED = {'404.html', 'privacy/index.html'}
problems = []


def target(url):
    url = url.split('#')[0].split('?')[0]
    if url.startswith(('/img/', '/css/', '/favicon')):
        return url[1:]
    return 'index.html' if url == '/' else url.strip('/') + '/index.html'


expected_nav = [(h, l.replace('&amp;', '&')) for h, l in lib.NAV]
for p in pages:
    s = open(p, encoding='utf-8').read()
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            json.loads(block)
        except ValueError as e:
            problems.append(f'{p}: JSON-LD does not parse ({e})')
    for ref in re.findall(r'(?:href|src|srcset)="([^"]+)"', s):
        if ref.startswith('#'):
            if ref[1:] not in ids[p]:
                problems.append(f'{p}: missing anchor {ref}')
        elif ref.startswith('/') and not ref.startswith('//'):
            t = target(ref)
            if not os.path.exists(t):
                problems.append(f'{p}: broken link {ref}')
            elif '#' in ref and ref.split('#')[1] not in ids.get(t, set()):
                problems.append(f'{p}: missing anchor {ref}')
    cited = set(re.findall(r'href="#s(\d+)"', s))
    listed = re.findall(r'<li id="s(\d+)"', s)
    if listed and cited != set(listed):
        problems.append(f'{p}: citations and sources differ {sorted(cited ^ set(listed))}')
    if listed and [int(x) for x in listed] != list(range(1, len(listed) + 1)):
        problems.append(f'{p}: sources not numbered 1..n')
    if s.count('<table') != s.count('<div class="table-wrap"><table'):
        problems.append(f'{p}: table without table-wrap')
    if f'/css/site.css?v={lib.CSS_VERSION}"' not in s:
        problems.append(f'{p}: stylesheet version is not v={lib.CSS_VERSION}')
    nav = re.search(r'<nav class="topnav".*?</nav>', s, re.S)
    if nav:
        found = [(h, html.unescape(l)) for h, l in re.findall(r'<a href="([^"]+)"[^>]*>([^<]+)</a>', nav.group(0))]
        if found != expected_nav:
            problems.append(f'{p}: navigation differs from lib.NAV')
    title = html.unescape(re.search(r'<title>(.*?)</title>', s).group(1))
    if len(title) > 60:
        problems.append(f'{p}: title is {len(title)} characters')
    if p not in NOT_INDEXED:
        url = lib.SITE + '/' + ('' if p == 'index.html' else p[:-len('index.html')])
        if f'<loc>{url}</loc>' not in sitemap:
            problems.append(f'{p}: not in sitemap.xml')

build = subprocess.run([sys.executable, os.path.join(ROOT, 'build.py'), '--check'], capture_output=True, text=True)
if build.returncode:
    problems.append('generated pages are out of date:\n' + build.stdout)

if problems:
    print('\n'.join(problems))
    sys.exit(1)
print(f'{len(pages)} pages checked, no problems.')
