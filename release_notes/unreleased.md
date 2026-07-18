**Unreleased**

* Updated connector development tooling and supported Python versions.
* Enabled TLS certificate verification by default for new assets. Existing assets retain their saved setting and should be reviewed after upgrade.
* Rejected Vault secret locations containing parent-directory path segments to keep requests inside the configured mount.
