# MCP Builder Compliance Review (pharma-research skill)

## Scope and methodology
- Goal: assess whether the local pharma-research skill aligns with the Anthropics MCP Builder SKILL spec.
- Limitation: direct access to the upstream SKILL specification URL is blocked in this environment (HTTP 403), so verification is based on local artifacts only.【3db7cd†L1-L9】

## Current implementation snapshot
- The skill lives at `.claude/skills/pharma-research/SKILL.md` with YAML frontmatter defining `name` and a long `description`, followed by narrative guidance for when and how to use the skill.【F:.claude/skills/pharma-research/SKILL.md†L1-L27】
- The body focuses on a two-part research framework (indication and medication analyses) plus German-language search patterns and tool parameters for the Perplexity MCP tools.【F:.claude/skills/pharma-research/SKILL.md†L28-L120】
- A single reference file (`references/query-strategies.md`) provides additional German pharma query patterns and search tactics, suggesting progressive disclosure is intended.【F:.claude/skills/pharma-research/references/query-strategies.md†L1-L80】
- Internal planning docs reiterate that the skill is designed as a lean (~350 lines) definition with minimal references and no auxiliary scripts or assets.【F:docs/plan.md†L13-L38】

## Gaps relative to the MCP Builder SKILL spec
Because the authoritative spec could not be fetched, the following are inferred risks rather than confirmed violations:
- **Incomplete frontmatter metadata**: only `name` and `description` are present. If the MCP Builder spec requires fields such as `version`, `author`, `requirements`, or dependency declarations, they are currently missing.【F:.claude/skills/pharma-research/SKILL.md†L1-L27】
- **Missing explicit tool bindings**: the narrative references `perplexity_search` and `perplexity_social` usage, but there is no structured section that maps tools, arguments, or expected outputs. If the spec expects declarative tool definitions, those are absent in the SKILL file.【F:.claude/skills/pharma-research/SKILL.md†L109-L120】
- **No embedded validation hooks**: the repo does not contain a local copy of the SKILL spec or automated lint/packaging scripts to verify compliance. The absence of the spec makes drift likely over time.【F:docs/plan.md†L22-L49】

## Recommendations
1. **Mirror the official SKILL spec locally**: vendor the MCP Builder SKILL.md into `docs/` (or another tracked location) so it remains accessible offline and can be cited in future audits.【3db7cd†L1-L9】
2. **Audit frontmatter against the spec**: once the spec is available, add any required metadata fields (e.g., `version`, `author`, `dependencies`, `tools`) and keep descriptions concise to aid auto-discovery.【F:.claude/skills/pharma-research/SKILL.md†L1-L27】
3. **Document explicit tool contracts**: if the spec expects declarative tool usage, add a section summarizing available MCP tools, required parameters, defaults, and output expectations to reduce ambiguity for the runner.【F:.claude/skills/pharma-research/SKILL.md†L109-L120】
4. **Add a validation step**: integrate a lightweight check (e.g., a script or CI job) that validates SKILL.md structure against the MCP Builder spec so future edits stay compliant.【F:docs/plan.md†L13-L38】