---
name: pharma-research
description: Precision research assistant for analyzing the German pharmaceutical market. Use when users need business-oriented assessment of specific indications and medications in Germany, including epidemiology, market positioning, competitive landscape, prescriber analysis, unmet needs, market access barriers, or therapy efficacy comparisons. Triggers on German pharma terms (Indikation, Medikament, Therapie, Ärzte, Markt, Versorgung) or requests for German healthcare market data.
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

**Requirements:**
- **Specific data with years** - Never use generic claims without numbers and dates
- **Context** - Always show change over time + relevant benchmarks
- **Transparency** - Clearly state when reliable data is unavailable (no guessing)
- **Structured** - Follow format: Key facts → Data points → Interpretation → Sources

**Data source hierarchy (prioritize in this order):**
1. Official statistics: Destatis, RKI, KBV, Kassenärztliche Vereinigung
2. Professional associations: DGHO, DDG, DGK, specialty societies
3. Health insurance data: AOK, Barmer, TK reports
4. Industry reports: IQVIA, Insight Health (verify recency)
5. Academic studies: peer-reviewed publications
6. Media reports: Use only for context, not primary data

**Red flags (verify carefully):**
- Outdated data (>3 years old without noting limitations)
- Conflicting numbers across sources (investigate discrepancy)
- Industry-sponsored data without independent validation
- Vague terms ("many", "most", "growing") without quantification

## Output Structure

Deliver findings in this exact format:

### [Indication Name] – [Medication Name] | German Market Analysis

#### 1) Indication: [Name] (Germany)

**Epidemiology & Market Size**
- [5-8 bullet points with specific numbers and years]

**Unmet Need**
- [3-5 bullet points quantifying treatment gaps]

**Care Pathway & Access**
- [4-6 bullet points on specialists, guidelines, reimbursement]

**Key Insights:**
[5-8 concise bullet points synthesizing the most important findings with numbers]

**Interpretation:**
[3-5 sentences providing business context and implications]

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
[5-8 concise bullet points synthesizing medication-specific findings]

**Interpretation:**
[3-5 sentences on strategic implications and positioning]

#### Data Points
- [Bulleted list of all specific statistics with year]
- [Include: numbers, percentages, growth rates, comparisons]

#### Quellen
1. [Institution/Source Name] ([Year]) - [URL]
2. [Institution/Source Name] ([Year]) - [URL]
[Continue numbering all sources]

---

*Recherchiert: [Date]*
*Methode: Perplexity Pro Search auf Web-Quellen (sonar-pro)*
*Anfrage: [Original user query]*

## Quality Checklist

Before finalizing the report, verify:

- [ ] All numbers include year/date
- [ ] Change over time shown for key metrics
- [ ] Benchmark comparisons included where relevant
- [ ] Data gaps explicitly stated (no speculation)
- [ ] Sources are authoritative (official stats, professional associations)
- [ ] German terminology used consistently
- [ ] Business implications clearly articulated
- [ ] Report saved to file if requested

## Tips for Effective Research

**Maximize Perplexity search quality:**
- Use precise German medical/pharma terminology
- Include year in queries for recent data
- Combine general terms + specific drug/disease names
- Search incrementally: broad → specific → validation

**Handle data gaps:**
- State explicitly: "Keine aktuellen Daten verfügbar für [metric]"
- Provide related available data as proxy if reasonable
- Note data limitations in interpretation section

**Optimize for business utility:**
- Lead with actionable insights (market size, growth, competitive threats)
- Quantify unmet needs in patient numbers or economic terms
- Highlight differentiation factors that affect market access
- Connect epidemiology to commercial opportunity

## Example Application

**User query:** "Analyze the German pharmaceutical market for Psoriasis and Cosentyx"

**Skill execution:**
1. Extract parameters: Indication = Psoriasis, Medication = Cosentyx
2. Formulate 5-6 German Perplexity queries covering all framework dimensions
3. Execute searches with `language="de"`, `search_type="pro"`
4. Synthesize findings following output structure
5. Validate data quality (years, sources, context)
6. Generate markdown report with sources
7. Save to `reports/Psoriasis_Cosentyx_[date].md`

**Expected output:** 3-5 page business-oriented report with 15-25 cited sources, specific numbers with years, clear competitive positioning, and actionable market insights.
