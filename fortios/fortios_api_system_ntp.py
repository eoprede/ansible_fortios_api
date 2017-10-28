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
module: fortios_api_system_ntp
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages system ntp configuration.
description:
    - Manages system syslog configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Can use all of the parameters supported by Fortigate API

options:
    ntp:
        description: Settings for ntp
        type: dict
        required: true
        suboptions:
            type:
                descritpion: Type of NTP servers
                required: true
                options: ['fortiguard','custom']

'''
EXAMPLES = '''
# Note that if you are using custom NTP servers
# you have to set them up first with fortios_api_ntp_server
---
name: set system ntp settings
fortios_api_system_ntp:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
        http: socks5://127.0.0.1:9000
  ntp:
  - type: custom

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
    description: Whether a change was required for the device configuration.
    returned: always
    type: boolean
msg:
    description: A short description of the success of the change and status of the device.
    returned: always
    type: str
'''

from ansible.module_utils.fortios_api import API

module_args = {
    "endpoint": ['cmdb', 'system', 'ntp'],
    "list_identifier": 'ntp',
    "object_identifier": "",
    "default_ignore_params": [],
}


def main():
    forti_api = API(module_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
