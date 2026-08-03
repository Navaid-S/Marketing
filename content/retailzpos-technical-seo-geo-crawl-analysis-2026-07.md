# RetailzPOS — Technical SEO/GEO Crawl Analysis
**Prepared:** July 30, 2026
**Source:** Screaming Frog "Issues Overview Report" (40 issues, site-wide crawl, ~93 pages)
**Scope:** This is exactly the follow-up the last two documents called for — `retailzpos-ai-visibility-audit-2026-07.md` couldn't fetch retailzpos.com directly (blocked), and `retailzpos-aeo-geo-improvement-strategy-2026-07.md` flagged the technical/on-site component as unverified. This crawl turns that unknown into real data.

---

## 0. What this data is, and its limits

This is Screaming Frog's **Issues Overview** — a summary count per issue type, not a per-URL export (that's the report you said the free tier won't produce without a license). That means I can tell you *what's wrong and how much of the site it touches*, but not *which exact URLs* for most issues — the numbers below are real and worth acting on, but a handful of the highest-priority items need one more step: opening Screaming Frog's UI, clicking into the specific issue, and reading the actual URL list (that view is normally available even on the free/unlicensed tier — it's just the bulk CSV export of *all* data that's gated).

**Site size:** the percentages imply roughly **93 pages** were crawled (cross-checked against several issues with clean, isolated counts — "H1: Missing" = 3 URLs = 3.23% → ~93 total; "Meta Description: Missing" = 3 URLs = 3.23% → same). Some issues (like "Canonicals: Missing") compute against a very slightly different base (likely indexable-only URLs), which is normal Screaming Frog behavior, not an error in the data.

**Not covered by this export:** structured data / schema.org validation. None of the 40 issues relate to JSON-LD, FAQPage, Product, or Organization schema — meaning the schema recommendations in the GEO strategy doc are still unverified either way. If you can run Screaming Frog's structured data validation (`Config > Spider > Extraction > Structured Data`) and export that separately, send it over — it's the one piece this crawl doesn't answer.

---

## 1. The two things to fix first — High priority

### Directives: Noindex — 5 URLs (3.29%)

**This is the single most urgent line in the entire report.** A `noindex` directive tells search engines — and by extension the AI engines that draw from those same indexes — to actively drop a page from consideration. If any of these 5 pages are among the ones this whole project has been trying to get cited (`liquor-store-pos-systems-2026`, `best-liquor-store-pos-systems`, the compliance guide, or any comparison post), that alone would explain a meaningful chunk of the AI Visibility Audit's findings — no amount of backlink-building or schema work fixes a page that's explicitly told not to be indexed.

**Action:** Open the "Directives: Noindex" issue in Screaming Frog and check the 5 URLs by eye. Cross-reference them against the target pages from the GEO strategy. If any shouldn't be noindexed, removing the directive is a five-minute fix with outsized impact — do this before anything else on this list.

### Hreflang: Missing Return Links — 79 URLs (84.95%)

Hreflang is the tag that tells search engines "this page has an alternate version in another language/region, and here's where it lives" — and it only works if it's reciprocal: page A pointing to page B requires page B to point back to page A. 85% of the site is missing that return link.

**The real question to answer first: does RetailzPOS need hreflang at all?** Everything about this project — the product, the target verticals (liquor, smoke shop, convenience), the content — points to a single-market US business with no indication of multi-language or multi-region versions. If that's accurate, hreflang tags likely got added by a CMS plugin, theme default, or migration artifact rather than a deliberate choice, and the fix isn't "repair 79 broken reciprocal links" — it's **remove the hreflang implementation entirely** if there's genuinely only one version of each page. That's a much smaller job than fixing it, and it stops search engines from trying to interpret relationships that don't actually exist.

If there *is* a real reason for hreflang (a regional variant site, a planned expansion), then it needs proper reciprocal tagging across all 79 pages — but confirm the "why" before deciding which fix applies.

---

## 2. What directly explains the AI visibility gap — Medium priority, AEO-relevant

These aren't just generic SEO hygiene — they connect directly to why AI engines struggle to cite RetailzPOS pages individually, per the visibility audit.

