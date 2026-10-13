# ClaudeBaby MCP connector for WorkBuddy

WorkBuddy supports remote MCP connectors using HTTPS Streamable HTTP and a user-supplied token form. ClaudeBaby connects at `https://claudebaby.cn/mcp`, with a personal API key in the Authorization header.

## Current release status

On 2026-10-13, the ClaudeBaby Data MCP connector v1.0.1 was submitted to WorkBuddy and its developer list showed “under review”. This is not a claim that it is already available in the marketplace. Check the current market status before asking users to install it.

## Credential setup

The connector's password-type field is `CLAUDEBABY_API_KEY`. WorkBuddy substitutes it in `Authorization: Bearer ${CLAUDEBABY_API_KEY}`. Each user supplies their own key; the published package contains no account key. The minimum declared client version is 4.24.0, covering token mode and bilingual example fields.

Once the connector is available, install it through WorkBuddy's connector interface, fill your own key, discover the tools and run a small query. If your current client exposes custom MCP settings, use the same HTTPS endpoint and header according to its documentation; the exact client UI is not guaranteed here.

## Verification

First ask which sources and tools are available. Then run one real platform query and check its results. Protocol and source-support tests do not establish that a complete research task succeeded.

Reference: [WorkBuddy's official connector specification](https://open.workbuddy.cn/docs/connector).

[General quickstart](getting-started.md) · [Home](../README.en.md)
