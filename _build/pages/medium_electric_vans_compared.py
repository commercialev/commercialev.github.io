"""Head-to-head comparison of four medium electric vans. The table is built from data/vans.json."""
from lib import page, refs

META = {
    'slug': 'medium-electric-vans-compared',
    'title': 'E-Transit Custom vs ID. Buzz Cargo vs PV5 vs Vivaro (2026)',
    'desc': 'Ford E-Transit Custom vs VW ID. Buzz Cargo vs Kia PV5 vs Vauxhall Vivaro Electric: range, payload, load space, charging, towing and price compared.',
    'og_desc': 'Range, payload, load space, charging, towing and price for the four most-compared medium electric vans.',
    'crumb': 'Medium electric vans compared',
    'h1': 'E-Transit Custom vs ID. Buzz Cargo vs Kia PV5 vs Vivaro Electric',
    'published': '2026-10-10',
    'modified': '2026-10-10',
}

BODY = r'''    <p class="meta">Updated 10 October 2026. Figures are manufacturers' and reviewers' published specifications, each linked to its source. Specs and prices vary by version and change often, so check the exact van before you buy. We're not paid by any manufacturer or dealer. <a href="/about/">How we check facts</a>.</p>
    <p>The Ford E-Transit Custom, Volkswagen ID. Buzz Cargo, Kia PV5 Cargo and Vauxhall Vivaro Electric are the medium electric vans UK businesses most often weigh up. Here's how they compare on range, payload, load space, charging, towing and price.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer: which should you buy?</h2>
      <ul>
        <li><strong>Heavy loads and towing:</strong> the Ford E-Transit Custom. It has the most load space, up to 9.0m³, can tow up to 2,000kg and carries over a tonne. [[etc_spec]] [[etc_tow]]</li>
        <li><strong>Maximum payload:</strong> the Vauxhall Vivaro Electric, at up to 1,226kg, but it charges the slowest and has the shortest range. [[viv_spec]] [[viv_fn]]</li>
        <li><strong>Range and fast charging:</strong> the Volkswagen ID. Buzz Cargo, with up to 277 miles and 185kW charging, but the least load space and payload. [[idb_spec]] [[idb_dc]] [[idb_vd]]</li>
        <li><strong>Lowest price:</strong> the Kia PV5 Cargo, from £27,645 before the grant (£22,645 after), with room for two Euro pallets, but under 800kg of payload. [[pv5_price]] [[pv5_rev]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#table">Side-by-side comparison</a></li>
        <li><a href="#range">Range</a></li>
        <li><a href="#payload">Payload and load space</a></li>
        <li><a href="#charging">Charging speed</a></li>
        <li><a href="#towing">Towing</a></li>
        <li><a href="#price">Price</a></li>
        <li><a href="#verdict">Which van suits which job</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="table">How do the four vans compare side by side?</h2>
    <p class="swipe-hint" aria-hidden="true">Scroll the table sideways to see all four vans.</p>
{{compare_table}}
    <p class="note">Prices are on the bases shown, because manufacturers and reviewers quote them differently. Medium vans of 2.5 to 4.25 tonnes qualify for up to £5,000 off through the <a href="/commercial-electric-vehicles-uk/#grant">Zero Emission Van Grant</a>, and dealers often discount further, so get quotes.</p>

    <h2 id="range">Which medium electric van has the longest range?</h2>
    <p>The Volkswagen ID. Buzz Cargo, at up to 277 miles on the official test, followed by the Kia PV5 Cargo with its larger battery (258 miles), the Ford E-Transit Custom (232 miles) and the Vauxhall Vivaro Electric (205–219 miles). [[idb_spec]] [[pv5_spec]] [[etc_range]] [[viv_spec]] Real-world range is lower, especially in winter and with heavy loads; see <a href="/electric-vans-uk/#real-range">how far electric vans really go</a>.</p>

    <h2 id="payload">Which carries the most?</h2>
    <ul>
      <li><strong>Payload:</strong> the Vivaro Electric leads at up to 1,226kg, with the E-Transit Custom close behind at up to 1,088kg. The PV5 Cargo (up to 790kg) and ID. Buzz Cargo (about 600–765kg, by version) carry much less. [[viv_spec]] [[etc_spec]] [[pv5_rev]] [[idb_vd]]</li>
      <li><strong>Load space:</strong> the E-Transit Custom is the biggest, from 5.8m³ up to 9.0m³ in the long, high-roof version. The Vivaro Electric offers 5.3m³ or 6.1m³, the PV5 Cargo 4.4m³ (enough for two Euro pallets) or 5.1m³ with a high roof, and the ID. Buzz Cargo 3.9m³. [[etc_spec]] [[viv_fn]] [[pv5_rev]] [[idb_vd]]</li>
      <li><strong>Coming soon:</strong> a long-wheelbase ID. Buzz Cargo with an 86kWh battery and 4.4m³ of load space went on order in Europe in September 2026. [[idb_lwb]]</li>
    </ul>

    <h2 id="charging">Which charges fastest?</h2>
    <p>On a rapid charger, the ID. Buzz Cargo is quickest, at up to 185kW and 26 minutes from 10% to 80%. The PV5 Cargo (150kW) and E-Transit Custom (125kW) both take around half an hour. The Vivaro Electric is slowest, at 100kW and about 45 minutes from 0% to 80%. [[idb_dc]] [[pv5_dc]] [[etc_ford]] [[viv_fn]] Most vans charge overnight at home or a depot, where these differences matter less; see <a href="/charging-an-electric-van/">charging an electric van</a>.</p>

    <h2 id="towing">Which can tow the most?</h2>
    <p>The E-Transit Custom, at up to 2,000kg braked. The ID. Buzz Cargo can tow 1,000kg, or 1,800kg with four-wheel drive (4MOTION), and the Vivaro Electric 1,000kg, well below the 2,500kg of the diesel Vivaro. [[etc_tow]] [[idb_vd]] [[viv_fn]] We couldn't find a towing figure for the PV5 Cargo in its UK specifications, so check with Kia if you tow.</p>

    <h2 id="price">Which is cheapest?</h2>
    <p>The Kia PV5 Cargo, from £27,645 excluding VAT with the standard battery, or £22,645 after the £5,000 grant. [[pv5_price]] The ID. Buzz Cargo starts at £34,460 [[idb_spec]], the Vivaro Electric at £38,450 after the grant [[viv_price]] and the E-Transit Custom at about £43,630 before the grant. [[etc_price]] For running costs against a diesel Transit Custom, see <a href="/diesel-vs-electric-vans/">diesel vs electric vans</a>.</p>

    <h2 id="verdict">Which van suits which job?</h2>
    <ul>
      <li><strong>Trades carrying heavy kit or towing a trailer:</strong> E-Transit Custom, for its load space, towing and payload.</li>
      <li><strong>Parcel and multi-drop work with heavy loads but short routes:</strong> Vivaro Electric, for the highest payload, as long as its range covers your day.</li>
      <li><strong>Long daily mileage with lighter loads:</strong> ID. Buzz Cargo, for the longest range and fastest charging.</li>
      <li><strong>Tight budgets and city work:</strong> PV5 Cargo, the cheapest of the four, with room for two Euro pallets.</li>
    </ul>
    <p>For the battery maker behind each van, see <a href="/electric-van-batteries/">who makes electric van batteries</a>. For small and large vans, see <a href="/electric-vans-uk/">electric vans compared</a>.</p>
'''

