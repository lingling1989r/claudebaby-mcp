# ClaudeBaby Research for Codex

This plugin connects Codex to the hosted ClaudeBaby MCP service and adds a reusable research workflow for supported social and ecommerce sources.

## Install from the GitHub marketplace

Add the public repository as a Codex plugin marketplace source:

```sh
codex plugin marketplace add lingling1989r/claudebaby-mcp
```

Then open Codex's Plugins directory, choose the **ClaudeBaby MCP** marketplace, and install **ClaudeBaby Research**. If your Codex client does not show the repository marketplace, use the ZIP download below and the local plugin instructions for your client version.

## Connect your account

The plugin connects to `https://claudebaby.cn/mcp` using a bearer API key. Create or sign in to your ClaudeBaby account at <https://claudebaby.cn/console/register?ref=M8YYGRN4>, then configure your own key in Codex's private MCP credential flow. Never commit a key, put it in this repository, or paste it into a prompt.

The service may consume account credits. Check the current account terms and pricing before broad or repeated queries. Inspect live tool names and source support after connecting; platform availability and query coverage can change.

## Included

- Remote ClaudeBaby MCP connection (Streamable HTTP)
- `claudebaby-research` skill for evidence-aware social and ecommerce research

## Official directory status

This package is ready for Codex marketplace distribution. Public directory submission is a separate OpenAI review process. As of October 13, 2026, OpenAI's submission portal does not provide a connection flow for fixed API-key/bearer authentication; ClaudeBaby currently uses that authentication model. Do not embed a key in the package or bypass the portal limitation. Public-directory publication requires a supported connection/authentication setup, tool scan, identity/domain checks, reviewer materials, and approval.

## License

The plugin package and included skill are distributed under the repository's MIT license. This does not grant rights to redistribute third-party source content or change the ClaudeBaby hosted service's terms.
