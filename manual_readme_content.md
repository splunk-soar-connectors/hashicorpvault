## Authentication

The app supports two authentication methods. When configuring the asset, you may provide either AppRole credentials or a Vault token. If both are provided, **AppRole takes priority** as it is considered more secure.

### AppRole Authentication (Recommended)

Provide both **Role ID** (`vault_role_id`) and **Secret ID** (`vault_secret_id`) in the asset configuration. Both fields must be set together — providing only one will result in an error. A Vault namespace (`vault_namespace`) may optionally be specified for HCP Vault or enterprise deployments.

### Token Authentication

Provide a **Vault token** (`vault_token`) in the asset configuration. This method is used only when AppRole credentials are not configured. Token authentication is considered less secure than AppRole because tokens do not rotate automatically.

### Priority

| AppRole credentials set | Token set | Method used |
|-------------------------|-----------|----------------|
| Yes | Yes | AppRole |
| Yes | No | AppRole |
| No | Yes | Token |
| No | No | Error — no valid credentials |

## Port Information

The app uses HTTP/ HTTPS protocol for communicating with the Hashicorp Vault server. Below are the
default ports used by the Splunk SOAR Connector.

| SERVICE NAME | TRANSPORT PROTOCOL | PORT |
|--------------|--------------------|------|
| http | tcp | 80 |
| https | tcp | 443 |
