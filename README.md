# Hashicorp Vault

Publisher: Splunk Community  
Connector Version: 1.1.2  
Product Vendor: Dallan  
Product Name: Hashicorp Vault  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 6.2.1  

This is an app that supports various interactions with the Hashicorp Vault REST API


## Port Information

The app uses HTTP/ HTTPS protocol for communicating with the Hashicorp Vault server. Below are the
default ports used by the Splunk SOAR Connector.

| SERVICE NAME | TRANSPORT PROTOCOL | PORT |
|--------------|--------------------|------|
| http         | tcp                | 80   |
| https        | tcp                | 443  |

### Configuration Variables

The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Hashicorp Vault asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**verify_server_cert** |  optional  | boolean | Verify server certificate
**vault_url** |  required  | string | URL of the Hashicorp Vault instance
**vault_mountpoint** |  required  | string | Vault mountpoint to connect with
**vault_token** |  required  | password | Token used to authenticate requests to Hashicorp Vault when using token authentication
**vault_namespace** |  optional  | string | Vault Namespace
**vault_role_id** |  optional  | password | Role ID if using AppRole authentication
**vault_secret_id** |  optional  | password | Secret ID if using AppRole authentication

### Supported Actions  

[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied credentials  
[set secret](#action-set-secret) - Set secret value at the specified path  
[get secret](#action-get-secret) - Get secret value present at the specified path  
[list secrets](#action-list-secrets) - List secret values present at the specified path  

## action: 'test connectivity'

Validate the asset configuration for connectivity using supplied credentials

Type: **test**  
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output  

## action: 'set secret'

Set secret value at the specified path

Type: **generic**  
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**location** |  required  | Location to keep the secret value | string |  `hashicorp vault location`
**update** |  optional  | Update secret value if already exists | boolean |
**secret_json** |  required  | JSON formatted object of dictionary to store at the given location | string |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.location | string |  `hashicorp vault location`  |  
action_result.parameter.secret_json | string |  |  
action_result.parameter.update | boolean |  |   True  False
action_result.data.\*.succeeded | boolean |  |   True  False
action_result.status | string |  |   success  failed
action_result.summary | string |  |  
action_result.message | string |  |  
summary.total_objects | numeric |  |   1
summary.total_objects_successful | numeric |  |   1

## action: 'get secret'

Get secret value present at the specified path

Type: **investigate**  
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**location** |  required  | Location of the secret value | string |  `hashicorp vault location`

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.location | string |  `hashicorp vault location`  |  
action_result.data.\*.secret_value | string |  |  
action_result.data.\*.succeeded | boolean |  |   True  False
action_result.status | string |  |   success  failed
action_result.summary | string |  |  
action_result.message | string |  |  
summary.total_objects | numeric |  |   1
summary.total_objects_successful | numeric |  |   1

## action: 'list secrets'

List secret values present at the specified path

Type: **investigate**  
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**location** |  required  | Location of the secret values | string |  `hashicorp vault location`

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.location | string |  `hashicorp vault location`  |  
action_result.data.\*.secret_values | string |  |  
action_result.data.\*.succeeded | boolean |  |   True  False
action_result.status | string |  |   success  failed
action_result.summary | string |  |  
action_result.message | string |  |  
summary.total_objects | numeric |  |   1
summary.total_objects_successful | numeric |  |   1

