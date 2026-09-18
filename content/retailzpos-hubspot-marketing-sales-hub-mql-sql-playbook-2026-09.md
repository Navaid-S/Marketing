---
title: "RetailzPOS — HubSpot Marketing Hub & Sales Hub Playbook"
subtitle: "MQL/SQL tracking and Marketing–Sales alignment · Prepared September 2026"
---

# 0. Where this starts from — not a from-scratch adoption

Two things already exist and this builds directly on them, not around them:

1. **`crm-recommendation-ads-marketing-sales-2026-07.md`** (July 2026) compared HubSpot, Zoho, and Freshsales, and flagged the decisive fact that shapes everything below: **"Marketing Qualified Lead" is a native, built-in lifecycle stage in HubSpot's data model** — not a custom field you have to invent. RetailzPOS is on the **Starter Customer Platform bundle** (Marketing Hub Starter + Sales Hub Starter + Service Hub Starter, one shared contact database, ~$15–20/seat/month).
2. **`retailzpos-sales-hub-pitch-2026-07.pptx`** confirms Sales Hub Starter is already live/piloting with the sales team — Full Contact Timeline, Email Tracking, Templates & Snippets, Click-to-Call, Meeting Scheduler, and a Deal Pipeline Board are in active use. That deck was also explicit about what **isn't** included yet: Sequences, Forecasting, and Playbooks & Reporting are gated to Sales Hub Professional, and Phase 2 was framed as something earned by pilot results, not assumed on day one.

This document carries that same discipline forward into Marketing Hub and the MQL/SQL handoff specifically: what's genuinely usable today at Starter, what requires a Professional-tier jump, and — since RetailzPOS's whole positioning is "we don't oversell what isn't built yet" — no claim below skips that distinction.

---

# 1. What Marketing Hub actually does for RetailzPOS, tier by tier

## Already live or immediately usable at Starter

- **Native UTM capture on every form and landing page** — every demo request, benchmark-report download, or newsletter signup already gets tagged with source campaign automatically. This is genuinely turnkey and needs no new setup.
- **One shared contact record across Marketing, Sales, and Service Hub** — this is the actual mechanism that makes "Marketing and Sales working in tandem" possible at all, and it's live at Starter, not gated to Professional. A rep opening a lead in Sales Hub sees the exact same contact timeline — every email, form fill, and page view — that Marketing sees. Section 4 builds directly on this.
- **Basic email sends and simple, single-step automation** — a "form submitted → send this one email" workflow works today. What doesn't work yet is a multi-step nurture sequence branching on behavior (see below).
- **List segmentation** by persona, vertical, and content engaged with — enough to build a manual or semi-manual MQL view even before any scoring engine is turned on.

## Requires a Marketing Hub Professional upgrade ($890/month for 2,000 contacts, per the July memo's figures — verify current pricing before committing)

- **True lead scoring** — a point-based engine that increments automatically as a contact engages (visits the pricing page, downloads the benchmark report, watches 50%+ of the product tour) and promotes them to MQL on its own.
- **Multi-step, behavior-triggered nurture workflows** — "if they downloaded the benchmark report AND haven't booked a demo in 14 days, send this specific follow-up" — Starter only handles one-off sends, not branching logic.
- **Progressive profiling** — forms that stop re-asking for information already on file, which matters once the content library is being used repeatedly by the same returning visitor.
- **Multi-touch attribution reporting** — connecting a closed deal back to every piece of content and every one of the four AI-search citation surfaces (editorial, YouTube, Reddit/Quora, LinkedIn) that touched it along the way, not just the last click.

**The honest read, consistent with how the Sales Hub pilot was framed:** none of Section 2's design below requires Professional to start. It requires it to stop being partly manual. That's a real, deliberate distinction — build the system on Starter first, and let actual lead volume be the thing that proves Professional is worth the jump, the same logic the July memo already used to justify starting cheap and the Sales Hub deck used to frame Phase 2.

---

# 2. Defining MQL and SQL for RetailzPOS specifically — not generic definitions

Generic MQL/SQL definitions are exactly what current best practice warns against — over 60% of B2B teams define MQL too broadly ("downloaded anything + has a work email"), which quietly wrecks MQL→SQL conversion rates. RetailzPOS already has the real inputs to define this precisely: five named personas, five messaging pillars, a mindset ladder, and a confirmed true-north metric (demo requests) from the 90-Day Marketing Plan and Brief.

## Lifecycle stage mapping

| HubSpot lifecycle stage | RetailzPOS mindset-ladder equivalent | What moves someone here |
|---|---|---|
| Subscriber | Unaware | Newsletter signup, no other engagement yet |
| Lead | Problem-aware | Read a blog post, visited a comparison page, no gated content yet |
| **MQL** | Solution-aware (skeptical) | See criteria below — real, repeated, vertical-specific engagement |
| **SQL** | Product-aware | Requested a demo AND fits ICP — see criteria below |
| Opportunity | — | Demo held, deal created in the Sales Hub pipeline |
| Customer | — | Closed-won |

## Proposed MQL criteria (any one of these, not a vague "engaged with content")

- Downloaded the flagship benchmark report (*The State of Independent Retail POS 2026*)
- Watched 50%+ of the recorded product tour
- Visited the What's Included page **and** a vertical-specific comparison/best-for page (liquor, convenience, smoke/vape, or CBD) in the same session or return visit
- Engaged with two or more pieces of compliance-authority content (a strong signal specifically for the Ray and Danny personas, where compliance anxiety is the documented top objection)

