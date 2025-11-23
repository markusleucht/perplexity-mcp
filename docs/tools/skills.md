# Claude Code Skills - Available Capabilities

**Purpose:** Progressive disclosure of installed skills and their triggers.

**Last Updated:** November 23, 2025

---

## pharma-research

**Version:** 2.0.2
**Location:** `~/.claude/skills/pharma-research/`
**Repository:** https://github.com/markusleucht/claude-code-skills
**Status:** ✅ Active, Production-Ready
**Spec Compliance:** ✅ Validated via `validate_skill.py`

### What It Does
Comprehensive, data-driven analysis of the German pharmaceutical market for specific indication-medication-company combinations. Delivers business-oriented assessments with concrete numbers, temporal context, and strategic portfolio analysis.

### When to Use

**Trigger Keywords (German):**
- Indikation, Medikament, Therapie
- Ärzte, Markt, Versorgung
- Firma, Portfolio, Hersteller

**Trigger Keywords (English):**
- pharmaceutical market Germany
- drug analysis, indication research
- epidemiology, prescriber analysis
- market access, AMNOG
- portfolio position

**Use Cases:**
- German pharmaceutical market analysis
- Indication prevalence or treatment landscape in Germany
- Medication competitive positioning or market access
- Prescriber analysis by specialty
- Therapy frequency or efficacy comparisons
- Market size, growth trends, or unmet needs
- AMNOG assessments or reimbursement outlook
- Company portfolio strategy and product positioning

### How to Use

**Natural language activation:**
```
"Analyze the German pharmaceutical market for Psoriasis and Bimekizumab"
"Analyze Psoriasis, Bimekizumab, and UCB Pharma's portfolio position"
"What role does Ozempic play in Novo Nordisk's portfolio strategy?"
"Research Diabetes Type 2 treatment landscape in Germany"
"How many dermatologists prescribe biologics in Germany?"
```

**Parameters (auto-extracted):**
- Indication: Detected from query (e.g., "Psoriasis", "Diabetes Type 2")
- Medication: Detected from query (e.g., "Bimekizumab", "Ozempic")
- Company: Detected or auto-identified from medication (e.g., "UCB Pharma", "Novo Nordisk")

### What You Get

**Output Structure:**
1. **Indication Analysis (Germany)**
   - Epidemiology & market size (with specific numbers and years)
   - Unmet needs (quantified treatment gaps)
   - Care pathway & access (specialists, guidelines, reimbursement)

2. **Medication Analysis (Germany)**
   - Market position & competition
   - Differentiation factors
   - Market access (pricing, AMNOG, reimbursement)
   - Adoption barriers
   - Risks & opportunities

3. **Company & Portfolio Analysis** *(v2.0.0+)*
   - Company financials (revenue, R&D, employees)
   - Portfolio overview (top products, therapeutic areas)
   - Strategic product positioning (revenue share, lifecycle)
   - Peak sales guidance and growth trajectory
   - Marketing investment priority (1-5 star scoring)
   - Budget recommendations and negotiation leverage

4. **Data Points**
   - All statistics with years
   - 20-30 authoritative citations (RKI, G-BA, company reports)

**Report Length:** 5-7 pages (markdown format)

### Research Process

**Automated workflow (6-10 searches):**
1. Phase 1: Indication epidemiology and care pathway (2-3 searches)
2. Phase 2: Company financials and portfolio overview (3-4 searches)
3. Phase 3: Medication market position and access (2-3 searches)
4. Phase 4: Strategic positioning and peak sales (1-2 searches)

**Uses:**
- `mcp__perplexity__perplexity_search` with language="de", search_type="auto"
- Targeted German and English queries
- Official sources prioritized (Destatis, RKI, KBV, company financials)

### Cost
- **Per report:** ~$0.06-0.10 (6-10 Perplexity searches @ auto mode)
- **Breakdown:**
  - Indication: ~$0.02
  - Company/portfolio: ~$0.03-0.04
  - Medication: ~$0.02
- **Budget:** $5 Perplexity credit = ~50-80 reports

