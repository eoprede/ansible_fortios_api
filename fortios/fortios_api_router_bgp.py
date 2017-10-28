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
module: fortios_api_router_bgp
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
    bgp:
        description:
            - BGP connection parameters, must be a list with 1 object
        required: true
        suboptions:
            as:
                description:
                    - Firewall AS
                required: true
            router-id:
                description:
                    - Firewall router-id
                required: false
                default: null
            neighbor:
                description:
                    - List of BGP neighbors
                required: false
                default: null
            aggregate-address:
                description:
                    - List of aggregate prefixes
                required: false
                default: null
            network:
                description:
                    - List of network prefixes
                required: false
                default: null
'''
EXAMPLES = '''
# Note that you have to supply the whole redistribute list, even if you need to redistribute just protocol
---
name: Test BGP
tags:
- bgp
fortios_api_router_bgp:
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
  bgp:
  - as: 65001
    router-id: 192.0.5.1
    log-neighbour-changes: enable
    graceful-restart: enable
    neighbor:
    - ip: 192.0.5.2
      soft-reconfiguration: enable
      remote-as: 65002
      prefix-list-in: default_only
    aggregate-address:
    - prefix: 10.254.166.0 255.255.254.0
    - prefix: 10.254.164.0 255.255.252.0
    network:
    - prefix: 10.254.166.0 255.255.255.0
    redistribute:
    - name: connected
      status: enable
    - name: rip
      status: disable
    - name: ospf
      status: disable
    - name: static
      status: disable
    - name: isis
      status: disable

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
    "endpoint": ["cmdb", "router", "bgp"],
    "list_identifier": 'bgp',
    "object_identifier": None,
    "permanent_objects": [],
    "default_ignore_params": [],
}


def main():
    forti_api = API(router_bgp_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
