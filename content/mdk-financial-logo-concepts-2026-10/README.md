# MDK Financial Services: Logo Concepts (Oct 2026)

Four concepts that build the letters **M-D-K** from finance imagery. Each one comes as a
self-contained vector `.svg` (the text is converted to outlines, so it needs no fonts) and a 1600px-wide `.png`.
`mdk-logo-concepts-overview.png` shows all four together.

| # | File | Idea | Palette |
|---|------|------|---------|
| 1 | `concept-1-ascent` | The **M** is drawn like a stock chart: its right peak is higher than its left. The upper arm of the **K** turns into a growth arrow. | Burgundy `#7A1F2B`, charcoal `#3D3F45` (from the current MDK logo) |
| 2 | `concept-2-pie-chart-d` | The **D** is a pie chart with a gold slice pulled out. The arm of the **K** is a gold growth arrow. | Purple `#5B3BAF`, gold `#C9922E` (from the current MDK logo, with the "Your financial growth begins here" tagline) |
| 3 | `concept-3-bar-chart-letters` | All three letters are built from chart bars. In the **K**, the upper arm becomes rising green bars that end in an arrow. | Navy `#0F2A4A` / `#2F5C8F`, green `#1FA36B` |
| 4 | `concept-4-crest-monogram` | A shield crest for trust and protection. The **M** and **D** share one stem, and the **K** arm is an arrow. | Black `#14171C`, gold `#C8A04A` → `#E6C878` |

Fonts used: Montserrat and Playfair Display (both Google Fonts, under the SIL Open Font License).

To regenerate: `source/gen.py source/concepts.py` writes the SVGs, and `source/render.js <dir>` exports the PNGs (requires fontTools and Playwright).
