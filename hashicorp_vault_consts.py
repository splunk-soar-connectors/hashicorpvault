# File: hashicorp_vault_consts.py
#
# Copyright (c) 2020-2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
#
# Action Identifier constants
ACTION_ID_TEST_ASSET_CONNECTIVITY = "test_asset_connectivity"
ACTION_ID_SET_SECRET = "set_secret"
ACTION_ID_GET_SECRET = "get_secret"
ACTION_ID_LIST_SECRETS = "list_secrets"
HASHICORP_VAULT_STATE_FILE_CORRUPT_ERR = "Error occurred while loading the state file due to its unexpected format.\
     Resetting the state file with the default format. Please try again."

# Error message handling constants
ERR_MSG_UNAVAILABLE = "Error message unavailable. Please check the asset configuration and|or action parameters"

# Authentication method messages
HASHICORP_VAULT_USING_APPROLE_AUTH = "AppRole credentials provided. Using AppRole authentication (preferred over token)"
HASHICORP_VAULT_USING_TOKEN_AUTH = "Token provided. Using token authentication"
HASHICORP_VAULT_NO_AUTH_CREDENTIALS_ERR = (
    "No valid authentication credentials found. "
    "Please provide either AppRole credentials (Role ID + Secret ID) or a Vault token in the asset configuration."
)
HASHICORP_VAULT_INCOMPLETE_APPROLE_ERR = "Incomplete AppRole credentials: both 'vault_role_id' and 'vault_secret_id' must be provided together."