VANS = ['etc', 'idb', 'pv5', 'vivaro']
ROWS = [('Battery', 'battery'), ('Range, up to (official)', 'range'), ('Payload', 'payload_detail'),
        ('Load space', 'load'), ('Fastest DC charging', 'dc'), ('Braked towing', 'towing'),
        ('Price from, excl. VAT', 'price')]


def cell(v, field):
    f = v[field]
    text, src = f['v'], list(f['src'])
    if field == 'battery' and 'battery_note' in v:
        text += '; ' + v['battery_note']['v']
        src += [k for k in v['battery_note']['src'] if k not in src]
    return (text + ' ' + refs(src)).strip()


def compare_table(data):
    vans = {v['id']: v for v in data['vans']}
    cols = [vans[i] for i in VANS]
    head = ''.join(f"<th>{v['compare_name']}</th>" for v in cols)
    rows = [f"        <tr><td>{label}</td>" + ''.join(f"<td>{cell(v, field)}</td>" for v in cols) + '</tr>'
            for label, field in ROWS]
    return ('    <div class="table-wrap"><table class="wide compare">\n'
            '      <caption>Medium electric vans compared, as of October 2026 (best figure for each van; varies by version)</caption>\n'
            f'      <thead><tr><th>&nbsp;</th>{head}</tr></thead>\n'
            '      <tbody>\n' + '\n'.join(rows) + '\n      </tbody>\n    </table></div>')


def build(data):
    body = BODY.replace('{{compare_table}}', compare_table(data))
    return META['slug'], page(**META, body=body)
