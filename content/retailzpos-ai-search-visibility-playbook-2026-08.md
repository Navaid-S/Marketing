# RetailzPOS — AI Search Visibility Playbook
**Prepared:** August 2026 · Consolidates and updates six prior AEO/GEO documents in this repo with fresh research on what's changed since July.

---

## 0. How this fits with what's already built

This repo already has substantial AEO/GEO work, done thoroughly in July 2026:

| Document | What it covers |
|---|---|
| `retailzpos-ai-visibility-audit-2026-07.md` | Per-engine scores (ChatGPT 45, Copilot 48, Perplexity 42, Google AI Overviews/Gemini 38 out of 100) and the 3 specific unbranded queries RetailzPOS currently loses |
| `retailzpos-aeo-geo-improvement-strategy-2026-07.md` | The tiered fix plan (citation/authority gap → AEO restructuring → schema → reviews), a 90-day roadmap, and engine-specific tactical notes |
| `retailzpos-aeo-geo-reddit-quora-strategy-2026-07.md` | 12 live, answerable Quora questions, target subreddits, and a non-promotional participation plan |
| `retailzpos-technical-seo-geo-crawl-analysis-2026-07.md` | Site-wide crawl issues (noindex, hreflang, cannibalization) blocking GEO performance |
| `retailzpos-content-seo-backlink-hybrid-strategy-2026-07.md` | The content system (comparisons, compliance guides, trade press, Reddit/Quora, benchmark report) and 90-day rollout |
| `retailzpos-guest-posting-backlink-strategy-2026-07.md` | Confirmed real editorial programs (Retail Dive, Retail TouchPoints) for page-specific backlinks |

**This document does not repeat that work — it does three new things:** (1) reports what's materially changed in AI-search behavior since July that changes the priority order, (2) adds two workstreams the prior research didn't cover (entity/knowledge-graph building, and YouTube as a citation surface), and (3) delivers the thing none of the six documents fully is — a single, large, ready-to-use **topic bank**: specific comparison pages, FAQ questions, video topics, and community-question targets, mapped to the personas, features, and pillars already established in the Marketing Plan and Content Book.

If you haven't executed the July roadmap yet, start there — Sections 2 (schema) and 3 (Reddit/Quora) of the Improvement Strategy are still the correct Week 1-4 actions. Everything below assumes that work is underway or done, and tells you what to layer on next.

---

## 1. Why this still deserves real budget, in one paragraph

Gartner projects a 25% decline in organic search traffic to commercial sites by the end of 2026 as buyers shift first-touch research to AI assistants, and 94% of B2B buyers now say they use an LLM somewhere in their buying journey. Google AI Overviews now appear in up to 48% of US searches, and a page cited inside an AI Overview earns roughly 35% more organic clicks and 91% more paid clicks than an equivalent uncited page. This isn't a side channel anymore — for a buyer typing "best POS for a liquor store" into ChatGPT or Google, the AI-generated answer *is* the shortlist, and RetailzPOS is currently not reliably on it. [Source: [Firebrand, GEO Best Practices 2026](https://www.firebrand.marketing/2025/12/geo-best-practices-2026/), [Heroic Rankings, Google AI Overview Statistics 2026](https://heroicrankings.com/seo/managed/google-ai-overview-statistics-2026/), [PartnerStack, AEO for B2B SaaS 2026](https://partnerstack.com/resources/guides/answer-engine-optimization-the-ultimate-2026-guide-for-b2b-saas-teams)]

---

## 2. What's changed since the July research — the delta that matters

### 2.1 YouTube has overtaken Reddit as the top social citation source — this is the single biggest shift

Between August and December 2025, YouTube's share of social AI citations rose from 18.9% to 39.2%, and by Q1 2026 YouTube (16% of LLM answers) had passed Reddit (10%) as the most-cited social platform across major LLMs. The split by engine: Perplexity draws 38.7% of its YouTube citations, Google AI Overviews 36.6%, AI Mode 19.6%, ChatGPT a smaller 4.4%. Long-form video dominates — 94% of YouTube AI citations go to long-form uploads, Shorts only 5.7%. Google AI Overview now cites YouTube with **timestamped deep links** into the specific segment that answers the query, and videos that state the direct answer in the **first 30 seconds** get cited more than general explainers. [Source: [Averi, YouTube Beat Reddit for AI Citations 2026](https://www.averi.ai/blog/youtube-beat-reddit-for-ai-citations-the-b2b-pivot), [Search Engine Journal, The AI Overviews YouTube Gap](https://www.searchenginejournal.com/the-ai-overviews-youtube-gap-the-platform-your-team-skipped-for-20-years/582702/), [Socialync, YouTube Videos in Google AI Overview 2026](https://www.socialync.io/blog/youtube-videos-google-ai-overview-2026)]

