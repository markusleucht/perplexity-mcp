# Perplexity AI API Reference

> **Source:** Context7 documentation aggregation from official Perplexity AI docs
> **Last Updated:** 2025-12-10

---

## Overview

Perplexity AI provides real-time, web-wide research and conversational AI capabilities through its **Sonar** model family. The API enables:

- **Chat Completions** with web search integration
- **Search API** for raw search results without LLM processing
- **Async operations** for long-running research tasks
- **Structured outputs** (JSON Schema, Regex)

---

## Available Models

### Search Models

| Model | Use Case | Context | Features |
|-------|----------|---------|----------|
| `sonar` | Fast responses, straightforward queries | Standard | Real-time web search |
| `sonar-pro` | Complex analysis, deeper research | 200K tokens | Advanced search, citations |
| `sonar-deep-research` | Exhaustive research, detailed reports | Extended | Async support, reasoning |

### Reasoning Models

| Model | Use Case | Features |
|-------|----------|----------|
| `sonar-reasoning` | Fast problem-solving, analytical tasks | Quick reasoning |
| `sonar-reasoning-pro` | Complex queries, multi-step analysis | Premier reasoning, extended thinking |

---

## Pricing (2025)

### Sonar Pro
| Metric | High | Medium | Low |
|--------|------|--------|-----|
| Input Tokens (Per Million) | $3 | $3 | $3 |
| Output Tokens (Per Million) | $15 | $15 | $15 |
| Price per 1000 Requests | $5 | $5 | $5 |

### Sonar (Standard)
| Metric | High | Medium | Low |
|--------|------|--------|-----|
| Input Tokens (Per Million) | $1 | $1 | $1 |
| Output Tokens (Per Million) | $1 | $1 | $1 |
| Price per 1000 Requests | $5 | $5 | $5 |

### Sonar Reasoning
| Metric | High | Medium | Low |
|--------|------|--------|-----|
| Input Tokens (Per Million) | $1 | $1 | $1 |
| Output Tokens (Per Million) | $5 | $5 | $5 |
| Price per 1000 Requests | $12 | $8 | $5 |

### Deep Research
| Metric | Cost |
|--------|------|
| Input Tokens (Per Million) | $2 |
| Output Tokens (Per Million) | $8 |
| Price per 1000 Requests | Variable |

---

## API Endpoints

### 1. Chat Completions

**Endpoint:** `POST https://api.perplexity.ai/chat/completions`

#### Request Body

```json
{
  "model": "sonar-pro",
  "messages": [
    {"role": "system", "content": "Be precise and concise."},
    {"role": "user", "content": "What are the latest AI trends?"}
  ],
  "max_tokens": 1024,
  "temperature": 0.2,
  "top_p": 0.9,
  "stream": false,
  "search_mode": "web",
  "web_search_options": {
    "search_context_size": "high"
  }
}
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `model` | string | Yes | Model to use (sonar, sonar-pro, sonar-deep-research, etc.) |
| `messages` | array | Yes | Conversation history with role/content objects |
| `max_tokens` | integer | No | Max completion tokens (default: 1024) |
| `temperature` | number | No | Randomness 0-2 (default: 0.2) |
| `top_p` | number | No | Nucleus sampling (default: 0.9) |
| `stream` | boolean | No | Enable streaming (default: false) |
| `search_mode` | string | No | `web`, `academic`, or `sec` |
| `search_recency_filter` | string | No | `day`, `week`, `month`, `year` |
| `reasoning_effort` | string | No | For deep research: `low`, `medium`, `high` |

#### Response

```json
{
  "id": "chatcmpl-12345",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "sonar-pro",
  "usage": {
    "prompt_tokens": 50,
    "completion_tokens": 100,
    "total_tokens": 150,
    "search_context_size": "high",
    "citation_tokens": 20,
    "num_search_queries": 2
  },
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "The response content..."
      }
    }
  ],
  "citations": ["https://source1.com", "https://source2.com"],
  "search_results": [
    {
      "title": "Result Title",
      "url": "https://example.com",
      "date": "2025-01-15"
    }
  ]
}
```

---

### 2. Search API (Raw Results)

**Endpoint:** `POST https://api.perplexity.ai/search`

