#!/usr/bin/python
#
# Ansible module for managing Fortigate devices via API
# (c) 2017, Will Wagner <willwagner602@gmail.com> and Eugene Opredelennov <eoprede@gmail.com>
# GNU General Public License v3.0+ (see COPYING or
# https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: fortios_api_router_ospf
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages router BGP configuration.
description:
    - Manages router BGP configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Can use all of the parameters supported by Fortigate API

options:
    ospf:
        description:
            - OSPF connection parameters
        required: true
        suboptions:
            default-information-originate:
                description:
                    - Originate default route
                required: true
            router-id:
                description:
                    - Firewall router-id
                required: false
                default: null
            area:
                description:
                    - List of area IDs
                required: false
                default: null
            network:
                description:
                    - List of network prefixes
                required: false
                default: null
'''
EXAMPLES = '''
---
name: Test OSPF
tags:
- ospf
fortios_api_router_ospf:
  print_current_config: false
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
      http: socks5://127.0.0.1:9000
  ospf:
  - auto-cost-ref-bandwidth: 100000
    default-information-originate: enable
    default-information-metric: 150
    router-id: 1.2.3.4
    area:
    - id: 0.0.0.0
    network:
    - prefix: 192.0.5.0 255.255.255.0
      area: 0.0.0.0
'''

RETURN = '''
proposed:
    description: k/v pairs of parameters passed into module
    returned: always
    type: dict
existing:
    description:
        - k/v pairs of existing configuration
    returned: always
    type: dict
end_state:
    description: k/v pairs of configuration after module execution
    returned: always
    type: dict
updates:
    description: command sent to the device
    returned: always
    type: list
changed:
    description: check to see if a change was made on the device
    returned: always
    type: boolean
'''

from ansible.module_utils.fortios_api import API

router_bgp_args = {
    "endpoint": ["cmdb", "router", "ospf"],
    "list_identifier": 'ospf',
    "object_identifier": None,
    "permanent_objects": [],
    "default_ignore_params": [],
}


def main():
    forti_api = API(router_bgp_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
