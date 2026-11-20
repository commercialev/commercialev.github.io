"""Head-to-head comparison of small electric vans. The table is built from data/vans.json."""
from lib import page, refs

META = {
    'slug': 'small-electric-vans-compared',
    'title': 'Best Small Electric Vans UK 2026: Range, Price & Payload',
    'desc': 'Small electric vans compared: Ford E-Transit Courier, Vauxhall Combo Electric, Renault Kangoo E-Tech and Kia PV5 on range, payload, towing and price.',
    'og_desc': 'Range, payload, load space, charging, towing and price for the small electric vans on sale in the UK.',
    'crumb': 'Small electric vans compared',
    'h1': 'Small electric vans compared: E-Transit Courier vs Combo Electric vs Kangoo E-Tech vs PV5',
    'published': '2026-11-20',
    'modified': '2026-11-20',
}

BODY = r'''    <p class="meta">Updated 20 November 2026. Figures are manufacturers' and reviewers' published specifications, each linked to its source. Specs and prices vary by version and change often, so check the exact van before you buy. We're not paid by any manufacturer or dealer. <a href="/about/">How we check facts</a>.</p>
    <p>Three families of small electric van are on sale in the UK: the Ford E-Transit Courier, the Vauxhall Combo Electric and its twins, and the Renault Kangoo E-Tech and its twins. We've also included the Kia PV5 Cargo. It's bigger than all three, but What Car? ranks it as the best small electric van of 2026. [[whatcar_small]]</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer: which small electric van should you buy?</h2>
      <ul>
        <li><strong>Towing:</strong> the Renault Kangoo E-Tech and its twins, rated to tow 1,500kg, twice the 750kg of the E-Transit Courier and Combo Electric. [[whatvan_kangoo]] [[whatvan_courier]] [[whatcar_epartner]]</li>
        <li><strong>Range in a compact van:</strong> the Vauxhall Combo Electric and its twins, at up to 213 miles, with the most payload of the three compact vans, up to 781kg. [[whatcar_epartner]]</li>
        <li><strong>Lowest price of the compact vans:</strong> the Ford E-Transit Courier, at about £24,500 excluding VAT after the grant, but it has the least load space, 2.9m³. [[whatvan_courier]] [[evguide_cheapest]]</li>
        <li><strong>More space, range and faster charging:</strong> the Kia PV5 Cargo, with 4.4–5.1m³, up to 258 miles and 150kW charging, from £22,645 after the larger £5,000 grant. [[pv5_rev]] [[pv5_spec]] [[pv5_dc]] [[pv5_price]]</li>
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
        <li><a href="#twins">Which vans are twins</a></li>
        <li><a href="#verdict">Which van suits which job</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="table">How do small electric vans compare side by side?</h2>
    <p class="swipe-hint" aria-hidden="true">Scroll the table sideways to see all four vans.</p>
{{compare_table}}
    <p class="note">Prices are on the bases shown, because manufacturers and reviewers quote them differently. The <a href="/commercial-electric-vehicles-uk/#grant">Zero Emission Van Grant</a> takes up to £2,500 off small vans and up to £5,000 off vans of 2.5 to 4.25 tonnes, and dealers often discount further, so get quotes.</p>

    <h2 id="range">Which small electric van has the longest range?</h2>
    <p>The Kia PV5 Cargo with its larger battery, at up to 258 miles on the official test, or 184 miles with the standard battery. [[pv5_spec]] [[whatcar_small]] Of the compact vans, the Combo Electric and its twins go furthest, at up to 213 miles, followed by the E-Transit Courier, at up to 207 miles in its 2026 form (182 miles at launch), and the Kangoo E-Tech, at 186 miles. [[whatcar_epartner]] [[ford_courier_2026]] [[whatvan_courier]] [[hj_kangoo]] Real-world range is lower, especially in winter and with heavy loads; see <a href="/electric-vans-uk/#real-range">how far electric vans really go</a>.</p>

    <h2 id="payload">Which small electric van carries the most?</h2>
    <ul>
      <li><strong>Payload:</strong> the PV5 Cargo carries up to 790kg and the Combo Electric up to 781kg, depending on version. The Kangoo E-Tech carries up to 764kg and the E-Transit Courier up to 698kg. [[pv5_rev]] [[whatcar_epartner]] [[hj_kangoo]] [[whatvan_courier]]</li>
      <li><strong>Load space:</strong> the PV5 Cargo has 4.4m³, enough for two Euro pallets, or 5.1m³ with a high roof. The Kangoo E-Tech has 3.3m³, or 4.2m³ in long form, and the Combo Electric 3.3m³ or 3.9m³, with 0.5m³ more on versions with a load-through bulkhead. The E-Transit Courier is the smallest, at 2.9m³. [[pv5_rev]] [[whatvan_kangoo]] [[whatcar_epartner]] [[whatvan_courier]]</li>
    </ul>

    <h2 id="charging">Which small electric van charges fastest?</h2>
    <p>On a rapid charger, the PV5 Cargo is quickest, at up to 150kW and under 30 minutes from 10% to 80%. The E-Transit Courier takes about 26 minutes from 10% to 80% at up to 100kW, and the Combo Electric about 30 minutes from 20% to 80%, also at 100kW. The Kangoo E-Tech is slowest, at 75kW and about 42 minutes to 80%. [[pv5_dc]] [[ford_courier_2026]] [[whatcar_epartner]] [[whatvan_kangoo]] Check the exact version: What Car? notes that base versions of the Nissan Townstar, the Kangoo's twin, can't fast charge at all. [[whatcar_townstar]] Most vans charge overnight at home or a depot; see <a href="/charging-an-electric-van/">charging an electric van</a>.</p>

    <h2 id="towing">Which small electric van can tow the most?</h2>
    <p>The Kangoo E-Tech and its twins, at up to 1,500kg braked. [[whatvan_kangoo]] The E-Transit Courier and the Combo Electric and its twins are limited to 750kg. [[whatvan_courier]] [[whatcar_epartner]] We couldn't find a towing figure for the PV5 Cargo in its UK specifications, so check with Kia if you tow.</p>

    <h2 id="price">Which small electric van is cheapest?</h2>
    <p>The Kia PV5 Cargo, from £22,645 excluding VAT after the £5,000 grant, because it's heavy enough to qualify for the larger grant. [[pv5_price]] Of the compact vans, the E-Transit Courier costs £27,000 before the £2,500 grant, about £24,500 after. [[whatvan_courier]] [[evguide_cheapest]] The Combo Electric starts at £26,800 after the grant [[vr_combo]] and the Kangoo E-Tech at a list price of £27,665. [[whatcar_small]] For running costs against a diesel van, see <a href="/diesel-vs-electric-vans/">diesel vs electric vans</a>.</p>

    <h2 id="twins">Which small electric vans are the same underneath?</h2>
    <ul>
      <li><strong>Vauxhall Combo Electric</strong> is sold as the Citroën ë-Berlingo, Peugeot e-Partner, Fiat E-Doblò and Toyota Proace City Electric. The specifications above are shared, though prices and equipment differ by badge.</li>
      <li><strong>Renault Kangoo E-Tech</strong> is sold as the Nissan Townstar EV and Mercedes-Benz eCitan.</li>
      <li><strong>Ford E-Transit Courier</strong> and the <strong>Kia PV5 Cargo</strong> have no twins.</li>
    </ul>

    <h2 id="verdict">Which small electric van suits which job?</h2>
    <ul>
      <li><strong>Towing a trailer:</strong> Kangoo E-Tech, Townstar EV or eCitan, the only vans here rated to tow 1,500kg.</li>
      <li><strong>City deliveries on a tight budget:</strong> E-Transit Courier, the cheapest of the compact vans after the grant, if 2.9m³ is enough.</li>
      <li><strong>Longer days with heavier loads:</strong> Combo Electric and its twins, for the most range and payload of the compact vans.</li>
      <li><strong>Pallets, bulky loads or rapid charging:</strong> PV5 Cargo, with the most space and the fastest charging, at the lowest price after the grant.</li>
    </ul>
    <p>Need more space still? Compare <a href="/medium-electric-vans-compared/">medium electric vans</a>, or see <a href="/electric-vans-uk/">every electric van on sale</a>. For who makes each battery, see <a href="/electric-van-batteries/">electric van batteries</a>.</p>
'''