## Proposed SQL criteria (requires the demo request AND a fit check — see Section 3 on why this shouldn't be fully automated)

- Requested a demo through the site or a campaign CTA
- Fits the ICP: an actual liquor, convenience, smoke/vape, or CBD retail business (not a student, vendor, or competitor doing research — a real, recurring noise source worth explicitly screening for)
- Has a plausible decision-making role (owner/operator, not a general inquiry)

**Persona and vertical should be a required custom property on every contact**, set at first form fill and refined as more content is engaged with — this is what lets Section 5's reporting break MQL/SQL volume down by Danny/Farah/Ray/Priya/Sam rather than one undifferentiated pile.

---

# 3. The MQL → SQL handoff should not be fully automated — here's the actual mechanism

Current HubSpot best practice is explicit on this, and it also happens to match how a small, relationship-driven sales motion should work: **don't auto-promote MQL straight to SQL.** The transition is a judgment call, not a score crossing a threshold.

**The recommended flow:**
1. A contact meets the MQL criteria in Section 2 → lifecycle stage updates to MQL (manually via list view today at Starter; automatically via lead score at Professional).
2. This **creates a task for the assigned rep**, not an automatic SQL promotion — due within a defined SLA window (see Section 4).
3. The rep reviews the contact's actual timeline (the shared record from Section 1) and either:
   - **Confirms SQL** — logged the moment a demo is actually booked via the Meeting Scheduler already live in Sales Hub, which is the cleanest, least-debatable trigger available.
   - **Disqualifies with a reason code** (wrong vertical, not a real business, too early, price-shopping competitor) — this reason code is what feeds Section 6's feedback loop back to Marketing.
4. **Score decay does not auto-demote a stage.** If an MQL goes quiet, that triggers a re-engagement review, not a silent reversion to Lead — reverting a stage automatically erases the record of what content actually worked to get them there in the first place.

This is also, not incidentally, an extension of the same "a human answers" pillar RetailzPOS already uses externally — internally, it means a real person, not a score, decides when a lead is sales-ready.

---

# 4. How Marketing and Sales actually work in tandem — the concrete mechanics

## The shared record is the whole mechanism, and it's already live

Because Marketing Hub and Sales Hub sit on one Smart CRM record, a rep opening a contact in the Deal Pipeline Board sees the exact campaign, content, and lifecycle history Marketing built — full context before the first call, which is literally the improvement the Sales Hub pilot deck already promised reps ("full context on the record — source campaign, product line, prior touches — before you dial"). Nothing new needs to be built for this part; it needs to actually be used consistently.

## A written stage-ownership agreement — do this before scaling volume, not after

Best practice is blunt about this: both teams use Lifecycle Stage, but each owns specific transitions within it, and neither team should unilaterally redefine a stage the other owns. Proposed ownership split for RetailzPOS:

| Stage transition | Owner |
|---|---|
| Subscriber → Lead → MQL | Marketing |
| MQL → SQL | Sales (per Section 3's manual review) |
| SQL → Opportunity → Customer | Sales |
| Reopening a disqualified MQL | Joint — requires the reason code review from Section 3 |

## An internal SLA on SQL response time

The same discipline behind the "a human answers" support-response commitment, applied to leads: define and hold a real number (e.g., first-touch within one business day of a demo request) — a lead worked minutes after converting is a genuinely different conversation than one worked days later, which is exactly the logic already used to sell the sales team on this system in the first place.

## The closed loop back to content strategy

Every disqualification reason code Sales logs should roll up monthly against the Content Mix Tracker and Post Grading system already built in the 90-Day Calendar & Tracker workbook. The question this answers: which pillar, persona, or one of the four AI-search citation surfaces (editorial, YouTube, Reddit/Quora, LinkedIn) is producing MQLs that actually convert to real SQLs, versus volume that just looks good in a reach number. This is the same logic already driving the post-publish grading system — extend it one stage further into the funnel instead of stopping at engagement.

---

# 5. Reporting — what both teams should be looking at, and how often

| Metric | Cadence | Ties back to |
|---|---|---|
| Demo requests (true-north metric) | Weekly | Brief's stated measurement philosophy — no numeric targets before enough baseline data exists |
| MQL volume by persona/vertical | Weekly | Section 2's criteria |
| MQL → SQL conversion rate | Monthly | Section 3's handoff; recalibrate MQL criteria quarterly against this number specifically if it's trending down |
| SQL → Customer conversion rate | Monthly | Standard pipeline health check |
| Disqualification reason codes, by frequency | Monthly | Section 4's closed loop — this is the number that tells Marketing what to stop producing, not just what to produce more of |
| Cost/MQL and cost/SQL, by channel | Monthly once paid spend is live | Only fully automatable at Marketing Hub Professional (multi-touch attribution) — build the manual version first with UTM-tagged campaigns and list views, same "prove it, then upgrade" sequencing as everywhere else in this document |

---

# 6. Sequencing recommendation

Don't jump to Marketing Hub Professional to build this. Build the lifecycle-stage structure, the manual/list-based MQL flagging, the task-based handoff, and the reason-code feedback loop entirely on the Starter bundle already in place — every mechanism in Sections 2 through 5 works today with more manual list-review discipline instead of automatic scoring. Treat the Professional upgrade exactly the way the Sales Hub pilot deck already treats Sales Hub Professional: **the case for it should be built from real MQL volume outgrowing manual review, not assumed on day one.** If review volume starts genuinely bottlenecking a rep's ability to work the SLA in Section 4, that's the actual trigger — not a calendar date.
