# KeepAliveD

This role deploys and configures KeepAlived.

## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

## Role Variables

| Variable Name                           | Type    | Required | default value         | Description |
| --------------------------------------- | ------- | -------- | --------------------- | ----------- |
| `keepalived_enabled`                    | boolean | True     | `false`               | Enables or disables KeepaliveD. This is used as a safeguard to prevent accidental deployment. This variable must be present on each system you require KeepAliveD installing |

### Helper Variables

These are designed to do very simple deployments of KeepAliveD. It is recommended to only use these in basic deployments.

| Variable Name                           | Type    | Required | default value         | Description |
| --------------------------------------- | ------- | -------- | --------------------- | ----------- |
| `keepalived_vip`                        | list    | True     | ''                    | The IP Addresses you wish to set as Virtual IP |
| `keepalived_vrid`                       | int     | True     | `123`                 | Your VRRP Virtual Router ID. Do not duplicate these on the same network | 
| `keepalived_priority`                   | int     | True     | `100`                 | for electing MASTER, highest priority wins |
| `keepalived_state`                      | string  | True     | `BACKUP`              | This can either be `MASTER`, or `BACKUP`. To prevent service flapping, it is suggested to use `BACKUP` on all nodes and set the priority equally on each node. |

### Global Variables

| Variable Name                           | Type    | Required | default value         | Description |
| --------------------------------------- | ------- | -------- | --------------------- | ----------- |
| `keepalived_max_auto_priority`          | string  | True     | `99`                  | To limit the maximum increased automatic priority, specify the following. (0 doesn't use automatic priority increases, and is the default. -1 disables the warning message at startup). Omitting the priority sets the maximum value. |
| `keepalived_vrrp_version`               | int     | False    | `2`                   | Set the default VRRP version to use. (default: 2, but IPv6 instances will use version 3) | 
| `keepalived_router_id`                  | string  | False    |                       | String identifying the machine (doesn't have to be hostname) |
| `keepalived_checkscript_user`           | boolean | True     | `keepalived_script`   | Specify the default username to run scripts under |
| `keepalived_checkscript_group`          | boolean | True     | `keepalived_script`   | Specify the default groupname to run scripts under |
| `keepalived_checkscript_path`           | boolean | True     | *See below*           | *See below* |

### Checkscript Variables

| Variable Name                           | Type    | Required | default value         | Description |
| --------------------------------------- | ------- | -------- | --------------------- | ----------- |
| `keepalived_checkscript_enabled`        | boolean | True     | `false`               | |

**keepalived_checkscript_path:** The location of where check scripts will be stored. This is variable is preset based on the host OS family that you're installing to, but can be overritten in your playbook if you wish.

The default for RHEL-based systems is `/usr/libexec/keepalived` - this directory is created by keepalived with the appropriate SELinux permissions to allow the Keepalived script user that is defined in global_defs to run scripts. The role will ensure that all scripts deployed to this directory will have the correct owner/group/mode set.

Information Ref: [https://opensource-db.com/working-with-keepalived-and-selinux-ensuring-ha-and-security/](https://opensource-db.com/working-with-keepalived-and-selinux-ensuring-ha-and-security/)

### Keepalived VRRP

variables for the `keepalived_vrrp` dictionary instances

| Variable Name              | Type    | Required | default value | Recommended Value | Description |
| -------------------------- | ------- | -------- | ------------- | ---------------------------------------------------------------------------- | ------------|
| `name`                     | boolean | True     | `False`       | `VI_1`                                                                       | The unique name of the VRRP instance |
| `state`                    | string  | True     | `BACKUP`      | `BACKUP`                                                                     | This can either be `MASTER`, or `BACKUP`. To prevent service flapping, it is suggested to use `BACKUP` on all nodes and set the priority equally on each node. |
| `interface`                | string  | True     | ``            | `"{{ ansible_default_ipv4['alias'] }}"`                                      | interface for inside_network, bound by vrrp. If you want to keep it simple, use the recommended value and it will fetch the alias of the adapter used for your Ansible connection. |
| `priority`                 | int     | True     | ``            | `100`                                                                        | for electing MASTER, highest priority wins |
| `virtual_router_id`        | int     | True     | ``            | ``                                                                           | Your VRRP Virtual Router ID. Do not duplicate these on the same network! |
| `advert_int`               | int     | True     | ``            | `1`                                                                          | VRRP Advert interval in seconds |
| `garp`                     | dict    | False    | ``            |                                                                              | Dictionary for the entries below. |
|  - `master_refresh`        | int     | False    | ``            | `5`                                                                          | minimum time interval for refreshing gratuitous ARPs while MASTER |
|  - `master_refresh_repeat` | int     | False    | ``            | `1`                                                                          | number of gratuitous ARP messages to send at a time while MASTER |
| `authentication`           | dict    | False    | ``            |                                                                              | Use of this option is non-compliant and can cause problems; avoid |
|  - `type`                  | string  | False    | ``            | `PASS`                                                                       | PASS - Simple password (suggested), AH - IPSEC (not recommended) |
|  - `pass`                  | string  | False    | ``            | `"{{ lookup('community.general.random_string', length=8, special=false) }}"` | Password for accessing vrrpd. should be the same on all machines. Only the first eight (8) characters are used.|
| `unicast_src_ip`           | string  | True     | ``            | `"{{ ansible_default_ipv4.address }}"`                                       | default IP for binding vrrpd is the primary IP on interface. If you want to hide the location of vrrpd, use this IP as src_addr for multicast or unicast vrrp packets. (since it's multicast, vrrpd will get the reply packet no matter what src_addr is used). |
| `unicast_peer`             | string  | False    | ``            | `"{{ keepalived_iplist }}"`                                                  | Use the default value here to automatically populate a list of all hosts in the play. Do not send VRRP adverts over a VRRP multicast group. Instead it sends adverts to the following list of ip addresses using unicast.  `<IPADDR> [min_ttl {0..255}] [max_ttl {0..255}]` |
| `vip`                      | list    | True     | `[]`          | ``                                                                           | The IP Addresses you wish to set as Virtual IP |
| `checkscript`              | list    | False    | `[]`          | ``                                                                           | The list of checkscripts that you wish to call for this VRRP instance. These must match a name value for the checkscript dictionary below. |

### Keepalived Checkscript Scripts

| Variable Name | Type    | Required | default value | Recommended Value   | Description |
| ------------- | ------- | -------- | ------------- | ------------------- | ------------|
| `name`        | boolean | True     | ``            | `name_of_script`    | The name of the script. This must be called in the `vrrp.[0].checkscript` list. |
| `filename`    | string  | True     | ''            | `name_of_script.py` | The name of the script that will be created, including the filetype. |
| `exec`        | string  | True     | ''            | `--opt_flag value ` | Any flags or options you wish to pass to the script |
| `content`     | string  | True     | *See Below*   | *See Below*         | *See Below* |
| `mode`        | string  | True     | ''            | `0700`              | Make the script executable |
| `interval`    | int     | True     | ''            | `2`                 | Run script every 2 seconds |
| `fall`        | int     | True     | ''            | `1`                 | If script returns non-zero 2 times in succession, enter FAULT state |
| `rise`        | int     | True     | ''            | `3`                 | If script returns zero r times in succession, exit FAULT state |
| `timeout`     | int     | True     | ''            | `2`                 | Wait up to t seconds for script before assuming non-zero exit code |
| `weight`      | int     | True     | ''            | `50`                | Reduce priority by 50 on fall |

### Checkscript Content

## Checkscripts

### Hashicorp Vault

To use this script in the `keepalived_checkscript_scripts.[0]`, set the following fields:

```yaml
vars:
    keepalived_vrrp:
      - name: VI_1
        ...
        checkscript:
          - vault_active_node_script

    keepalived_checkscript_enabled: true

    keepalived_checkscript_scripts:
      - name: vault_active_node_script
        filename: check_vault.py
        exec: --timeout=1 --url='https://127.0.0.1:8200'
        content: "{{ lookup('ansible.builtin.file', 'hashicorp/vault/check_vault.py') }}"
        mode: '0700'
        interval: 2  # Run script every 2 seconds
        fall: 1  # If script returns non-zero 2 times in succession, enter FAULT state
        rise: 3  # If script returns zero r times in succession, exit FAULT state
        timeout: 2  # Wait up to t seconds for script before assuming non-zero exit code
        weight: 50  # Reduce priority by 50 on fall
```

### Grafana Server

**WARNING:** This script requires the python3-click module to be installed. It is recommended you install using a `pretask` section of your playbook. i.e:

```yaml
- name: Install Python3 Click reqreq
  become: true
  ansible.builtin.package:
    name: python3-click
    state: present

```

To use this script in the `keepalived_checkscript_scripts.[0]`, set the following fields:

```yaml

  vars:
    keepalived_vrrp:
      - name: VI_1
        ...
        checkscript:
          - check_grafana_health_api

    keepalived_checkscript_enable: true

    keepalived_checkscript_scripts:
      - name: check_grafana_health_api
        filename: check_grafana_health_api.py
        exec: --url http://localhost:3000/api/health --field database --response ok --timeout 3 --quiet'
        content: "{{ lookup('ansible.builtin.file', 'generic/check_json_api.py') }}"
        mode: '0700'
        interval: 2  # Run script every 2 seconds
        fall: 1  # If script returns non-zero 2 times in succession, enter FAULT state
        rise: 3  # If script returns zero r times in succession, exit FAULT state
        timeout: 2  # Wait up to t seconds for scrip

```

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

## License

BSD


## Author Information

**Tristan Findley**

Find out more about me [here](https://tfindley.co.uk).

If you're fan of my work and would like to show your support:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Z8Z016573P)