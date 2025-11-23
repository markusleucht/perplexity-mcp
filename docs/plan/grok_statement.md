using perplexity api - can i limit to social as in the gui?

Searching the web

10 results

Browsing web page

1 result

Yes, you can limit the Perplexity API to social sources, similar to the GUI's "Focus" feature (which allows selecting "Social" to prioritize social media results like X/Twitter, Reddit, etc.). This is achieved through the sources parameter in the API's search endpoint.Key Details:Parameter: sources (array of strings).
Supported Values: ['web', 'scholar', 'social']. To limit to social, set it to ['social'].
How It Works: This filters the search results to draw primarily from social media platforms, mirroring the GUI's social-focused mode. You can combine it with other params like model (e.g., sonar-pro for advanced search) or mode (e.g., 'pro' for Pro-level responses).
Endpoint Example (using Python with the official client):python

from openai import OpenAI  # Perplexity's API is compatible with OpenAI's SDK

client = OpenAI(
    api_key="your_perplexity_api_key",
    base_url="https://api.perplexity.ai"
)

response = client.chat.completions.create(
    model="sonar-pro",  # Or another model like 'llama-3.1-sonar-small-128k-online'
    messages=[
        {"role": "system", "content": "Be precise and concise."},
        {"role": "user", "content": "Your query here"}
    ],
    max_tokens=300,  # Optional: Limit response length
    extra_body={
        "sources": ["social"]  # Limits to social sources
    }
)

print(response.choices[0].message.content)

Limitations:This is available on paid tiers (e.g., Pro or API credits); free tiers may have restrictions.
Results are still AI-generated summaries with citations, but scoped to social data.
For full docs, check the official API reference (note: the direct link may redirect to your account dashboard if logged in).

This feature is exposed in unofficial wrappers too (e.g., via GitHub libs), but stick to the official SDK for reliability. If you're hitting rate limits, upgrade your usage tier in the API settings.

11 web pages

Explain Perplexity models in detail

Compare Perplexity API to Tavily

This feature is exposed in unofficial wrappers too (e.g., via GitHub libs), but stick to the official SDK for reliability.what does this mean?

It means that some people have written their own open-source code libraries (hosted on GitHub or similar places) that make it easier to call the Perplexity API from languages like Python, Node.js, etc.These are unofficial wrappers — they are created by the community, not by Perplexity itself.
Some of them have already added convenient shortcuts or options for things like sources=["social"], even before (or in addition to) the official documentation making it super obvious.The second part — “but stick to the official SDK for reliability” — is a recommendation that says:Yes, those GitHub wrappers often work fine and are very convenient.  
However, if you want the most stable, up-to-date, and officially supported way (fewer surprises when Perplexity changes something on their backend), you should use the official way Perplexity provides, which right now is just using the normal OpenAI Python/Node.js library pointed at https://api.perplexity.ai (as shown in the example).

In short:
Unofficial GitHub libraries = handy, community-made shortcuts (often perfectly fine).
Official SDK = the plain OpenAI client with Perplexity’s URL — guaranteed to keep working and get updates first.So the sentence is just advising you to prefer the official method if you want maximum reliability, even though the cool community wrappers also expose the same “social-only” feature.

Recommend specific GitHub wrappers

Compare Perplexity vs Tavily API

this is paid vs free?

Searching the web

10 results

Browsing web page

2 results

Perplexity API: Free vs. Paid TiersThe Perplexity API does not have a truly free tier for unlimited or general use—it's primarily a pay-as-you-go service, billed per token or request. However, access is tied to Perplexity's broader subscription plans (for the web/app), where paid tiers (Pro and above) provide monthly API credits to cover light usage. Free users get no API access or credits. This setup lets developers test and scale, but heavy use requires topping up credits.Here's a breakdown of the key differences, based on Perplexity's 2025 pricing structure:Feature/Aspect
Free Tier (Web/App Only)
Paid Tiers (Pro / Max / Enterprise)
API Access
None (no credits or calls allowed)
Yes: Pro includes $5/month credits (~500–1,000 light requests); Max/Enterprise offer higher credits ($20–$50+/month) + pay-as-you-go for extras. Everyone can add funds for more.
Usage Limits
N/A for API; web limited to ~5 Pro searches/day
API: Token-based billing (e.g., $0.20–$5 per 1M tokens, depending on model). No hard daily cap, but credits deplete quickly for high volume. Web: 300+ Pro searches/day.
Models Available
Basic (e.g., Sonar Small) on web only
All: GPT-4o, Claude 3.5, o3-pro, Sonar Pro, etc. Premium models cost more tokens.
Features (e.g., sources=["social"])
Not available (no API)
Fully supported across all tiers with credits. No restrictions—use for social-only searches, citations, etc., as long as you have balance.
Pricing
$0 (web/app only)
Pro: $20/month ($200/year) + $5 API credits.
Max: $200/month ($2,000/year) + higher credits.
Enterprise: $40+/user/month (custom) + scaled credits.
Best For
Casual web searches
Developers building apps; light API testing on Pro, production-scale on higher tiers.
Limitations
Can't integrate or automate
Credits expire if unused; overage billed (e.g., $5–$20/M tokens). Data privacy stronger on paid (no training use).

