# ClaudeBaby MCP platform support and evidence limits

Checked 2026-10-13. This is a dated snapshot, not a service guarantee. Use [live discovery](https://claudebaby.cn/.well-known/mcp.json) and your authenticated tool catalogue before each study.

| Surface | Snapshot | What still needs validation |
| --- | --- | --- |
| Social sources | Reddit, X, Xiaohongshu, YouTube, Douyin, TikTok labelled live | Account access, tool schemas, search/detail/comment coverage, timestamps and actual results |
| Commerce sources | 1688, Amazon, Shopee, Temu, TikTok Shop, Walmart labelled live | Models, markets, currencies, SKU options, price tiers and returned records |
| Planned platforms | Bilibili, LinkedIn, Instagram and others | Do not advertise them as callable |
| Unsupported source | Facebook reported unsupported | Do not turn unsupported into “no data found” |

## Business tools

| Tool | Status | Purpose |
| --- | --- | --- |
| `business_capabilities` | Available | Lists available and planned business contracts |
| `source_support` | Available | Checks a source and optional named capability |
| `product_research` | Available | Searches selected marketplaces and returns source-aware partial results |
| `market_research` | Planned | Not callable as a business tool yet |
| `content_search` | Planned | Use actual platform-native tools instead |
| `topic_monitor` | Planned | No unified monitoring claim |

Names may be namespaced by the host. Platform-native tools and their schema are discovered at runtime. Do not infer full commercial data access from a live marker.

## What was verified

On 2026-10-13, live MCP checks passed for rejected missing/invalid authentication, initialization, initialized notification, tools/list, a Reddit source-support query, invalid tool arguments and an unknown tool. This verifies those behaviours, not every data platform or all client applications.

[Sanitized support-response sample](../examples/capability-check.json). A supported declaration is weaker evidence than a returned post/product record. A returned record is still weaker than independently validated claims about sales, customer acquisition or supplier quality.

## Preserve these distinctions

- Original source text versus a researcher's inference.
- Publication date versus retrieval date; earliest found versus absolutely earliest.
- Likes/views/comments versus sales or revenue.
- Listing price versus delivered cost and profit.
- Development board versus complete kit; pack size and SKU variant matter.
- Source cover image versus a screenshot or full-video review.

[Home](../README.en.md)
