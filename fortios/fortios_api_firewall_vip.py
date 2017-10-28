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
module: fortios_api_firewall_vip
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages Firewall VIP configuration.
description:
    - Manages Firewall VIP configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM

options:
    vip:
        description:
            - Full list of VIPs to be applied to the Firewall. Note that any VIP not present in the list will be DELETED.
        required: true
        suboptions:
            name:
                description:
                    - Name of the VIP (must be unique among VIPs and firewall addresses and address groups)
                required: true
            extip:
                description:
                    - External IP of the pool
                required: true
            mappedip:
                description:
                    - Mapped IP of the pool
                required: true
            extintf:
                description:
                    - External interface on which pool will be active
                required: false

'''
EXAMPLES = '''
---
name: set firewall IP pool
fortios_api_firewall_vip:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
      http: socks5://127.0.0.1:9000
  print_current_config: false
  vip:
  - name: test_vip
    extintf: port3
    extip: 192.0.5.10
    mappedip:
    - range: 1.2.3.4
  - name: test_vip_range
    extintf: port3
    extip: 192.0.5.11-192.0.5.12
    mappedip:
    - range: 1.2.3.5-1.2.3.6
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
    'endpoint': 'cmdb/firewall/vip',
    'list_identifier': 'vip',
    'object_identifier': 'name',
    'default_ignore_params': []
}


def main():
    forti_api = API(system_global_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