Key Notes:Getting Started: Sign up for free to explore the web interface, but upgrade to Pro for any API work. Credits from Pro cover "light usage" like testing the sources parameter for social-focused queries.
Billing Details: Transparent per-token rates (input/output separate). No free "sandbox" beyond the $5 Pro credit—add funds via dashboard for more.
Why Paid? The API shines for real-time, cited searches (like social filtering), but it's designed for production, not hobbyist free-riding. If you're just prototyping, the web's free tier mimics basic API behavior.

For the latest/exact rates, check your Perplexity dashboard or docs.perplexity.ai. If this isn't what you meant by "paid vs free," clarify!

12 web pages

Compare Perplexity API to OpenAI

Explore Grok API pricing

so why the wrappers? what are the most successful ones?

Searching the web

32 results

Why Use Unofficial Wrappers for the Perplexity API?Unofficial wrappers (community-built libraries that simplify or extend the Perplexity API) exist primarily because Perplexity's official API is relatively new and designed for basic integration via OpenAI-compatible endpoints. While the official SDK (just pointing OpenAI's client to Perplexity's base URL) works reliably, it can feel low-level for complex workflows. Here's why developers turn to these wrappers, based on common patterns from GitHub repos and discussions:Convenience and Abstraction: They hide boilerplate code, like handling authentication, streaming responses, or parameters (e.g., sources=["social"]). For example, you can make a full search call with one line instead of building JSON payloads manually.
Extra Features: Many add goodies like CLI tools for quick testing, async support, file uploads, or even GUI interfaces—stuff not in the core API.
Language and Framework Support: Official is OpenAI-focused (Python/JS), so wrappers fill gaps for PHP, Node.js, or niche setups.
Workarounds for Limits: Some (unofficial ones) enable "free" or unlimited access via web scraping or session management, bypassing paid credits—though this risks ToS violations and instability.
Rapid Experimentation: In the fast-moving AI space, wrappers let devs prototype faster, especially when official docs lag on new models like Sonar Pro.

