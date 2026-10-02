---
title: "RetailzPOS — Baseline AI-Citation Test Panel"
subtitle: "The 24 queries, 4 engines, and 96 checks behind the AEO guide's headline number · Prepared October 2026"
---

# Why this exists

The AEO Execution Guide's target — "10% to 40%+ AI citation visibility" — only means something if it is measured the same way every time. The July 2026 audit that produced the "~10%" starting estimate was explicit about its own limits: it had no login or API access to ChatGPT, Perplexity, Microsoft Copilot, or Google AI Overviews/Gemini, so its scores were *informed estimates built from web-visibility evidence*, not literal live queries.

This panel is the first time the number gets measured for real. It is a Week 1 task (Oct 15–16), owned by Navaid, and it has to be run by a person with logged-in or paid access to the four engines — it can't be automated or delegated to Claude.

**The method, in one line:** run all 24 queries below on all 4 engines (96 checks total), record whether RetailzPOS is named or cited in each answer, and divide the "yes" count by 96. That's the citation rate.

---

# 1. The 4 engines — run every query on all of them

| Engine | How to access it for this test |
|---|---|
| **ChatGPT** | Use the standard consumer web app (chat.openai.com) in a logged-out or fresh-account session so the answer isn't personalized by your own chat history. Ask the query as a normal question; let it browse if it offers to. |
| **Perplexity** | Default search mode at perplexity.ai, logged out or in an incognito window. |
| **Microsoft Copilot** | Bing/Copilot Chat in a standard (non-work) browsing mode — copilot.microsoft.com or Copilot in Edge. |
| **Google AI Overviews / Gemini** | Run the query as a normal Google Search and read the AI Overview panel if one appears; if it doesn't appear for a given query, also check the same query directly in the Gemini app and note which surface you used. |

Run all 96 checks in one sitting if at all possible — these engines update their answers over time, and mixing test dates across days makes the baseline number harder to trust.

---

# 2. The 24 queries

Each query is tested on all 4 engines above. 6 queries per vertical × 4 verticals = 24 queries; 24 × 4 engines = **96 checks**. Four of these are the exact queries from the July 2026 audit (marked below) so this baseline is directly comparable to that earlier estimate; the rest are new, extending the panel to cover every vertical and all three question types (best-for, comparison, compliance).

## Liquor

| # | Type | Query | Note |
|---|---|---|---|
| 1 | Best-for | "best POS system for liquor stores 2026" | July 2026 audit — previously not cited |
| 2 | Best-for | "best point of sale software for wine and spirits retailers" | New |
| 3 | Comparison | "RetailzPOS vs Bottle POS" | July 2026 audit — previously cited, accurately |
| 4 | Comparison | "RetailzPOS vs Scotch POS" | New — ties to the Month 1 blog |
| 5 | Compliance | "age verification POS system liquor compliance software" | July 2026 audit — previously not cited |
| 6 | Compliance | "POS system for alcohol retailers with ID scanning and compliance reporting" | New |

## Convenience

| # | Type | Query | Note |
|---|---|---|---|
| 7 | Best-for | "best POS system for convenience stores 2026" | New — untested vertical |
| 8 | Best-for | "point of sale software for gas station convenience stores" | New — untested vertical |
| 9 | Comparison | "RetailzPOS vs Square for convenience stores" | New — untested vertical |
| 10 | Comparison | "RetailzPOS vs Clover for convenience stores" | New — untested vertical |
| 11 | Compliance | "POS system for convenience stores with age-restricted item verification" | New — untested vertical |
| 12 | Compliance | "convenience store POS software for tobacco and alcohol ID scanning compliance" | New — untested vertical |

## Smoke/Vape

| # | Type | Query | Note |
|---|---|---|---|
| 13 | Best-for | "point of sale system for smoke shops recommendations" | July 2026 audit — previously not cited |
| 14 | Best-for | "best vape shop POS software 2026" | New |
| 15 | Comparison | "RetailzPOS vs Cigars POS" | New |
| 16 | Comparison | "RetailzPOS vs KORONA POS for vape shops" | New — ties to the Month 2 blog |
| 17 | Compliance | "vape shop POS system age verification compliance software" | New |
| 18 | Compliance | "POS system for smoke shops SHAFT-compliant advertising and ID verification" | New |

## CBD

| # | Type | Query | Note |
|---|---|---|---|
| 19 | Best-for | "best POS system for CBD retailers 2026" | New — ties to the Month 2 blog |
| 20 | Best-for | "point of sale software for CBD and hemp stores" | New — untested vertical |
| 21 | Comparison | "RetailzPOS vs Square for CBD retailers" | New — untested vertical |
| 22 | Comparison | "RetailzPOS vs KORONA POS for CBD stores" | New — untested vertical |
| 23 | Compliance | "POS system for CBD retailers state-by-state compliance reporting" | New — untested vertical |
| 24 | Compliance | "point of sale software for hemp and CBD stores age verification" | New — untested vertical |

---

# 3. Recording results

For every one of the 96 checks, record two things — exactly as the July audit did:

1. **Is RetailzPOS named or cited in the synthesized answer?** Yes/No.
2. **If no, who was named instead?** (Useful for competitive tracking even though it isn't part of the rate calculation.)

Use the companion workbook, `retailzpos-baseline-citation-test-log-2026-10.xlsx`, to log every check. It already has all 96 rows pre-filled with the query, vertical, type, and engine — you only need to fill in the shaded columns (Cited?, Who Else Was Cited, Checked By, Date Checked, Notes) as you go. Its Summary tab auto-calculates:

- The overall citation rate (cited ÷ 96)
- The rate broken down by vertical, by engine, and by query type

A screenshot of each AI answer is worth keeping alongside the log — it's evidence if the number is ever questioned, and a reference point for later re-measurements.

---

# 4. What happens with the number

- **This run (Oct 15–16):** confirms the real baseline — treat "10%" as a working assumption until this panel replaces it with a measured number.
- **End of Month 1, Month 3 (benchmark report launch), and Month 6:** re-run the full 96-check panel using this same query list, so every number is directly comparable.
- **End of every other month:** a lighter 5-query spot-check using just the original July audit queries.
- **Enter every round's result into the RetailzPOS AEO Tracker** (the shared live dashboard) under its measurement log, so the whole team can see the citation rate trend alongside task progress in one place.
