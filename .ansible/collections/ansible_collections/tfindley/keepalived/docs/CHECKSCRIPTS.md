# Check Scripts

## Pre-Packaged

This colletion includes pre-packaged keepalived monitoring scripts

### Hashicorp Vault

For Hashicorp Vault, use the fillowing script settings:
```yaml
keepalived_checkscript_enabled: true
keepalived_checkscript_scripts:
  - name: vault_active_node_script
    filename: check_vault.py
    exec: --timeout=1 --url='https://127.0.0.1:8200'
    content:
    mode: "0700"
    interval: 2  # Run script every 2 seconds
    fall: 1  # If script returns non-zero 2 times in succession, enter FAULT state
    rise: 3  # If script returns zero r times in succession, exit FAULT state
    timeout: 2  # Wait up to t seconds for script before assuming non-zero exit code
    weight: 50  # Reduce priority by 50 on fall
```

Add the following to your keepalived_vrrp dictionary:

```yaml
keepalived_vrrp:
  - name: VI_1
    checkscript:
      - vault_active_node_script
```

## Custom Script

### In-line code

```yaml
keepalived_checkscript_enabled: true
keepalived_checkscript_scripts:
  - name: inline_check
    filename: check_vault.sh
    # exec:
    content: |
      #!/bin/bash
      some_command
    mode: "0700"
    interval: 2  # Run script every 2 seconds
    fall: 1  # If script returns non-zero 2 times in succession, enter FAULT state
    rise: 3  # If script returns zero r times in succession, exit FAULT state
    timeout: 2  # Wait up to t seconds for script before assuming non-zero exit code
    weight: 50  # Reduce priority by 50 on fall
```

Add the following to your keepalived_vrrp dictionary:

```yaml
keepalived_vrrp:
  - name: VI_1
    checkscript:
      - inline_check
```

### File

```yaml
keepalived_checkscript_enabled: true
keepalived_checkscript_scripts:
  - name: uploaded_file_check
    filename: check_script.py
    exec: --key=value
    content: "{{ lookup('ansible.builtin.file', '/path/to/check_script.py') }}"
    mode: "0700"
    interval: 2  # Run script every 2 seconds
    fall: 1  # If script returns non-zero 2 times in succession, enter FAULT state
    rise: 3  # If script returns zero r times in succession, exit FAULT state
    timeout: 2  # Wait up to t seconds for script before assuming non-zero exit code
    weight: 50  # Reduce priority by 50 on fall
```

Add the following to your keepalived_vrrp dictionary:

```yaml
keepalived_vrrp:
  - name: VI_1
    checkscript:
      - uploaded_file_check
```