| Issue | Scope | Why it matters for AEO/GEO specifically |
|---|---|---|
| Page Titles: Duplicate | 26 pages (28%) | If over a quarter of the site shares titles, AI engines can't reliably tell pages apart — this directly undermines the "each comparison page is a distinct, citable answer" strategy the content library was built around. |
| Meta Description: Duplicate | 25 pages (27%) | Same problem — the meta description is often what an AI engine's snippet extraction leans on for a quick page summary. |
| Content: Low Content Pages | 18 pages (18%), under 200 words | Thin pages give an AI engine nothing substantial to extract or cite. Worth checking whether any of these 18 overlap with pages meant to answer real buyer questions. |
| H1: Missing | 3 pages | The H1 is one of the clearest topical signals a page has — missing it entirely on any page that matters removes a key on-page cue. |
| H1: Multiple | 6 pages | Multiple competing H1s dilute which topic a page is actually "about," which matters for both ranking and AI extraction. |
| Canonicals: Missing | 5 pages | Without a declared canonical, Google can pick the "wrong" version of a page to trust — which fragments the authority the backlink work in the GEO strategy is trying to build up in the first place. |

**Recommended action:** pull the URL lists for these six specifically (not the full 40) and check them against the pages this project has been actively trying to get cited. That overlap check is worth doing before any of the broader content/backlink work in the GEO strategy — fixing a duplicate title or a missing canonical on a page nobody's trying to promote is low value; fixing it on `liquor-store-pos-systems-2026` is high value.

---

## 3. Site-wide templating issues — fix once, fixes everywhere

A cluster of issues sit at 80-99% of the site — that scale is the tell that these aren't page-by-page content problems, they're a shared template, theme, or footer/CTA block repeated across nearly every page. Fixing the template fixes all of them at once:

- **H2: Duplicate** — 78 pages (84%)
- **Links: Non-Descriptive Anchor Text In Internal Outlinks** — 78 pages (84%) — almost certainly generic "click here" / "learn more" links baked into a repeated CTA component
- **Links: Internal Outlinks With No Anchor Text** — 92 pages (99%) — near-universal, strongly suggests an icon link or image link without alt/anchor text in the header, footer, or nav
- **H2: Multiple** — 84 pages (90%)
- **H1: Non-Sequential** — 72 pages (77%)
- **H2: Non-Sequential** — 49 pages (53%)

**Action:** find the shared template element causing the non-descriptive/no-anchor-text links first (likely the highest-value single fix in this cluster, since it's nearly site-wide) — check the site header, footer, and any repeated CTA banner or card component. The H1/H2 sequencing issues likely trace back to a page-builder pattern (e.g., a hero component that renders an H2 before the page's actual H1, or a "Related Posts" block that injects its own heading out of order) — worth a quick look at whichever page-builder or CMS template generates that structure.

---

## 4. Lower-priority cleanup — real, but not urgent

Everything else in the report is legitimate but lower-leverage — worth working through, but not ahead of Sections 1-3:

- **Title/meta length opportunities** (over 60 chars, over 561px, below 30 chars, below 200px, over/under various meta description limits) — 8-34 pages depending on the specific check. Genuine room to tighten copy for CTR and truncation, but not blocking visibility the way the items above are.
- **Content: Readability Difficult** — 24 pages (24%) scoring at a "college graduate" reading level per Flesch-Kincaid. Worth a look if any of these are the buyer-facing comparison/FAQ content this project has focused on — AI-extractable answers tend to be clear, direct sentences, not dense copy.
- **Security: Unsafe Cross-Origin Links** — 92 links missing `rel="noopener"` on `target="_blank"` links. Legitimate, low-effort, low-risk fix.
- **URL formatting** (spaces, underscores, repetitive paths, over-length URLs) — tiny counts (1-2 URLs each), fix opportunistically rather than as a project.
- **Response code issues** (external 4xx, external no-response, internal 3xx redirects) — worth a pass to clean up broken external links and reduce internal redirect chains, but these are maintenance items, not visibility blockers.

---

## 5. Updated priority order for the GEO improvement strategy

This crawl doesn't replace `retailzpos-aeo-geo-improvement-strategy-2026-07.md` — it gives Tier 2b (technical schema implementation) a real starting point instead of an unverified one, and it surfaces one item urgent enough to jump the queue:

