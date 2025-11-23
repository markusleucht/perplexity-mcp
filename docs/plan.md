# Pharma-Research Skill: Implementation Plan

**Created:** 2025-11-23
**Status:** Implemented and ready for testing
**Location:** `~/.claude/skills/pharma-research/` (user-level)

---

## Executive Summary

This document outlines the implementation of the `pharma-research` skill for Claude Code, designed to conduct precision research on the German pharmaceutical market. The skill leverages the existing Perplexity MCP server to deliver business-oriented assessments of indication-medication pairs.

**Key Design Decisions:**
- ✅ **Skill** (not sub-agent or slash command) for automatic discovery
- ✅ **Progressive disclosure** with references/ folder for token efficiency
- ✅ **Lean SKILL.md** (~350 lines) following Reddit guide best practices
- ✅ **Flexible methodology** that guides without constraining Perplexity
- ✅ **Portable structure** for transfer to other workspaces

---

## Architecture Overview

### File Structure

```
~/.claude/skills/pharma-research/
├── SKILL.md                          # Main skill definition (350 lines)
└── references/
    └── query-strategies.md           # Query formulation guidance (optional loading)
```

**Rationale:**
- No scripts/ folder (no custom code needed - uses existing Perplexity MCP)
- No assets/ folder (no templates to avoid binding Perplexity output)
- No examples/ folder (user doesn't have existing examples)
- Minimal references/ (just strategic guidance, not prescriptive)

### Integration Points

**Perplexity MCP Server:**
- Location: `/Users/markus/perplexity/`
- Tools available: `perplexity_search`, `perplexity_social`
- Configuration: `.mcp.json` (already set up)

**Claude Code:**
- Skill auto-discovery via description keywords
- Natural language invocation
- Progressive disclosure for token efficiency

---

## SKILL.md Structure

### YAML Frontmatter

```yaml
---
name: pharma-research
description: Precision research assistant for analyzing the German pharmaceutical
market. Use when users need business-oriented assessment of specific indications
and medications in Germany, including epidemiology, market positioning, competitive
landscape, prescriber analysis, unmet needs, market access barriers, or therapy
efficacy comparisons. Triggers on German pharma terms (Indikation, Medikament,
Therapie, Ärzte, Markt, Versorgung) or requests for German healthcare market data.
---
```

**Trigger Keywords:**
- German terms: Indikation, Medikament, Therapie, Ärzte, Markt, Versorgung
- English terms: pharmaceutical market, German, indication, medication, epidemiology
- Actions: analyze, research, assess, evaluate

### Content Sections (8 major sections)

1. **Overview** - What the skill does
2. **When to Use This Skill** - Trigger scenarios with examples
3. **Core Research Framework** - The structured assessment you requested:
   - Part 1: Indication Analysis (Epidemiology, Unmet Need, Care Pathway)
   - Part 2: Medication Analysis (Market Position, Differentiation, Market Access, Adoption Barriers, Risks & Opportunities)
4. **Research Methodology** - 3-step process:
   - Step 1: Query Formulation (German search patterns)
   - Step 2: Execute Perplexity Searches (tool usage guidance)
   - Step 3: Data Validation & Quality Standards
5. **Output Structure** - Exact format for final report
6. **Quality Checklist** - Pre-delivery verification
7. **Tips for Effective Research** - Best practices
8. **Example Application** - Concrete usage scenario

**Design Principle:** Provides methodology and quality standards while keeping Perplexity's search flexibility intact.

---

## Research Framework Details

### Part 1: Indication Analysis

**Epidemiology & Market Size**
- Prevalence rates with year and source
- Incidence trends over time
- Patient population size and growth trajectory
- European benchmarks for context

**Unmet Need**
- Treatment gaps (% untreated, undertreated)
- Disease burden (economic + clinical)
- Patient segments with high unmet need

**Care Pathway & Access**
- Specialist involvement by stage
- Guideline recommendations (S3-Leitlinien, etc.)
- Reimbursement landscape (GKV, AOK)
- Patient journey mapping

### Part 2: Medication Analysis

**Market Position & Competition**
- Competitive set with drug classes
- Market share trends
- Generic vs. innovation dynamics

**Differentiation**
- Mechanism of action
- Efficacy endpoints with data
- Dosing convenience
- Safety profile

**Market Access**
- Pricing level
- AMNOG benefit assessment outcome
- Reimbursement status
- Launch date and uptake trajectory

**Adoption Barriers**
- Physician acceptance
- Safety concerns
- Adherence challenges
- Administrative burden

**Risks & Opportunities**
- Regulatory risks
- Patent timeline
- Pipeline competition
- Innovation potential

---

## Perplexity Integration Approach

### Tool Usage Guidance (Not Binding)

The skill provides **strategic guidance** on how to use Perplexity effectively:

```
Call perplexity_search with:
- query: [Targeted German query]
- language: "de"
- search_type: "pro" (deep research) | "auto" (balanced) | "fast" (quick)
- sources: ["web"] | ["social"] | ["scholar"]
- max_tokens: 1024-2000
- save_to_file: Optional
```

**Key Design Choice:**
- ✅ Shows HOW to call the tool
- ✅ Explains WHEN to use different parameters
- ❌ Doesn't enforce rigid query templates
- ❌ Doesn't include fixed examples that might become outdated

### Search Sequencing Strategy

Recommends 4-6 targeted searches:
1. Start broad: Indication epidemiology + market overview
2. Narrow focus: Medication positioning + competitive set
3. Deep dive: Prescriber behavior, market access specifics
4. Synthesis: Risks, opportunities, trends

### Quality Standards (Built-in)

The skill emphasizes the quality guidelines already in Perplexity MCP:
- Specific data with years (no generic statements)
- Context with change over time + benchmarks
- Transparent about data gaps
- Structured output

**Data Source Hierarchy:**
1. Official statistics (Destatis, RKI, KBV)
2. Professional associations (DGHO, DDG, DGK)
3. Health insurance data (AOK, Barmer, TK)
4. Industry reports (IQVIA, Insight Health)
5. Academic studies
6. Media reports (context only)

---

## Progressive Disclosure Implementation

### Metadata Layer (~100 tokens)
Always loaded: Name + description with trigger keywords

### SKILL.md Body (~350 lines)
Loaded when skill triggers: Complete research framework and methodology

### References Layer (Optional)
`references/query-strategies.md` loaded only when Claude needs deeper guidance on query formulation.

**Expected Token Efficiency:** 40-60% reduction compared to full-context loading (per Reddit guide)

---

## Output Format Specification

### Report Structure

```markdown
### [Indication Name] – [Medication Name] | German Market Analysis

#### 1) Indication: [Name] (Germany)

**Epidemiology & Market Size**
- [5-8 bullet points with specific numbers and years]

**Unmet Need**
- [3-5 bullet points quantifying treatment gaps]

**Care Pathway & Access**
- [4-6 bullet points on specialists, guidelines, reimbursement]

**Key Insights:**
[5-8 concise bullet points synthesizing findings with numbers]

**Interpretation:**
[3-5 sentences providing business context]

#### 2) Medication: [Name] (Germany)

**Market Position & Competition**
- [4-6 bullet points on competitive landscape]

**Differentiation**
- [3-5 bullet points on unique value proposition]

**Market Access**
- [4-5 bullet points on pricing, AMNOG, reimbursement]

**Adoption Barriers**
- [3-5 bullet points on challenges]

**Risks & Opportunities**
- [4-6 bullet points on future outlook]

**Key Insights:**
[5-8 concise bullet points]

**Interpretation:**
[3-5 sentences on strategic implications]

#### Data Points
- [Bulleted list of all specific statistics with year]

#### Quellen
1. [Institution/Source Name] ([Year]) - [URL]
2. [Institution/Source Name] ([Year]) - [URL]
...

---

*Recherchiert: [Date]*
*Methode: Perplexity Pro Search auf Web-Quellen (sonar-pro)*
*Anfrage: [Original user query]*
```

**Expected Output:** 3-5 page reports with 15-25 cited sources

---

## Usage Examples

### Example 1: Direct Natural Language

**User:** "Analyze the German pharmaceutical market for Psoriasis and Cosentyx"

**Skill Execution:**
1. Claude detects German pharma keywords → loads pharma-research skill
2. Extracts parameters: Indication = Psoriasis, Medication = Cosentyx
3. Formulates 5-6 German Perplexity queries following methodology
4. Executes searches with `language="de"`, `search_type="pro"`
5. Synthesizes findings into structured report
6. Validates against quality checklist
7. Delivers markdown report with sources

### Example 2: With Explicit Parameters

**User:** "Research the German market for Type 2 Diabetes and Ozempic, focusing on competitive landscape and AMNOG assessment"

**Skill Execution:**
1. Skill activates
2. Prioritizes searches for: competition + market access dimensions
3. May use fewer searches (3-4) focused on specified areas
4. Delivers report emphasizing requested sections

### Example 3: Save to File

**User:** "Analyze Atopic Dermatitis and Dupixent in Germany, save the report"

**Skill Execution:**
1. Full research workflow
2. Uses `save_to_file` parameter in Perplexity calls
3. Report saved to `reports/Neurodermitis_Dupixent_[date].md`
4. User receives file path confirmation

---

## Portability Instructions

### Current Location (User-Level)
```
~/.claude/skills/pharma-research/
```

**Pros:**
- Available across all Claude Code sessions for this user
- Survives project deletions

**Cons:**
- Not transferred when moving to new computer
- Not version-controlled with project

### Making It Portable (Project-Level)

**Option 1: Copy to Project Directory**
```bash
# From within /Users/markus/perplexity/
mkdir -p .claude/skills
cp -r ~/.claude/skills/pharma-research .claude/skills/

# Commit to git
git add .claude/skills/pharma-research
git commit -m "Add pharma-research skill for German market analysis"
```

**Option 2: Symlink (Advanced)**
```bash
# Create project-level skills directory
mkdir -p /Users/markus/perplexity/.claude/skills

# Symlink from user-level to project-level
ln -s ~/.claude/skills/pharma-research /Users/markus/perplexity/.claude/skills/pharma-research
```

**Option 3: Package and Transfer**
```bash
# Package the skill (creates .tar.gz)
~/.claude/skills/skill-creator/scripts/package_skill.py ~/.claude/skills/pharma-research

# Transfer pharma-research.tar.gz to new machine
# Unpack in new machine's ~/.claude/skills/ or .claude/skills/
```

### Transfer to Another Computer

**Step 1: Package (on current machine)**
```bash
cd ~/.claude/skills
tar -czf pharma-research.tar.gz pharma-research/
```

**Step 2: Transfer**
```bash
# Via cloud storage, USB, scp, etc.
scp pharma-research.tar.gz user@newmachine:~/
```

**Step 3: Install (on new machine)**
```bash
# User-level (available everywhere)
cd ~/.claude/skills
tar -xzf ~/pharma-research.tar.gz

# OR project-level (specific to one project)
cd /path/to/perplexity/project/.claude/skills
tar -xzf ~/pharma-research.tar.gz
```

**Recommended Approach:**
- Keep master version in project `.claude/skills/` and commit to git
- This makes skill portable and version-controlled
- Clone repo on new machine → skill automatically available

---

## Validation & Testing

### Validation Command

```bash
~/.claude/skills/skill-creator/scripts/package_skill.py ~/.claude/skills/pharma-research
```

**Checks:**
- SKILL.md exists and has valid YAML frontmatter
- No broken references
- Proper directory structure
- File permissions correct

### Testing Plan

**Test 1: Basic Activation**
```
Query: "Analyze the German pharmaceutical market for Psoriasis and Cosentyx"
Expected: Skill activates, performs 4-6 Perplexity searches, delivers structured report
```

**Test 2: Parameter Extraction**
```
Query: "Research Multiple Sclerosis and Ocrevus in Germany"
Expected: Correctly identifies Indication = Multiple Sclerosis, Medication = Ocrevus
```

**Test 3: German Language Detection**
```
Query: "Untersuche den deutschen Pharmamarkt für Diabetes Typ 2 und Ozempic"
Expected: Skill activates, uses German language for all searches
```

**Test 4: Partial Information**
```
Query: "What's the German market for biologics in rheumatoid arthritis?"
Expected: Handles indication-only query, researches competitive landscape
```

**Test 5: File Saving**
```
Query: "Analyze Atopic Dermatitis and Dupixent, save the report"
Expected: Report saved to reports/ directory with timestamp
```

### Success Criteria

- [ ] Skill activates on relevant queries (German pharma keywords)
- [ ] Correctly extracts indication and medication parameters
- [ ] Executes multiple Perplexity searches with German language
- [ ] Delivers report following exact structure specification
- [ ] Includes 15-25 cited sources
- [ ] Report contains specific numbers with years
- [ ] Quality checklist items satisfied
- [ ] Can save to file when requested

---

## Maintenance & Iteration

### When to Update the Skill

**Update SKILL.md if:**
- New research dimensions become important (e.g., digital health adoption)
- Perplexity MCP tool parameters change
- Output format needs refinement based on user feedback
- New German data sources emerge (e.g., new RKI databases)

**Update references/ if:**
- Query patterns evolve
- New search strategies prove more effective
- German terminology changes

### Versioning Strategy

Since skills don't have built-in versioning:

**Option 1: Git Tags**
```bash
cd /Users/markus/perplexity
git tag -a pharma-research-v1.0 -m "Initial pharma-research skill release"
git push origin pharma-research-v1.0
```

**Option 2: Version in SKILL.md**
Add to frontmatter:
```yaml
---
name: pharma-research
version: 1.0.0
last_updated: 2025-11-23
description: ...
---
```

### Feedback Collection

After each use, note:
- Did the skill activate correctly?
- Were the searches effective?
- Was the output structure useful?
- Any missing research dimensions?
- Token efficiency (check Claude Code logs)

---

## Cost Considerations

### Perplexity API Usage

**Per Research Report:**
- 4-6 Pro Search queries @ ~$0.01-0.02 each
- **Total cost per report:** $0.04-0.12

**Budget Monitoring:**
- $5 in credits = ~40-125 research reports
- Monitor at: https://www.perplexity.ai/settings/api

**Cost Optimization:**
- Use `search_type="auto"` for less critical queries
- Use `search_type="fast"` for quick validations
- Target searches precisely to reduce query count

### Claude Code Token Usage

**Without Progressive Disclosure:** ~5,000 tokens per skill activation (entire SKILL.md + all references)

**With Progressive Disclosure:** ~1,500-2,500 tokens (metadata + SKILL.md only, references loaded as needed)

**Savings:** 40-60% token reduction (per Reddit guide recommendations)

---

## Troubleshooting

### Issue: Skill doesn't activate

**Diagnosis:**
- Check if keywords match user query
- Verify SKILL.md description is specific enough
- Confirm skill is in correct directory

**Solutions:**
1. Make description more specific and add more trigger keywords
2. Use explicit invocation: "Use the pharma-research skill to analyze..."
3. Check Claude Code logs for skill discovery

### Issue: Perplexity searches return irrelevant results

**Diagnosis:**
- Query formulation too broad or in wrong language
- Wrong source type selected

**Solutions:**
1. Review query-strategies.md for better patterns
2. Ensure `language="de"` parameter is used
3. Use more specific medical terminology
4. Try `sources=["scholar"]` for clinical data

### Issue: Report missing data

**Diagnosis:**
- Data genuinely unavailable for this indication/medication
- Wrong sources searched
- Query didn't capture the right terminology

**Solutions:**
1. Follow skill guidance: explicitly state data unavailable
2. Try alternative query formulations
3. Use `sources=["social"]` for qualitative insights
4. Search for proxy data or European benchmarks

### Issue: Output doesn't follow structure

**Diagnosis:**
- Skill loaded but Claude deviated from instructions
- Output structure section not clear enough

**Solutions:**
1. Reference the "Output Structure" section explicitly in follow-up
2. Ask Claude to reformat using the template
3. Update SKILL.md with more explicit formatting instructions

---

## Next Steps

### Immediate Actions

1. ✅ Skill created and ready
2. ⏭️ Validate using package_skill.py
3. ⏭️ Test with sample query
4. ⏭️ Create portable copy in project directory
5. ⏭️ Commit to git for version control

### Future Enhancements (Optional)

**Phase 2: Hooks Integration**
If you build multiple domain skills and need auto-activation:
- Create `.claude/hooks/user-prompt-submit.js`
- Create `skill-rules.json` with keywords and patterns
- Test auto-activation reliability

**Phase 3: Additional Skills**
Potential complementary skills:
- `clinical-trials-research` - For pipeline analysis
- `health-economics` - For cost-effectiveness research
- `regulatory-intel` - For EMA/G-BA tracking

**Phase 4: Workflow Automation**
If reports follow predictable patterns:
- Create templates in assets/
- Add scripts for data aggregation
- Automate report generation pipeline

---

## References

### Documentation
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Skill Creator GitHub](https://github.com/anthropics/skills/tree/main/skill-creator)
- [Reddit: Claude Code Best Practices](https://www.reddit.com/r/ClaudeAI/comments/1oivjvm/claude_code_is_a_beast_tips_from_6_months_of/)

### Related Files
- CLAUDE.md: `/Users/markus/perplexity/CLAUDE.md` (Perplexity MCP usage guide)
- MCP Config: `/Users/markus/perplexity/.mcp.json` (Perplexity server config)
- Skill Definition: `~/.claude/skills/pharma-research/SKILL.md`
- Query Strategies: `~/.claude/skills/pharma-research/references/query-strategies.md`

### German Data Sources
- **Destatis**: https://www.destatis.de (Official German statistics)
- **RKI**: https://www.rki.de (Robert Koch Institute - public health)
- **KBV**: https://www.kbv.de (National Association of Statutory Health Insurance Physicians)
- **G-BA**: https://www.g-ba.de (Federal Joint Committee - AMNOG)
- **IQWiG**: https://www.iqwig.de (Institute for Quality and Efficiency in Health Care)

---

**End of Implementation Plan**

*This plan serves as both documentation and reference for maintaining and transferring the pharma-research skill across workspaces and machines.*
