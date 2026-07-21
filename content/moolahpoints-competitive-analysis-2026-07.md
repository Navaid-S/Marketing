# Moolah Points — Competitive Analysis
### Customer Loyalty / Rewards Software Market, with Focus on Liquor, Convenience, Smoke/Vape, and Independent Retail
**Prepared:** July 21, 2026
**Analyst:** Competitive Analyst persona, desk research via public web sources (search-engine index; direct fetch of moolahpoints.com and most competitor sites was blocked by sandbox network policy, so findings rely on indexed/cached page content, third-party review sites, and search snippets rather than first-hand page reads in most cases — see sourcing notes throughout)

---

## 0. Methodology & Sourcing Caveats

This analysis was built entirely from public web search results (Google index via WebSearch). Direct WebFetch of moolahpoints.com and nearly every competitor's own site returned HTTP 403 (sandbox-level block, not specific to any one vendor), so claims about Moolah Points and competitors are drawn from search-result snippets of those companies' own pages, plus third-party sources: review aggregators (Capterra, G2, GetApp, SoftwareAdvice, SaaSWorthy), trade press, and app-store listings. Where only one source supports a claim, it is flagged **[single-source]**. Where pricing could not be found publicly, it is stated as **not publicly disclosed** rather than estimated. No figures in this report are invented — anything that could not be verified is labeled as such.

One important namespacing caution: there is an unrelated company also called "Moolah" (Moolah LLC / moolah.cc) that sells payment processing to dental practices. Some review-site listings ("Moolah Payments," G2/Capterra pages for "Moolah") refer to that company, not Moolah Points the loyalty platform. This report excludes that content and flags it was found during research so it isn't mistakenly attributed to Moolah Points elsewhere.

---

## 1. Moolah Points — What It Actually Is (per moolahpoints.com, current site content)

- Positioned as a **"mobile-first loyalty solution built for how people shop now"** — real-time, phone-based, integrated at checkout rather than via a plastic card or separate app-only experience.
- Core mechanics: points earned automatically at POS, personalized SMS/email campaigns, location-based nudges to bring nearby enrolled customers back into the store, and a merchant portal for campaign building.
- **POS integration** is a headline feature — "plug-and-play integration with most POS systems, especially RetailzPOS." An `/integrations/` page exists on the site (content not readable via fetch, but its existence and the search snippet confirm POS integration is marketed as a distinct capability, not just a RetailzPOS-only add-on).
- **Confirmed sibling relationship with RetailzPOS**: RetailzPOS's own blog describes Moolah Points as "a seamless loyalty program integrated at the heart of RetailzPOS," and positions the pairing as "RetailzPOS processes sales efficiently, while Moolah Points rewards customers instantly." This confirms the products are marketed as a combined POS+loyalty stack from the same company, with Moolah Points also pitched as usable with non-RetailzPOS POS systems.
- **Vertical landing pages** exist for liquor stores, smoke shops, and (per search snippets) convenience stores — each with vertical-specific reward mechanics called out (e.g., liquor: double points for trying a new wine, free tastings; smoke shop: bonus points for bundling a vaporizer with e-liquid; convenience: bonus points for pairing coffee with breakfast items). This is a genuine, real content investment in vertical relevance, not generic templating — a meaningful positioning asset.
- **Consumer-facing network angle**: Moolah Points markets itself to shoppers as a multi-retailer rewards network ("a wide network of retail partners — from liquor shops to salons — where customers can collect points with every interaction," redeemable "in cash, products, or services"), and cites example categories spanning "nail salons in Miami to lifestyle brands in Seattle." This is a real structural choice — Moolah is trying to be a shared consumer rewards network, not just a private-label program per store, which puts it in more direct structural competition with Fivestars and NRS's network products (see §3) than with single-tenant platforms like Smile.io or Zinrelo.
- **Pricing**: not publicly disclosed anywhere found in this research. No pricing page content surfaced in search results; the site appears to be lead-gen / demo-request oriented rather than self-serve. This is itself a data point (see §5).
- **App quality signal [single-source]**: one Apple App Store reviewer described the Moolah Points customer app as "clunky with lots of little peculiarities for how to input data, update your profile, and make selections," and reported having to log in twice. This is a single review and should not be over-weighted, but it's a concrete, sourced data point worth tracking, especially since UX friction in the consumer-facing app directly undermines the "mobile-first, built for how people shop now" positioning claim.
- Review-site presence (Capterra, G2, SoftwareAdvice) for "Moolah Points" specifically appears thin to nonexistent in current search results — most "Moolah" hits on those platforms resolve to the unrelated dental-payments company (see §0). Sparse third-party review volume is itself a competitive signal: most named competitors below have visible Capterra/G2/GetApp review profiles; Moolah Points largely does not yet.

