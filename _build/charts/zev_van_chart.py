"""Draw the 'electric van sales vs the ZEV mandate target' chart.

Writes img/zev-van-sales-vs-target.svg (published, 800x480) and a taller
mobile layout to _build/charts/out/zev-van-sales-vs-target-mobile.svg. Then
render both to PNG with:  node _build/charts/render.js

Update SALES each month when SMMT publishes van registrations, and the
alt text, figcaption and figures on /commercial-electric-vehicles-uk/.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Battery-electric share of new UK van sales (SMMT), with a note for a part year.
SALES = {2024: ('6.3', None), 2025: ('9.5', None), 2026: ('11.0', 'Jan–Oct')}
TARGET = {2024: 10, 2025: 16, 2026: 24, 2027: 34, 2028: 46, 2029: 58, 2030: 70}
OPTIONS_2030 = [60, 50, 40]  # 2030 van target options in the 2026 review
SOURCES = 'Sources: SMMT (via NFDA, Motor Transport, AM Online); GOV.UK. Chart: CommercialEVs.co.uk, CC BY 4.0'

BG, GRID, AXIS, INK, SOFT, FAINT = '#0c1512', '#22302b', '#9aa9a3', '#f2f5f3', '#c9d3cf', '#7d8c86'
GREEN, TGT, AMBER = '#22c55e', '#3b4b45', '#f5b942'
FONT = "Inter, system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif"


def describe():
    parts = []
    for y, (pct, note) in SALES.items():
        when = 'from January to October 2026' if note else f'in {y}'
        lead = f'{pct}% of new UK van sales {when}' if not parts else f'{pct}% {when}'
        parts.append(f'{lead} against {"a " if not parts else ""}{TARGET[y]}%{" target" if not parts else ""}')
    later = [y for y in TARGET if y not in SALES]
    rises = ', '.join(f'{TARGET[y]}% in {y}' for y in later[:-1]) + f' and {TARGET[later[-1]]}% in {later[-1]}'
    opts = ', '.join(f'{o}%' for o in OPTIONS_2030[:-1]) + f' or {OPTIONS_2030[-1]}%'
    return (f'Battery-electric vans were {", ".join(parts[:-1])}, and {parts[-1]}. '
            f'The van target rises to {rises}. The 2026 review proposes {opts} for 2030, '
            'or keeping 70% with longer flexibilities.')


def f1(x):
    return f'{x:.1f}'


def desktop():
    left, right, base, scale = 64, 704, 372.0, 2.6
    years = list(TARGET)
    slot = (right - left) / len(years)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="800" height="480" role="img" aria-labelledby="t d">',
         '<title id="t">Electric van sales against the ZEV mandate target, 2024 to 2030</title>',
         f'<desc id="d">{describe()}</desc>',
         f'<rect width="800" height="480" fill="{BG}"/>',
         f'<g font-family="{FONT}">',
         f'<text x="32" y="44" font-size="22" font-weight="700" fill="{INK}">Electric van sales vs the ZEV mandate target</text>',
         f'<text x="32" y="72" font-size="14" fill="{AXIS}">Battery-electric share of new UK van sales (SMMT) against the yearly van target</text>']
    for p in (0, 25, 50, 75, 100):
        y = base - p * scale
        o.append(f'<line x1="{left}" y1="{f1(y)}" x2="{right}" y2="{f1(y)}" stroke="{GRID}" stroke-width="1"/>')
        o.append(f'<text x="54" y="{f1(y + 4)}" font-size="12" fill="{AXIS}" text-anchor="end">{p}%</text>')
    for i, yr in enumerate(years):
        cx = left + slot * (i + 0.5)
        t = TARGET[yr]
        if yr in SALES:
            pct, note = SALES[yr]
            tx, sx = cx - 32, cx + 2
        else:
            pct, note, tx = None, None, cx - 15
        h = t * scale
        o.append(f'<rect x="{f1(tx)}" y="{f1(base - h)}" width="30" height="{f1(h)}" fill="{TGT}"/>')
        o.append(f'<text x="{f1(tx + 15)}" y="{f1(base - h - 7)}" font-size="12" fill="{SOFT}" text-anchor="middle">{t}%</text>')
        if pct:
            h = float(pct) * scale
            o.append(f'<rect x="{f1(sx)}" y="{f1(base - h)}" width="30" height="{f1(h)}" fill="{GREEN}"/>')
            o.append(f'<text x="{f1(sx + 15)}" y="{f1(base - h - 7)}" font-size="12" font-weight="700" fill="{GREEN}" text-anchor="middle">{pct}%</text>')
        o.append(f'<text x="{f1(cx)}" y="392" font-size="13" fill="{INK}" text-anchor="middle">{yr}</text>')
        if note:
            o.append(f'<text x="{f1(cx)}" y="408" font-size="11" fill="{AXIS}" text-anchor="middle">{note}</text>')
        if yr == 2030:
            for opt in OPTIONS_2030:
                y = base - opt * scale
                o.append(f'<line x1="{f1(cx - 34)}" y1="{f1(y)}" x2="{f1(cx + 30)}" y2="{f1(y)}" stroke="{AMBER}" stroke-width="2" stroke-dasharray="5 3"/>')
                o.append(f'<text x="{f1(cx + 36)}" y="{f1(y + 4)}" font-size="12" fill="{AMBER}">{opt}%</text>')
    o += [f'<rect x="32" y="418" width="12" height="12" fill="{GREEN}"/>',
          f'<text x="50" y="428" font-size="12" fill="{SOFT}">Battery-electric share of sales</text>',
          f'<rect x="246" y="418" width="12" height="12" fill="{TGT}"/>',
          f'<text x="264" y="428" font-size="12" fill="{SOFT}">ZEV mandate van target</text>',
          f'<line x1="430" y1="424" x2="452" y2="424" stroke="{AMBER}" stroke-width="2" stroke-dasharray="5 3"/>',
          f'<text x="458" y="428" font-size="12" fill="{SOFT}">2030 options in the 2026 review</text>',
          f'<text x="32" y="458" font-size="11" fill="{FAINT}">{SOURCES}</text>',
          '</g></svg>']
    return '\n'.join(o) + '\n'


def mobile():
    """Horizontal bars, 400x592, for screens up to 640px wide."""
    x0, x1, top, bottom = 76, 356, 132, 445
    scale = (x1 - x0) / 100
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 592" width="400" height="592" role="img" aria-labelledby="t d">',
         '<title id="t">Electric van sales against the ZEV mandate target, 2024 to 2030</title>',
         f'<desc id="d">{describe()}</desc>',
         f'<rect width="400" height="592" fill="{BG}"/>',
         f'<g font-family="{FONT}">',
         f'<text x="20" y="38" font-size="20" font-weight="700" fill="{INK}">Electric van sales vs</text>',
         f'<text x="20" y="64" font-size="20" font-weight="700" fill="{INK}">the ZEV mandate target</text>',
         f'<text x="20" y="91" font-size="12.5" fill="{AXIS}">Battery-electric share of new UK van sales</text>',
         f'<text x="20" y="109" font-size="12.5" fill="{AXIS}">(SMMT) against the yearly van target</text>']
    for p in (0, 25, 50, 75, 100):
        x = x0 + p * scale
        o.append(f'<line x1="{f1(x)}" y1="{top}" x2="{f1(x)}" y2="{bottom}" stroke="{GRID}" stroke-width="1"/>')
        o.append(f'<text x="{f1(x)}" y="{bottom + 17}" font-size="11" fill="{AXIS}" text-anchor="middle">{p}%</text>')
    y = 136
    for yr, t in TARGET.items():
        two = yr in SALES
        ty = y if two else y + 5
        w = t * scale
        o.append(f'<text x="20" y="{ty + 13}" font-size="14" fill="{INK}">{yr}</text>')
        o.append(f'<rect x="{x0}" y="{ty}" width="{f1(w)}" height="16" fill="{TGT}"/>')
        o.append(f'<text x="{f1(x0 + w + 6)}" y="{ty + 13}" font-size="12" fill="{SOFT}">{t}%</text>')
        if two:
            pct, note = SALES[yr]
            w = float(pct) * scale
            o.append(f'<rect x="{x0}" y="{y + 19}" width="{f1(w)}" height="16" fill="{GREEN}"/>')
            o.append(f'<text x="{f1(x0 + w + 6)}" y="{y + 32}" font-size="12" font-weight="700" fill="{GREEN}">{pct}%</text>')
            if note:
                o.append(f'<text x="20" y="{y + 31}" font-size="10.5" fill="{AXIS}">{note}</text>')
        if yr == 2030:
            for opt in OPTIONS_2030:
                x = x0 + opt * scale
                o.append(f'<line x1="{f1(x)}" y1="{ty - 5}" x2="{f1(x)}" y2="{ty + 21}" stroke="{AMBER}" stroke-width="2" stroke-dasharray="4 3"/>')
                o.append(f'<text x="{f1(x)}" y="{ty - 10}" font-size="10" fill="{AMBER}" text-anchor="middle">{opt}</text>')
        y += 46
    o += [f'<rect x="20" y="483" width="13" height="13" fill="{GREEN}"/>',
          f'<text x="40" y="494" font-size="12.5" fill="{SOFT}">Battery-electric share of sales</text>',
          f'<rect x="20" y="507" width="13" height="13" fill="{TGT}"/>',
          f'<text x="40" y="518" font-size="12.5" fill="{SOFT}">ZEV mandate van target</text>',
          f'<line x1="20" y1="537" x2="33" y2="537" stroke="{AMBER}" stroke-width="2" stroke-dasharray="4 3"/>',
          f'<text x="40" y="541" font-size="12.5" fill="{SOFT}">2030 options in the 2026 review (%)</text>',
          f'<text x="20" y="566" font-size="10.5" fill="{FAINT}">Sources: SMMT (via NFDA, Motor Transport,</text>',
          f'<text x="20" y="581" font-size="10.5" fill="{FAINT}">AM Online); GOV.UK. Chart: CommercialEVs.co.uk, CC BY 4.0</text>',
          '</g></svg>']
    return '\n'.join(o) + '\n'


if __name__ == '__main__':
    out = os.path.join(ROOT, '_build', 'charts', 'out')
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(ROOT, 'img', 'zev-van-sales-vs-target.svg'), 'w') as f:
        f.write(desktop())
    with open(os.path.join(out, 'zev-van-sales-vs-target-mobile.svg'), 'w') as f:
        f.write(mobile())
    print('wrote img/zev-van-sales-vs-target.svg and _build/charts/out/zev-van-sales-vs-target-mobile.svg')
    print(describe())