1. **New, jumps to the front of everything:** check the 5 noindex URLs and the hreflang situation (Section 1) — five minutes of investigation that could explain part of the audit's findings directly.
2. **Before the Tier 1 backlink work begins:** confirm none of the duplicate-title, missing-canonical, or low-content pages (Section 2) overlap with the pages that backlink effort is about to be pointed at — no sense building authority toward a page with a technical problem undermining it.
3. **Alongside Tier 2b schema work:** fix the template-level issues in Section 3 at the same time, since it's a single fix with sitewide reach.
4. **Still unanswered:** whether FAQPage/Organization/Product schema exists at all — this crawl didn't check it. Worth a follow-up structured-data export if you can get one.

---

## 6. Full issue table (all 40, as reported)

| Issue | Type | Priority | URLs | % of Total |
|---|---|---|---|---|
| H2: Duplicate | Opportunity | Low | 78 | 83.87% |
| H2: Non-Sequential | Warning | Low | 49 | 52.69% |
| URL: Repetitive Path | Warning | Low | 1 | 0.45% |
| Links: Pages With High External Outlinks | Warning | Low | 25 | 26.88% |
| H1: Over 70 Characters | Opportunity | Low | 16 | 17.20% |
| Response Codes: External No Response | Warning | Low | 4 | 1.41% |
| Links: Non-Descriptive Anchor Text In Internal Outlinks | Opportunity | Low | 78 | 83.87% |
| Content: Readability Difficult | Opportunity | Low | 24 | 24.24% |
| Response Codes: External Client Error (4xx) | Warning | Low | 5 | 1.76% |
| Page Titles: Duplicate | Opportunity | Medium | 26 | 27.96% |
| H1: Missing | Issue | Medium | 3 | 3.23% |
| Meta Description: Over 155 Characters | Opportunity | Low | 34 | 36.56% |
| Page Titles: Below 30 Characters | Opportunity | Medium | 14 | 15.05% |
| Page Titles: Below 200 Pixels | Opportunity | Medium | 8 | 8.60% |
| H1: Multiple | Warning | Medium | 6 | 6.45% |
| Meta Description: Duplicate | Opportunity | Low | 25 | 26.88% |
| URL: Contains Space | Issue | Low | 1 | 0.45% |
| Hreflang: Missing X-Default | Warning | Low | 80 | 86.02% |
| Meta Description: Missing | Opportunity | Low | 3 | 3.23% |
| Response Codes: Internal Redirection (3xx) | Warning | Low | 72 | 25.35% |
| Meta Description: Below 70 Characters | Opportunity | Low | 2 | 2.15% |
| Directives: Noindex | Warning | High | 5 | 3.29% |
| Content: Low Content Pages | Opportunity | Medium | 18 | 18.18% |
| Links: Internal Outlinks With No Anchor Text | Opportunity | Low | 92 | 98.92% |
| Meta Description: Over 985 Pixels | Opportunity | Low | 13 | 13.98% |
| Hreflang: Missing Return Links | Issue | High | 79 | 84.95% |
| Page Titles: Over 60 Characters | Opportunity | Medium | 22 | 23.66% |
| URL: Over 115 Characters | Opportunity | Low | 2 | 0.89% |
| Page Titles: Same as H1 | Opportunity | Low | 7 | 7.53% |
| H2: Multiple | Warning | Low | 84 | 90.32% |
| H2: Missing | Warning | Low | 3 | 3.23% |
| URL: Underscores | Opportunity | Low | 1 | 0.45% |
| Security: Unsafe Cross-Origin Links | Warning | Low | 92 | 41.07% |
| Meta Description: Below 400 Pixels | Opportunity | Low | 1 | 1.08% |
| Canonicals: Missing | Warning | Medium | 5 | 5.05% |
| Hreflang: Missing Self Reference | Warning | Low | 79 | 84.95% |
| H2: Over 70 Characters | Opportunity | Low | 10 | 10.75% |
| Page Titles: Over 561 Pixels | Opportunity | Medium | 23 | 24.73% |
| H1: Non-Sequential | Warning | Low | 72 | 77.42% |
| H1: Duplicate | Opportunity | Low | 14 | 15.05% |

*Source: Screaming Frog Issues Overview Report, uploaded July 30, 2026. Percentages and counts as reported by the tool; total site size (~93 pages) is an inference from cross-checking multiple issue rows, not a directly stated figure in this export type.*
