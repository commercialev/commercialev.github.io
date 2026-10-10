"""Electric trucks and HGVs in the UK."""
from lib import page

META = {
    'slug': 'electric-trucks-uk',
    'title': 'Electric Trucks & HGVs UK 2026: Grants, Models & Rules',
    'desc': 'Electric trucks and HGVs in the UK: the 2026 truck grant by weight, models and range, the 2035 and 2040 deadlines, charging, licences and running costs.',
    'og_desc': 'The 2026 truck grant, models and range, diesel deadlines, charging, licences and running costs for UK electric HGVs.',
    'crumb': 'Electric trucks and HGVs',
    'h1': 'Electric trucks and HGVs in the UK',
    'published': '2026-10-10',
    'modified': '2026-10-10',
}

BODY = r'''    <p class="meta">Updated 10 October 2026. Every figure links to its source. Grant rates, rules and specifications change, so check them before you buy. <a href="/about/">How we check facts</a>.</p>
    <p>What a business needs to know before buying an electric lorry in the UK: the grant, the deadlines for new diesel trucks, the models on sale, charging, licences and running costs.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>Grant:</strong> up to £15,000 off an electric truck of 4.25 to 12 tonnes, rising to £81,000 for trucks over 26 tonnes, from April 2026 to March 2030. [[grant]] [[sau]]</li>
        <li><strong>Deadlines:</strong> new non-zero-emission HGVs up to 26 tonnes can be sold until 2035, and heavier ones until 2040. [[phaseout]]</li>
        <li><strong>Sales:</strong> 587 zero-emission HGVs were registered in 2025, 1.4% of all new HGVs. In the first half of 2026 their share was 0.9%. [[smmt25]] [[h126]]</li>
        <li><strong>Range:</strong> Mercedes-Benz and DAF claim up to about 500 km (311 miles) for their biggest batteries, and Volvo has announced up to 700 km (435 miles). [[eactros600]] [[daf]] [[volvo700]]</li>
        <li><strong>Licence:</strong> an electric truck over 4.25 tonnes needs an HGV licence: C1 up to 7.5 tonnes, C for heavier rigid trucks and C+E for articulated lorries. [[licence]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#market">Electric truck sales in the UK</a></li>
        <li><a href="#grant">Electric truck grant 2026</a></li>
        <li><a href="#deadlines">When new diesel HGVs end</a></li>
        <li><a href="#models">Electric trucks on sale</a></li>
        <li><a href="#batteries">Who makes truck batteries</a></li>
        <li><a href="#charging">Charging an electric truck</a></li>
        <li><a href="#licence">Licences</a></li>
        <li><a href="#costs">Running costs vs diesel</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="market">How many electric trucks are sold in the UK?</h2>
    <ul>
      <li><strong>2025:</strong> new HGV registrations fell 10% to 40,504, but zero-emission HGVs rose 170.5% to a record 587, or 1.4% of the market. That made the UK Europe's second-largest market for zero-emission trucks by volume, after Germany. [[smmt25]]</li>
      <li><strong>2026 so far:</strong> 18,158 new HGVs were registered in the first half of the year, down 8.9%. Zero-emission volumes fell 6.6%, to 0.9% of the market, compared with a first half of 2025 that had been boosted by government demonstrator funding. SMMT blames higher purchase prices, slow grid connections for depots and limited public charging. [[h126]]</li>
    </ul>

    <h2 id="grant">How much is the electric truck grant in 2026?</h2>
    <div class="table-wrap"><table>
      <caption>Zero Emission Truck Grant, 2026/27</caption>
      <thead><tr><th>Truck size (gross vehicle weight)</th><th>Grant</th></tr></thead>
      <tbody>
        <tr><td>4.25 to 12 tonnes</td><td>up to £15,000</td></tr>
        <tr><td>12 to 18 tonnes</td><td>up to £37,000</td></tr>
        <tr><td>18 to 26 tonnes</td><td>up to £52,000</td></tr>
        <tr><td>Over 26 tonnes</td><td>up to £81,000</td></tr>
      </tbody>
    </table></div>
    <ul>
      <li><strong>How it works:</strong> the Zero Emission Truck Grant runs from 1 April 2026 to 31 March 2030, or until its budget runs out. For the heaviest trucks it can cover up to 40% of the price. The dealer claims it through the government's grant portal and takes it off the price. [[grant]] [[sau]] [[portal]]</li>
      <li><strong>Lower than early 2026:</strong> from January to March 2026, a temporary top-up offered up to £20,000, £60,000, £80,000 and £120,000 across the same weight bands. Those rates have ended. [[jan26]]</li>
      <li><strong>Depot chargers:</strong> the Depot Charging Scheme pays up to 70% of chargepoint and installation costs, up to £1 million, and its next window opens on 28 October 2026. <a href="/commercial-electric-vehicles-uk/#charging">Details on the grants page</a>.</li>
    </ul>

    <h2 id="deadlines">When will new diesel lorries be banned?</h2>
    <p>The UK has committed to ending sales of new non-zero-emission HGVs in two steps: [[phaseout]]</p>
    <ul>
      <li><strong>2035:</strong> trucks up to 26 tonnes.</li>
      <li><strong>2040:</strong> all new HGVs, including the heaviest articulated lorries.</li>
    </ul>
    <p>Both dates cover new sales only. Diesel trucks already on the road can still be used and sold second-hand. The government has said it will look at a limited set of exemptions to the 2035 date. [[phaseout]]</p>
    <p><strong>How it will be enforced:</strong> in January 2026 the Department for Transport consulted on the rules to get there, choosing between tougher CO<sub>2</sub> standards for manufacturers and a zero-emission sales mandate like the one for cars and vans. The consultation closed on 17 March 2026, and the government plans to consult again on the detail. [[co2consult]] For the car and van rules, see <a href="/commercial-electric-vehicles-uk/#zev-mandate">the ZEV mandate</a>.</p>

    <h2 id="models">Which electric trucks can you buy in the UK?</h2>
    <div class="table-wrap"><table class="wide">
      <caption>Heavy electric trucks on sale in the UK, manufacturers' figures</caption>
      <thead><tr><th>Truck</th><th>Type</th><th>Battery</th><th>Claimed range</th></tr></thead>
      <tbody>
        <tr><td>Mercedes-Benz eActros 600</td><td>Long-haul tractor unit</td><td>621 kWh (LFP)</td><td>up to 500 km (311 miles) [[eactros600]]</td></tr>
        <tr><td>Mercedes-Benz eActros 400</td><td>Lighter version of the eActros 600</td><td>—</td><td>up to 480 km (298 miles) [[eactros400]]</td></tr>
        <tr><td>DAF XD Electric and XF Electric</td><td>XD for distribution, XF for long haul</td><td>210 to 525 kWh (LFP, two to five packs)</td><td>200 to over 500 km (124 to 311+ miles) [[daf]]</td></tr>
        <tr><td>Volvo FH Aero Electric</td><td>Long-haul tractor unit</td><td>Not yet published for the new version</td><td>up to 700 km (435 miles), announced in 2026 [[volvo700]]</td></tr>
      </tbody>
    </table></div>
    <p class="note">Ranges are manufacturers' figures. Load, weather, terrain and speed all reduce them, so plan routes with a margin.</p>
    <p>For lighter work, the Fuso eCanter is a 7.5-tonne electric truck. DPD, Hovis and Wincanton were among its first UK users. [[ecanter]] DAF's electric trucks take DC charging at up to 325 kW, and the eActros 600 is designed for megawatt charging. [[daf]] [[eactros600]]</p>

    <h2 id="batteries">Who makes electric truck batteries?</h2>
    <ul>
      <li><strong>Mercedes-Benz:</strong> CATL supplies the battery packs for the eActros long-haul truck, sold as the eActros 600, under a deal that runs beyond 2030. [[catldaimler]]</li>
      <li><strong>Volvo:</strong> Samsung SDI supplies the cells and modules, which Volvo assembles into 90 kWh packs at its plant in Ghent, Belgium. Its FH, FM and FMX electric trucks carry up to six. [[volvosdi]]</li>
      <li><strong>DAF:</strong> uses LFP (lithium iron phosphate) cells, which contain no cobalt or nickel. It hasn't named the supplier. [[daf]]</li>
    </ul>
    <p>For battery makers, battery types and prices across vans and trucks, see <a href="/electric-van-batteries/">who makes electric van batteries</a>.</p>

    <h2 id="charging">Where can electric trucks charge?</h2>
    <p>Most electric trucks charge overnight at the operator's depot, so a depot's grid connection is usually the biggest hurdle. Maritime Transport, for example, is putting 56 electric HGVs into service at 13 sites during 2026, backed by more than 22 MW of charging. [[maritime]] Public charging for HGVs is only starting:</p>
    <ul>
      <li><strong>Milence, Immingham:</strong> the charging company set up by Daimler Truck, Traton and Volvo opened its first UK hub at Immingham, off the A180, in March 2025, with four chargers of up to 400 kW serving eight bays. [[milence]]</li>
      <li><strong>GRIDSERVE Electric Freightway:</strong> the first public electric HGV hubs opened at Extra Baldock on the A1(M) and Moto Exeter on the M5, the first of seven due to open during 2026. [[gridserve]]</li>
      <li><strong>Government-backed network:</strong> about £200 million is funding 54 zero-emission HGV hubs, run by four partnerships, with more than 70 depot and public charging or refuelling installations planned by 2030. [[zehid]]</li>
      <li><strong>Megawatt charging:</strong> Mercedes-Benz expects the eActros 600 to charge from 20% to 80% in about 30 minutes once megawatt chargers are available. [[eactros600]]</li>
    </ul>
    <p>Grants for depot chargers are on <a href="/commercial-electric-vehicles-uk/#charging">the grants page</a>, and typical charger costs are in <a href="/charging-an-electric-van/#depot-chargers">charging an electric van</a>.</p>

    <h2 id="licence">What licence do you need to drive an electric truck?</h2>
    <ul>
      <li><strong>Up to 4.25 tonnes:</strong> a car (category B) licence covers zero-emission vans up to 4.25 tonnes. <a href="/commercial-electric-vehicles-uk/#licence">More on the 4.25-tonne rule</a>.</li>
      <li><strong>Up to 7.5 tonnes:</strong> category C1, which covers vehicles of 3.5 to 7.5 tonnes. You'd need it for a 7.5-tonne electric truck such as the Fuso eCanter. [[licence]]</li>
      <li><strong>Over 7.5 tonnes:</strong> category C for rigid trucks, and C+E for a truck towing a trailer over 750kg, including articulated lorries. [[licence]]</li>
    </ul>

    <h2 id="costs">Are electric trucks cheaper to run than diesel?</h2>
    <ul>
      <li><strong>It depends on the work:</strong> the government-backed Electric Freightway trial found electric HGVs can match diesel's total cost of ownership after about five years in some operations, with high-mileage work benefiting most. [[freightway]]</li>
      <li><strong>The heaviest work is hardest:</strong> a Road Haulage Association survey of 114 operators, published in March 2026, estimated that a 44-tonne electric 6x2 tractor unit costs £28,282 a year more to run than a diesel one, mainly because heavy batteries reduce how much it can carry. [[rha]]</li>
      <li><strong>Weight limits:</strong> zero-emission trucks already get an extra two tonnes of weight allowance, but that doesn't help operators already working at the 44-tonne limit. The RHA wants the limit for electric trucks raised to 46 tonnes. [[rha]]</li>
      <li><strong>The grant narrows the gap:</strong> up to £81,000 off the heaviest trucks. See <a href="#grant">the grant table</a>.</li>
    </ul>
    <p>For the van equivalent, see <a href="/diesel-vs-electric-vans/">diesel vs electric vans</a>.</p>
'''

def build(data):
    return META['slug'], page(**META, body=BODY)
