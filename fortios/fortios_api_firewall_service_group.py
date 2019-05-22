#!/usr/bin/python
#
# Ansible module to manage arbitrary objects via API in fortigate devices
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
module: fortios_api_firewall_service_group
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages Firewall custom service group configuration.
description:
    - Manages Firewall custom service group configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
      Daryl Banttari (@dbanttari)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Assumes the list of default (permanent) objects. This list may have to be edited in the library (or moved to device config) if it changes over time.

options:
    services:
        description:
            - Full list of service groups to be applied to the Firewall. Note that any service group not present in the list will be DELETED.
        required: true
        suboptions:
            name:
                description:
                    - Name of the firewall service
                required: true
            groups:
                description:
                    - List of named services
                required: true
'''
EXAMPLES = '''
# Sample FW service
- name: update firewall services
    fortios_api_firewall_service_group:
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
      groups:
      - name: dns_ldap
        services: DNS LDAP LDAPS
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
    'endpoint': 'cmdb/firewall.service/group',
    'list_identifier': 'groups',
    'object_identifier': 'name',
    'default_ignore_params': [],
    'ignore_objects': []
}


def main():
    forti_api = API(system_global_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
