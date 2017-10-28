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
module: fortios_api_ospf_interface
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages router ospf interface information
description:
    - Manages router ospf interface information
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Can use all of the parameters supported by Fortigate API

options:
    interface:
        description:
            - OSPF interface parameters, must be a list of interface objects
'''
EXAMPLES = '''
# Sample interface
fortios_api_router_ospf_interface:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
        http: socks5://127.0.0.1:9000
  interface:
  - name: "test"
    interface: "port3"
    authentication: md5
    md5-key: "1 test"
    cost: 100
    priority: 200
'''

RETURN = '''
proposed:
    description: k/v pairs of parameters passed into module and sent to the device for changes
    returned: always
    type: list
    sample: '[{"authentication": "md5", "cost": 100, "interface": "port3", "md5-key": "1 test", "name": "test", "priority": 200}]'
existing:
    description: k/v pairs of existing configuration
    returned: always
    type: list
    sample: '[]'
end_state:
    description: k/v pairs of configuration after module execution
    returned: always
    type: list
    sample: '[{"authentication": "md5", "authentication-key": "ENC XXXX", "bfd": "global", "cost": 100,
              "database-filter-out": "disable", "dead-interval": 0, "hello-interval": 0, "hello-multiplier": 0,
              "interface": "port3", "ip": "0.0.0.0", "md5-key": "1 * ", "mtu": 0, "mtu-ignore": "disable",
              "name": "test", "network-type": "broadcast", "prefix-length": 0, "priority": 200, "q_origin_key": "test",
              "resync-timeout": 40, "retransmit-interval": 5, "status": "enable", "transmit-delay": 1}]'
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
    "endpoint": ['cmdb', 'router', 'ospf', 'ospf-interface'],
    "list_identifier": 'interface',
    "object_identifier": "name",
    "permanent_objects": [],
    "default_ignore_params": [],
    "match_ignore_params": ["md5-key"]
}


def main():
    forti_api = API(router_ospf_ospf_interface_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
