# Page builder

GitHub Pages doesn't publish this folder (Jekyll skips folders that start with `_`).

Some guide pages are generated from templates and shared data, so a figure is
written once and every page that shows it stays in step. The rest are
hand-written HTML.

| Page | Built from |
|---|---|
| `/electric-vans-uk/` | `pages/electric_vans_uk.py` + `data/vans.json` |
| `/medium-electric-vans-compared/` | `pages/medium_electric_vans_compared.py` + `data/vans.json` |
| `/electric-van-batteries/` | `pages/electric_van_batteries.py` + `data/vans.json` |
| `/electric-trucks-uk/` | `pages/electric_trucks_uk.py` |
| `/clean-air-zones-vans/` | `pages/clean_air_zones_vans.py` + `data/zones.json` |

Generated pages carry a comment at the top saying so. Edit the source, not the HTML.

## Common jobs

```sh
python3 _build/build.py          # rebuild the generated pages
python3 _build/check.py          # check every page (links, citations, sitemap, nav, stale builds)
```

- **Change a van figure:** edit `data/vans.json`, rebuild. Each figure is
  `{"v": "value", "src": ["source_key"]}`, and the tables on the vans,
  comparison and batteries pages all read it.
- **Change a zone's charge:** edit `data/zones.json`, rebuild. Yearly costs are
  worked out from `daily` x `days_per_year`.
- **Cite a source:** add it once to `data/sources.json`, then write
  `[[source_key]]` in a page template. Numbers and the sources list are
  generated in order of first use.
- **Change the stylesheet:** bump `CSS_VERSION` in `lib.py` and the `?v=`
  number in the hand-written pages, so browsers fetch the new file.
- **Change the navigation:** edit `NAV` in `lib.py` and the hand-written
  pages; `check.py` flags any page whose navigation differs.
- **New page:** add a page or its URL to `sitemap.xml`; `check.py` flags any
  indexable page missing from it.

Before committing, run both commands. `check.py` also fails if a generated
page no longer matches a fresh build.
