[comment]: # "Auto-generated SOAR connector documentation"
# Hashicorp Vault

Publisher: Splunk Community  
Connector Version: 1\.0\.1  
Product Vendor: Dallan  
Product Name: Hashicorp Vault  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This is an app that supports various interactions with the Hashicorp Vault REST API

[comment]: # " File: readme.md"
[comment]: # "  Copyright (c) 2020 Splunk Inc."
[comment]: # ""
[comment]: # "  Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)"
[comment]: # ""
## Licensing details for the app

### hvac

This app uses the hvac module, which is licensed under the Apache Software License, Copyright (c)
Ian Unruh, Jeffrey Hogan.

### six

This app uses the six module, which is licensed under the MIT License (MIT), Copyright (c) Benjamin
Peterson.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Hashicorp Vault asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**verify\_server\_cert** |  required  | boolean | Verify server certificate
**vault\_url** |  required  | string | URL of the Hashicorp Vault instance
**vault\_mountpoint** |  required  | string | Vault mountpoint to connect with
**vault\_token** |  required  | password | Token used to authenticate requests to Hashicorp Vault

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
**update** |  required  | Update secret value if already exists | boolean | 
**secret\_json** |  required  | JSON formatted object of dictionary to store at the given location | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.location | string |  `hashicorp vault location` 
action\_result\.parameter\.update | boolean | 
action\_result\.parameter\.secret\_json | string | 
action\_result\.data\.\*\.succeeded | boolean | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get secret'
Get secret value present at the specified path

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**location** |  required  | Location of the secret value | string |  `hashicorp vault location` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.location | string |  `hashicorp vault location` 
action\_result\.data\.\*\.secret\_value | string | 
action\_result\.data\.\*\.succeeded | boolean | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list secrets'
List secret values present at the specified path

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**location** |  required  | Location of the secret values | string |  `hashicorp vault location` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.location | string |  `hashicorp vault location` 
action\_result\.data\.\*\.secret\_values | string | 
action\_result\.data\.\*\.succeeded | boolean | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 