**What this means for RetailzPOS specifically:** the Content Book already scripted three strong long-form video assets this quarter — the Week 10/11 "day in the store" workflow videos and the product tour. None were planned for a dedicated, AEO-structured YouTube channel; they were scoped as Instagram/Facebook/TikTok social content. That's a gap worth closing now, not next quarter — see Section 4.

### 2.2 Reddit is still rising fast, just no longer alone at the top

Reddit's citation share still grew at least 73% from October 2025 to January 2026 across every tracked category. Perplexity draws 24% of all its citations from Reddit alone (31% from social overall); Reddit accounts for 44% of Google AI Overviews' social citations specifically; ChatGPT cites Reddit in over 5% of responses. Wikipedia remains the single most-cited domain overall (8.9% of all citation slots), with Reddit close behind (11.4%). Gemini is the outlier — it cites Reddit in only 0.1% of responses, so don't expect Reddit work to move the Gemini score. **The July prioritization of Reddit/Quora as the top lever for Perplexity specifically is still correct and now has harder numbers behind it — this doesn't change, it gets reinforced.** [Source: [SaaS Intelligence, Reddit's AI Citation Share Grew 73%](https://saasintelligence.substack.com/p/reddits-ai-citation-share-just-grew), [QuickSEO, How Reddit Affects AI Visibility 2026](https://quickseo.ai/blog/how-reddit-affects-ai-visibility-2026)]

### 2.3 Entity and knowledge-graph signals are now a named, separate workstream — not covered in the July docs at all

Gemini is trained directly on Google's Knowledge Graph, and entity clarity — can Google/an LLM unambiguously identify RetailzPOS as a real, specific company, distinct from every other "POS" or "retail" mention — now measurably affects AI Overview and Gemini appearance. Wikidata is the structured backbone feeding the Knowledge Graph, Wikipedia, and other AI retrieval surfaces; a basic, accurate Wikidata entity record is available to any real business, not just large brands with PR budgets. In B2B software specifically, Wikipedia citation density correlates as strongly as 0.577 (Spearman) with AI Overview visibility — one of the strongest single signals found in category-specific research. **This is genuinely new territory for RetailzPOS — nothing in the July research touched Wikidata or Wikipedia citability, and it's now a confirmed, addressable gap.** [Source: [Digital Applied, Entity SEO & Knowledge Graph Guide 2026](https://www.digitalapplied.com/blog/entity-seo-knowledge-graph-optimization-guide-2026), [SearchBloom, Entity Optimization for AI Search](https://www.searchbloom.com/ai-seo/inclusion/entity-optimization/)]

### 2.4 Google AI Overview ranking factors got more specific — and confirm, don't contradict, the July finding

New research quantifies what "citable content" means structurally: passages scoring high on semantic completeness — a **134-167 word, fully self-contained answer to one specific question** — are 4.2x more likely to be cited than sprawling, multi-topic paragraphs. Multimodal pages (text + image + video + structured data together) get selected 156% more often than text-only pages. E-E-A-T still anchors everything — named authors with real, checkable credentials raise citation probability, and Domain Authority alone is now a weak signal (r=0.18). On position: 47% of AI citations come from pages ranking below position #5 — which doesn't contradict the July finding that ~76% of citations come from the top 10 (positions 6-10 are "below #5" and still inside the top 10). **The practical read: RetailzPOS doesn't need to out-rank Square or KORONA for position #1 to get cited — top 10 is enough, but the passage itself has to be a tight, complete, 134-167-word answer block, not buried in narrative.** This sharpens Section 4's "direct-answer block" recommendation from the Improvement Strategy into something you can literally count words against. [Source: [Digivate, How to Rank in Google AI Overviews 2026](https://digivate.com/blog/ai/how-to-rank-in-google-ai-overviews-2026), [Memeburn, Google AI Overview Statistics 2026](https://memeburn.com/google-ai-overview-statistics/)]

### 2.5 llms.txt — confirmed, harder now, still not worth prioritizing

June 2026 adoption data across a fixed panel shows 51.8%, but the more representative Tranco top-1,000 shows only 8.7-10.1%. More importantly: across 500M+ monitored AI bot visits over 90 days, only 408 requests hit `/llms.txt` directly — GPTBot, ClaudeBot, PerplexityBot, and Google-Extended overwhelmingly crawl HTML directly and ignore the file. No major AI lab (OpenAI, Google, Anthropic, Meta, Mistral) has committed to reading it in production, and Google's own June 2026 documentation states explicitly that it has no effect on Search or AI Overviews. **The July call — cheap to add once schema is done, don't expect it to move a score — holds exactly, now with a harder number (408 real hits) behind it.** [Source: [Rankability, LLMS.txt Adoption Data](https://www.rankability.com/data/llms-txt-adoption/), [aeo.press, The State of llms.txt in 2026](https://ai.aeo.press/the-state-of-llms-txt-in-2026)]

---

## 3. The four-surface citation stack for RetailzPOS

Current B2B SaaS AEO practice converges on one framing: **Editorial/backlinks + YouTube + Reddit/Quora + LinkedIn** is the four-surface stack that wins B2B AI citations in 2026. [Source: [Averi, YouTube Beat Reddit for AI Citations](https://www.averi.ai/blog/youtube-beat-reddit-for-ai-citations-the-b2b-pivot)] Mapped to what RetailzPOS already has or is building:

| Surface | Status | Owner document |
|---|---|---|
| Editorial / backlinks | Strategy built, execution in progress | `retailzpos-guest-posting-backlink-strategy-2026-07.md` |
| Reddit / Quora | Strategy built, execution in progress | `retailzpos-aeo-geo-reddit-quora-strategy-2026-07.md` |
| LinkedIn | Covered as a content channel in the 90-Day Plan, not yet AEO-structured | `retailzpos-90-day-marketing-plan-2026-08.docx`, Section 11 |
| **YouTube** | **Not yet built as a dedicated, AEO-structured surface** | **New — Section 5 below** |

Entity/knowledge-graph work (Section 2.3) sits underneath all four — it's what lets any engine confirm RetailzPOS is a real, specific, cross-referenced company once one of these surfaces mentions it.

---

## 4. Sharpened on-page best practices (apply to every new and existing page)

1. **One self-contained, 134-167 word answer block per question, placed in the first 2-3 sentences of the section.** Not a teaser that leads into three paragraphs of setup — the actual, complete answer, sized to the citation sweet spot in Section 2.4.
2. **Comparison tables above the fold**, scannable, one row per differentiator — already the right call in the July strategy; now backed by the multimodal-selection data in Section 2.4.
3. **Named, credentialed authorship** on every guide and comparison post (a real name and title, not "RetailzPOS Team") — E-E-A-T is still the anchor signal across every engine tested.
4. **Visible publish and last-updated dates** on every page, and actually update pages on a cadence rather than leaving a stale date — freshness is an explicit AI Overview signal for queries where recency matters (pricing pages, compliance guides, "2026" buyer's guides).
5. **Multimodal by default** — every comparison/guide page should carry at least one image, and, once Section 5 is running, an embedded relevant YouTube video, not text alone.
6. **Standard page types, not one-off blog posts** — for each vertical, build the AEO-standard set: a **Comparison** page (RetailzPOS vs. named competitor), an **Alternatives** page ("Best Bottle POS Alternatives," already partially covered by `retailzpos-blog-04`), a **Best-for** page ("Best POS for Liquor Stores 2026"), and a **FAQ** block with FAQPage schema on each. [Source: [Gracker AI, AEO for B2B SaaS](https://gracker.ai/blog/aeo-for-b2b-saas-strategies)]

---

## 5. New workstream — YouTube as an AEO surface

**Why now:** Section 2.1's data is the whole case — YouTube is the fastest-growing, now-largest social citation source, and RetailzPOS has zero presence there today.

**What to build, using assets already scripted:**

1. **Repurpose, don't reshoot.** The Content Book's W10-U3 and W11-U3 "full day" long-form videos and the PRE-U3 product tour were already scripted at 60-90 seconds for social. For YouTube, extend each into a genuine 6-10 minute long-form video — the social cut becomes a teaser/trailer that links to the full YouTube video, not a separate production.
2. **Structure every video to state the direct answer in the first 30 seconds**, then use YouTube's chapter/timestamp feature to mark each subsequent segment with a specific question as the chapter title (e.g., "0:00 What is hard-block age verification?" / "1:45 How does case-break inventory work?") — this is exactly the structure Google AI Overview now deep-links into.
3. **Publish a transcript and a matching on-site blog post for every video**, cross-linked both directions — this gives text-based engines (ChatGPT, Gemini) the same content video-native engines (Perplexity, AI Overviews) pull from the video itself.
4. **Target long-form only.** Given 94% of YouTube AI citations go to long-form video, treat Shorts as a distribution/awareness tactic (already covered by the Reels/TikTok plan in the Content Book) — not as the AEO play.

See Section 6.5 below for the first batch of YouTube-specific video topics.

---

## 6. The topic bank

Every topic below is mapped to a real RetailzPOS persona, pillar, or feature already established in the Marketing Plan and Content Book — nothing here is generic.

### 6.1 Comparison / Alternatives / Best-for pages (the AEO-standard page types from Section 4.6)

| Page | Type | Vertical / Persona | Status |
|---|---|---|---|
| RetailzPOS vs. Bottle POS | Comparison | Liquor / Danny | **Live** — `retailzpos-blog-01` |
| RetailzPOS vs. NRS POS | Comparison | Cross-vertical | **Live** — `retailzpos-blog-02` |
| RetailzPOS vs. Clover | Comparison | Cross-vertical | **Live** — `retailzpos-blog-05` |
| RetailzPOS vs. Square for Retail | Comparison | Cross-vertical | **Live** — `retailzpos-blog-06` |
| RetailzPOS vs. Loyverse | Comparison | Cross-vertical, cost-sensitive | **Live** — `retailzpos-blog-07` |
| Best LMS-POS Alternatives | Alternatives | Liquor / Danny | **Live** — `retailzpos-blog-04` |
| RetailzPOS vs. KORONA POS | Comparison | Cross-vertical, content-authority rival | **New — write this one.** KORONA is the strongest direct content competitor per the existing deep-dive; there is no head-to-head comparison page yet. |
| Best POS for Liquor Stores 2026 | Best-for | Liquor / Danny | Confirmed losing query per the audit — restructure per Section 4, don't rewrite from scratch |
| Best POS for Smoke Shops & Vape Retailers 2026 | Best-for | Smoke/vape / Ray | Confirmed losing query per the audit — restructure per Section 4 |
| Best POS for Convenience Stores with Multiple Locations | Best-for | Convenience / Farah, Priya | **New** |
| Best POS for CBD Retailers 2026 | Best-for | CBD / Sam | **New** — genuinely uncontested; no major competitor has published this page per the Plan's competitive research |
| RetailzPOS vs. a Generic/General-Merchandise POS (the category-education page) | Educational comparison | All | **New** — targets buyers who haven't realized they need a vertical-specific system yet (Month 1 mindset-ladder stage) |

### 6.2 FAQ question bank (for FAQPage schema — phrase exactly as a buyer would type it)

**Compliance & age verification (Ray, Danny)**
- Does RetailzPOS hard-block a sale if age verification fails?
- What's the difference between hard-block and soft-block age verification?
- Is RetailzPOS compliant with PACT Act requirements for vape/tobacco retailers?
- Does RetailzPOS keep an audit log of every ID check?
- How does RetailzPOS handle SHAFT and TCPA rules for SMS marketing to a liquor or smoke-shop customer list?

**Inventory & case-break (Farah)**
- What is case-break inventory tracking?
- Does RetailzPOS auto-convert a case to single units when it's opened?
- How does RetailzPOS's AI reorder alert decide when to reorder?
- Can RetailzPOS reconcile distributor EDI invoices automatically?

**Loyalty (Danny, Priya)**
- What is Moolah Points and how does it work with RetailzPOS?
- Can RetailzPOS automatically text a customer who hasn't visited in a while?
- Is Moolah Points loyalty marketing compliant for alcohol and tobacco retailers specifically?

**Multi-location (Priya)**
- Does RetailzPOS support multiple store locations on one account?
- Can I see inventory and sales across all my stores in one dashboard with RetailzPOS?
- How does RetailzPOS handle onboarding for a growing multi-location retailer?

**CBD (Sam)**
- Is RetailzPOS compliant with CBD retail regulations?
- Does POS software handle state-by-state CBD legal differences?

**Pricing (all — answer per the never-published policy, framed honestly)**
- How much does RetailzPOS cost?
- Does RetailzPOS charge per location or a flat rate?
- Is there a free trial or demo of RetailzPOS?

### 6.3 Compliance-authority topics (extends the existing compliance guide, doesn't replace it)

- A state-by-state primer on age-verification requirements for alcohol retail (structured as one 134-167-word answer per state or region, not one long narrative — direct application of Section 2.4)
- What auditors actually ask for during a compliance review, and how a POS audit log answers it
- PACT Act reporting requirements for vape/tobacco retailers, explained for a non-lawyer owner
- CBD retail compliance by state — the "state-by-state reality" piece already scoped in the 90-Day Plan's Blog & SEO Plan (Week 8), expand into a standing, periodically-updated resource page rather than a one-time post, since freshness matters for this exact topic per Section 2.4

### 6.4 Data/benchmark topics (extends the existing benchmark report groundwork)

- The flagship report itself (already scoped — `retailzpos-benchmark-report-groundwork-2026-07.md`)
- A shorter, faster-to-ship companion: "How much revenue do independent liquor stores lose to shrinkage?" — one citable stat page, sourced and dated, published ahead of the full report to start earning citations sooner
- "How often does the average convenience store lose a customer without knowing it?" — same fast-companion approach, tied to the win-back/Moolah Points pillar

### 6.5 YouTube video topics (new — Section 5)

- "A Full Day at a Liquor Store Running RetailzPOS" (long-form version of Content Book W10-U3)
- "A Full Day at a Convenience/Smoke Shop Running RetailzPOS" (long-form version of W11-U3)
- "Hard-Block vs. Soft-Block Age Verification, Explained" (direct video companion to the W02-U1 blog)
- "How Case-Break Inventory Actually Works" (video companion to W03-U1)
- "RetailzPOS Full Product Tour" (long-form version of the PRE-U3 teaser)
- "RetailzPOS vs. [Competitor]: An Honest Comparison" — one video per live comparison blog in Section 6.1, same structure (state the verdict in the first 30 seconds, then walk through why)

### 6.6 Reddit/Quora — new question targets beyond the 12 already identified

The existing Reddit/Quora strategy's 12 live Quora questions and target-subreddit list remain the right starting set. Add these as ongoing monitoring keywords once that cadence is running, per Section 2.2's confirmation that Reddit is still worth real effort:
- "case break inventory software"
- "POS audit log compliance"
- "multi-location convenience store POS recommendation"
- "CBD store point of sale" (an intentionally uncontested search — expect low volume, high signal)
- "SMS marketing vape shop compliance"

### 6.7 LinkedIn / editorial byline topics (extends the existing guest-posting strategy)

- "What Independent Retailers Actually Need From POS Software in 2026" (Retail Dive Submit an Opinion angle)
- "The Compliance Gap in General-Purpose POS Systems" (Retail TouchPoints Executive ViewPoints angle, ties to the compliance-authority positioning already established)
- Founder/leadership first-person posts, reusing the voice established in Content Book units W09-U7 and W12-U7 — LinkedIn's own algorithm and its role in the four-surface stack both reward named-author, first-person posts over brand-voice ones

---

## 7. Updated action plan

Treat this as additive to the July 90-day roadmap (`retailzpos-aeo-geo-improvement-strategy-2026-07.md`, Section 9), not a replacement.

| Phase | Focus | New vs. July |
|---|---|---|
| **Now** | Confirm status of the July Phase 1 items (schema live? Reddit/Quora participation started?) before adding new work — don't layer YouTube/entity work on top of an unfinished foundation | — |
| **Weeks 1-2** | Claim/create the RetailzPOS Wikidata entity (Section 2.3); expand Organization schema `sameAs` to include it once live; identify 3-5 existing Wikipedia articles (POS software, retail technology, liquor retail compliance) where a factual, non-promotional RetailzPOS citation could be added by an independent editor | **New** |
| **Weeks 1-4** | Stand up the YouTube channel; publish the first 2 long-form videos from Section 6.5 (product tour, one comparison) with chapters and matching transcripts/blog posts | **New** |
| **Weeks 3-6** | Restructure the 3 audit-failed pages using the 134-167-word answer-block rule (Section 2.4/4.1) — sharper version of the July Tier 2a work | **Sharpened** |
| **Weeks 5-8** | Publish the RetailzPOS vs. KORONA comparison and the CBD best-for page (Section 6.1); publish 2 more long-form YouTube videos | **New content, existing cadence** |
| **Weeks 7-10** | Ship the fast benchmark-companion stat pages (Section 6.4) ahead of the full report | **New** |
| **Weeks 9-12** | Re-run the audit's benchmark queries (per July Section 8) plus two new ones: "RetailzPOS YouTube" and a direct Wikidata/Knowledge Panel check | **Sharpened** |

---

## 8. Measurement — what to add to the existing benchmark

Keep re-running the five queries already established in the July audit, monthly. Add:
- **YouTube-specific:** search "[competitor] vs RetailzPOS" and "best POS for liquor store" inside YouTube itself, and separately ask Perplexity/AI Overviews the same query while checking whether a YouTube result appears in the citation list.
- **Entity check:** search "RetailzPOS" directly in Google and note whether a Knowledge Panel appears, and check the Wikidata entity's inbound Wikipedia links (if any) quarterly.
- **Four-surface scorecard:** a simple present/absent tracker for each of the four surfaces in Section 3, reviewed monthly alongside the existing per-engine scores — the goal isn't a perfect score on any one surface, it's not having a zero on any of the four.

---

## 9. Sources

- [Firebrand, GEO Best Practices for 2026](https://www.firebrand.marketing/2025/12/geo-best-practices-2026/)
- [SEOTuners, Best Practices for Generative Engine Optimization 2026](https://seotuners.com/blog/generative-engine-optimization/generative-engine-optimization-best-practices/)
- [Rankability, LLMS.txt Adoption: 8.7% of the Top 1,000](https://www.rankability.com/data/llms-txt-adoption/)
- [aeo.press, The State of llms.txt in 2026](https://ai.aeo.press/the-state-of-llms-txt-in-2026)
- [Digital Applied, Entity SEO & Knowledge Graph Optimization Guide 2026](https://www.digitalapplied.com/blog/entity-seo-knowledge-graph-optimization-guide-2026)
- [SearchBloom, Entity Optimization for AI Search](https://www.searchbloom.com/ai-seo/inclusion/entity-optimization/)
- [SaaS Intelligence, Reddit's AI Citation Share Just Grew 73%](https://saasintelligence.substack.com/p/reddits-ai-citation-share-just-grew)
- [QuickSEO, How Reddit Affects AI Visibility in 2026](https://quickseo.ai/blog/how-reddit-affects-ai-visibility-2026)
- [Averi, YouTube Beat Reddit for AI Citations — The B2B Pivot](https://www.averi.ai/blog/youtube-beat-reddit-for-ai-citations-the-b2b-pivot)
- [Search Engine Journal, The AI Overviews YouTube Gap](https://www.searchenginejournal.com/the-ai-overviews-youtube-gap-the-platform-your-team-skipped-for-20-years/582702/)
- [Socialync, YouTube Videos in Google AI Overview: Get Cited in 2026](https://www.socialync.io/blog/youtube-videos-google-ai-overview-2026)
- [Digivate, How to Rank in Google AI Overviews in 2026](https://digivate.com/blog/ai/how-to-rank-in-google-ai-overviews-2026)
- [Memeburn, Google AI Overview Statistics 2026](https://memeburn.com/google-ai-overview-statistics/)
- [PartnerStack, Answer Engine Optimization: The Ultimate 2026 Guide for B2B SaaS Teams](https://partnerstack.com/resources/guides/answer-engine-optimization-the-ultimate-2026-guide-for-b2b-saas-teams)
- [Gracker AI, AEO for B2B SaaS: 8 Proven Strategies](https://gracker.ai/blog/aeo-for-b2b-saas-strategies)
