#!/usr/bin/env python3
"""
SKILL Specification Validator

Validates pharma-research SKILL.md against MCP Builder SKILL spec requirements.
Checks frontmatter metadata, structure, and required fields.
"""

import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Required frontmatter fields based on MCP Builder SKILL spec
REQUIRED_FIELDS = ['name', 'version', 'description']
RECOMMENDED_FIELDS = ['author', 'repository', 'requirements', 'dependencies', 'tools', 'triggers']

def parse_yaml_frontmatter(content: str) -> Tuple[Dict, str]:
    """Extract YAML frontmatter and body from markdown."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)

    if not match:
        return {}, content

    frontmatter_text = match.group(1)
    body = match.group(2)

    # Simple YAML parser (handles our use case)
    frontmatter = {}
    current_key = None
    indent_level = 0

    for line in frontmatter_text.split('\n'):
        if not line.strip():
            continue

        # Top-level key
        if line and not line.startswith(' '):
            if ':' in line:
                key, value = line.split(':', 1)
                current_key = key.strip()
                value = value.strip()
                if value:
                    frontmatter[current_key] = value.strip('"\'')
                else:
                    frontmatter[current_key] = []
        # Nested content
        else:
            if current_key:
                if not isinstance(frontmatter[current_key], list):
                    frontmatter[current_key] = []
                frontmatter[current_key].append(line.strip())

    return frontmatter, body

def validate_frontmatter(frontmatter: Dict) -> List[str]:
    """Validate frontmatter has required fields."""
    errors = []
    warnings = []

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            errors.append(f"❌ Missing required field: '{field}'")
        elif not frontmatter[field]:
            errors.append(f"❌ Required field '{field}' is empty")

    # Check recommended fields
    for field in RECOMMENDED_FIELDS:
        if field not in frontmatter:
            warnings.append(f"⚠️  Missing recommended field: '{field}'")

    # Validate version format (semver)
    if 'version' in frontmatter:
        version = frontmatter['version']
        if not re.match(r'^\d+\.\d+\.\d+', str(version)):
            warnings.append(f"⚠️  Version '{version}' doesn't follow semver (x.y.z)")

    # Validate repository URL
    if 'repository' in frontmatter:
        repo = frontmatter['repository']
        if not repo.startswith('http'):
            warnings.append(f"⚠️  Repository should be a full URL: {repo}")

    return errors + warnings

def validate_structure(body: str) -> List[str]:
    """Validate markdown structure has key sections."""
    errors = []

    # Check for essential sections
    essential_sections = [
        ('Overview', r'##\s+Overview'),
        ('When to Use', r'##\s+When to Use'),
        ('Research Framework', r'##\s+(Core )?Research Framework'),
        ('Methodology', r'##\s+Research Methodology'),
    ]

    for section_name, pattern in essential_sections:
        if not re.search(pattern, body, re.IGNORECASE):
            errors.append(f"⚠️  Missing recommended section: '{section_name}'")

    return errors

def validate_tools_declaration(frontmatter: Dict) -> List[str]:
    """Validate that MCP tools are properly declared."""
    issues = []

    if 'tools' not in frontmatter:
        issues.append("⚠️  No 'tools' section in frontmatter - MCP tools should be explicitly declared")
        return issues

    tools = frontmatter.get('tools', [])
    if not tools:
        issues.append("⚠️  'tools' section is empty - should list mcp__perplexity tools")
        return issues

    # Check for expected Perplexity tools
    tool_text = ' '.join(str(t) for t in tools)
    if 'perplexity_search' not in tool_text.lower():
        issues.append("⚠️  Missing tool declaration: perplexity_search")

    return issues

def check_file_size(content: str) -> List[str]:
    """Check if SKILL.md is reasonably sized."""
    warnings = []
    lines = content.split('\n')

    if len(lines) > 300:
        warnings.append(f"⚠️  SKILL.md is long ({len(lines)} lines). Consider moving detailed content to references/")

    return warnings

def main():
    """Run validation checks."""
    skill_path = Path(__file__).parent / 'SKILL.md'

    if not skill_path.exists():
        print(f"❌ SKILL.md not found at: {skill_path}")
        sys.exit(1)

    print("🔍 Validating pharma-research SKILL.md...")
    print()

    content = skill_path.read_text()
    frontmatter, body = parse_yaml_frontmatter(content)

    all_issues = []

    # Run validation checks
    all_issues.extend(validate_frontmatter(frontmatter))
    all_issues.extend(validate_structure(body))
    all_issues.extend(validate_tools_declaration(frontmatter))
    all_issues.extend(check_file_size(content))

    # Report results
    if not all_issues:
        print("✅ All validation checks passed!")
        print()
        print("Frontmatter fields found:")
        for key in frontmatter.keys():
            print(f"  ✓ {key}")
        return 0

    # Separate errors and warnings
    errors = [i for i in all_issues if i.startswith('❌')]
    warnings = [i for i in all_issues if i.startswith('⚠️')]

    if errors:
        print("Errors:")
        for error in errors:
            print(f"  {error}")
        print()

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  {warning}")
        print()

    if errors:
        print("❌ Validation failed with errors")
        return 1
    else:
        print("⚠️  Validation passed with warnings")
        return 0

if __name__ == '__main__':
    sys.exit(main())
