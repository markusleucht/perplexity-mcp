# Pharma-Research Skill Guide

**Last Updated:** November 23, 2025
**Version:** v2.0.0 (Production-Ready)
**Audience:** Pharmaceutical market researchers
**Prerequisites:** Claude Code, Perplexity MCP server

---

## What It Does

Automatically conducts structured business analysis of German pharma markets with strategic portfolio context:
- **Indication Analysis:** Epidemiology, unmet needs, care pathways, market access
- **Medication Analysis:** Competition, differentiation, pricing, adoption barriers, opportunities
- **Company Portfolio Analysis:** Corporate financials, portfolio composition, strategic product positioning **(NEW in v2.0.0)**
- **Marketing Investment Scoring:** 1-5 star priority rating with budget recommendations **(NEW in v2.0.0)**
- **Negotiation Context:** Leverage assessment, partnership potential, budget tier guidance **(NEW in v2.0.0)**
- **Quality:** Data-driven reports with 20-30 sources, specific numbers with years
- **Production-Validated:** Successfully tested with real-world analysis (Psoriasis, Bimekizumab & UCB Pharma)

---

## Usage

Just ask naturally:
```
"Analyze the German pharmaceutical market for Psoriasis and Bimekizumab"
"Analyze Psoriasis, Bimekizumab, and UCB Pharma's portfolio position"
"What role does Ozempic play in Novo Nordisk's portfolio strategy?"
"Research Diabetes Type 2 and Ozempic in Germany"
```

The skill automatically:
1. Extracts indication, medication, and company parameters (auto-detects if not specified)
2. Performs 6-10 targeted Perplexity searches (German + English)
   - Phase 1: Indication epidemiology
   - Phase 2: Company financials and portfolio
   - Phase 3: Medication market position
   - Phase 4: Strategic positioning and peak sales
3. Calculates marketing investment priority score (1-5 stars)
4. Synthesizes findings into structured business report with budget recommendations
5. Delivers 5-7 page report with 20-30 sources
6. Saves report to `reports/` folder

---

## Real-World Example

**Query:** "Analyze the German pharmaceutical market for Psoriasis, Bimekizumab, and UCB Pharma"

**Result (v2.0.0):**
- 5-7 page comprehensive business report with 3 major sections
- **Indication:** 2.2M patients, 2-3% prevalence, biologics adoption 35%
- **Medication:** Dual IL-17A/F inhibitor, PASI 90: 84-93%, market share 5-8%
- **Company:** UCB 6.15 Mrd. EUR revenue, 29% R&D ratio, portfolio transformation
- **Portfolio Position:** Bimzelx 799 Mio. EUR (H1 2025), peak sales >4 Mrd. EUR target, 26% revenue share
- **Strategic Role:** Growth Driver compensating Cimzia patent loss, mission-critical
- **Investment Priority:** ⭐⭐⭐⭐⭐ (5/5) - Blockbuster launch
- **Budget Recommendation:** Premium tier, high negotiation leverage, long-term partnership potential
- 25-30 authoritative sources (RKI, G-BA, UCB investor reports, Fierce Pharma)
- Cost: ~$0.08 (8 searches @ "auto" mode)

---

## Installation

**Already installed** in your user-level skills directory (`~/.claude/skills/pharma-research/`).

**To use on another machine:**
```bash
git clone https://github.com/markusleucht/claude-code-skills.git
cp -r claude-code-skills/pharma-research ~/.claude/skills/
# Restart Claude Code
```

**Requirements:**
- Claude Code
- Perplexity MCP server configured (this project)

---

## Documentation

- **Skill README:** `~/.claude/skills/pharma-research/README.md` (complete setup & usage guide)
- **Skill Definition:** `~/.claude/skills/pharma-research/SKILL.md` (research framework)
- **Query Strategies:** `~/.claude/skills/pharma-research/references/query-strategies.md`
- **Example Report:** `~/.claude/skills/pharma-research/examples/Psoriasis_Bimzelx_UCB_Example.md` **(NEW in v2.0.0)**
- **GitHub Repository:** https://github.com/markusleucht/claude-code-skills

---

## Cost per Report

- **Typical analysis with company context:** 6-10 Perplexity searches @ "auto" mode
- **Cost:** ~$0.06-0.10 per comprehensive report (was $0.03-0.045 in v1.0.0)
- **Cost breakdown:**
  - Indication analysis: 2-3 searches (~$0.02)
  - Company/portfolio analysis: 3-4 searches (~$0.03-0.04) **[NEW]**
  - Medication analysis: 2-3 searches (~$0.02)
- **Your $5 budget:** ~50-80 detailed pharma market reports with portfolio context

---

## Related Documentation

- **Skill Manifest** → [`../tools/skills.md`](../tools/skills.md)
- **MCP Server Tools** → [`../tools/mcp-servers.md`](../tools/mcp-servers.md)
- **User Guide** → [`USER_GUIDE.md`](USER_GUIDE.md)
- **Developer Guide** → [`DEVELOPER_GUIDE.md`](DEVELOPER_GUIDE.md)
- **GitHub Repository** → https://github.com/markusleucht/claude-code-skills