VANS = ['courier', 'berlingo', 'kangoo', 'pv5']
ROWS = [('Battery', 'battery'), ('Range, up to (official)', 'range'), ('Payload, up to', 'payload'),
        ('Load space', 'load'), ('Fastest DC charging', 'dc'), ('Braked towing', 'towing'),
        ('Price from, excl. VAT', 'price')]


def cell(v, field):
    if field == 'payload' and 'payload_detail' in v:
        field = 'payload_detail'
    f = v[field]
    return (f['v'] + ' ' + refs(f['src'])).strip()


def compare_table(data):
    vans = {v['id']: v for v in data['vans']}
    cols = [vans[i] for i in VANS]
    head = ''.join(f"<th>{v['compare_name']}</th>" for v in cols)
    rows = [f"        <tr><td>{label}</td>" + ''.join(f"<td>{cell(v, field)}</td>" for v in cols) + '</tr>'
            for label, field in ROWS]
    return ('    <div class="table-wrap"><table class="wide compare">\n'
            '      <caption>Small electric vans compared, as of November 2026 (best figure for each van; varies by version)</caption>\n'
            f'      <thead><tr><th>&nbsp;</th>{head}</tr></thead>\n'
            '      <tbody>\n' + '\n'.join(rows) + '\n      </tbody>\n    </table></div>')


def build(data):
    body = BODY.replace('{{compare_table}}', compare_table(data))
    return META['slug'], page(**META, body=body)
