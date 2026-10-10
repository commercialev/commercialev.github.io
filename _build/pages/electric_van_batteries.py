"""Who makes electric van batteries. The per-van supplier table is built from data/vans.json."""
from lib import page, refs

META = {
    'slug': 'electric-van-batteries',
    'title': 'Who Makes Electric Van Batteries? CATL, LG & More (2026)',
    'desc': 'Who makes the battery in each UK electric van and truck, LFP vs NMC explained, battery prices, UK battery factories and the 2027 UK-EU tariff rules.',
    'og_desc': 'CATL, LG Energy Solution and more: who makes the battery in each electric van and truck sold in the UK.',
    'crumb': 'Electric van batteries',
    'h1': 'Who makes electric van batteries?',
    'published': '2026-10-10',
    'modified': '2026-10-10',
}

BODY = r'''    <p class="meta">Updated 10 October 2026. Every figure links to its source. Van makers can change battery suppliers between model years, and many don't publish them. <a href="/about/">How we check facts</a>.</p>
    <p>Which companies make the batteries in the electric vans and trucks sold in the UK, the difference between the two main battery types, what batteries cost, and the trade rules that could affect van prices from 2027.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>Biggest maker:</strong> China's CATL made 39.2% of the world's electric vehicle batteries in 2025, ahead of BYD (16.4%) and South Korea's LG Energy Solution (9.2%). [[sne]]</li>
        <li><strong>In vans:</strong> CATL supplies the cells for the Mercedes-Benz eSprinter and Kia PV5, and LG Energy Solution for the Renault Master E-Tech. Many other van makers don't say. [[esprinter]] [[pv5]] [[master]]</li>
        <li><strong>Battery types:</strong> LFP batteries cost less and last more charge cycles, while NMC batteries store more energy for their weight. In 2025, LFP packs averaged $81 per kWh against $128 for NMC. [[bnef]] [[lfpnmc]]</li>
        <li><strong>Made in the UK:</strong> AESC opened a battery cell factory in Sunderland in December 2025. Tata's Agratas factory in Somerset is due to start production in 2027. [[aesc]] [[agratas]]</li>
        <li><strong>2027 tariff risk:</strong> from 1 January 2027, electric vehicles traded between the UK and EU need more locally made content, including in the battery, or face a 10% tariff. [[roo]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#makers">The biggest EV battery makers</a></li>
        <li><a href="#vans">Who makes the battery in each electric van</a></li>
        <li><a href="#trucks">Electric truck batteries</a></li>
        <li><a href="#chemistry">LFP vs NMC batteries</a></li>
        <li><a href="#prices">Battery prices</a></li>
        <li><a href="#uk">Batteries made in the UK</a></li>
        <li><a href="#tariff">The 2027 tariff rules</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="makers">Who are the biggest electric vehicle battery makers?</h2>
    <div class="table-wrap"><table>
      <caption>Share of electric vehicle batteries installed worldwide, 2025</caption>
      <thead><tr><th>Company</th><th>Based in</th><th>Share</th></tr></thead>
      <tbody>
        <tr><td>CATL</td><td>China</td><td>39.2%</td></tr>
        <tr><td>BYD</td><td>China</td><td>16.4%</td></tr>
        <tr><td>LG Energy Solution</td><td>South Korea</td><td>9.2%</td></tr>
        <tr><td>CALB</td><td>China</td><td>5.3%</td></tr>
        <tr><td>Gotion High-tech</td><td>China</td><td>4.5%</td></tr>
        <tr><td>SK On</td><td>South Korea</td><td>3.7%</td></tr>
      </tbody>
    </table></div>
    <p>Installations came to about 1,187 GWh in 2025, up 31.7% on 2024. CATL alone installed 464.7 GWh, more than BYD and LG Energy Solution combined. [[sne]]</p>

    <h2 id="vans">Who makes the battery in each electric van?</h2>
{{battery_table}}
    <p class="note">Van makers often use more than one battery supplier and can switch between model years. We only name a supplier where the manufacturer or a named report confirms it.</p>
    <p><strong>Stellantis</strong>, which owns Vauxhall, Peugeot, Citroën and Fiat, signed an initial agreement with CATL in 2022 to buy LFP cells for its European models. The two companies are now building an LFP battery plant in Zaragoza, Spain, due to start production by the end of 2026. [[stellantis]] [[zaragoza]]</p>
    <p>For range, payload and battery warranties by model, see <a href="/electric-vans-uk/">electric vans compared</a>.</p>

    <h2 id="trucks">Who makes electric truck batteries?</h2>
    <ul>
      <li><strong>Mercedes-Benz eActros 600:</strong> CATL supplies the battery packs under a deal with Daimler Truck that runs beyond 2030. The truck's three LFP packs total 621 kWh. [[catldaimler]] [[eactros600]]</li>
      <li><strong>Volvo:</strong> Samsung SDI supplies the cells and modules, which Volvo assembles into 90 kWh packs in Ghent, Belgium. [[volvosdi]]</li>
      <li><strong>DAF XD and XF Electric:</strong> LFP cells in two to five packs, from 210 to 525 kWh. DAF hasn't named the supplier. [[daf]]</li>
      <li><strong>What's next:</strong> CATL launched its Tectrans II truck battery at the IAA Transportation 2026 show in Hanover, claiming up to 1,000 km of range for heavy trucks and support for battery swapping. [[tectrans]]</li>
    </ul>
    <p>Grants, models and charging for trucks are in <a href="/electric-trucks-uk/">electric trucks and HGVs in the UK</a>.</p>

    <h2 id="chemistry">LFP or NMC: what's the difference?</h2>
    <div class="table-wrap"><table class="wide">
      <caption>The two main battery types in electric vans and trucks</caption>
      <thead><tr><th>Feature</th><th>LFP (lithium iron phosphate)</th><th>NMC (nickel manganese cobalt)</th></tr></thead>
      <tbody>
        <tr><td>Average pack price, 2025</td><td>$81 per kWh</td><td>$128 per kWh [[bnef]]</td></tr>
        <tr><td>Energy per kg of pack</td><td>about 125–145 Wh</td><td>about 140–180 Wh [[lfpnmc]]</td></tr>
        <tr><td>Typical charge cycles</td><td>2,000–6,000+</td><td>1,000–2,500 [[lfpnmc]]</td></tr>
        <tr><td>Cobalt and nickel</td><td>None</td><td>Yes [[daf]]</td></tr>
        <tr><td>Examples</td><td>Mercedes-Benz eSprinter and eActros 600, DAF electric trucks</td><td>Kia PV5, Renault Master E-Tech, Vauxhall Vivaro Electric</td></tr>
      </tbody>
    </table></div>
    <p>In practice, LFP suits vans and trucks that charge every day and need a long battery life at a lower price. NMC fits more energy into the same weight, which helps range and payload. For how long van batteries last and what the warranties cover, see <a href="/electric-vans-uk/#battery">how long electric van batteries last</a>.</p>

    <h2 id="prices">How much do electric vehicle batteries cost?</h2>
    <ul>
      <li>The average lithium-ion battery pack price fell 8% in 2025 to a record low of $108 per kWh, across all uses. Packs for battery electric vehicles averaged $99 per kWh. [[bnef]]</li>
      <li>Prices in China averaged $84 per kWh, lower than elsewhere. [[bnef]]</li>
      <li>BloombergNEF expects prices to fall again in 2026. [[bnef]]</li>
    </ul>

    <h2 id="uk">Are electric vehicle batteries made in the UK?</h2>
    <ul>
      <li><strong>AESC, Sunderland:</strong> AESC opened its new cell factory in December 2025, with an initial capacity of 15.8 GWh a year that could rise to 35 GWh in later phases. Its cells go into the new Nissan Leaf, built at Nissan's Sunderland plant. [[aesc]]</li>
      <li><strong>Expansion on hold:</strong> AESC has delayed a third production line after talks to supply Jaguar Land Rover stalled. [[agratas]]</li>
      <li><strong>Agratas, Somerset:</strong> Tata Group's battery company is building a factory near Bridgwater with a planned capacity of 40 GWh a year. Production is now due to start in 2027. [[agratas]]</li>
    </ul>

    <h2 id="tariff">Will the 2027 battery rules raise van prices?</h2>
    <p>Under the UK–EU trade deal, an electric vehicle can cross between the UK and EU without a tariff only if enough of its value, including the battery, comes from the UK or EU. Looser rules were extended once, to the end of 2026. [[roo]]</p>
    <ul>
      <li><strong>From 1 January 2027:</strong> at least 55% of an electric vehicle's value must come from the UK or EU, with higher local-content thresholds for battery packs and cells. Vehicles that fall short face the standard 10% tariff. [[roo]]</li>
      <li><strong>Industry warning:</strong> in September 2026, the European carmakers' association ACEA asked for the current rules to be kept until the end of 2029 for electric cars and vans. It estimates about 426,000 vehicles, 82% of those affected, would fail the new rules, costing €1.47 billion in tariffs in 2027. [[acea]]</li>
      <li><strong>What it means for buyers:</strong> if the rules aren't relaxed, electric vans built in the EU with batteries made in Asia could cost more in the UK from 2027. We'll update this page when the UK and EU decide.</li>
    </ul>
'''

ORDER = ['esprinter', 'pv5', 'master', 'etransit', 'etc', 'vivaro', 'idb']


def battery_table(data):
    vans = {v['id']: v for v in data['vans']}
    rows = []
    for vid in ORDER:
        v = vans[vid]
        name = v.get('battery_name', v.get('compare_name', v['name']))
        note = v['cell_note'].replace('{battery}', v['battery']['v'])
        rows.append(f"        <tr><td>{name}</td><td>{v['cells']}</td><td>{v['chemistry']}</td><td>{note} {refs(v['cell_src'])}</td></tr>")
    return ('    <div class="table-wrap"><table class="wide">\n'
            '      <caption>Battery cell suppliers for electric vans sold in the UK</caption>\n'
            '      <thead><tr><th>Van</th><th>Battery cells from</th><th>Type</th><th>Notes</th></tr></thead>\n'
            '      <tbody>\n' + '\n'.join(rows) + '\n      </tbody>\n    </table></div>')


def build(data):
    body = BODY.replace('{{battery_table}}', battery_table(data))
    return META['slug'], page(**META, body=body)