Returns ranked search results **without** LLM processing.

#### Request Body

```json
{
  "query": "latest AI developments 2024",
  "max_results": 10,
  "search_domain_filter": ["nature.com", "science.org"],
  "search_language_filter": ["en", "de"],
  "search_recency_filter": "week",
  "max_tokens_per_page": 1024,
  "country": "US",
  "search_after_date": "10/15/2025",
  "search_before_date": "12/01/2025"
}
```

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | string/array | Search query (max 5 queries for multi-query) |
| `max_results` | integer | 1-20 results (default: 10) |
| `search_domain_filter` | array | Limit to specific domains (max 20) |
| `search_language_filter` | array | Filter by language codes |
| `search_recency_filter` | string | `day`, `week`, `month`, `year` |
| `max_tokens_per_page` | integer | Tokens per webpage (default: 1024) |
| `country` | string | Geographic filter (US, GB, DE, etc.) |
| `search_after_date` | string | Format: `%m/%d/%Y` |
| `search_before_date` | string | Format: `%m/%d/%Y` |

#### Response

```json
{
  "results": [
    {
      "title": "Article Title",
      "url": "https://example.com/article",
      "snippet": "Brief excerpt from the content...",
      "date": "2025-03-20",
      "last_updated": "2025-09-19"
    }
  ]
}
```

---

### 3. Async Chat Completions

For long-running research tasks (especially with `sonar-deep-research`).

**Create Task:** `POST https://api.perplexity.ai/chat/completions/async`

```json
{
  "model": "sonar-deep-research",
  "messages": [{"role": "user", "content": "Comprehensive analysis of..."}],
  "reasoning_effort": "high"
}
```

**Response:**
```json
{"task_id": "5b9f8f8f-8f8f-8f8f-8f8f-8f8f8f8f8f8f"}
```

**Poll Status:** `GET https://api.perplexity.ai/chat/completions/async/{task_id}`

**Response:**
```json
{
  "status": "completed",
  "choices": [{"message": {"role": "assistant", "content": "..."}}],
  "usage": {"prompt_tokens": 20, "completion_tokens": 100}
}
```

---

## Structured Outputs

### JSON Schema

Request structured JSON responses with defined schema:

```python
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{
        "role": "user",
        "content": "Find top 3 AI startups with recent funding"
    }],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "schema": {
                "type": "object",
                "properties": {
                    "startups": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "company_name": {"type": "string"},
                                "funding_amount": {"type": "string"},
                                "focus_area": {"type": "string"}
                            },
                            "required": ["company_name", "funding_amount", "focus_area"]
                        }
                    }
                },
                "required": ["startups"]
            }
        }
    }
)
```

### Regex Pattern Matching

Extract specific patterns from responses:

```python
completion = client.chat.completions.create(
    model="sonar",
    messages=[{
        "role": "user",
        "content": "Find the investor relations email for Tesla Inc."
    }],
    response_format={
        "type": "regex",
        "regex": {
            "regex": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        }
    }
)
```

---

## Code Examples

### Python SDK

```python
from perplexity import Perplexity

client = Perplexity()

# Standard search
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "What is quantum computing?"}]
)

# Advanced search with Sonar Pro
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{
        "role": "user",
        "content": "Analyze economic implications of renewable energy"
    }]
)

# Reasoning tasks
completion = client.chat.completions.create(
    model="sonar-reasoning",
    messages=[{
        "role": "user",
        "content": "Solve this problem step by step..."
    }]
)
```

### TypeScript SDK

```typescript
import Perplexity from "@perplexity/client";

const client = new Perplexity();

const completion = await client.chat.completions.create({
  model: "sonar-pro",
  messages: [
    { role: "user", content: "What are the latest AI developments?" }
  ]
});

console.log(completion.choices[0].message.content);
```

