# KeepAliveD

This role deploys and configures KeepAlived.

## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

## Role Variables

| Variable Name                           | Type    | Required | default value         | Description |
| --------------------------------------- | ------- | -------- | --------------------- | ----------- |
| `keepalived_enabled`                    | boolean | True     | `false`               | Enables or disables KeepaliveD. This is used as a safeguard to prevent accidental deployment. This variable must be present on each system you require KeepAliveD installing |
| `keepalvied_vip`                        | string  | True     | ''                    | The IP Address you wish to set for the Virtual IP |
| `keepalived_vrid`                       | int     | True     | `123`                 | | 
| `keepalived_priority`                   | int     | True     | `100`                 | |
| `keepalived_state`                      | string  | True     | `BACKUP`              | |
| `keepalived_checkscript_enabled`        | boolean | True     | `false`               | |

### Keepalived VRRP



| Variable Name              | Type    | Required | default value         | Description |
| -------------------------- | ------- | -------- | --------------------- | ----------- |
| `name`                     | boolean | True     | `False`               |  |
| `interface`                | string  | True     | ''                    |  |
| `priority`                 | int     | True     | | |
| `virtual_router_id`        | int     | True     | | |
| `advert_int`               | int     | True     | | |
| `garp`                     |         | True     | | |
|  - `master_refresh`        | int     | True     | | |
|  - `master_refresh_repeat` | int     | True     | | |
| `authentication`           |         | True     | | |
|  - `type`                  | string  | True     | | |
|  - `pass`                  | string  | True     | | |
| `unicast_src_ip`           | string  | True     | | |
| `unicast_peer`             | string  | True     | | |
| `vip`                      | list    | True     | | |
| `checkscript`              | list    | True     | | |

### Keepalived Checkscript Scripts

| Variable Name | Type    | Required | default value         | Description |
| ------------- | ------- | -------- | --------------------- | ----------- |
| `name`        | boolean | True     | `False`               |  |
| `filename`    | string  | True     | ''                    |  |
| `exec`        | string  | True     | | |
| `content`     | string  | True     | | |
| `mode`        | string  | True     | | |
| `interval`    | int     | True     | | |
| `fall`        | int     | True     | | |
| `rise`        | int     | True     | | |
| `timeout`     | int     | True     | | |
| `weight`      | int     | True     | | |

## Checkscripts

### **check_vault**

To use this script in the `keepalived_checkscript_scripts.[0].content` field: `"{{ lookup('ansible.builtin.file', 'hashicorp/vault/check_vault.py') }}"`

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