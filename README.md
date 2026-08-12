# Zong 5G — Corporate Business Products

A static marketing site for Zong Business's corporate/enterprise product portfolio, with an interest form that routes leads straight to your inbox — no backend required, so it runs entirely on **GitHub Pages**.

## What's in this repo

```
index.html                    Home page — hero + 8 category overview cards + "why us"
data-connectivity.html        Category detail page (4 products)
fixed-solutions.html          Category detail page (5 products)
international-carrier.html    Category detail page (6 products)
iot.html                      Category detail page (5 products)
voice.html                    Category detail page (5 products)
software.html                 Category detail page (9 products)
communication.html            Category detail page (4 products)
digital-transformation.html   Category detail page (2 products)
contact.html                  Interest form page
thanks.html                   Post-submit confirmation page
styles.css                    Shared stylesheet (light theme, Zong red accents)
script.js                     Shared behaviour: mobile nav, "interest list", form wiring
build_pages.py                Python script that generated the 8 category pages —
                               edit the CATEGORIES list in here and re-run to add/change products
sitemap.xml                   XML sitemap listing every page, for search engines
robots.txt                    Allows crawling, points to sitemap.xml

resources/                    SEO content section — long-form articles, one per category
  index.html                    Resources hub — links to every article below
  software-houses.html          Pillar page: security/compliance pitch for micro software houses
  data-connectivity.html        Deep-dive: use cases, process, diagram, FAQ, illustrative scenario
  fixed-solutions.html          Deep-dive (same structure)
  international-carrier.html    Deep-dive (same structure)
  iot.html                       Deep-dive (same structure) — the strongest security/software-house angle
  voice.html                    Deep-dive (same structure)
  software.html                 Deep-dive (same structure)
  communication.html            Deep-dive (same structure)
  digital-transformation.html   Deep-dive (same structure) — ISO 27001/PCI DSS compliance angle
build_resources.py            Python script that generated everything in resources/ —
                               edit the CATEGORIES / PILLAR data in here and re-run to update articles
```

## How the interest form works

Every product card has an **ADD** button. Clicking it saves that product name in the visitor's browser (`localStorage`) and shows a floating "N products selected" bar. That selection follows them across pages and shows up as removable chips on the Contact page — so someone can browse three different category pages, add a few products from each, then land on one form with everything already listed.

Submissions are handled by **[FormSubmit.co](https://formsubmit.co)** — a free service with no signup required. The form on `contact.html` posts to:

```
https://formsubmit.co/kahmed_3085@hotmail.com
```

**Important — one-time step:** the *first* time someone submits the form, FormSubmit sends a confirmation email to `kahmed_3085@hotmail.com` with an activation link. Click that link once, and every submission after that is delivered automatically — no further action needed. Until it's confirmed, submissions won't arrive.

To change the destination email later, replace the address in the `action="https://formsubmit.co/..."` attribute in `contact.html`.

## Deploying to GitHub Pages

You've already got the repo created (`kahmed3085/Zong-5g--Corporate-Business-Products`), so:

1. On the repo page, click **Add file → Upload files**.
2. Drag in every file from this folder (keep them all at the top level of the repo — do not put them in a subfolder).
3. Commit the changes (the default commit message is fine).
4. Go to **Settings → Pages**.
5. Under "Build and deployment", set **Source** to `Deploy from a branch`, branch `main`, folder `/ (root)`. Save.
6. Wait 1–2 minutes — your site will be live at:

```
https://kahmed3085.github.io/Zong-5g--Corporate-Business-Products/
```

## Customizing

- **Colors / branding:** all colors are defined as CSS variables at the top of `styles.css` (`--zong-red`, `--ink`, etc.) — change them there and the whole site updates.
- **Logo:** the header currently uses a text wordmark ("zong.business") rather than an image, since no official logo file was provided. To use the real Zong logo, drop a `logo.png` or `logo.svg` into an `assets/` folder and swap the `.logo` element in each page's `<header>` for an `<img>` tag.
- **Adding/editing products:** edit the `CATEGORIES` list in `build_pages.py`, then run `python3 build_pages.py` to regenerate the 8 category pages.
- **Form fields:** edit the `<form id="interestForm">` block in `contact.html` directly — any new `<input name="...">` will automatically appear as a column in the email FormSubmit sends you (with `_template` set to `table`).

## The `/resources` SEO content section

Each of the 8 product categories now has a long-form article at `resources/<category>.html` — written to actually rank and to be genuinely useful, not just keyword-stuffed. Every article follows the same structure: intro, use cases, a "why this matters for software houses" security callout, an illustrative scenario, a step-by-step deployment process, a static SVG diagram, and an FAQ section (marked up with FAQPage schema for rich results).

There's also `resources/software-houses.html` — a dedicated pillar page pulling together the security/compliance angle across IoT, Fixed Solutions, Communication and Digital Transformation specifically for micro and small software houses evaluating Zong for client projects.

**Important — "illustrative scenario" is doing real work in these articles.** I can't fabricate case studies that read as real, named client stories — that would effectively be inventing testimonials about a real telecom's real customers. Every scenario is clearly labeled "Illustrative scenario — not a specific named client" and is a realistic hypothetical, not a claim about an actual deal. If you have real (anonymized, if needed) GCSS outcomes you want written up instead, send them over and I'll swap specific scenarios for the real thing — that will perform better for both SEO and trust than hypotheticals.

**SEO notes:**
- All content is static HTML — fully crawlable, no JavaScript required to read it (per your instruction, no animation/motion was added to these pages, so there's nothing slowing them down either).
- Each article has its own title tag, meta description, canonical URL, Open Graph tags, and JSON-LD (Article + FAQPage) structured data.
- `sitemap.xml` and `robots.txt` are new at the repo root — submit the sitemap URL to Google Search Console after deploying so indexing starts faster.
- Internal linking runs both directions: every category page (e.g. `iot.html`) links to its matching deep-dive article, and every article links back to its category page and to 3 related articles.
- Keyword targeting is Pakistan-specific throughout (e.g. "dedicated internet access Pakistan", "IoT fleet tracking Pakistan", "ISO 27001 cloud hosting Pakistan") rather than generic global terms.

To edit or add content, change the `CATEGORIES` / `PILLAR` data structures in `build_resources.py` and re-run `python3 build_resources.py` — it regenerates all 10 files in `resources/` from scratch.

## Notes

This is an informational lead-generation page for Zong Business (CMPak Ltd) corporate products, intended to route interested prospects to the corporate sales team. Product names, availability and pricing are illustrative — final terms are confirmed by Zong directly. Case-study content in `/resources` is explicitly labeled as illustrative and does not reference real named clients.