### cURL

```bash
curl -X POST "https://api.perplexity.ai/chat/completions" \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "messages": [
      {"role": "system", "content": "Be precise and concise."},
      {"role": "user", "content": "What are the latest AI trends?"}
    ],
    "max_tokens": 1024
  }'
```

---

## Search Filters

### Domain Filtering

```python
response = client.search.create(
    query="climate change research",
    max_results=20,
    search_domain_filter=["nature.com", "science.org", "cell.com"]
)
```

### Language Filtering

```python
response = client.search.create(
    query="artificial intelligence",
    max_results=10,
    search_language_filter=["en", "de"]
)
```

### Date Range Filtering

```bash
curl -X POST 'https://api.perplexity.ai/search' \
  -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "AI developments",
    "search_after_date": "01/01/2025",
    "search_before_date": "12/01/2025"
  }'
```

---

## MCP Server Integration

### Environment Variables

```bash
export PERPLEXITY_API_KEY="pplx-your-api-key-here"
export PERPLEXITY_TIMEOUT_MS="600000"  # 10 minutes for long research

# Optional: Proxy configuration
export PERPLEXITY_PROXY="https://proxy.company.com:8080"
```

### Claude Code Configuration

```json
{
  "mcpServers": {
    "perplexity": {
      "command": "npx",
      "args": ["@perplexity-ai/mcp-server"],
      "env": {
        "PERPLEXITY_API_KEY": "pplx-your-key-here"
      }
    }
  }
}
```

### Docker Deployment

```bash
# Build image
docker build -t perplexity-mcp-server .

# Run with API key
docker run --rm -e PERPLEXITY_API_KEY=your_key_here perplexity-mcp-server

# Run with env file
docker run --rm --env-file .env perplexity-mcp-server
```

---

## Rate Limits by Tier

| Model | Tier 1-4 | Tier 5 |
|-------|----------|--------|
| sonar | 50-500 RPM | 2000 RPM |
| sonar-pro | 50-500 RPM | 2000 RPM |
| sonar-reasoning | 50-500 RPM | 2000 RPM |
| sonar-reasoning-pro | 50-500 RPM | 2000 RPM |
| sonar-deep-research | 10-50 RPM | 100 RPM |

---

## Best Practices

### 1. Model Selection

- **Quick queries:** Use `sonar` for fast, straightforward responses
- **Complex analysis:** Use `sonar-pro` for deeper research with more citations
- **Exhaustive research:** Use `sonar-deep-research` for detailed reports
- **Problem-solving:** Use `sonar-reasoning` or `sonar-reasoning-pro`

### 2. Cost Optimization

- Use `search_context_size: "low"` for simple queries
- Limit `max_tokens` to what you actually need
- Use Search API when you only need raw results
- Batch related queries when possible

### 3. Quality Enhancement

```python
system_message = """You are a precision research assistant.

Requirements:
- Use specific data with year (no generic statements)
- Always add context: change over time + comparison to benchmarks
- If no reliable sources: clearly say so (no guessing)
- Structure:
  1) Key facts (2-3 sentences, with numbers)
  2) Data points (bullets, incl. year)
  3) Brief interpretation
  4) Sources (institution + year)
"""
```

---

## Error Handling

### Common Error Responses

```json
{
  "failed_at": 1677652288,
  "error_message": "Rate limit exceeded",
  "status": "error"
}
```

### Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| 400 | Bad Request | Check request parameters |
| 401 | Unauthorized | Verify API key |
| 429 | Rate Limited | Wait and retry, or upgrade tier |
| 500 | Server Error | Retry with exponential backoff |

---

## Related Resources

- [Perplexity API Docs](https://docs.perplexity.ai)
- [API Cookbook](https://github.com/ppl-ai/api-cookbook)
- [Official MCP Server](https://github.com/perplexityai/modelcontextprotocol)
- [Perplexity Dashboard](https://www.perplexity.ai/settings/api)
