"""Clean air zones, ULEZ and low emission zones for vans. Both tables are built from data/zones.json."""
from lib import page, refs

META = {
    'slug': 'clean-air-zones-vans',
    'title': 'Clean Air Zones & ULEZ for Vans UK 2026: Charges by City',
    'desc': 'Every UK clean air zone, ULEZ and low emission zone that affects vans: daily charges, hours, which vans pay, yearly costs and what electric vans pay.',
    'og_desc': 'Daily charges, hours and yearly costs for vans in every UK clean air zone, the London ULEZ and Scotland\'s low emission zones.',
    'crumb': 'Clean air zones for vans',
    'h1': 'Clean air zones and ULEZ for vans: charges by city',
    'published': '2026-10-10',
    'modified': '2026-10-10',
}

BODY = r'''    <p class="meta">Updated 10 October 2026. Charges come from TfL, council websites and trade press, each linked below. Councils can change charges and boundaries, so check the council's own page before you travel. <a href="/about/">How we check facts</a>.</p>
    <p>Which UK zones charge vans, how much they cost a day and over a year, and why an electric van avoids almost all of them.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>Electric vans</strong> don't pay any clean air zone, ULEZ or low emission zone charge. The one charge they pay is London's Congestion Charge, at £9 a day with Auto Pay. [[tfl_cc]]</li>
        <li><strong>Older diesel vans</strong> pay from £8 a day in Birmingham to £12.50 a day in London's ULEZ and in Newcastle and Gateshead. [[bham]] [[tfl_ulez]] [[tyneside]]</li>
        <li><strong>Over a year</strong>, driving into one zone five days a week costs an older diesel van £2,080 to £3,250. [[peugeot_caz]]</li>
        <li><strong>Newer diesel vans</strong> that meet Euro 6 avoid clean air zone and ULEZ charges, but still pay London's Congestion Charge and Oxford's Zero Emission Zone. [[tfl_cc]] [[oxford]]</li>
        <li><strong>In Scotland</strong>, older vans can't enter low emission zones at all: penalties start at £60 and rise to £480. [[scot_lez]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#zones">Every zone that affects vans</a></li>
        <li><a href="#yearly">What a zone costs over a year</a></li>
        <li><a href="#which-vans">Which vans have to pay</a></li>
        <li><a href="#electric">Do electric vans pay?</a></li>
        <li><a href="#london">London: ULEZ and Congestion Charge</a></li>
        <li><a href="#scotland">Scotland's low emission zones</a></li>
        <li><a href="#oxford">Oxford's Zero Emission Zone</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="zones">Which UK zones charge vans?</h2>
    <p class="swipe-hint" aria-hidden="true">Scroll the table sideways to see every column.</p>
{{zones_table}}
    <p class="note">"Non-compliant" means a diesel van below Euro 6 or a petrol van below Euro 4. Greater Manchester isn't listed: in January 2025 the government approved its plan to clean up the air without a charging zone, so vans aren't charged. [[gm_caz]]</p>

    <h2 id="yearly">How much does a clean air zone cost over a year?</h2>
    <p>For a van that has to pay, driving into the zone five days a week for a year (260 days): [[peugeot_caz]]</p>
{{yearly_table}}
    <p class="note">Oxford's £8 is the rate for a Euro 6 diesel; older diesels pay £20 a day, or £5,200 a year. The Congestion Charge applies to every petrol and diesel van, however new. [[oxford]] [[tfl_cc]]</p>
    <p>Those charges add to a diesel van's higher running costs. See <a href="/diesel-vs-electric-vans/">diesel vs electric vans</a> for the full cost per mile.</p>

    <h2 id="which-vans">Which vans have to pay?</h2>
    <p>In every clean air zone, the London ULEZ and Scotland's low emission zones, a diesel van needs to meet the Euro 6 emissions standard and a petrol van Euro 4. Vans that meet them don't pay. [[tfl_ulez]] [[bham]] [[scot_lez]] Use the government's vehicle checker to see whether your van complies before you drive in. [[govuk_caz]]</p>
    <p>Two charges are different: London's Congestion Charge and Oxford's Zero Emission Zone apply to every petrol and diesel van, however new. [[tfl_cc]] [[oxford]]</p>

    <h2 id="electric">Do electric vans pay clean air zone charges?</h2>
    <p>No. Fully electric vans meet every clean air zone, ULEZ and low emission zone standard, and enter Oxford's Zero Emission Zone free. [[tfl_ulez]] [[oxford]] The exception is the London Congestion Charge: electric vans lost their exemption on 25 December 2025 and now pay £9 a day with Auto Pay, half the £18 standard charge. The discount falls to 25% in March 2030. [[tfl_cc]]</p>
    <p>Grants can take up to £5,000 off a new electric van; see <a href="/commercial-electric-vehicles-uk/#grant">van and truck grants</a>.</p>

    <h2 id="london">How do the London ULEZ and Congestion Charge work for vans?</h2>
    <ul>
      <li><strong>ULEZ:</strong> covers all London boroughs, 24 hours a day, every day except Christmas Day. Vans up to 3.5 tonnes that don't meet the standards pay £12.50 a day. [[tfl_ulez]]</li>
      <li><strong>Congestion Charge:</strong> covers central London, 7am to 6pm on weekdays and 12pm to 6pm at weekends and on bank holidays, with no charge between Christmas Day and the New Year's Day bank holiday. It's £18 a day for petrol and diesel vans and £9 for electric vans on Auto Pay. [[tfl_cc]]</li>
      <li><strong>Both at once:</strong> an older diesel van in central London on a weekday pays both, £30.50 a day. [[tfl_cc]] [[tfl_ulez]]</li>
    </ul>

    <h2 id="scotland">How do Scotland's low emission zones work for vans?</h2>
    <p>Glasgow, Edinburgh, Aberdeen and Dundee have low emission zones that run 24 hours a day. There's no daily charge to pay: vans that don't meet the standards aren't allowed in, and cameras issue penalties instead. [[scot_lez]]</p>
    <ul>
      <li><strong>Penalties for vans:</strong> £60 for the first, then £120, £240 and £480 for repeat entries. They're halved if paid within 14 days, and the scale resets after 90 days without another entry. [[scot_lez]]</li>
      <li><strong>Enforced since:</strong> Glasgow 1 June 2023, Dundee 30 May 2024, and Aberdeen and Edinburgh 1 June 2024. [[scot_lez]]</li>
    </ul>

    <h2 id="oxford">How does Oxford's Zero Emission Zone work for vans?</h2>
    <p>Oxford's pilot Zero Emission Zone charges every petrol and diesel vehicle, including hybrids, from 7am to 7pm every day. Rates set for the pilot from August 2025 are £8 a day for a Euro 6 diesel and £20 for older diesels. Electric vans enter free. Oxford plans a much larger zone from 2027. [[oxford]]</p>
'''

