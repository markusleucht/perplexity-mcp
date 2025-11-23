# MCP Builder SKILL Specification (Mirrored Locally)

**Source**: [anthropics/skills repository - agent_skills_spec.md](https://github.com/anthropics/skills/blob/main/agent_skills_spec.md)
**Version**: 1.0 (Released October 16, 2025)
**Last Updated**: November 23, 2025

---

## Core Definition

A **skill** is "a folder of instructions, scripts, and resources that agents can discover and load dynamically to perform better at specific tasks."

The only **required file** is `SKILL.md`.

---

## Folder Structure

**Minimal requirement:**
```
my-skill/
└── SKILL.md          # Required
```

**Extended structure (optional):**
```
my-skill/
├── SKILL.md          # Required: Core prompt and metadata
├── scripts/          # Optional: Python/Bash executables
├── references/       # Optional: Documentation files
├── assets/           # Optional: Templates and binaries
└── examples/         # Optional: Usage examples
```

---

## SKILL.md Format

The file consists of **YAML frontmatter** followed by **Markdown content**.

### Format Structure

```yaml
---
name: your-skill-name
description: What this Skill does and when to use it
license: MIT                           # Optional
allowed-tools: Read, Grep, Glob        # Optional, Claude Code only
metadata:                              # Optional
  key1: value1
  key2: value2
---

# Your Skill Name

## Instructions
[Step-by-step guidance for Claude]

## Examples
[Concrete usage demonstrations]

[Additional sections as needed]
```

---

## YAML Frontmatter Properties

### Required Properties

#### `name` (string, required)
- **Format**: Hyphen-case identifier (lowercase Unicode alphanumeric + hyphens)
- **Restriction**: Must match the folder name
- **Max Length**: 64 characters
- **Example**: `pharma-research`, `data-analyzer`, `code-reviewer`

#### `description` (string, required)
- **Purpose**: Explains the skill's purpose and when Claude should use it
- **Max Length**: 1024 characters
- **Best Practice**: Include:
  - **What it does**: Core functionality and capabilities
  - **When to use it**: Specific triggers or use cases
- **Example**:
  ```yaml
  description: Precision research assistant for analyzing the German pharmaceutical market. Use when users need business-oriented assessment of specific indications and medications in Germany.
  ```

### Optional Properties

#### `license` (string, optional)
- **Purpose**: Identifies the skill's license
- **Best Practice**: Keep concise (e.g., "MIT", "Apache-2.0")
- **Example**:
  ```yaml
  license: MIT
  ```

#### `allowed-tools` (string, optional)
- **Support**: Claude Code only
- **Format**: Comma-separated list of pre-approved tools
- **Purpose**: Restricts which tools the skill can use
- **Example**:
  ```yaml
  allowed-tools: Read, Grep, Glob, WebFetch
  ```

#### `metadata` (object, optional)
- **Purpose**: String key-value pairs for client-specific properties
- **Best Practice**: Use unique naming to avoid conflicts
- **Example**:
  ```yaml
  metadata:
    version: "2.0.1"
    author: "Your Name"
    repository: "https://github.com/user/skill"
    last_updated: "2025-11-23"
  ```

---

## Markdown Body

- **Flexibility**: No restrictions on Markdown content formatting
- **Best Practices**:
  - Keep under 5,000 words to prevent context bloat
  - Use third person in descriptions for consistent discovery
  - Use separate `references/` directory for detailed documentation
  - Bundle supporting files only when relevant

---

## Validation Rules

| Field | Requirements | Max Length | Format |
|-------|--------------|-----------|--------|
| `name` | Lowercase letters, numbers, hyphens only | 64 characters | Hyphen-case |
| `description` | Clear what it does + when to use it | 1024 characters | Plain text |
| `license` | SPDX license identifier or custom | N/A | String |
| `allowed-tools` | Comma-separated tool names | N/A | String |
| `metadata` | String key-value pairs | N/A | Object |

---

## Reference Implementation

The official repository includes `template-skill` as a minimal working example:

```yaml
---
name: template-skill
description: A minimal skill template demonstrating the required structure
---

# Template Skill

This is a minimal skill showing the basic structure.

## When to Use
Use this template as a starting point for creating new skills.

## Instructions
1. Copy this template
2. Rename the folder and update the name field
3. Write your skill instructions
4. Add any supporting files as needed
```

---

## Extended Metadata (pharma-research Implementation)

While the official spec only requires `name` and `description`, the pharma-research skill implements extended metadata for better tooling and validation:

```yaml
---
name: pharma-research
version: 2.0.1                        # Semantic versioning
author: Markus Leucht                 # Creator identification
repository: https://github.com/...    # Source repository
description: [concise description]
requirements:                         # Dependency declarations
  - claude_code: ">=0.1.0"
  - mcp_servers:
      - perplexity: [...]
dependencies:                         # Runtime requirements
  required:
    - Perplexity MCP server
tools:                                # Explicit tool declarations
  - name: mcp__perplexity__perplexity_search
    parameters: [...]
    returns: [...]
triggers:                             # Activation patterns
  - German pharma terms: "..."
---
```

**Note**: This extended metadata is not required by the official spec but provides enhanced validation, documentation, and tooling support.

---

## Best Practices

### 1. Keep SKILL.md Concise
- Target: Under 5,000 words
- Move detailed content to `references/` directory
- Use progressive disclosure

### 2. Clear Description
- Explain what the skill does
- Specify when to use it
- Include trigger keywords

### 3. Progressive Disclosure
```
skill-name/
├── SKILL.md              # Core behavior (concise)
├── references/
│   ├── detailed-guide.md # In-depth documentation
│   ├── examples.md       # Extended examples
│   └── api-reference.md  # Technical details
```

### 4. Tool Declaration
If using MCP tools or specialized capabilities, document them clearly:
- Tool names
- Required parameters
- Expected outputs
- Error handling

### 5. Validation
Include validation scripts to ensure spec compliance:
```bash
# Example validation
python3 validate_skill.py
```

---

## Resources

### Official Documentation
- **GitHub Repository**: [anthropics/skills](https://github.com/anthropics/skills)
- **Claude Code Docs**: [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)
- **Support Article**: [How to create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

### Community Resources
- [Agent Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Agent Skills Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/)
- [Inside Claude Code Skills](https://mikhail.io/2025/10/claude-code-skills/)

---

## Changelog

### Version 1.0 (October 16, 2025)
- Public launch of official SKILL specification
- Established required fields: `name`, `description`
- Defined optional fields: `license`, `allowed-tools`, `metadata`
- Created minimal folder structure requirements

---

**This document is a local mirror for offline reference and validation purposes.**
**Always refer to the official specification at https://github.com/anthropics/skills for the latest updates.**
