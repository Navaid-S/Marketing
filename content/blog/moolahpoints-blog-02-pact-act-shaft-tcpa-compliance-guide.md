# The Liquor Store & Vape Shop Guide to PACT Act, SHAFT, and TCPA Compliance in Loyalty Marketing

**Meta description:** A plain-language guide to PACT Act, SHAFT, and TCPA rules for liquor, vape, and tobacco loyalty marketing — what they actually require, and what a compliant SMS campaign looks like.
**Target keywords:** SMS compliance liquor store, TCPA vape marketing, SHAFT compliance loyalty texts
**Funnel stage:** Consideration → Decision

*This article is general information, not legal advice. Regulations vary by state and change over time — confirm current requirements with your own counsel before launching a campaign.*

---

Most loyalty platforms were not built with liquor, tobacco, and vape retailers in mind, because most loyalty platforms don't sell to liquor, tobacco, and vape retailers. That's a problem, because this is one of the few retail categories where a badly-worded marketing text isn't just ineffective — it can get your number blocked by a carrier, or worse, create real regulatory exposure.

Here's what actually governs loyalty marketing for age-restricted products, in plain language, and what a compliant campaign looks like in practice.

## The three things that actually apply to your loyalty texts

### 1. Age verification (FDA rules + the PACT Act)