ROW_FIELDS = ['name', 'area', 'who', 'charge', 'hours', 'electric']


def zones_table(z):
    rows = []
    for zone in z['zones']:
        cells = [zone[f] for f in ROW_FIELDS]
        cells[-1] = cells[-1] + ' ' + refs(zone['src'])
        rows.append('        <tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
    return ('    <div class="table-wrap"><table class="wide compare">\n'
            f'      <caption>Charging and low emission zones that affect vans, as of October 2026</caption>\n'
            '      <thead><tr><th>Zone</th><th>Area</th><th>Which vans pay</th><th>Daily charge</th><th>Hours</th><th>Electric van</th></tr></thead>\n'
            '      <tbody>\n' + '\n'.join(rows) + '\n      </tbody>\n    </table></div>')


def money(x):
    return f'£{x:,.0f}' if x == int(x) else f'£{x:,.2f}'


def yearly_table(z):
    days = z['days_per_year']
    rows = []
    for zone in sorted((zn for zn in z['zones'] if zn['daily']), key=lambda zn: -zn['daily']):
        ev = zone['ev_daily'] * days
        rows.append(f"        <tr><td>{zone['name']}</td><td>{money(zone['daily'])}</td><td>{money(zone['daily'] * days)}</td>"
                    f"<td>{money(ev) if ev else '£0'}</td></tr>")
    return ('    <div class="table-wrap"><table class="wide">\n'
            f'      <caption>Yearly cost of one zone, five days a week ({days} days)</caption>\n'
            '      <thead><tr><th>Zone</th><th>Daily charge, van that has to pay</th><th>Yearly</th><th>Electric van, yearly</th></tr></thead>\n'
            '      <tbody>\n' + '\n'.join(rows) + '\n      </tbody>\n    </table></div>')


def build(data):
    z = data['zones']
    body = BODY.replace('{{zones_table}}', zones_table(z)).replace('{{yearly_table}}', yearly_table(z))
    return META['slug'], page(**META, body=body)