Sources: [moolahpoints.com](https://www.moolahpoints.com/), [Liquor Store Loyalty Program page](https://www.moolahpoints.com/liquor-store/), [Smoke Shop Loyalty Program page](https://www.moolahpoints.com/smoke-shop/), [Integrations page](https://www.moolahpoints.com/integrations/), [RetailzPOS blog: "Love in Every Transaction"](https://www.retailzpos.com/love-in-every-transaction-how-retailzpos-moolah-points-make-this-valentines-day-unforgettable/), [Moolah Points on App Store](https://apps.apple.com/us/app/moolah-points/id6739277541), [Moolah Points on Google Play](https://play.google.com/store/apps/details?id=app.moolahpoints&hl=en_US)

---

## 2. Competitive Landscape Overview

The market breaks into four tiers relevant to Moolah Points' ICP (independent liquor stores, c-stores, smoke/vape shops, general independent retail):

### Tier A — Standalone loyalty platforms with real vertical relevance to regulated/age-restricted retail
These are the closest direct competitors: purpose-built loyalty software, sold independently of a specific POS, with product or content investment specifically in liquor/cannabis/vape/tobacco.
- **Preferred Patron Loyalty**
- **springbig**
- **Loyal-n-Save**
- **bLoyal** (identified via research into the above; not deeply researched but repeatedly surfaced as a regulated-retail loyalty competitor)

### Tier B — General-purpose standalone loyalty platforms for small/local business (not vertical-specific)
Broad SMB loyalty networks that liquor/c-store/smoke shop owners evaluate as generic alternatives.
- **Fivestars**
- **TapMango**
- **Kangaroo Rewards**
- **Belly** — **defunct**; useful only as a cautionary precedent (see §6)

### Tier C — POS-bundled loyalty (the "buy the add-on from your POS vendor" substitute)
This is the most direct decision-level substitute for Moolah Points' RetailzPOS-linked pitch: a retailer already on a POS platform asks "why pay for a separate loyalty product when my POS vendor sells one?"
- **Square Loyalty** (Square POS)
- **Clover Rewards** (Clover POS)
- **Lightspeed Loyalty** (Lightspeed Retail)
- **Toast Loyalty** (Toast POS — restaurant-only, low relevance to this ICP but useful as a bundling-economics comparator)
- **SpotOn Loyalty** (SpotOn POS)
- **Loyverse** (free POS with built-in loyalty)
- **National Retail Solutions (NRS)** — POS bundled with a points/club loyalty program AND its own multi-retailer discount network ("BR Club," Boss Local Shopping App) — see below, this is arguably Moolah Points' single most structurally similar and dangerous competitor
- **Bottle POS** (liquor-specific POS with built-in loyalty)
- **LMS-POS** (liquor-specific POS with built-in loyalty)

### Tier D — Adjacent / indirect competitors (different core motion, occasionally substitutable)
- **Smile.io, Zinrelo, LoyaltyLion** — e-commerce/Shopify-first loyalty; low direct overlap with brick-and-mortar independent retail but relevant if a liquor/smoke shop also sells online
- **Thanx, Punchh (PAR Technology), Paytronix** — enterprise/multi-location restaurant and c-store chain loyalty; priced and built for large chains (Paytronix specifically serves large c-store/fuel chains), not the single-store independent Moolah targets, but Paytronix in particular sets the "state of the art" bar for c-store/fuel loyalty that could move downmarket

Sources: see individual vendor citations in §3–4.

---

## 3. Competitor Profiles

### Tier A: Vertical-relevant standalone platforms

**Preferred Patron Loyalty** ([preferredpatron.com](https://www.preferredpatron.com/))
- Offer: points, tiers, gift cards, milestone/referral/reactivation campaigns, automated SMS/email, from one platform with real-time retention/revenue tracking.
- Vertical fit: has a dedicated **"Regulated Retail Loyalty" line for Cannabis, Vape, Tobacco & Liquor** — including age-aware enrollment, consent-gated "Exclusive Private Messaging" for compliant marketing to regulated-product buyers, and store credit/tier/milestone structures built around regulatory constraints. This is a direct, explicit overlap with Moolah's liquor/smoke-shop focus.
- Integrations: direct POS integrations including Lightspeed Series X, Square POS, and Barnet POS, plus REST API/webhooks — notably **no RetailzPOS integration surfaced in research**.
- Pricing: sources conflict — one source cites $29/mo (Small Business) up to $199/mo (Growth) and custom Enterprise; another cites $79/mo for up to 500 members. Treat as **directionally low-to-mid, exact tier structure unconfirmed** [conflicting sources].
- Differentiator: compliance-first design for age-restricted categories is a genuine, well-documented specialization — this is Moolah's most credible like-for-like competitor on the "built for liquor/vape" claim.
- Weakness/gap: general "regulated retail" framing (spans cannabis/CBD/gaming too) rather than deep liquor-specific or c-store-specific content; not visibly RetailzPOS-integrated.

**springbig** ([springbig.com](https://springbig.com/))
- Offer: SMS-first loyalty/CRM SaaS for cannabis retail; 1,300+ clients, 2,400+ cannabis retail locations cited on their own site. Points-per-dollar and tiered loyalty, subscription program tooling, branded wallet app, referral marketing, segmented SMS/email.
- Vertical fit: cannabis-first; alcohol/vape not confirmed as core focus in this research (a springbig "Alcohol Loyalty" landing page surfaced in search results, suggesting some alcohol-vertical push, but was not independently verified beyond the page title).
- Pricing: reported around **$600/month** base, with a user review citing bill growth from $300–600/mo to $1,600–2,200/mo over a 3-year relationship [single-source review]. This is materially more expensive than the SMB tier of most other competitors in this list.
- Differentiator: deep SMS marketing automation and scale (public company — springbig Holdings, Inc. — with investor-relations disclosures), strong compliance/social-equity program features for cannabis specifically.
- Weakness/gap: pricing appears to run high relative to a single independent liquor/smoke shop's budget, and cost escalation was flagged by at least one reviewer; core DNA is cannabis, not liquor/c-store.

**Loyal-n-Save** ([merchant.loyalnsave.com](https://merchant.loyalnsave.com/))
- Offer: merchant mobile app, points, cash discounts, "Swag Shop," Campaign Builder, "umbrella loyalty program" concept, built-in **age verification** for compliant enrollment.
- Vertical fit: has dedicated pages for liquor store, bar, grocery, and convenience store — i.e., matches Moolah's exact vertical set (liquor + c-store) plus bar/grocery.
- Pricing: has a public pricing page (URL found) but specific numbers did not surface in search results — **not publicly confirmed** in this research.
- Differentiator: age-verification-by-design plus a broad umbrella/multi-vertical structure very close to Moolah's own vertical-page strategy — likely Moolah's closest content/positioning mirror among smaller players.
- Weakness/gap: appears to be a smaller/less-established player (limited press/review footprint found); POS integration breadth unconfirmed.

### Tier B: General SMB loyalty networks

**Fivestars** ([fivestars.com](https://www.fivestars.com/))
- Offer: touchscreen/text-to-join enrollment, customer database, "AutoPilot" automated win-back campaigns, Fivestars Pay (payments + loyalty + marketing automation bundle).
- Scale: self-reported **60 million consumers**, **13,000–14,000+ local businesses** on the network (figures vary slightly by source) — this is the category's dominant consumer-side network, and directly competes with Moolah's own "network of retail partners" pitch to consumers.
- Pricing: Essentials and Pro tiers, **quote-based, not public**.
- Differentiator: scale and brand recognition among SMBs; proven "up to 70% increase in repeat business" claim (Fivestars' own marketing figure, not independently verified).
- Weakness/gap: not liquor/c-store/smoke-shop specific; generic SMB horizontal play. A liquor store owner gets a broad network but no regulated-retail-specific tooling (age-gating, compliant messaging) that Preferred Patron or Loyal-n-Save offer.

**TapMango** ([tapmango.com](https://www.tapmango.com/))
- Offer: branded-to-the-business loyalty + engagement, in-store tablet check-in, memberships/prepaid deals/gift cards, SMS/push/email marketing portal, mobile ordering.
- POS integrations confirmed: **Square, Shopify, Clover, Lightspeed, Vend**.
- Pricing: **not publicly disclosed** in results found.
- Differentiator: strong membership/prepaid-deal monetization model beyond simple points; broad POS integration list.
- Weakness/gap: no liquor/c-store/smoke-shop vertical content surfaced; positioned generically across "any retail store or restaurant."

**Kangaroo Rewards** ([loyalty.kangaroorewards.com](https://loyalty.kangaroorewards.com/))
- Offer: points, tiers, referrals, reviews, gamification, geofencing, white-label branded app, AI-powered campaigns at top tier.
- Pricing: **published and transparent** — Starter $79/mo, Plus $199/mo, Elite $349/mo, custom Enterprise. This is the clearest public pricing ladder found among any competitor in this research, and a notable transparency contrast to Moolah Points' apparent lack of public pricing.
- Integrations: Lightspeed, Shopify confirmed.
- Differentiator: pricing transparency and a full self-serve tier ladder up to a genuinely feature-rich Elite plan (API access, white-label app).
- Weakness/gap: no liquor/regulated-retail specialization found; positioned as a horizontal SMB/franchise platform.

**Belly — defunct.** Acquired by Mobivity in 2018; small-business features discontinued and the consumer app was sunset, reportedly abruptly, leaving merchants without a stated data-export path. Not a current competitive threat, but relevant as a cautionary tale for the category: point-network loyalty products acquired/orphaned can strand a store's customer data with no notice. Worth using as a talking point for platform durability/reliability messaging (see §7). [Wikipedia](https://en.wikipedia.org/wiki/Belly_(loyalty_program)), [loop.fans summary](https://loop.fans/blog/belly-loyalty-program)

### Tier C: POS-bundled loyalty (the real "buy vs. build-in" decision)

**National Retail Solutions (NRS)** ([nrsplus.com](https://nrsplus.com/)) — **flagged as the single most structurally similar and likely highest-priority competitive threat found in this research.**
- NRS is a subsidiary of IDT Corporation (NYSE: IDT), and is explicitly described in search results as serving "thousands of convenience stores, bodegas, liquor stores, tobacco shops, grocery stores, and gas stations" — i.e., **the exact same ICP as Moolah Points/RetailzPOS**, at meaningfully larger scale.
- NRS bundles: points-based loyalty, "exclusive club programs," and — critically — a **multi-retailer discount/rewards network** via the **Boss Local Shopping App** and a **"BR Club" loyalty program serving 3.4 million+ customers** on a nationwide discount network, plus SMS/email marketing via "Contact My Customers," integrated with NRS Pay processing.
- This is nearly a mirror of Moolah Points' own value proposition (POS-integrated points + a cross-retailer consumer network + SMS/email campaigns), but bundled into a POS platform that is already a major, well-capitalized competitor to RetailzPOS itself in the same store categories.
- Weakness/gap (from what's publicly visible): loyalty appears to be a bundled feature of the broader NRS POS/payments ecosystem rather than a deeply configurable, vertical-tuned product in its own right; no evidence found of liquor-specific reward mechanics (e.g., wine-tasting point bonuses) comparable to Moolah's content investment.

**Bottle POS** and **LMS-POS** — both liquor-specific POS systems (direct RetailzPOS competitors) with **built-in loyalty as a bundled feature**, explicitly pitched to avoid needing "expensive third-party marketing platforms" (LMS-POS's own phrasing). This is the clearest articulation of the core objection Moolah Points must overcome: liquor store owners already using a competing POS may be told point-blank that they don't need an add-on loyalty product at all.

**Square Loyalty** — $45–49/month per location (sources vary slightly), card-linked, built into Square POS apps, no extra integration work; strongest in food & beverage (45% of use) and general retail (35%). Cheap, frictionless, but generic — no regulated-retail or liquor-specific mechanics.

**Clover Rewards** — **free at the basic tier**, included with Clover POS plans; points or punch-card mechanics, multi-channel enrollment (app, SMS, email, counter). The "free" price point is a serious pricing floor competitor for any paid standalone product targeting Clover users.

**Lightspeed Loyalty** — gated behind specific Lightspeed Retail pricing tiers ($109–339/mo range depending on source and tier for the base POS product itself); loyalty may require upgrading tiers or negotiating a custom add-on.

**SpotOn Loyalty** — $65/month add-on to SpotOn POS; covers "basic mechanics only — no referral programs or sophisticated behavioral automation" per one review source, and SpotOn itself is flagged as weaker for high-volume multi-location retail inventory needs — relevant mainly as a low-end bundled-price benchmark.

**Loyverse** — POS itself is **free**, with a built-in barcode-card loyalty program at no additional charge; paid add-ons exist for extra functionality. This sets an extremely low price anchor for cost-sensitive independent retailers evaluating "do I need to pay anything at all for loyalty."

**Toast Loyalty** — restaurant-only, $185/month as part of a "Marketing Essentials" bundle on top of base Toast subscription (reported total $254–379/mo minimum). Low direct relevance to liquor/c-store/smoke shop, but a useful data point: even a well-resourced POS vendor prices loyalty as a meaningful incremental spend, and locks the loyalty data to its own hardware/platform — a lock-in risk worth naming when positioning Moolah as POS-agnostic-ish (works with "most POS systems").

### Tier D: Adjacent/enterprise

**Paytronix** — cloud guest-engagement platform serving 1,800+ restaurant and convenience-store brands; sets the technical bar for fuel-plus-in-store loyalty (bundling pump purchases with in-store rewards, subscription programs, cross-brand engagement even for customers loyal to a competing fuel brand). Enterprise/chain-oriented — not a realistic head-to-head for a single independent store today, but the standard a well-funded challenger could bring downmarket.

**Punchh (PAR Technology)** and **Thanx** — both enterprise, custom/sales-led pricing, targeting large multi-location chains (Thanx's stated sweet spot is ~40+ locations). Not realistic competitors for a single independent liquor store or smoke shop, but relevant if RetailzPOS/Moolah ever pursue small regional chains, since these vendors would be the incumbents to displace at that tier.

**Smile.io, Zinrelo, LoyaltyLion** — e-commerce/Shopify-native loyalty. Zinrelo pricing starts around $199/mo for up to 1,000 members and is described as fitting brands at $10M+ revenue; Smile.io has a free tier and scales with order volume. Low direct relevance to in-store liquor/c-store/smoke-shop purchases unless the retailer also runs meaningful e-commerce, but worth monitoring if any of these platforms build POS/in-store modules.

---

## 4. Feature & Positioning Comparison Table

*Note: cells marked "not disclosed" reflect the limits of public search-based research, not confirmation of absence. Pricing figures are as publicly reported at time of research and may reflect promotional or outdated rates — verify directly with vendors before quoting to customers.*

| Vendor | Category | Liquor/C-store/Smoke-shop specific? | POS model | Multi-retailer consumer network? | Publicly disclosed pricing | Key strength | Key gap |
|---|---|---|---|---|---|---|---|
| **Moolah Points** | Standalone loyalty, RetailzPOS-linked | Yes — dedicated liquor, smoke shop, c-store pages w/ vertical mechanics | Integrates with "most POS," strongest tie to RetailzPOS | Yes — markets a cross-retailer rewards network to consumers | Not found publicly | Genuine vertical content depth; mobile-first, no-card design; sibling integration with RetailzPOS | No public pricing; thin third-party review footprint; one reported app UX complaint [single-source] |
| **Preferred Patron Loyalty** | Standalone loyalty | Yes — explicit "Regulated Retail" line (cannabis/vape/tobacco/liquor) | Lightspeed X, Square, Barnet POS; REST API | Not found | $29–199/mo tiers reported (conflicting sources) up to custom Enterprise | Compliance-first design (age-aware enrollment, gated messaging) | No RetailzPOS integration found; broader "regulated retail" framing dilutes liquor focus |
| **springbig** | Standalone loyalty | Cannabis-first; alcohol page exists but unverified depth | Multiple cannabis POS integrations (per other sources) | Not found | ~$600/mo reported, escalating per one review [single-source] | SMS automation depth, scale, public-company resources | Price point likely too high for a single independent store; not liquor-native |
| **Loyal-n-Save** | Standalone loyalty | Yes — liquor, bar, grocery, c-store pages | Not confirmed | "Umbrella loyalty program" language suggests some network element | Pricing page exists, figures not confirmed | Built-in age verification; vertical page parity with Moolah | Limited press/review footprint found |
| **Fivestars** | Standalone SMB network | No | POS-integrated (broad) | Yes — 13,000–14,000+ businesses, ~60M consumers | Quote-based only | Massive network scale and brand recognition | No regulated-retail tooling; generic horizontal fit |
| **TapMango** | Standalone SMB loyalty | No | Square, Shopify, Clover, Lightspeed, Vend | Not confirmed | Not disclosed | Membership/prepaid monetization; broad POS list | No liquor/c-store content found |
| **Kangaroo Rewards** | Standalone SMB loyalty | No | Lightspeed, Shopify | Not confirmed | Published: $79 / $199 / $349/mo + custom | Full public pricing transparency; rich top-tier feature set | No regulated-retail specialization |
| **Belly** | Defunct | No | N/A | Was network-based | N/A | N/A (historical) | Shut down/orphaned merchants — cautionary precedent |
| **NRS (National Retail Solutions)** | POS-bundled + network | Serves same verticals (liquor, c-store, tobacco, bodega) but no liquor-specific reward mechanics found | Full POS/payments platform (IDT-owned) | Yes — Boss Local Shopping App + BR Club, 3.4M+ customers | Bundled with POS/payments, no separate figure found | Massive scale, same exact ICP, well-capitalized parent | Loyalty appears feature-bundled/generic, not deeply vertical-tuned |
| **Bottle POS** | POS-bundled | Yes — liquor-native POS | Liquor-specific POS | No | Bundled into POS pricing | Built-in, no separate purchase decision needed | Not a standalone/portable loyalty product |
| **LMS-POS** | POS-bundled | Yes — liquor-native POS | Liquor-specific POS | No | Bundled into POS pricing | Explicitly marketed as replacing need for 3rd-party loyalty tools | Same lock-in tradeoff as Bottle POS |
| **Square Loyalty** | POS-bundled | No | Square POS only | No | $45–49/mo per location | Cheap, zero extra integration | Generic mechanics, no vertical fit |
| **Clover Rewards** | POS-bundled | No | Clover POS only | No | Free (basic tier) | Free price floor | Generic, basic mechanics |
| **Lightspeed Loyalty** | POS-bundled | No | Lightspeed Retail only | No | Gated behind $109–339/mo POS tiers | Deep POS/inventory integration | Requires specific/higher POS tier |
| **SpotOn Loyalty** | POS-bundled | No | SpotOn POS only | No | $65/mo add-on | Simple, low cost | "Basic mechanics only" per reviewers; weak for multi-location retail |
| **Loyverse** | Free POS + bundled loyalty | No | Loyverse POS only | No | Free (POS + basic loyalty) | Zero cost | Very basic card/barcode mechanics |
| **Toast Loyalty** | POS-bundled | No (restaurant-only) | Toast POS only | No | ~$185/mo bundle (+ base POS $254–379/mo total) | Deep restaurant-specific tooling | Restaurant-only; hardware lock-in |
| **Paytronix** | Enterprise guest engagement | C-store/fuel focus | Multi-POS, enterprise | Some (competing fuel-brand interop) | Not disclosed, enterprise | State-of-the-art fuel+in-store loyalty | Enterprise/chain-scale, not independent-store-accessible |
| **Punchh / Thanx** | Enterprise loyalty | No (restaurant/large retail chains) | Enterprise multi-POS | No | Custom, sales-led | Deep automation, ML-driven | Priced/built for 40+ locations, inaccessible to independents |
| **Smile.io / Zinrelo / LoyaltyLion** | E-commerce loyalty | No | Shopify/e-comm platforms | No | Smile.io has free tier; Zinrelo ~$199/mo+ | Deep e-commerce/DTC fit | Not built for in-store/POS-driven purchase flows |

---

## 5. Where Moolah Points Is Differentiated / Has a Real Edge

1. **Genuine vertical content and mechanic design for liquor, smoke shop, and convenience retail simultaneously.** Most competitors pick one lane: Preferred Patron and springbig lean cannabis/regulated-retail broadly; Loyal-n-Save covers liquor/c-store but with a thinner public footprint; Fivestars/TapMango/Kangaroo are fully horizontal. Moolah appears to be one of very few platforms with dedicated, mechanic-specific content (wine-tasting point bonuses, vaporizer+e-liquid bundling, coffee+breakfast bundling) across all three of Moolah's named ICP verticals at once. This is a real, defensible content and product-thinking edge if the underlying campaign engine actually supports these mechanics natively (not just blog copy) — worth internally verifying, but it's a stronger starting position than most named competitors.

2. **Sibling-product integration with RetailzPOS.** For a retailer already on or considering RetailzPOS, Moolah is the path of least resistance — same vendor relationship, same support line, marketed as "integrated at the heart of RetailzPOS." This mirrors the exact lock-in advantage that Toast, Clover, Square, and NRS enjoy with their own bundled loyalty products, except Moolah is a separate purchase decision rather than a built-in feature — which is both an opportunity (can be sold as more full-featured/purpose-built than a bundled afterthought) and a vulnerability (see §6, item 1).

3. **No-card, checkout-embedded design** ("builds loyalty functionality directly into your checkout system, eliminating the need for separate plastic cards or external apps") is aligned with where the category is heading and matches or beats older card/punch-based competitors (Loyverse's barcode card system, for instance, is a step behind this).

4. **A real consumer-facing multi-retailer network claim**, which most standalone vertical competitors (Preferred Patron, springbig, Loyal-n-Save, Bottle POS, LMS-POS) do not appear to offer — those are single-tenant, store-branded programs. Only Fivestars and NRS's Boss/BR Club clearly compete on this specific dimension. If Moolah's network has real cross-store redemption density in liquor/c-store/smoke-shop categories specifically (unverified — network size not found in public sources), that's a differentiated wedge versus single-tenant competitors, though it trails Fivestars (13,000+ businesses, ~60M users) and NRS (3.4M+ customers) badly on scale if compared head-to-head as a network play.

## 6. Where Competitors Are Stronger / Moolah Points Has Exposure

1. **The single biggest threat is NRS**, not any of the standalone loyalty vendors. NRS sells to the identical ICP (liquor, c-store, bodega, tobacco, gas) at large scale (IDT-backed), bundles POS + payments + loyalty + a multi-retailer discount network (Boss/BR Club, 3.4M+ customers) into one relationship, and is a direct competitor to RetailzPOS itself. A retailer choosing between RetailzPOS+Moolah vs. NRS is choosing between two vertically-integrated stacks — this is an existential-tier competitive question for the parent company, not just a "which loyalty app" question, and should likely be flagged up to product/GTM leadership rather than treated as a marketing messaging problem alone.

2. **"Why pay extra when my POS already has it" is a live objection**, and it's strong: Clover Rewards is free at the basic tier; Loyverse is free entirely; Bottle POS and LMS-POS (both liquor-specific POS competitors to RetailzPOS) explicitly market their bundled loyalty as replacing the need for "expensive third-party marketing platforms." Moolah has to justify a separate line-item against multiple free-or-bundled alternatives, and — since no Moolah Points pricing is public — cannot currently make that value case at the point of search/comparison the way Kangaroo Rewards (fully public $79/$199/$349 ladder) or even Square/Clover/SpotOn (public per-location pricing) can.

3. **Pricing opacity is a competitive gap, not just an omission.** In a market where Kangaroo Rewards, Square Loyalty, Clover Rewards, SpotOn, and Toast all publish clear pricing, an independent liquor/smoke shop owner comparison-shopping will more easily rule Moolah Points in or out if pricing is visible. A sales-assisted/quote-only model can work for higher-touch categories (it works for Thanx and Punchh at the enterprise tier), but at the single-independent-store tier, opacity more often reads as "probably expensive" or simply causes the prospect to bounce to a competitor with visible pricing.

4. **Preferred Patron and springbig have more explicit regulatory/compliance feature depth** for age-restricted product marketing (age-aware enrollment, consent-gated messaging specifically built for cannabis/vape/liquor). If Moolah's SMS/email campaign tooling doesn't have comparably explicit compliance guardrails documented, that's a credibility gap with more sophisticated liquor/smoke-shop buyers who are wary of TCPA/age-restricted marketing risk.

5. **Thin third-party review/proof footprint.** Nearly every competitor in this research (Fivestars, TapMango, Kangaroo, springbig, Preferred Patron, Square Loyalty, Clover Rewards) has a visible, populated Capterra/G2/GetApp/SoftwareAdvice profile with review counts and star ratings. Moolah Points does not appear to have a comparable public review presence yet (research turned up essentially none that weren't for the unrelated dental-payments "Moolah"). For a prospective buyer doing typical vendor diligence, this absence is itself a negative signal versus better-reviewed alternatives.

6. **One sourced but single-instance UX complaint** about the consumer app being "clunky" with login friction — worth verifying internally (is this outdated / fixed / isolated?) since it directly cuts against the "mobile-first, built for how people shop now" positioning claim if it's representative rather than an outlier.

7. **Scale disadvantage versus network-model competitors.** If Moolah's pitch to consumers depends partly on network effects (redeem points at other participating stores), it is competing against Fivestars (13,000+ businesses) and NRS's Boss/BR Club (3.4M+ customers) with, as far as public sources show, an unstated and likely much smaller number of participating locations. Network-effect products are winner-take-most; being a distant third network is a structurally weaker position than being the best single-tenant, store-branded product in a vertical.

## 7. Strategic Recommendations

1. **Publish pricing, at least directionally.** Even a simple published tier (as Kangaroo Rewards does) removes the biggest single friction point versus comparison-shopping competitors and signals confidence. If usage-based or POS-tied pricing makes a flat public number impractical, publish a "starting at $X/mo" anchor the way SpotOn ($65) and Square ($45) do.

2. **Lead with the RetailzPOS bundle as the primary offer, and make the "why not just use my POS's bundled loyalty" objection explicit in sales/marketing content** — directly naming and out-featuring the free/bundled alternatives (Clover Rewards, Loyverse, Bottle POS, LMS-POS) on the specific dimensions Moolah wins on: vertical reward mechanics, cross-store network redemption, and no-card mobile-first design. Don't let the comparison stay implicit — retailers will make it themselves via search, and Moolah should control the framing (comparison/alternatives content, similar to how loop.fans and merchantmaverick already do this for competitors).

3. **Treat NRS as the primary strategic competitor, not the standalone loyalty vendors.** Since NRS competes at the POS+payments+loyalty+network bundle level against RetailzPOS+Moolah as a combined stack, competitive response should be coordinated between RetailzPOS and Moolah Points messaging — e.g., emphasizing liquor/smoke-shop-specific reward mechanics and campaign sophistication that NRS's more generic "club" loyalty doesn't appear to match, since out-featuring NRS on loyalty depth may be more achievable than out-scaling its POS distribution.

4. **Build and surface compliance/age-gating features explicitly**, matching or exceeding Preferred Patron's and Loyal-n-Save's public messaging on age-aware enrollment and consent-gated SMS/email for regulated products. This directly matters for liquor and smoke/vape retailers who face real TCPA and age-verification exposure, and currently only Tier A competitors are visibly claiming this — it's an open positioning lane Moolah can occupy without much price competition.

5. **Invest in third-party review presence** (Capterra, G2, GetApp) — claim/verify the correct listing (distinct from the unrelated dental-payments "Moolah"), and actively solicit reviews from existing RetailzPOS+Moolah customers. This is a low-cost fix for a real, visible gap versus nearly every competitor profiled.

6. **Quietly audit the consumer app UX** referenced in the single sourced App Store complaint. If representative, this is a real risk to the "mobile-first, built for how people shop now" positioning claim and should be resolved before it's amplified by a competitor or review site doing exactly this kind of comparison research.

7. **Consider whether to compete on network scale or concede it.** Moolah cannot realistically out-scale Fivestars (13,000+ businesses) or NRS (3.4M+ customers) as a cross-retailer network in the near term. A more defensible strategy may be to de-emphasize the "shop at other Moolah stores too" network pitch in favor of doubling down on being the best single-tenant, vertical-specific program (à la Preferred Patron's compliance focus or Loyal-n-Save's vertical page parity) where Moolah's real content/mechanic advantage already lives — rather than competing head-on in a category (network scale) where two much larger players already have a multi-year head start.

---

## 8. Open Questions / Recommended Follow-Up (Not Answerable from Public Search Alone)

- Actual Moolah Points pricing, contract terms, and whether it's sold only bundled with RetailzPOS or also as a true standalone product for non-RetailzPOS merchants (site references "most POS systems" but only RetailzPOS integration was concretely confirmed in research).
- Real participating-location count for Moolah's consumer network, to size it against Fivestars/NRS.
- Whether the single App Store UX complaint is representative or an outlier — needs internal QA/support-ticket review, not further web search.
- Direct competitive win/loss data from RetailzPOS/Moolah sales conversations against NRS, Bottle POS, and LMS-POS specifically — this research could only establish that these are plausible competitors based on public product overlap, not actual deal-level outcomes.
- bLoyal, Cheers POS, and Bepoz surfaced repeatedly in adjacent searches as liquor-store loyalty/POS players but were not deeply researched in this pass — worth a follow-up round if a more exhaustive Tier A/C list is needed.

---

*All claims above are sourced to the specific pages/searches cited inline. Where a figure could not be verified, it is explicitly marked as unconfirmed, conflicting, or not publicly disclosed rather than estimated.*
