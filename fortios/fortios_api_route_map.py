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
module: fortios_api_route_map
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages router route-map configuration.
description:
    - Manages router route-map configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Can use all of the parameters supported by Fortigate API

options:
    route-map:
        description:
            - Full list of route-maps to be applied to the Firewall. Note that any route-maps not present in the list will be DELETED.
        required: true
        suboptions:
            name:
                description:
                    - Name of the route-map list
                required: true
            rule:
                description:
                    - List of rules for the route-map
                required: true
                suboptions:
                    match-ip-address:
                        description:
                            - Prefix list to reference for IP address matching
                        required: true
                    match-flags:
                        description:
                            - Not clear what it is, but is needed when matching something in route-map
                    set-flags:
                        description:
                            - Not clear what it is, but is needed when setting something in route-map

'''
EXAMPLES = '''
# I am not sure what set-flags and match-flags are and they aren't documented well anywhere
# You may have to create a sample rule manually to see which values are assigned and add it to the playbook
---
name: update router route-map
fortios_api_route_map:
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
  route-map:
  - comments: comment
    name: test_default
    rule:
    - match-flags: 2
      match-ip-address: default_only
      set-flags: 0
    - match-flags: 2
      match-ip-address: test_block
      set-flags: 2
      set-metric: 200

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


prefix_list_api_args = {
    'endpoint': ["cmdb", "router", "route-map"],
    'list_identifier': 'route-map',
    'object_identifier': 'name',
    'default_ignore_params': [],
}


def main():
    forti_api = API(prefix_list_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
