# ClaudeBaby MCP — social and ecommerce research data for AI agents

[中文](README.md) · [Quickstart](docs/getting-started.md) · [Capabilities](docs/platforms.md) · [Website](https://claudebaby.cn/)

ClaudeBaby is a hosted Model Context Protocol data service. Connect an AI agent over HTTPS to query available social posts, comments and marketplace products for brand research, customer needs, competitor analysis and sourcing comparisons.

This repository contains public connection templates, research workflows and troubleshooting guides. The hosted service uses account permissions and credits; you do not need to clone or run the backend.

![Question → capability check → query → sources and reusable methods](assets/research-flow.svg)

## Make your first verified query

1. [Register with ClaudeBaby](https://claudebaby.cn/console/register?ref=M8YYGRN4) and obtain your own API key from the console. Existing users can keep their account.
2. Add `https://claudebaby.cn/mcp` as a Streamable HTTP server. Authentication uses the `Authorization: Bearer YOUR_API_KEY` header.
3. Discover the current tools, then use `business_capabilities` and `source_support` to check your target source and capability.
4. Run one small platform query. Inspect links, dates, fields and errors before expanding the sample.

Keep the key in your personal client configuration. See the [quickstart](docs/getting-started.md), [Codex template](examples/codex.config.toml) and [Cursor template](examples/cursor.mcp.example.json). Clients may namespace tool names; use the actual tool catalogue.

## Research workflows

| Question | Approach | Guide |
| --- | --- | --- |
| What are Reddit users saying about a brand? | Read posts and real comments; separate reported outcomes from inference | [Reddit brand research](docs/reddit-brand-research.md) |
| Is a cheap ESP32 listing a board or a complete kit? | Verify SKU, included parts, MOQ and tier prices before comparing overseas offers | [1688 sourcing and kit comparison](docs/1688-kit-comparison.md) |
| Which Xiaohongshu and YouTube brand examples are worth studying? | Search each available platform, retain sources and analyze methods | [Social case research](docs/social-case-research.md) |
| How do I connect WorkBuddy? | Remote MCP with a user-supplied key, then tool discovery and a small query | [WorkBuddy guide](docs/workbuddy.md) |

[Research prompts](examples/research-prompts.md) also cover B2B acquisition, community needs and negative reviews. These are agent workflows, not automatic publishing, purchasing or report-generation features.

## Availability is a live check

Check the public [discovery document](https://claudebaby.cn/.well-known/mcp.json), your account's `tools/list` and an actual business query.

The 2026-10-13 discovery snapshot labels Reddit, X, Xiaohongshu, YouTube, Douyin, TikTok, 1688, Amazon, Shopee, Temu, TikTok Shop and Walmart as live. This does not verify every field or guarantee access for your account. Bilibili, LinkedIn and Instagram are among planned sources; Facebook is reported as unsupported.

The business catalogue currently exposes `business_capabilities`, `source_support` and `product_research`. `market_research`, unified `content_search` and `topic_monitor` are planned. Use available platform-native tools for social queries. See [capabilities and evidence limits](docs/platforms.md).

## Samples, pricing and reports

The [capability-check sample](examples/capability-check.json) records a real, sanitized support response. It is not proof of a successful full market-data query. Research results depend on actual account access and data coverage.

Queries may consume credits. Check your console and the [pricing catalogue](https://claudebaby.cn/pricing.json) before a large study. The MIT licence covers these docs and templates, not hosted-service access or third-party media rights.

For an illustrated Excel case library and method breakdowns, combine the data connection with the separate [social-case-to-excel Skill](https://github.com/lingling1989r/social-case-to-excel). Keep source evidence, reported effects, inference and business outcomes distinct.

## Feedback

[Report a reproducible issue](https://github.com/lingling1989r/claudebaby-mcp/issues/new/choose) with your client version, platform, tool name and sanitized error. If the configurations or workflows help, ⭐ Star the repository to save it for later.

See the [FAQ](docs/faq.md). Updated 2026-10-13.
