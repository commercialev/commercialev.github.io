"""Electric vans compared. The three model tables are built from data/vans.json."""
from lib import page, refs

META = {
    'slug': 'electric-vans-uk',
    'title': 'Electric Vans UK 2026: Range, Payload & Price Compared',
    'desc': 'The main electric vans on sale in the UK compared: official range, payload and battery, plus prices, real-world winter range and battery warranties.',
    'og_desc': 'Official range, payload, battery and charging speed for the main electric vans on sale in the UK.',
    'crumb': 'Electric vans compared',
    'h1': 'Electric vans in the UK: range, payload and price compared',
    'published': '2026-10-05',
    'modified': '2026-10-10',
}

BODY = r'''    <p class="meta">Updated 10 October 2026. Every figure links to its source. Specifications vary by version, so check the exact van with the dealer. <a href="/about/">How we check facts</a>.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>Longest range:</strong> Renault Master E-Tech, up to 285 miles (official figure). [[fw_master]]</li>
        <li><strong>Most payload:</strong> Renault Master E-Tech, up to 1,625kg; Ford E-Transit van, up to 1,460kg. [[fw_master]] [[fn_etransit]]</li>
        <li><strong>Lowest price after the grant:</strong> Kia PV5 Cargo, from £22,645 plus VAT. [[pv5_price]]</li>
        <li><strong>Battery warranty:</strong> usually 8 years or 100,000 miles. [[warranty]]</li>
        <li><strong>Real-world range:</strong> plan on 60&ndash;70% of the official figure for a loaded van in winter. [[winter_range]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#small">Small electric vans</a></li>
        <li><a href="#medium">Medium electric vans</a></li>
        <li><a href="#large">Large electric vans</a></li>
        <li><a href="#longest-range">Which electric van has the longest range?</a></li>
        <li><a href="#payload">Which electric van carries the most?</a></li>
        <li><a href="#price">How much does an electric van cost?</a></li>
        <li><a href="#real-range">How far will an electric van really go?</a></li>
        <li><a href="#battery">How long do electric van batteries last?</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <p class="note">Range is the official WLTP figure for the longest-range version. Payload is the highest figure for that model; heavier-battery and passenger versions carry less. Models joined by a slash are near-identical vans sold under different badges.</p>

    <h2 id="small">Small electric vans</h2>
{{vans_table:small}}

    <h2 id="medium">Medium electric vans</h2>
{{vans_table:medium}}
    <p>Head to head: <a href="/medium-electric-vans-compared/">E-Transit Custom vs ID. Buzz Cargo vs Kia PV5 vs Vivaro Electric</a> compares range, payload, load space, charging, towing and price.</p>
    <p>Also in this size: the Mercedes-Benz eVito, and the new Renault Trafic E-Tech, due in late 2026. <a href="/diesel-vs-electric-vans/">See running costs</a> for a medium diesel vs electric comparison.</p>

    <h2 id="large">Large electric vans</h2>
{{vans_table:large}}
    <p>Many large electric vans come in 4.25-tonne versions to win back payload lost to battery weight. A car licence covers these if they're zero-emission. <a href="/commercial-electric-vehicles-uk/#licence">More on the licence rule</a>.</p>

    <h2 id="longest-range">Which electric van has the longest range?</h2>
    <p>The Renault Master E-Tech, at up to 285 miles on the official test, followed by the Volkswagen ID. Buzz Cargo (277 miles) and the Mercedes-Benz eSprinter (277 miles). The longest-range medium vans are the ID. Buzz Cargo and the Kia PV5 Cargo (258 miles). [[idb_spec]] [[pv5_spec]] [[fw_master]] [[fn_esprinter]]</p>

    <h2 id="payload">Which electric van carries the most?</h2>
    <p>Among panel vans, the Renault Master E-Tech (up to 1,625kg), the Vauxhall Movano Electric and its twins in 4.25-tonne form (up to 1,480kg) and the Ford E-Transit (up to 1,460kg). The heaviest-payload medium van is the Vauxhall Vivaro Electric and its twins (up to 1,226kg), followed by the Ford E-Transit Custom (up to 1,088kg). [[fw_master]] [[fn_etransit]] [[hj_movano]] [[viv_spec]] [[etc_range]]</p>

    <h2 id="price">How much does an electric van cost?</h2>
    <p>Launch list prices, excluding VAT:</p>
    <ul>
      <li><strong>Ford E-Transit Courier:</strong> from £27,000 before its £2,500 small-van grant, so about £24,500 after it. [[whatvan_courier]] [[evguide_cheapest]]</li>
      <li><strong>Kia PV5 Cargo:</strong> from £27,645 with the standard battery or £30,145 with the long-range battery, before the £5,000 grant. That makes it the cheapest electric van after the grant, from £22,645. [[pv5_price]]</li>
      <li><strong>Volkswagen ID. Buzz Cargo:</strong> from £34,460. [[idb_spec]]</li>
      <li><strong>Renault Master E-Tech:</strong> from £37,500, including the grant. [[fw_master]]</li>
      <li><strong>Farizon SV:</strong> from £45,000, rising to £56,000. [[fn_farizon]]</li>
    </ul>
    <p>Dealers often discount electric vans heavily, so these are starting points. The <a href="/commercial-electric-vehicles-uk/#grant">Zero Emission Van Grant</a>, which replaced the plug-in van grant in April 2026, takes up to £2,500 off small vans and £5,000 off larger ones, and the dealer applies it for you.</p>

    <h2 id="real-range">How far will an electric van really go?</h2>
    <p>Less than the official figure. Fleet tests suggest a fully loaded van in a British winter gets 60&ndash;70% of its official range. A van rated at 200 miles is safer planned at about 120&ndash;140 miles, especially if it can't be pre-heated while still plugged in. [[winter_range]]</p>

    <h2 id="battery">How long do electric van batteries last?</h2>
    <p>Most manufacturers cover the battery for 8 years or 100,000 miles, whichever comes first; Ford, Nissan and Volkswagen all do. Volkswagen's warranty promises the battery keeps at least 70% of its original capacity over that period. Check the terms for the exact van, especially if you're buying used. [[warranty]]</p>

    <p>To see which company makes the battery in each van, read <a href="/electric-van-batteries/">who makes electric van batteries</a>.</p>

    <p>See which UK companies run these vans in <a href="/electric-van-fleets-uk/">the biggest electric van fleets</a>. Next: <a href="/charging-an-electric-van/">how to charge an electric van, and what it costs</a>.</p>

'''

CAPTIONS = {'small': 'Small electric vans on sale in the UK, 2026',
            'medium': 'Medium electric vans on sale in the UK, 2026',
            'large': 'Large electric vans on sale in the UK, 2026'}


def vans_table(data, size):
    rows = []
    for v in data['vans']:
        if v['size'] != size:
            continue
        src = []
        for field in ('battery', 'range', 'payload'):
            src += [k for k in v[field]['src'] if k not in src]
        rows.append(f"        <tr><td>{v['name']}</td><td>{v['battery']['v']}</td><td>{v['range']['v']}</td>"
                    f"<td>{v['payload']['v']} {refs(src)}</td></tr>")
    return ('    <div class="table-wrap"><table class="models">\n'
            f'      <caption>{CAPTIONS[size]}</caption>\n'
            '      <thead><tr><th>Van</th><th>Battery</th><th>Range, up to</th><th>Payload, up to</th></tr></thead>\n'
            '      <tbody>\n' + '\n'.join(rows) + '\n      </tbody>\n    </table></div>')


def build(data):
    body = BODY
    for size in CAPTIONS:
        body = body.replace('{{vans_table:%s}}' % size, vans_table(data, size))
    return META['slug'], page(**META, body=body)
