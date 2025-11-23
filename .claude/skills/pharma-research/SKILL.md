---
name: pharma-research
version: 2.0.1
author: Markus Leucht
repository: https://github.com/markusleucht/claude-code-skills
description: Precision research assistant for analyzing the German pharmaceutical market with company portfolio context. Triggers on German pharma terms or requests for market analysis.
requirements:
  - claude_code: ">=0.1.0"
  - mcp_servers:
      - perplexity:
          tools:
            - perplexity_search
            - perplexity_social
          description: "Perplexity AI MCP server for deep research with web crawling"
          repository: "https://github.com/markusleucht/perplexity-mcp"
dependencies:
  required:
    - Perplexity MCP server configured with valid API key
  optional: []
tools:
  - name: mcp__perplexity__perplexity_search
    parameters:
      query: "string (required) - German or English search query"
      language: "string (default: 'de') - Response language"
      search_type: "string (default: 'auto') - Search depth: pro|auto|fast"
      sources: "array (default: ['web']) - Sources: web|social|scholar"
      max_tokens: "integer (default: 1024) - Response length 100-4000"
      save_to_file: "string (optional) - Path to save markdown report"
    returns: "Markdown report with citations and source URLs"
  - name: mcp__perplexity__perplexity_social
    parameters:
      query: "string (required) - Social media search query"
      max_tokens: "integer (default: 1024) - Response length"
      save_to_file: "string (optional) - Path to save report"
    returns: "Social media insights with verified citations"
triggers:
  - German pharma terms: "Indikation, Medikament, Therapie, Ärzte, Markt, Versorgung, Firma, Portfolio, Hersteller"
  - English requests: "pharmaceutical market Germany, drug analysis, indication research"
  - Market analysis: "epidemiology, prescriber analysis, market access, AMNOG, portfolio position"
---

# German Pharmaceutical Market Research

## Overview

Conduct comprehensive, data-driven analysis of the German pharmaceutical market for specific indication-medication combinations. Deliver business-oriented assessments with concrete numbers, temporal context, and clear source attribution.

## When to Use This Skill

Activate when users request:
- German pharmaceutical market analysis
- Indication prevalence or treatment landscape in Germany
- Medication competitive positioning or market access
- Prescriber analysis by specialty
- Therapy frequency or efficacy comparisons
- Market size, growth trends, or unmet needs
- AMNOG assessments or reimbursement outlook

**Example queries:**
- "Analyze the German market for Psoriasis and Cosentyx"
- "Research Diabetes Type 2 treatment landscape in Germany"
- "How many dermatologists prescribe biologics in Germany?"

## Core Research Framework

Execute this structured assessment for every indication-medication pair:

### Part 1: Indication Analysis (Germany)

**1. Epidemiology & Market Size**
- Prevalence rates with year and source
- Incidence trends over time (show change)
- Patient population size and growth trajectory
- Compare to European benchmarks where relevant

**2. Unmet Need**
- Treatment gaps (% untreated, undertreated)
- Disease burden: economic (cost of illness) + clinical (QALYs, hospitalizations)
- Identify specific patient segments with high unmet need

**3. Care Pathway & Access**
- Specialist involvement (which specialties, at what stage)
- Guideline recommendations (S3-Leitlinien, DEGAM, etc.)
- Reimbursement landscape (GKV coverage, AOK policies)
- Patient journey from diagnosis to treatment

### Part 2: Medication Analysis (Germany)

**1. Market Position & Competition**
- Competitive set: list direct competitors with drug class
- Market share trends (if available)
- Generic vs. innovation dynamics
- Therapeutic class maturity

**2. Differentiation**
- Mechanism of action (unique aspects)
- Efficacy endpoints (primary outcomes with data)
- Dosing convenience (frequency, route, patient burden)
- Safety profile (comparative advantages/disadvantages)

**3. Market Access**
- Pricing level (list price, discounts if known)
- AMNOG benefit assessment outcome (zusatznutzen rating)
- Reimbursement status (unrestricted, quota, prior authorization)
- Launch date and uptake trajectory

**4. Adoption Barriers**
- Physician acceptance (prescribing patterns, specialty uptake)
- Safety concerns or contraindications
- Adherence challenges (complexity, side effects)
- Administrative burden (documentation requirements)

**5. Risks & Opportunities**
- Regulatory risks (label changes, warnings)
- Patent timeline (exclusivity end date)
- Pipeline competition (upcoming alternatives)
- Innovation potential (new indications, line extensions)

## Research Methodology

### Step 1: Query Formulation

Craft targeted Perplexity searches in German for maximum precision:

**Epidemiology queries:**
- "Prävalenz [Indikation] Deutschland [Jahr]"
- "Anzahl Patienten [Indikation] Deutschland Statistik"
- "Inzidenz [Indikation] Trend Deutschland"

**Market/Competition queries:**
- "[Medikament] Marktanteil Deutschland Vergleich"
- "[Therapeutische Klasse] Wettbewerb Deutschland"
- "Verschreibungszahlen [Medikament] [Jahr] Deutschland"

**Prescriber queries:**
- "Fachärzte [Indikation] Deutschland Anzahl"
- "[Spezialität] Verschreibungsverhalten [Medikament]"
- "Praxen [Indikation] Behandlung Deutschland"

**Market access queries:**
- "[Medikament] AMNOG Nutzenbewertung"
- "[Medikament] Erstattung GKV"
- "[Medikament] Preis Deutschland [Jahr]"

### Step 2: Execute Perplexity Searches

Use the Perplexity MCP tools with German language parameter:

**For each research dimension (4-6 searches recommended):**

```
Call perplexity_search with:
- query: [Targeted German query from Step 1]
- language: "de"
- search_type: "pro" (for deep research with web crawling)
- sources: ["web"] (default, most comprehensive)
- max_tokens: 1024-2000 (depending on topic complexity)
- save_to_file: Optional, use for archiving raw research
```

**When to use different source types:**
- `sources: ["web"]` - Default for most queries (guidelines, statistics, market reports)
- `sources: ["social"]` - Patient perspectives, physician discussions, treatment experiences
- `sources: ["scholar"]` - Clinical efficacy data, epidemiology studies

**Search sequencing strategy:**
1. Start broad: Indication epidemiology + market overview
2. Narrow focus: Medication positioning + competitive set
3. Deep dive: Prescriber behavior, market access specifics
4. Synthesis: Risks, opportunities, trends

### Step 3: Data Validation & Quality Standards

- **Specific data with years** - Never use generic claims without numbers and dates
- **Context** - Always show change over time + relevant benchmarks
- **Transparency** - Clearly state when reliable data is unavailable
- **Structured** - Follow format: Key facts → Data points → Interpretation → Sources

Prioritize authoritative sources: Official statistics (Destatis, RKI, KBV) > Professional associations > Health insurance data > Industry reports > Academic studies.

**For detailed quality guidelines, templates, and checklists, see `references/output-templates.md`**

## Output Structure

Generate comprehensive markdown report with three main sections:

1. **Indication Analysis**: Epidemiology, unmet needs, care pathway
2. **Medication Analysis**: Market position, differentiation, access, barriers, outlook
3. **Data Points & Sources**: All statistics with years, 20-30 authoritative citations

**Complete formatting template available in `references/output-templates.md`**
