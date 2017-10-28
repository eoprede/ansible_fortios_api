#!/usr/bin/python
#
# Ansible module to manage arbitrary objects via API in fortigate devices
# (c) 2017, Will Wagner <willwagner602@gmail.com> and Eugene Opredelennov <eoprede@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: fortios_api_system_admin
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages system administration configuration.
description:
    - Manages system administration configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Can use all of the parameters supported by Fortigate API

options:
    admins:
        description:
            - System administrator parameters, must be a list of system admin objects.
        type: list
        required: true
        suboptions:
            name:
                descritpion:
                    - User account name
                required: true
            password:
                description:
                    - Password in unencrypted form
            accprofile:
                description:
                    - Profile for this admin
            trsuthostX:
                description:
                    - IP ranges that are allowed to connect with this account. It appears that 10 is the limit
'''
EXAMPLES = '''
# Note that "admin" entry must be present if you want to keep default admin user,
# otherwise it will get deleted.
---
- name: Update system admin
  ignore_errors: true
  fortios_api_system_admin:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
        http: socks5://127.0.0.1:9000
    admins:
    - name: test_admin
      comments: test_update
      password: test1
      accprofile: prof_admin
      trusthost1: 192.168.0.0 255.255.0.0
    - name: admin
      comments: manually configured admin
'''

RETURN = '''
proposed:
    description: k/v pairs of parameters passed into module and sent to the device for changes
    returned: always
    type: list
    sample: '[{"accprofile": "prof_admin", "comments": "test_update", "name": "test_admin", "password": "test"}, {"name": "admin"}]'
existing:
    description: k/v pairs of existing configuration
    returned: always
    type: list
    sample: '[]'
end_state:
    description: k/v pairs of configuration after module execution
    returned: always
    type: list
changed:
    description: Whether a change was required for the device configuration.
    returned: always
    type: boolean
    sample: true
msg:
    description: A short description of the success of the change and status of the device.
    returned: always
    type: str
    sample: "Configuration updated."
'''

from ansible.module_utils.fortios_api import API

router_ospf_ospf_interface_args = {
    "endpoint": ['cmdb', 'system', 'admin'],
    "list_identifier": 'admins',
    "object_identifier": "name",
    "permanent_objects": ["admin"],
    "default_ignore_params": [],
    "match_ignore_params": ['password']
}


def main():
    forti_api = API(router_ospf_ospf_interface_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
