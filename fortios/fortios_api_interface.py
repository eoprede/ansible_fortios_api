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
module: fortios_api_interface
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages interface configuration.
description:
    - Manages interface configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Assumes the list of default (permanent) objects.

options:
    permanent_objects:
        description:
            - List of all the permanent interfaces, so that module doesn't attempt to delete them.
              It varies depending on the FW model and must be accurate for module to work.
        required: true
    interfaces:
        description:
            - List of interfaces with specified parameters. If the interface is not specified,
              but is in a permanent list, it will be reset to default state.
        required: true
        suboptions:
            name:
                description:
                    - Interface name
                required: false
                default: null
            ip:
                description:
                    - Interface IP address
                required: false
                default: null
            description:
                description:
                    - Interface description
                required: false
                default: null
            vdom:
                description:
                    - Vdom to which the port belongs
                required: true
'''
EXAMPLES = '''
---
name: Update interfaces on Fortigate VM (note permanent object list)
fortios_api_interface:
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
  permanent_objects:
  - ssl.root
  - port1
  - port2
  - port3
  - port4
  - port5
  - port6
  - port7
  - port8
  - port9
  - port10
  interfaces:
    - name: port1
      allowaccess: ping ssh http
      ip: 192.0.2.5 255.255.255.0
      type: physical
      description: Management
    - name: port2
      vdom: root
      ipv6:
        autoconf: disable
        dhcp6-client-options: iapd iana dns
        dhcp6-prefix-delegation: enable
        dhcp6-prefix-hint: "::/60"
        ip6-allowaccess: ping
        ip6-mode: dhcp
    - name: port3
      vdom: root
      allowaccess: ping https http
      type: physical
      ip: 192.0.5.4 255.255.255.0
    - name: port5
      vdom: root
      vlanforward: enable
      type: physical
    - name: testint
      vdom: root
      allowaccess: ping
      ip: 192.0.3.56 255.255.255.0
      role: lan
      interface: port5
      vlanid: 5
      vrrp-virtual-mac: enable

# For unknown reason (most likely API limitation)
# you can not set up VRRP directly from the interface
# module. Use generic module like in example below

- name: Update vrrp for testint
  fortios_api:
    endpoint_information:
      endpoint: cmdb/system/interface/testint/vrrp
      list_identifier: vrrp
      object_identifier: vrid
    conn_params: "{{ test_fw }}"
    vrrp:
    - vrid: 1
      vrip: 194.0.3.1
      priority: 200

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

interface_api_args = {
    "endpoint": ["cmdb", "system", "interface"],
    "list_identifier": "interfaces",
    "object_identifier": "name",
    "default_ignore_params": ['macaddr', 'vdom', 'type']
}


def main():
    forti_api = API(interface_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
