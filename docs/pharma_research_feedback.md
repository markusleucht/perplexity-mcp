 Pharma-Research Skill Review

## Summary
- The skill provides a thorough research framework for German pharmaceutical market analysis, but the core definition is verbose and mixes operational guidance with example data.
- Key best-practice gaps include missing explicit tool/dependency declarations in the skill definition, unclear separation between executable prompts and reference material, and example content that presents unsourced numbers as if they were production-ready outputs.

## Findings
### Strengths
- Clear activation context and research framework, including structured market, medication, and portfolio analysis steps.【F:SKILL.md†L12-L158】
- README documents installation, expected outputs, and cost considerations to set user expectations.【F:README.md†L22-L169】

### Deviations from best practice
1. **Skill definition lacks explicit tool dependencies and metadata**
   - The SKILL references `perplexity_search` calls and parameter choices but does not declare tool requirements or other metadata (version, authors) in the front matter, which can hinder automated validation and onboarding.【F:SKILL.md†L1-L4】【F:SKILL.md†L195-L206】

2. **Excessive length and mixed purposes in SKILL.md**
   - The skill file spans hundreds of lines with output templates, data quality checklists, and example workflows that belong in supporting documentation, making the core behavior harder to scan and maintain.【F:SKILL.md†L249-L377】【F:SKILL.md†L447-L486】
   - Much of this material duplicates the README’s usage and configuration sections, increasing drift risk.【F:README.md†L59-L169】

3. **Example file presents unverifiable figures as canonical output**
   - The example report includes numerous numeric claims (e.g., prevalence, pricing, market shares) without citations or explicit “sample data” labeling, which could be mistaken for validated outputs.【F:examples/Psoriasis_Bimzelx_UCB_Example.md†L9-L105】

4. **Missing quick-start MCP configuration**
   - README references the Perplexity MCP server but defers setup details to the main project, leaving newcomers without a minimal `.mcp.json` snippet or validation step to confirm the dependency is wired up.【F:README.md†L24-L29】【F:README.md†L180-L188】

## Recommendations
1. Add explicit skill metadata and tool declarations (name, version, owner, required MCP tools) in the SKILL front matter so environments can validate dependencies before activation.
2. Refactor SKILL.md to a concise operational definition (triggers, required tools, core flow); move templates, checklists, and long-form guidance to README or the `references/` directory to reduce maintenance overhead.
3. Update the example report to mark numbers as illustrative and add citations or placeholders so readers do not treat the figures as validated research outputs.
4. Expand README with a short MCP setup snippet and a post-setup check (e.g., `perplexity_search` smoke test) to make the dependency path self-contained.