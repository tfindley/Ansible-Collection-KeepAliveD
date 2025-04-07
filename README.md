# Ansible Collection - tfindley.keepalived

Documentation for the collection.

## Roles

## Playbooks

### deploy_pass

Calling this script will automatically deploy KeepAliveD with a password protected connection. This password will be regenerated on each run as it's not idempotent.

```yaml
- name: Deploy KeepAliveD from collection playbook

  # become: true  # This shouldn't occour at the playbook level
  import_playbook: tfindley.keepalived.deploy_pass

  vars:
    keepalived_enabled: true
    keepalived_vip: 192.168.69.201
    keepalived_vrid: 123
    keepalived_state: 'BACKUP'

    keepalived_checkscript_enabled: true
    keepalived_checkscript_user: keepalived_script
    keepalived_checkscript_group: keepalived_script
    keepalived_checkscript_path: "{{ keepalived_checkscript_dir }}"
```

## KeepaliveD Check Scripts

See [Check Script Documentation](docs/CHECKSCRIPTS.md).

## License

MIT

## Author Information

**Tristan Findley**

Find out more about me [here](https://tfindley.co.uk).

If you're fan of my work and would like to show your support:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Z8Z016573P)