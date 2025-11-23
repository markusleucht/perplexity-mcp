# Troubleshooting Guide

**Last Updated:** November 23, 2025
**Audience:** All users encountering issues
**Quick Help:** Check this guide first, then consult related documentation

---

## Installation Issues

### "ModuleNotFoundError: No module named 'openai'"

The dependencies aren't installed. Run:

```bash
python3 -m pip install --user openai python-dotenv
```

### "PERPLEXITY_API_KEY not set"

Create a `.env` file with your API key:

```bash
echo "PERPLEXITY_API_KEY=pplx-your-key" > .env
```

### "command not found: /opt/homebrew/bin/python3.12"

Your `.mcp.json` has the wrong Python path. Update it with:

```bash
which python3
```

Then edit `.mcp.json` with the correct path.

### Dependencies auto-install on first run

The MCP server now automatically installs missing dependencies on first run. If you see:

```
📦 Installing missing dependencies: openai>=1.0.0, python-dotenv>=0.19.0
✓ Dependencies installed successfully
```

This is normal and means the setup is working correctly.

---

## Runtime Issues

### "API key not found"

**Symptom:** Searches fail with API key error

**Solution:** Check that `.env` file exists with `PERPLEXITY_API_KEY=pplx-...`

**Verification:**
```bash
cat .env  # Should show PERPLEXITY_API_KEY=pplx-...
```

### No results returned

**Symptoms:** Search completes but returns empty results

**Possible Causes:**
- API credits depleted
- Query too broad or ambiguous
- Search mode mismatch

**Solutions:**
- Try different search query
- Check API credits: https://www.perplexity.ai/settings/api
- Try `search_type="auto"` instead of "pro"
- Be more specific in your query (include year, context, specific keywords)

### Not getting sources

**Symptom:** Report generated but no source citations

**Explanation:** Sources come from Perplexity's search results. If none appear, the search may not have found relevant sources.

**Solutions:**
- Refine query to be more specific
- Try different search type (pro vs auto)
- Check if query is in supported language
- Verify API key has credits remaining

---

## Configuration Issues

### MCP server not responding

**Symptom:** Claude Code doesn't recognize Perplexity tools

**Solutions:**
1. Verify `.mcp.json` exists in project root
2. Check Python path in `.mcp.json` is correct
3. Restart Claude Code
4. Check MCP server logs

**Verification:**
```bash
# Check configuration
cat .mcp.json

# Test Python path
/opt/homebrew/bin/python3 --version

# Test MCP server manually
python3 src/perplexity_mcp.py
```

### Wrong Python version

**Symptom:** "SyntaxError" or compatibility errors

**Requirement:** Python 3.8 or higher

**Solution:**
```bash
python3 --version  # Should be 3.8+
which python3      # Update .mcp.json with this path
```

---

## API & Cost Issues

### Credits running low

**Monitor usage at:** https://www.perplexity.ai/settings/api

**Cost reference:**
- Pro Search: ~$0.01-0.02 per query
- Social Search: ~$0.01-0.02 per query
- $5 budget: 100-250 searches

**Optimization:**
- Use `search_type="auto"` for balanced cost/quality
- Use `search_type="fast"` for quick, cheaper searches
- Reserve "pro" for complex research queries

### Rate limiting

**Symptom:** "Rate limit exceeded" errors

**Solutions:**
- Wait 60 seconds between requests
- Reduce number of concurrent searches
- Check Perplexity API rate limits

---

## File & Path Issues

### Reports not saving

**Symptom:** `save_to_file` parameter doesn't create file

**Solutions:**
1. Check `reports/` directory exists
2. Verify write permissions
3. Use absolute or relative path correctly

**Auto-created directories:**
- `reports/` is created automatically if it doesn't exist

### Path errors in documentation

**Known issues:**
- Some old docs reference `docs/QUICKSTART.md` (should be `docs/guides/QUICKSTART.md`)
- Some old docs reference `docs/SKILL_SPEC.md` (should be `docs/specs/SKILL_SPEC.md`)

**Current structure:**
```
docs/
├── guides/         # User-facing guides
├── tools/          # Tool manifests
├── specs/          # Specifications
├── reports/        # Report examples
└── archive/        # Old documentation
```

---

## Getting More Help

### Documentation Resources

- **Installation Guide** → [`../../INSTALL.md`](../../INSTALL.md)
- **User Guide** → [`USER_GUIDE.md`](USER_GUIDE.md)
- **Developer Guide** → [`DEVELOPER_GUIDE.md`](DEVELOPER_GUIDE.md)
- **Quick Start** → [`QUICKSTART.md`](QUICKSTART.md)

### External Resources

- **Perplexity API Docs** → https://docs.perplexity.ai/
- **Perplexity API Dashboard** → https://www.perplexity.ai/settings/api
- **MCP Server Tools Reference** → [`../tools/mcp-servers.md`](../tools/mcp-servers.md)

### Support

- **GitHub Issues** → Report bugs or request features
- **Check CHANGELOG** → [`../../CHANGELOG.md`](../../CHANGELOG.md) for recent changes
- **Review Examples** → `reports/` directory for working examples

---

## Quick Diagnostic Checklist

Before reporting an issue, verify:

- [ ] Python 3.8+ installed (`python3 --version`)
- [ ] Dependencies installed (`pip list | grep openai`)
- [ ] `.env` file exists with valid API key
- [ ] `.mcp.json` configured correctly
- [ ] API credits available (check dashboard)
- [ ] Claude Code restarted after config changes
- [ ] Query is clear and specific
- [ ] Using correct language code (en, de, es, fr, it)

---

## Still Having Issues?

1. **Check logs** for error messages
2. **Review recent CHANGELOG** for known issues
3. **Verify all configuration files** are correct
4. **Test with simple query** first
5. **Consult documentation** for your specific use case

If problem persists, gather:
- Error message (full text)
- Configuration files (.mcp.json, .env structure)
- Python version
- Operating system
- Steps to reproduce

Then report via appropriate channel (GitHub issues, etc.)
