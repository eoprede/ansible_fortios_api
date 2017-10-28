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
module: fortios_api_syslogd_setting
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages system syslog configuration.
description:
    - Manages system syslog configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Can use all of the parameters supported by Fortigate API

options:
    setting:
        description:
            - Settings for syslogd
        type: list
        required: true
        suboptions:
            server:
                descritpion:
                    - Server IP address
                required: true
            status:
                description:
                    - Whether server is enabled or disabled
                options: ['enable','disable']
                required: false
'''
EXAMPLES = '''
# For some reason Fortigate decided to make each syslogd setting is a different API endpoint.
# If you need more than 1 syslog destination, use generalized fortigate_api module with endpoing cmdb/log.syslogdX/setting
---
name: set system syslog setting
tags:
- syslog
fortios_api_syslogd_setting:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
        http: socks5://127.0.0.1:9000
  setting:
  - server: 10.0.0.1
    status: enable
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

api_syslogd_setting_args = {
    "endpoint": ['cmdb/log.syslogd/setting'],
    "list_identifier": 'setting',
    "object_identifier": "",
    "default_ignore_params": [],
}


def main():
    forti_api = API(api_syslogd_setting_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