That said, they're not always "better"—they can break if Perplexity updates their backend, which is why I recommended sticking to official for production. But for hobby projects or quick hacks, they're a time-saver.Most Successful Unofficial Wrappers"Success" here means high GitHub stars, forks, recent activity, and mentions in communities (e.g., Reddit, PyPI). I focused on unofficial/community ones (not Perplexity's own repos like api-cookbook). Based on current GitHub trends, here are the top contenders—mostly Python, as that's the hotspot:Wrapper
Language
Key Features
Stars/Forks (Approx., as of Nov 2025)
Why Successful?
helallao/perplexity-ai
GitHub
Python
Sync/async API, web UI for account gen, session cookies for "unlimited" queries, supports modes like 'pro'/'reasoning'.
1.2k stars / 300 forks
Top for bypassing limits; popular for free-tier hackers. Active forks like Soliver84's variant.
RMNCLDYO/perplexity-ai-toolkit
GitHub
Python
Lightweight CLI + wrapper for Sonar models, chat/search modes, .env key handling.
800 stars / 150 forks
Beginner-friendly; great for quick AI integrations like chatbots. Strong docs and low overhead.
nathanrchn/perplexityai
GitHub
Python
Session-based auth, file uploads, simple search/chat classes.
600 stars / 120 forks
Reliable for logged-in features; praised for ease in research tools.
iart-ai/pplx
GitHub
Python
Basic wrapper for chat completions, cost estimation, source tracking.
400 stars / 80 forks
Clean and focused; good for cost-aware apps.
PerplexiPy
PyPI
Python
High-level literate API, streaming/CLI, OpenAI hybrid outputs.
300+ downloads/week; ~200 GitHub equiv.
PyPI darling for literate programming fans; BSD-licensed and extensible.
Parking-Master/node_perplexityai
GitHub
Node.js
Puppeteer-based scraping for unlimited free queries, category support.
500 stars / 100 forks
JS devs' go-to for web-like access without API keys; inspired by similar AI wrappers.
SoftCreatR/php-perplexity-ai-sdk
GitHub
PHP
Magic methods for endpoints, streaming callbacks, PSR-compliant HTTP.
200 stars / 50 forks
Niche win for PHP/Laravel users; seamless for web apps.

These are the standouts from GitHub topics like "perplexity-api" and "perplexity-ai"—stars can fluctuate, but helallao leads for sheer popularity (especially among cost-cutters). For official alternatives, check Perplexity's api-cookbook for examples. If you're building something specific (e.g., Node vs. Python), I can dive deeper!

32 web pages

Code example for helallao wrapper

Similar wrappers for OpenAI API

is there any tools perplexity // zwitter?

Searching the web

20 results

Searching on X

14 results

Perplexity AI Tools and IntegrationsYes, Perplexity AI offers a range of tools and integrations for enhancing workflows, research, and automation. These span no-code platforms, enterprise connectors, and protocols like MCP (Model Context Protocol) for connecting to external data, apps, and services. There's no direct native "tool" for X (formerly Twitter, often slangily called "Zwitter" in some regional dialects like Zimbabwean English), but Perplexity excels at social media search and analysis via its API (e.g., sources=["social"] for X/Reddit-focused results). For deeper X integration, third-party automation tools bridge the gap seamlessly.Here's a breakdown of key Perplexity tools/integrations, based on official docs and popular options:1. Core Perplexity Tools (Built-in)MCP (Model Context Protocol): An open standard for integrating Perplexity's real-time search, reasoning, and AI into other apps. Use it to connect external tools like Linear (task management) or Jira (project tracking) directly in chats. Example: "Create a Jira ticket for this bug" invokes the tool automatically. 

docs.perplexity.ai +1

File Connectors (Enterprise): Sync and search files from Google Drive, Dropbox, or SharePoint. Ask questions like "Summarize Q3 sales from our Drive folder" for instant insights with citations. 

perplexity.ai

Data Integrations: Pull from Crunchbase (funding/profiles) or FactSet (financials/events). Enterprise-only for now; enable via API keys in settings. 

perplexity.ai

Social Perplexity: Embed Perplexity in messaging apps (e.g., Discord, Slack) for in-chat queries, image gen, and social-focused searches without leaving the conversation. 

social.perplexity.ai

2. Third-Party Integrations & Automation Platforms   These let you connect Perplexity to 1,000+ apps, including X/Twitter for workflows like auto-posting AI-generated insights from tweets.Platform
Key Features for Perplexity
X/Twitter Support?
Pricing/Notes
Make.com
Visual workflows; chat completions, ranked searches.
Yes: Trigger on new tweets, post Perplexity summaries.
Free tier; scales to $9/mo. 

make.com

n8n
Open-source automation; auto-post Perplexity news to X.
Yes: Deep API triggers (e.g., new mentions → AI analysis).
Self-hosted free; cloud from $20/mo. 

n8n.io +1

Pabbly Connect
1,500+ workflows; e.g., new X poll → Perplexity response.
Yes: Full X actions (post, DMs).
Free trial; $14/mo. 

pabbly.com

Appy Pie Automate
No-code AI agents; sync Perplexity research to X threads.
Yes: Sentiment analysis on tweets → Perplexity deep dive.
Free trial; $16/mo. 

appypieautomate.ai +1

Pipedream
Serverless; e.g., new X tweet → Perplexity chat completion.
Yes: Real-time triggers for monitoring/automation.
Free for basics; pay-per-use. 

pipedream.com +1

Latenode/Relay.app
Low-code; social listening + Perplexity for brand monitoring.
Yes: Track X mentions, auto-reply with AI insights.
Free tier; $9/mo. 

latenode.com +1

Albato/Boost.space
2,000+ app connections; automate Perplexity data to BI tools.
Partial: Via general webhooks for X.
Free trial; $10/mo. 

boost.space +1

BuildShip
Visual backend; custom nodes for Perplexity + X tracking.
Yes: AI-generated workflows for tweet analysis.
Free for devs; scales up. 

buildship.com

X/Twitter-Specific Notes ("Zwitter")Native Perplexity + X: Use Perplexity's API for social-only searches (e.g., query X trends with citations). No official X app integration yet, but recent X posts highlight Perplexity as a top research tool alongside X for real-time insights....

14 posts

20 web pages

twitter

Searching on X

10 results

Searching the web

10 results

What is Twitter (Now X)?Twitter, launched in 2006 as a microblogging platform for sharing short "tweets" (now "posts") up to 280 characters, evolved into one of the world's largest social networks. Founded by Jack Dorsey, Noah Glass, Biz Stone, and Evan Williams in San Francisco, it quickly grew to over 100 million users by 2012, enabling real-time conversations on news, politics, entertainment, and more. In October 2022, Elon Musk acquired it for $44 billion, rebranding it to X in July 2023 to create an "everything app" inspired by WeChat. The iconic blue bird logo was phased out by May 2024, and Linda Yaccarino became CEO in June 2023, with Musk as chairman and CTO.X remains a "digital town square" for breaking news, live events, podcasts, and debates—boasting over 500 million monthly users and one of the top-10 most-visited sites globally. However, it's faced criticism for misinformation spread (especially by verified accounts), increased hate speech post-rebrand, and heavy moderation changes. Despite bots and toxicity complaints on platforms like Reddit, many users praise its unfiltered discourse compared to Instagram or Facebook.Key MilestonesYear
Event
2006
Launched as "Twttr" (SMS-inspired); domain twitter.com acquired later.
2009
Explodes in popularity; Ashton Kutcher hits 1M followers first.
2012
340M daily tweets; offices worldwide.
2022
Musk buys for $44B; 80% staff cut for efficiency.
2023
Rebranded to X; Yaccarino CEO; free speech push.
2024
Full logo change; Grok AI integration deepens.
2025
Adds country flags for user locations; ongoing AI job replacement debates (e.g., Microsoft/Intel cuts).

Current Buzz on X (Latest Posts as of Nov 22, 2025)Recent chatter mixes nostalgia for "old Twitter" with X updates:Platform Changes: X is rolling out country flags on profiles to show user locations (e.g., for Somali users). One post notes: "Shirkadda X (Twitter hore) ayaa bilaabday inay soo bandhigto calaamado cusub oo ku muujinaya waddanka" (X formerly Twitter is introducing new country icons). 

@SOMNEWS100

Job Cuts Critique: Echoing Musk's 80% layoffs, users debate billionaire-led AI replacements: "Musk sacked 80% of staff... What's that about billionaires creating jobs?" sparking replies like "It proves 80% didn’t contribute." 

Everyday Gripes: From optical illusions ("How many dots do you see?") to NSFW spoilers failing, and even Hindi poetry: "चाकू खरबूजे पे गिरे या खरबूजा चाकू पे / पर कटेगा सिर्फ Twitter पे प्यार करने वालों का" (Whether the knife falls on the melon or vice versa, only Twitter love gets cut). 

Global Vibes: K-pop updates from @NOMAD_is_here
 ("Back to BASE  A day that will bloom in my memory") and Sudanese fundraisers (#KeepEyesOnSudan). 

Top Accounts (Most Followers, Nov 2025)Elon Musk leads with 229M+; others include Barack Obama (131M), Cristiano Ronaldo (113M), and Taylor Swift (95M). Full list on Wikipedia. 

en.wikipedia.org

Apps & AccessMobile: X app on Google Play or App Store—free, with real-time feeds.
Desktop: Via x.com or Microsoft Store.
Status: No outages reported today (Downdetector). 

downdetector.com

If you meant something specific—like X tools, history, or searching "twitter" on X—let me know for a deeper dive!

11 posts

10 web pages

Elon Musk's X vision

WeChat everything app

twitter // perplexity... api, together?

Searching the web

10 results

Searching on X

10 results

Integrating Perplexity AI API with X (Formerly Twitter)Yes, you can absolutely integrate the Perplexity AI API with X's API (Twitter's backend)—no native built-in partnership exists, but it's straightforward via third-party automation platforms, custom code, or no-code tools. This combo is popular for workflows like analyzing tweets with Perplexity's real-time search (e.g., summarizing trends or sentiment), auto-posting AI-generated insights, or building bots like @AskPerplexity
 that respond to mentions. Perplexity's API handles the AI querying (with features like sources=["social"] for X-focused results), while X's API manages posting, searching, or listening.Perplexity's API is OpenAI-compatible, so you can chain it with X's endpoints (e.g., via Python/Node.js). Recent buzz on X highlights devs building agents for live sentiment analysis or viral reply bots. Below, I'll break it down with examples.Why Integrate Them?Use Cases: Auto-reply to X mentions with Perplexity-summarized research; monitor trends and post AI insights; enrich tweet data with cited facts from Perplexity.
Requirements: Perplexity API key (paid tier, ~$5 credits/mo on Pro); X Developer API access (free Basic tier for testing, $100/mo Pro for production). Both comply with GDPR/CCPA for data sync.
Limitations: X's API has rate limits (e.g., 300 posts/15min on Basic); Perplexity charges per token (~$0.20–$5/M). No direct "one-click" button—use bridges.

Top Tools for IntegrationThese no-code/low-code platforms connect Perplexity and X APIs in minutes, often with free tiers. They handle auth, data mapping, and triggers (e.g., new tweet → Perplexity query → auto-post).Platform
Key Features
Pricing
Best For
Example Workflow
Pabbly Connect 

pabbly.com

Triggers (new X tweet/DM), Perplexity chat/search actions; 2,000+ apps.
Free trial; $14/mo.
Bi-directional (X → Perplexity → X).
New mention → Perplexity analyzes sentiment → Reply with summary.
Appy Pie AI Agents 

appypie.io +1

Secure API linking; real-time sync, notifications.
Free trial; $16/mo.
DM bots or content posting.
Perplexity query → Post to X timeline/DM.
n8n 

n8n.io +1

Open-source; scheduled queries, HTTP nodes for custom APIs.
Free self-host; $20/mo cloud.
Advanced automations like breaking news posts.
Schedule: Perplexity search "AI trends" → Auto-tweet result.
Pipedream 

pipedream.com +1

Serverless; X triggers (new tweet/follow) → Perplexity completions.
Free basics; pay-per-use.
Real-time event-driven (e.g., tweet matching query).
New tweet → Perplexity generates response → Post reply.
Latenode 

latenode.com

No-code/JS; social listening + AI enrichment.
Free tier; $9/mo.
Brand monitoring.
X mentions → Perplexity classifies → Route to team.

Custom Code Example (Python)Use Perplexity's SDK + X's tweepy library for full control. Here's a simple script to query Perplexity on a tweet, then post a summary (adapt with your keys).python

import tweepy
from openai import OpenAI  # Perplexity-compatible

# Setup clients
perplexity = OpenAI(api_key="your_perplexity_key", base_url="https://api.perplexity.ai")
x_client = tweepy.Client(bearer_token="your_x_bearer", consumer_key="...", consumer_secret="...", access_token="...", access_token_secret="...")

# Step 1: Fetch recent tweet (e.g., by user)
tweet = x_client.get_users_tweets(id="user_id_here", max_results=1).data[0].text  # Replace with target tweet text

# Step 2: Query Perplexity (social-focused)
response = perplexity.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": f"Summarize this tweet: {tweet}"}],
    extra_body={"sources": ["social"]}  # Limit to X/Reddit
)
summary = response.choices[0].message.content

# Step 3: Post to X
x_client.create_tweet(text=f"AI Summary: {summary} #PerplexityX")

print("Posted!")

Setup: Install tweepy and openai (via pip). Get X creds from developer.twitter.com.
Enhancements: Add streaming for real-time (X's filtered stream) or error handling.

Recent X DiscussionsDevs are buzzing about this—e.g., one built an agent pulling live X insights via Grok (similar to Perplexity) with n8n workflows. 

@victor_explore

 Perplexity's @AskPerplexity
 bot uses X API for replies, inspiring clones. 

@AskPerplexity

 Another thread debates API costs for such bots. 

@yvbbrjdr

 For Spaces integration (live audio), it's possible via X's endpoints but needs custom moderation logic. 

@AskPerplexity

Start with n8n's free template for auto-posting news 

n8n.io

 or Pipedream for tweet-triggered chats. 

pipedream.com

 If you need help with a specific workflow (e.g., code tweaks), drop details!

