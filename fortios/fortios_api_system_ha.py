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
module: fortios_api_system_ha
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages firewall ha parameters.
description:
    - Manages firewall ha parameters
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Can use all of the parameters supported by Fortigate API

options:
    ha:
        description:
            - Set of ha parameters
        required: true
        type: list
        suboptions:
            mode:
                description:
                    - Mode of operation
                options: ['standalone','a-a','a-p']
                required: false
'''
EXAMPLES = '''
# Please note that my test VM hangs once I apply HA config (be it via API or CLI)
# This module SHOULD work, but it hasn't been properly tested
---
name: set system ha setup
fortios_api_system_ha:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
        http: socks5://127.0.0.1:9000
  ha:
  - group-name: testha
    hbdev: '"port10" 1 '
    mode: standalone
    priority: 200

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

system_global_api_args = {
    'endpoint': ["cmdb", "system", "ha"],
    'list_identifier': 'ha',
    'object_identifier': '',
    'default_ignore_params': [],
    "match_ignore_params": ['password', 'key']
}


def main():
    forti_api = API(system_global_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
