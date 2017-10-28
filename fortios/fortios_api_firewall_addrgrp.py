#!/usr/bin/python
#
# Ansible module for managing Fortigate devices via API
# (c) 2017, Will Wagner <willwagner602@gmail.com> and Eugene Opredelennov <eoprede@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: fortios_api_firewall_addrgrp
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages Firewall address group configuration.
description:
    - Manages Firewall address group configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM

options:
    addrgrp:
        description:
            - Full list of address groups to be applied to the Firewall. Note that any address group not present in the list will be DELETED.
        required: true
        suboptions:
            name:
                description:
                    - Name of the address group (must be unique)
                required: true
            member:
                description:
                    - List of the addresses (by name) to add to the address group
                required: false
'''
EXAMPLES = '''
---
name: set firewall address group
fortios_api_firewall_addrgrp:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
        http: socks5://127.0.0.1:9000
  addrgrp:
  - name: test_grp
    member:
    - name: test
    - name: test2
'''

RETURN = '''
proposed:
    description: k/v pairs of parameters passed into module and sent to the device for changes
    returned: always
    type: list

existing:
    description: k/v pairs of existing configuration
    returned: always
    type: list

end_state:
    description: k/v pairs of configuration after module execution
    returned: always
    type: list

changed:
    description: check to see if a change was made on the device
    returned: always
    type: boolean
'''

from ansible.module_utils.fortios_api import API

system_global_api_args = {
    'endpoint': 'cmdb/firewall/addrgrp',
    'list_identifier': 'addrgrp',
    'object_identifier': 'name',
    'default_ignore_params': []
}


def main():
    forti_api = API(system_global_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
