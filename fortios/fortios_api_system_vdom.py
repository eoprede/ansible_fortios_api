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
module: fortios_api_system_vdom
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages Firewall vdom configuration.
description:
    - Manages Firewall vdom configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM

options:
    vdoms:
        description:
            - Full list of vdoms to be configured.
        required: true
        suboptions:
            name:
                description:
                    - Name of the vdom
                required: true

'''
EXAMPLES = '''
#Due to limitatons of the Fortigate VM, this module was not fully tested.
---
name: Update link-monitor
fortios_api_link_monitor:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
      http: socks5://127.0.0.1:9000
  vdoms:
  - name: "root"
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
    'endpoint': 'cmdb/system/vdom',
    'list_identifier': 'vdoms',
    'object_identifier': 'name',
    'default_ignore_params': []
}


def main():
    forti_api = API(system_global_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
