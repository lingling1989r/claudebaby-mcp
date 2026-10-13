---
name: claudebaby-research
description: Use ClaudeBaby MCP for supported public social and ecommerce research. Check live tools and source support first, then run the smallest useful query and preserve evidence boundaries.
---

# ClaudeBaby Research

Use the ClaudeBaby MCP server when the user asks for social listening, public community discussion, brand or competitor research, ecommerce product comparisons, supplier discovery, or social case collection.

## Workflow

1. Inspect the connected server's current tool list. Tool names may be namespaced by the host; use the exact names and schemas exposed in this session.
2. Call `business_capabilities` and `source_support` when available. Confirm that the requested platform and capability are currently supported before making a data query.
3. Start with a narrow query: one platform, clear keywords, a recent time window, and only the fields needed. Ask the user to narrow the scope when a broad request would create many costly queries.
4. Preserve source URLs, publication dates, retrieval time, query scope, and platform where available. Separate source statements, observed metrics, and analysis.
5. Treat partial results, unsupported sources, authentication errors, and empty responses as distinct outcomes. Do not describe an empty or failed query as proof that no discussion exists.
6. For product comparisons, distinguish variant, quantity, MOQ, shipping, promotion, currency, and capture date. Do not infer that superficially similar listings are equivalent SKUs.
7. Present limitations and recommend a manual source check for consequential price, availability, or historical claims.

## Safety and boundaries

- Use public or account-authorized research only. Do not seek private personal data, bypass access controls, or infer sensitive traits.
- Do not publish, message, purchase, or change external account state as part of research unless the user separately requests that action.
- Do not claim complete platform coverage or guaranteed metrics. The live server schema and query result define what was actually available.
- Never ask users to paste API keys into chat or a repository. Credentials must be entered through the client's private MCP authentication flow or private local configuration.