### Limitations
- **Geography:** Germany only (no multi-country support yet)
- **Language:** German + English sources
- **Data availability:** Depends on public data for niche medications
- **Real-time:** Data is as current as Perplexity can find (typically 2024-2025)

### Dependencies
- **Required:**
  - Claude Code
  - Perplexity MCP server (`mcp__perplexity__perplexity_search`)
  - Valid Perplexity API key
- **Optional:** None

### Validation

**Check skill is loaded:**
```bash
# In Claude Code:
"List my available skills"
# Should show: pharma-research
```

**Run smoke test:**
```bash
# In Claude Code:
"What's the prevalence of Psoriasis in Germany?"
# Should return German epidemiology data with sources
```

**Validate spec compliance:**
```bash
cd ~/.claude/skills/pharma-research
python3 validate_skill.py
# Should show: ✅ All validation checks passed!
```

### Documentation
- **README:** `~/.claude/skills/pharma-research/README.md` (setup & usage)
- **SKILL Definition:** `~/.claude/skills/pharma-research/SKILL.md` (core framework)
- **Output Templates:** `~/.claude/skills/pharma-research/references/output-templates.md`
- **Query Strategies:** `~/.claude/skills/pharma-research/references/query-strategies.md`
- **Example Report:** `~/.claude/skills/pharma-research/examples/Psoriasis_Bimzelx_UCB_Example.md`
- **Validation Script:** `~/.claude/skills/pharma-research/validate_skill.py`

### Real-World Example

**Input:**
```
"Analyze the German pharmaceutical market for Psoriasis, Bimekizumab, and UCB Pharma"
```

**Output:**
- 5-7 page report
- **Indication:** 2.2M patients, 2-3% prevalence, biologics 35% adoption
- **Medication:** Dual IL-17A/F inhibitor, PASI 90: 84-93%, market share 5-8%
- **Company:** UCB 6.15B EUR revenue, 29% R&D, portfolio transformation
- **Portfolio:** Bimzelx 799M EUR (H1 2025), peak sales >4B EUR, 26% revenue share
- **Investment Priority:** ⭐⭐⭐⭐⭐ (5/5) - Blockbuster launch
- **Budget:** Premium tier, high leverage, long-term partnership potential
- 25-30 sources (official statistics, investor reports, pharma news)
- Cost: ~$0.08

---

## Adding New Skills

When installing a new Claude Code skill:

1. **Install the skill**
   ```bash
   # Copy to ~/.claude/skills/skill-name/
   # Ensure SKILL.md is present
   ```

2. **Verify SKILL.md frontmatter**
   ```yaml
   ---
   name: skill-name
   version: x.y.z
   description: What it does and when to use it
   # ... other metadata
   ---
   ```

3. **Test the skill**
   ```bash
   # Restart Claude Code
   # Try trigger phrases
   # Verify output
   ```

4. **Document in this file**
   - Add new section with skill name
   - Document triggers (keywords, patterns)
   - Explain what it does and when to use
   - Show example usage
   - List dependencies and costs
   - Provide validation steps
   - Link to documentation

5. **Validate against SKILL spec**
   ```bash
   cd ~/.claude/skills/skill-name
   python3 validate_skill.py  # If available
   # Or manually check against docs/SKILL_SPEC.md
   ```

6. **Commit documentation**
   ```bash
   git add docs/tools/skills.md
   git commit -m "docs: add [skill-name] skill documentation"
   ```

---

## Best Practices

1. **Test before documenting** - Verify skill activates and produces expected output
2. **Include real examples** - Show actual queries that trigger the skill
3. **Document costs** - Note any API usage or compute costs
4. **Spec compliance** - Validate against `docs/SKILL_SPEC.md`
5. **Update on changes** - When skill updates, update this manifest
6. **Cross-reference** - Link to skill's own documentation

---

## Skill Discovery

Claude Code automatically discovers skills from:
- User-level: `~/.claude/skills/`
- Project-level: `.claude/skills/`

Skills are loaded based on:
- SKILL.md frontmatter `description` field
- Trigger keywords and patterns
- User query context

---

**This manifest follows the progressive disclosure principle established in CLAUDE.md**