At the point of sale, [FDA rules](https://www.fda.gov/tobacco-products/compliance-enforcement-training/retail-sales-tobacco-products) require checking ID for anyone appearing under 30 — this part most retailers already know cold. Where it gets more complicated is remote or delivery sales: the [PACT Act](https://www.atf.gov/alcohol-tobacco/prevent-all-cigarette-trafficking-pact-act) (Prevent All Cigarette Trafficking Act, enforced by the ATF) governs shipping tobacco and vapor products, and requires full identity verification plus an adult signature on delivery. If your loyalty program ever supports online ordering, pickup, or delivery for tobacco or vapor products, PACT Act obligations follow the sale, not just the in-store register.

**What this means for your loyalty program:** enrollment and reward redemption tied to age-restricted products should never bypass age verification, even when the "purchase" is happening through a points-redemption flow rather than a standard checkout.

### 2. SHAFT content restrictions on bulk SMS

This is the one most retailers have never heard of, and it's the one most likely to get a campaign silently blocked. Wireless carriers enforce [CTIA's Messaging Principles and Best Practices](https://api.ctia.org/wp-content/uploads/2023/05/230523-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf) on bulk SMS traffic, which include content restrictions commonly shortened to **SHAFT** — no **S**ex, **H**ate, **A**lcohol, **F**irearms, or **T**obacco content in standard bulk messaging without special carrier-level approval.

That means a text like *"20% off all vodka this weekend — reply STOP to opt out"* can trip carrier filters and get suppressed before it ever reaches your customer, regardless of how good your loyalty platform is. This isn't a law with a courtroom penalty attached — it's an infrastructure-level restriction baked into how carriers route bulk SMS, which makes it easy to miss until a campaign mysteriously underperforms.

**What this means for your loyalty program:** campaigns need to be written to communicate the offer without triggering restricted-category keyword filtering — a solvable problem, but only if your platform's campaign builder is built with this in mind.

### 3. TCPA consent

The [Telephone Consumer Protection Act (TCPA)](https://www.fcc.gov/tags/telephone-consumer-protection-act-tcpa), enforced by the FCC, applies to all SMS marketing, not just regulated products — but the stakes are higher when the product category is already scrutinized. TCPA requires clear, documented opt-in consent before you text a customer, and a working opt-out mechanism on every message. For liquor, vape, and tobacco retailers specifically, sloppy consent practices compound with SHAFT filtering risk: you don't just want consent, you want a clean, defensible enrollment record.

## What a compliant loyalty campaign actually looks like

Here's the same offer, written two ways.

**Risky version:**
> "🍷 Buy 2 bottles of wine, get 500 bonus points! Reply STOP to opt out."

**Compliant version:**
> "You've got a reward waiting at [Store Name] — check your points balance and this week's bonus offer: [link]. Reply STOP to unsubscribe."

The second version drives the customer to a landing page (or an in-app/portal view) where the specific offer — and any product-specific detail — lives outside the SMS content itself. The text does its job (get the customer to open it and click) without carrying the exact content that triggers carrier-level filtering. Consent language and opt-out are present on every message, not just the first one.

This is a small structural choice, but it's the difference between a campaign that reliably lands and one that silently disappears into carrier filtering with no clear reason why.

## The benchmark other regulated-retail platforms are starting to set

Preferred Patron, one of the more established platforms serving cannabis, vape, tobacco, and liquor retail, has built age-aware enrollment and consent-gated messaging directly into its regulated-retail product line — not as an afterthought, but as a core feature. That's a reasonable standard for any platform serious about this category to be building toward, and it's the standard we hold our own campaign tooling to.

The honest reality is that most horizontal loyalty platforms — built for salons, gyms, and cafes — simply never had to think about any of this. If you're evaluating a loyalty tool and age-restricted products are a meaningful part of your business, it's worth asking directly: *does your campaign builder account for SHAFT filtering, or will I find out the hard way?*

## Frequently asked questions

**What is the PACT Act, and does it apply to my in-store loyalty program?**
The PACT Act primarily governs remote and delivery sales of tobacco and vapor products, requiring identity verification and adult signature on delivery. If your loyalty program only covers in-person purchases at the register, standard in-store age verification rules apply instead — but any online, pickup, or delivery component brings PACT Act obligations into play.

**What is SHAFT compliance, and why does it matter for SMS marketing?**
SHAFT refers to carrier-enforced content restrictions on bulk SMS covering Sex, Hate, Alcohol, Firearms, and Tobacco content. Messages that include this content directly can be blocked by carrier filters before reaching the customer, independent of any specific law.

**Is TCPA consent required for loyalty program SMS?**
Yes. The TCPA requires documented opt-in consent before sending marketing texts and a functioning opt-out mechanism on every message, regardless of product category — though the consequences of weak consent practices are more visible in a heavily scrutinized category like alcohol or tobacco.

**Can I still run alcohol or vape promotions through SMS at all?**
Yes — the fix isn't avoiding SMS marketing, it's structuring campaigns so the specific product/offer detail lives on a landing page or portal rather than in the raw text content, keeping the message itself outside SHAFT-restricted keyword territory while still driving the customer to the offer.

## Get the compliance checklist

We put together a one-page **SMS Compliance Checklist for Regulated Retail** — the plain-language version of everything above, plus a quick self-check before you send your next campaign. [Download it free →]

Compliance shouldn't be the reason a liquor store, vape shop, or smoke shop skips loyalty marketing altogether. It just needs to be built into the tool from the start.

---

## Sources

- [FDA — Retail Sales of Tobacco Products (age verification requirements)](https://www.fda.gov/tobacco-products/compliance-enforcement-training/retail-sales-tobacco-products)
- [ATF — Prevent All Cigarette Trafficking (PACT) Act](https://www.atf.gov/alcohol-tobacco/prevent-all-cigarette-trafficking-pact-act)
- [ATF — PACT Act Information Guide (PDF)](https://www.atf.gov/alcohol-tobacco/docs/guide/prevent-all-cigarette-trafficking-pact-act-information-guide/download)
- [CTIA — Messaging Principles and Best Practices (PDF, source of SHAFT content restrictions)](https://api.ctia.org/wp-content/uploads/2023/05/230523-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf)
- [FCC — Telephone Consumer Protection Act (TCPA) rules and orders](https://www.fcc.gov/tags/telephone-consumer-protection-act-tcpa)
- Preferred Patron regulated-retail loyalty product documentation (industry benchmark reference, publicly available product positioning)

*This article is general information, not legal advice — the sources above are the primary, authoritative references; confirm current requirements with your own counsel before launching a campaign, since regulations and carrier enforcement practices change.*
