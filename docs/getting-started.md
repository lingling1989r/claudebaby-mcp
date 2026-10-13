# Connect ClaudeBaby MCP to Codex, Cursor or another HTTP MCP client

ClaudeBaby uses `https://claudebaby.cn/mcp` with Streamable HTTP and an API key in the Authorization header. Start with capability discovery, then verify one real data query. A connection or a tool list alone does not prove data coverage.

## Account and credentials

[Create a ClaudeBaby account](https://claudebaby.cn/console/register?ref=M8YYGRN4), get your key from its console, and check your balance and permissions. Use your own key. Never put it in a URL, a GitHub issue, a shared example or a screenshot.

## Codex configuration

Merge [codex.config.toml](../examples/codex.config.toml) into your existing personal Codex configuration; do not overwrite other settings.

```toml
[mcp_servers.claudebaby]
url = "https://claudebaby.cn/mcp"
bearer_token_env_var = "CLAUDEBABY_API_KEY"
startup_timeout_sec = 30
tool_timeout_sec = 30
```

Set `CLAUDEBABY_API_KEY` in the local environment visible to the client, using your normal private secret-management method. This file stores only the variable name. A desktop app may not inherit a terminal's environment; check its documented environment setup rather than printing the secret to troubleshoot. Restart or reconnect after configuration changes.

These fields follow the [official Codex MCP documentation](https://developers.openai.com/codex/mcp). The configuration format was checked against that documentation; every client/version combination has not been tested here.

## Cursor configuration

Use Cursor's private global MCP configuration, typically `~/.cursor/mcp.json`. Start from [cursor.mcp.example.json](../examples/cursor.mcp.example.json), which contains an explicit placeholder:

```json
{
  "mcpServers": {
    "claudebaby": {
      "url": "https://claudebaby.cn/mcp",
      "headers": {"Authorization": "Bearer YOUR_API_KEY"}
    }
  }
}
```

Replace the placeholder only in your personal configuration, not in a tracked project file. Save and reconnect. If your installed client supports secure secret input, prefer that feature. See [Cursor's official MCP guide](https://prod.cursor.com/help/customization/mcp).

## Other clients

Choose remote HTTP/Streamable HTTP and supply this URL and Authorization header. Do not assume every client's JSON uses the same `type` field. Read that client's current documentation; OAuth-only clients require additional compatibility work because this integration uses a user-provided API key.

## Verification ladder

1. `initialize` and the initialized notification: protocol connection.
2. `tools/list`: available schemas for this account.
3. `business_capabilities` and `source_support`: availability declarations.
4. One actual platform search/detail call: business response.
5. Read returned source records and fields: usable research evidence.

Tool names may have client-added prefixes. For example, the source support tool can appear as `business_source_support`. Use the host catalogue rather than guessing a prefix.

First request:

> Use ClaudeBaby to check whether Reddit search is available. Discover the actual tools and schemas, then run a small search for ESP32 with no more than five candidates. Keep source links and dates, and report missing fields or failed steps.

The request may consume credits when it reaches a real data query. Set a small scope first.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| 401 | Missing, invalid or expired personal key; update the client credential |
| 403 | Account or capability permission; do not treat it as empty search results |
| Insufficient credits | Balance and current prices; recharge only through your own decision |
| Tool not found | Re-read the current tool list and namespacing |
| Invalid parameters | Read the exact input schema; keep required fields and types |
| Timeout / rate limit | Narrow the query; follow retry guidance and retry once, then report the gap |
| Empty or partial result | Inspect provenance and partial status; don't invent records |

[Capabilities](platforms.md) · [FAQ](faq.md) · [Home](../README.en.md)
