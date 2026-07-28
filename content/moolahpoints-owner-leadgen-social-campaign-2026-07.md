# Moolah Points — Store Owner Lead-Gen Social Campaign
**Prepared:** July 28, 2026
**Scope:** Social media content and paid campaign structure aimed at the B2B buyer — the liquor/convenience/smoke-vape store owner who would purchase Moolah Points — built to generate qualified leads (demo requests, trial sign-ups), not general brand awareness.

**How this is different from what's already been built:** Every other piece of Moolah Points social content in this project (`social-media-trending-topics-2026-07.md`, the static image post batches, the Gen Z personas doc) targets the **shopper** who enrolls in a loyalty program at the register. This document targets the **owner who decides to buy the software in the first place** — the three personas defined in `moolahpoints-owner-buyer-personas-2026-07.md`: the Compliance-Conscious Independent (liquor), the Volume Juggler (convenience), and the Scrutinized Specialist (smoke/vape). Platform choice, tone, and funnel logic are all built around that buyer, not the shopper — this is a genuinely different audience with different habits, so it gets a different plan rather than a reskin of the consumer content.

---

## 1. Platform strategy — where this buyer actually is, and why

The persona doc already established this buyer's trust sources: trade press, POS/distributor reps, and word of mouth from other independent owners — not the TikTok/Reels-first world the Gen Z consumer personas live in. That holds up against broader platform data:

**Facebook is the primary channel, both organically and for paid.** 96% of small business owners report using social media to market their business, and Facebook remains the single most-used platform for it — 86% of marketers use it, and 51% of B2C-focused marketers call it their most important platform. [Source: [Sprout Social, 2026 Social Media Statistics](https://sproutsocial.com/insights/social-media-statistics/), [Tabula Agency, Instagram vs LinkedIn vs Facebook for Small Business 2026](https://tabula.agency/blog/instagram-vs-linkedin-vs-facebook-small-business-2026/)] It's also where this specific buyer already congregates: real, active Facebook groups exist for exactly this audience — an Arizona gas station/liquor store/convenience store owners group, the Boston Convenience Store Owners Association, and the Asian American Convenience Store Association (AACSA) all have an organized Facebook presence. [Source: [Arizona Gas Station/Liquor Store/Convenience Store Owners group](https://www.facebook.com/groups/410547756636319/), [Marsello — Communities for Retail Business Owners](https://resources.marsello.com/blog/top-communities-for-independent-retailers), [Sprockets — Convenience Store Associations](https://sprockets.ai/blog/convenience-store-associations/)] Cost also favors Facebook: average cost-per-lead across Facebook Ads is **$27.66**, and retail specifically sits toward the lower end of that range compared to high-competition categories like finance or legal. [Source: [AdManage.ai, 2026 Facebook CPL Benchmarks](https://admanage.ai/blog/facebook-ads-cost-per-lead-benchmarks)]

**LinkedIn is a secondary, higher-intent channel — not the volume driver.** Among B2B marketers specifically, 44% cite LinkedIn as their key channel and 85% call it their highest-performing one. [Source: [Tabula Agency](https://tabula.agency/blog/instagram-vs-linkedin-vs-facebook-small-business-2026/)] But it's materially more expensive: native Lead Gen Forms run a median CPL of **$75-110** across B2B broadly, and cost rises for smaller target companies specifically — **roughly $146 CPL for businesses in the 2-50 employee range**, which is exactly this buyer's company size. [Source: [Cleverly, LinkedIn Lead Generation Cost 2026](https://www.cleverly.co/blog/linkedin-lead-generation-cost), [StackMatix, LinkedIn Ads CPL Benchmarks](https://www.stackmatix.com/blog/linkedin-ads-cost-per-lead-benchmarks)] Held against the buyer persona's own budget ceiling ($45-100/month for the product itself, per the persona doc), a $100+ CPL only pencils out for the highest-intent, bottom-funnel offers — not broad awareness. LinkedIn's real value here is precision job-title/industry targeting (Owner, General Manager, Proprietor in Retail/Tobacco/Food & Beverage), which makes it the right tool for a narrow, well-targeted demo-request push, not a content-volume channel.

**Instagram is tertiary — credibility, not discovery.** This buyer skews 40+ (64% of store owners are 40 or older, per the buyer persona doc), which is a materially older audience than Instagram's core usage base. Use it to mirror proof-point content (real or illustrative testimonials, behind-the-counter footage) for owners who click through from a Facebook or LinkedIn ad to check the brand is legitimate — not as a primary discovery surface.

**What this means practically:** Facebook (organic group participation + paid Lead Ads) carries the bulk of volume and cost-efficiency. LinkedIn Sponsored Content with Lead Gen Forms runs as a smaller, precisely-targeted budget line for bottom-funnel demo requests. Instagram exists as a supporting proof layer, not a standalone campaign.

---

## 2. Funnel architecture

| Stage | Goal | Primary channel | Content type |
|---|---|---|---|
| **TOFU** — Awareness | Get in front of owners who don't yet know they have a problem worth solving | Facebook organic + broad paid reach | Relatable pain-point posts, compliance-authority education |
| **MOFU** — Consideration | Make the "punch card is fine" belief feel incomplete | Facebook paid (retargeting website/page visitors) + LinkedIn | Problem/solution posts, proof, ROI framing |
| **BOFU** — Conversion | Capture a lead with minimal friction | Facebook Lead Ads + LinkedIn Lead Gen Forms | Gated lead magnets, demo requests, bundle offers |

**Why native lead forms over landing pages:** Native Lead Gen Forms (pre-filled with the platform's own profile data) reduce cost-per-lead by 25-35% versus sending traffic to an external landing page, and convert at roughly 13% versus 2.35% for off-platform pages. [Source: [StackMatix, LinkedIn Ads CPL Benchmarks](https://www.stackmatix.com/blog/linkedin-ads-cost-per-lead-benchmarks)] Given this buyer's low tech confidence and limited time (established in the persona doc), every extra click or page load between "interested" and "submitted" is a real drop-off risk — use Meta Lead Ads and LinkedIn Lead Gen Forms as the default capture mechanism for BOFU content, not a "learn more" link to a website form.

**Lead routing:** Every form should feed directly into the CRM already recommended in `crm-recommendation-ads-marketing-sales-2026-07.md`, with UTM parameters distinguishing platform, funnel stage, and vertical (e.g. `utm_source=facebook&utm_medium=leadad&utm_campaign=liquor_bofu_demo`) so downstream reporting can show which vertical and funnel stage is actually converting to paying accounts, not just leads.

---

## 3. Lead magnets

Gating content behind a form is what turns a scroll-past into a lead. Four magnets, ranked by funnel fit:

1. **The Silent Churn Calculator** *(BOFU, highest-intent)* — A simple interactive tool: owner enters average ticket size and estimated monthly customer count, and it estimates revenue at risk from the **30% of churn that happens silently** (a customer just stops coming, no complaint, no signal — cited in the market research and buyer persona docs). This directly targets the core anxiety every persona shares: they're flying blind on their own repeat-customer base. Strongest single lead magnet in this plan because it makes the abstract problem into a dollar figure specific to their store.
2. **"State of Independent Retail Loyalty 2026" benchmark report** *(TOFU/MOFU)* — Addresses a real, confirmed content gap: no published loyalty-adoption or ROI benchmark exists specifically for liquor, convenience, or smoke/vape retail (flagged as whitespace in `moolahpoints-market-research-2026-07.md`, Section 4d). Publishing this positions Moolah Points as the category's data source, not just a vendor — and doubles as a durable backlink asset, the same logic already applied to the RetailzPOS benchmark report groundwork.
3. **POS Refresh Checklist: What to Ask Before You Switch** *(MOFU/BOFU)* — Targets the single biggest purchase trigger identified across all three personas: a POS replacement moment. Positions Moolah Points as the loyalty layer to add "while you're already doing this," compatible with either RetailzPOS or PtechPOS depending on the owner's vertical.
4. **Free personalized demo** *(BOFU, standard)* — The default fallback CTA on every bottom-funnel post, for owners ready to talk without needing a gated asset first.

---

## 4. Paid campaign structure

### 4a. Meta (Facebook + Instagram) — primary budget

**Campaign objective:** Leads (native Lead Ads), not Traffic or Awareness — optimizing for the actual conversion event from day one avoids paying for clicks that were never going to convert.

**Ad set structure — split by vertical, not by funnel stage**, since the objections and proof points differ meaningfully by persona:

- Ad Set 1: Liquor store owners
- Ad Set 2: Convenience store owners
- Ad Set 3: Smoke/vape shop owners

**Targeting per ad set:**

- Age 35-60 (matches the 64%-are-40+ demographic reality without excluding the younger tail of owners)
- Detailed targeting: "Small business owner," "Retail management," job title fields where available, layered with category-specific interests (liquor: wine/spirits industry pages; convenience: NACS-adjacent pages; smoke/vape: vape/smoke shop trade pages)
- Geography: start metro-by-metro rather than national — a $27-ish average CPL budget goes further concentrated in a few launch metros than spread thin nationwide, and it lets the sales/onboarding team handle volume realistically at launch
- Custom Audiences: website visitors to the RetailzPOS/PtechPOS/Moolah Points blog and comparison content (warm retargeting pool), plus lookalike audiences built from existing paying accounts once there's a base list large enough to model against

**Creative format:** Static image and short-form video both work, but given the audience skews older and time-poor, prioritize **static image + carousel** (clear, scannable, no autoplay dependency) over short-form video, with video reserved for testimonial/proof content specifically.

### 4b. LinkedIn — secondary, precision channel

**Objective:** Lead Generation with native Lead Gen Forms, reserved for BOFU offers only (demo requests, the POS Refresh Checklist) — not top-of-funnel awareness content, given the CPL economics in Section 1.

**Targeting:**

- Job titles: Owner, Proprietor, General Manager, Store Manager
- Industries: Retail, Food & Beverage Services, Tobacco
- Company size: 1-50 employees (matches the CPL benchmark segment and this buyer's real company size)
- Consider excluding job seekers/students via LinkedIn's audience exclusions, a common filter to keep spend on decision-makers only

**Budget allocation guidance:** Given LinkedIn's ~$100-150+ realistic CPL for this segment against a product with a $45-100/month price point, LinkedIn should run at a fraction of the Meta budget (a reasonable starting split is roughly 80/20 Meta/LinkedIn) until CPL-to-paying-customer data proves it earns a larger share. **[ESTIMATE]** — this split is a reasoned starting point, not a benchmarked figure; adjust once real conversion data comes in.

### 4c. Organic Facebook group participation

The real owner-specific groups identified in Section 1 are a genuine organic opportunity, but they carry the same risk flagged earlier in this project for Reddit's r/POS: most owner communities have real or unwritten norms against overt vendor self-promotion, and getting that wrong burns the account's credibility in a tight-knit community. **Before posting in any specific group, read its posted rules directly** — this document does not assume specific rules for the Arizona, Boston, or AACSA groups since they weren't reviewed firsthand. The safer default posture, consistent with how this project handled Reddit: participate as a genuinely helpful presence (answering real questions about loyalty, compliance, or POS topics) before ever mentioning the product by name, and look for any group-sanctioned "vendor showcase" thread or sponsored-post option rather than posting cold pitches into the general feed.

---

## 5. Post copy — ready to use, organized by funnel stage

Each post below lists platform, funnel stage, vertical fit, the copy itself, CTA, and a visual direction note tied to Moolah's established brand system (ledger/receipt concept, Ledger Cream/Ink Charcoal/Moolah Gold/Token Teal/Cellar Burgundy, Anton/Nunito/Space Mono — see `moolahpoints-brand-guide-2026-07.html`).

### TOFU — Awareness

**Post 1 — "The customers you don't think about"**
*Platform: Facebook (organic + paid) | Vertical: All | Format: Static image*

> Copy: "You know your regulars by name. But do you know who *stopped* being a regular — and when? 30% of customer churn happens silently. No complaint. No goodbye. They just... stop showing up. If you don't have a way to see that, you're not behind on marketing. You're missing data you didn't know you needed."
> CTA: "See what you're missing →" (links to Silent Churn Calculator)
> Visual: Ledger-style receipt graphic with a row of customer visits fading out mid-list — Ink Charcoal on Ledger Cream, Moolah Gold accent on the CTA.

**Post 2 — "Built for stores that sell what needs an ID check" (Liquor + Vape only)**
*Platform: Facebook | Vertical: Liquor, Smoke/Vape | Format: Static image*

> Copy: "Marketing alcohol or tobacco isn't like marketing a coffee shop. One wrong SMS and you're not just annoying a customer — you're a compliance headache waiting to happen. Moolah Points is built loyalty-first for stores in regulated categories, with messaging designed around TCPA, SHAFT, and age-verification requirements from day one — not bolted on after the fact."
> CTA: "See how compliance-safe loyalty works →"
> Visual: Cellar Burgundy header band (liquor) or Token Teal (vape framing), ledger-line list of compliance checkmarks in Space Mono.

**Post 3 — "One system, every category" (Convenience only)**
*Platform: Facebook | Vertical: Convenience | Format: Static image*

> Copy: "Lottery. Coffee. Snacks. Cigarettes. Energy drinks. Your basket has more categories than almost any retail format out there — and your loyalty program should keep up, not treat every purchase the same. Moolah Points builds reward logic around what your customers actually buy."
> CTA: "See how it works for c-stores →"
> Visual: Receipt-style itemized list showing varied categories each earning points differently.

**Post 4 — Educational / compliance authority (native, no hard CTA)**
*Platform: Facebook + LinkedIn | Vertical: All (post separately per vertical if budget allows) | Format: Carousel*

> Copy (slide 1): "Quick question: does your SMS marketing know what SHAFT is?"
> (slide 2-4): brief explainer on SHAFT/TCPA basics, framed as owner education, not a pitch
> (final slide): "This is the kind of thing we build into Moolah Points by default. More on that →"
> CTA: "Read the full compliance guide" (links to Blog #2)
> Visual: Space Mono-heavy, ledger/checklist aesthetic — this one should read as genuinely useful reference content, shareable on its own merits.

### MOFU — Consideration

**Post 5 — "The punch card isn't wrong. It's just incomplete."**
*Platform: Facebook (retargeting) | Vertical: All | Format: Static image*

> Copy: "Your punch card works — for the customers who are already standing in front of you. It doesn't do anything for the ones who quietly stopped coming six weeks ago. Moolah Points isn't here to replace the relationship you've built. It's here to catch the customers you can't keep in your head."
> CTA: "See what you're not seeing →"
> Visual: Split visual — a worn paper punch card on one side, a Moolah Points ledger/receipt view on the other, Moolah Gold divider line.

**Post 6 — ROI framing / cost comparison**
*Platform: Facebook + LinkedIn | Vertical: All | Format: Static image (simple comparison table)*

> Copy: "A punch card costs nothing and does almost nothing. A loyalty platform costs $45-100/month and — if it's built right — pays for itself the first month it brings back customers you'd otherwise have lost for good. The real question isn't 'can I afford this.' It's 'can I afford to keep not knowing who's leaving.'"
> CTA: "Run your own numbers →" (links to Silent Churn Calculator)
> Visual: Simple two-column comparison, ledger-table styling, Space Mono figures.

**Post 7 — Illustrative proof / scenario post**
*Platform: Facebook + Instagram | Vertical: Rotate by vertical | Format: Carousel or short video*

> Copy: "*Illustrative example, not a specific customer.* A liquor store owner notices a regular hasn't been in for weeks. No way to know if that's normal or a warning sign — until now. Moolah Points flags lapsed high-value customers automatically, so a quick win-back offer goes out before that customer becomes a competitor's regular instead."
> CTA: "See how win-back campaigns work →"
> Note: Replace with a real customer story the moment one exists — label clearly as illustrative until then, consistent with how RetailzPOS blog content handles this.

**Post 8 — "While you're already doing this" (POS refresh trigger)**
*Platform: Facebook + LinkedIn | Vertical: All | Format: Static image*

> Copy: "Replacing your POS system? That's exactly the moment to add real loyalty tracking — not six months later as a separate project. Moolah Points runs alongside RetailzPOS or PtechPOS, so it's one setup, not two."
> CTA: "Get the POS Refresh Checklist →" (gated lead magnet)
> Visual: Ledger-style checklist graphic, Moolah Gold checkmarks.

### BOFU — Conversion

**Post 9 — Silent Churn Calculator (flagship lead magnet push)**
*Platform: Facebook Lead Ads + LinkedIn Lead Gen Form | Vertical: All | Format: Static image*

> Copy: "How much revenue are you losing to customers who just... stopped coming back? Most owners have no idea — because there's no punch card for the customers who disappear. Find out in under a minute."
> CTA: "Calculate your silent churn →" (native lead form: name, email, phone, store type)
> Visual: Bold, single-focus creative — a dollar figure partially obscured/faded, Cellar Burgundy urgency accent.

**Post 10 — Benchmark report gate**
*Platform: Facebook + LinkedIn | Vertical: All | Format: Static image*

> Copy: "No one's ever published real loyalty benchmarks for liquor, convenience, and smoke shop retail — until now. See how your store's likely repeat-customer rate compares, based on the first report built specifically for this industry."
> CTA: "Get the free report →" (native lead form)
> Visual: Report cover mockup in the Moolah brand system, ledger/receipt motif.

**Post 11 — Direct demo request**
*Platform: Facebook Lead Ads + LinkedIn Lead Gen Form | Vertical: All (swap first line by vertical) | Format: Static image*

> Copy: "See Moolah Points running on a store like yours — 15 minutes, no pressure, no generic sales deck. Just a walkthrough of what it actually looks like for a [liquor store / convenience store / smoke shop]."
> CTA: "Book my demo →" (native lead form)
> Visual: Clean, minimal — this is the highest-intent post, no need for elaborate creative competing with the CTA.

**Post 12 — Retargeting close (for warm audience only — website/engaged-viewer custom audience)**
*Platform: Facebook + Instagram | Vertical: All | Format: Static image*

> Copy: "Still thinking it over? Fair — it's your business. Here's the short version: Moolah Points shows you who's about to stop coming back, before they actually do, and it's built to run itself once it's set up. 15 minutes to see it in action."
> CTA: "Book my demo →"
> Visual: Warm, low-pressure tone — avoid urgency/scarcity tactics here specifically, since this buyer has already been burned by aggressive software sales pitches (per the persona doc's software-fatigue finding) and a pushy retargeting ad will read as exactly the pattern they're wary of.

---

## 6. Cadence and measurement

**Posting cadence (organic):** 2-3 posts/week on the Moolah Points Facebook business page, rotating TOFU and MOFU content; save BOFU content primarily for paid placement rather than organic feed (gated lead-magnet posts perform better as intentional ads than as organic posts competing with a feed algorithm that deprioritizes link-out content).

**Paid cadence:** Always-on Meta Lead Ads campaign at a modest baseline budget, with LinkedIn running as a smaller, consistent secondary line rather than a stop-start campaign — LinkedIn's lead form performance benefits from sustained delivery rather than short bursts, per the same CPL research cited in Section 1.

**What to watch, beyond CPL:** Cost-per-lead is a vanity number if lead quality is bad — the persona doc and this campaign both exist to serve one real number: **cost per demo-to-paying-customer**, by vertical and by platform. Track that in the CRM (per `crm-recommendation-ads-marketing-sales-2026-07.md`) from month one, not just ad-platform-reported CPL, since a cheap Facebook lead that never converts is worse than a pricier LinkedIn lead that does.

**A caveat worth stating plainly:** the $335/day → $2.3M-in-sales Facebook Ads case study sometimes cited in retail-and-POS advertising discussions [Source: [Merge Stream, Facebook Ads for In-Store Sales](https://mergestream.com/blogs/content/how-to-run-facebook-ads-for-in-store-sales)] is a **B2C foot-traffic case study for a jewelry retailer**, not a B2B software lead-gen campaign — it's included here only as evidence that Facebook Ads integrate well with POS data generally, not as a directly comparable benchmark for this campaign's expected returns. Don't set expectations against it.

---

## 7. Sources consulted

- [Sprout Social — 2026 Social Media Statistics](https://sproutsocial.com/insights/social-media-statistics/)
- [Tabula Agency — Instagram vs LinkedIn vs Facebook for Small Business 2026](https://tabula.agency/blog/instagram-vs-linkedin-vs-facebook-small-business-2026/)
- [AdManage.ai — 2026 Facebook Ads CPL Benchmarks](https://admanage.ai/blog/facebook-ads-cost-per-lead-benchmarks)
- [Cleverly — LinkedIn Lead Generation Cost 2026](https://www.cleverly.co/blog/linkedin-lead-generation-cost)
- [StackMatix — LinkedIn Ads Cost Per Lead Benchmarks](https://www.stackmatix.com/blog/linkedin-ads-cost-per-lead-benchmarks)
- [Clever Zebo — B2B SaaS LinkedIn Ads CPL Benchmark](https://cleverzebo.com/benchmarks/b2b-saas/linkedin/)
- [Arizona Gas Station/Liquor Store/Convenience Store Owners (Facebook group)](https://www.facebook.com/groups/410547756636319/)
- [Marsello — Communities for Retail Business Owners](https://resources.marsello.com/blog/top-communities-for-independent-retailers)
- [Sprockets — Convenience Store Associations With the Best Resources](https://sprockets.ai/blog/convenience-store-associations/)
- [Merge Stream — How to Run Facebook Ads for In-Store Sales](https://mergestream.com/blogs/content/how-to-run-facebook-ads-for-in-store-sales)
- Internal: `moolahpoints-owner-buyer-personas-2026-07.md`, `moolahpoints-market-research-2026-07.md` (Section 4d), `crm-recommendation-ads-marketing-sales-2026-07.md`, `moolahpoints-brand-guide-2026-07.html`

*Platform benchmark figures (CPL, conversion rates) are industry-wide 2026 averages, not Moolah-Points-specific results — treat Section 4's budget guidance as a starting point to test against, not a guaranteed outcome. Update this document once real campaign data exists.*
