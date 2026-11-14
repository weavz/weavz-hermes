# Weavz MCP with Hermes Agent

Connect an AI coding client to the apps authorized in one Weavz workspace through remote MCP. This example keeps client MCP configuration separate from the model provider and from project instructions.

## Requirements

- A current Hermes CLI or desktop client with remote Streamable HTTP MCP support.
- A reachable Weavz platform endpoint and a Weavz account.
- A model/provider configured in the isolated Hermes profile. `HERMES_HOME` starts a separate profile, so it will not inherit model credentials/settings from `~/.hermes`. Weavz OAuth does not configure or pay for model access.

See the [Hermes MCP guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/mcp.md) and [CLI reference](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/cli-commands.md) for current command details.

## Setup

Hermes MCP declarations live in its config. This example uses a dedicated `HERMES_HOME` under ignored `.local/` so the setup does not touch `~/.hermes/config.yaml`. `AGENTS.md` / `.hermes.md` provide project instructions but do not register MCP servers.

```sh
# A separate local Hermes profile, not the default ~/.hermes config.
mkdir -p .local/hermes
HERMES_HOME="$PWD/.local/hermes" hermes mcp add weavz --url https://platform.weavz.io/mcp/weavz --auth oauth
HERMES_HOME="$PWD/.local/hermes" hermes mcp list
HERMES_HOME="$PWD/.local/hermes" hermes mcp test weavz
```

Complete the browser sign-in, select the intended workspace, and approve the connector. The OAuth flow stores credentials in the client's own credential store. Do not add an `Authorization` header or paste a Weavz access token for the hosted personal connector.

For self-hosted Weavz, replace `https://platform.weavz.io/mcp/weavz` with `https://<your-public-weavz-host>/mcp/weavz`. The server must be reachable over HTTPS from the client.

## Verify

```sh
HERMES_HOME="$PWD/.local/hermes" hermes mcp test weavz
HERMES_HOME="$PWD/.local/hermes" hermes chat --oneshot -q "Use a Weavz read/search tool to confirm access. Do not modify anything."
```

`hermes mcp test weavz` probes this named server. The model-mediated prompt is a separate check: count it as passed only if the transcript shows a Weavz tool call and result. Review tool arguments and output. Do not infer live auth or a successful app action from configuration files alone.

## Project instructions

This repo includes `AGENTS.md` guidance. It does not install or configure MCP. See the client-native instruction file for rules loaded into the agent.

## Local checks

Run the dependency-free static contract checks:

```sh
python3 -m unittest discover -s tests -v
```

These check the checked-in client config and instruction/setup contract only; they make no network calls and do not prove OAuth or tool execution.

## Credentials and safety

- Keep OAuth in the client credential store. No Weavz API key, MCP access token, connected-app secret, or model key belongs in this repo.
- The endpoint scopes the connector to the workspace selected during Weavz sign-in. To change workspaces, disconnect and reauthorize.
- Tool availability follows that workspace's configuration and permissions. This example does not promise MCP App UI support.
- Before writing, sending, publishing, deleting, or changing external data, inspect the proposed action and obtain user approval.

## License

MIT. See [LICENSE](LICENSE).
