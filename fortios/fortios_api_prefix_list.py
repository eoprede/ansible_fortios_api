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
module: fortios_api_prefix_list
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages router prefix list configuration.
description:
    - Manages router prefix list configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Can use all of the parameters supported by Fortigate API

options:
    prefixes:
        description:
            - Full list of prefix lists to be applied to the Firewall. Note that any prefix-list not present in the list will be DELETED.
        required: true
        suboptions:
            name:
                description:
                    - Name of the prefix list
                required: true
            rule:
                description:
                    - List of rules for the prefix-list
                required: true
                suboptions:
                    prefix:
                        description:
                            - Prefix in IP netmask format
                        required: true
                    ge:
                        description:
                            - Greater equal prefix mask length. Broken in 5.4.5
                    le:
                        description:
                            - Lesser equal prefix mask length. Broken in 5.4.5

'''
EXAMPLES = '''
# Note that in 5.4.5 you can't set ge or le with API call. Firewall just sets them to null regardless of what you send
# This has been confirmed by support and I am expecting bug to be fixed in further releases
---
name: update router prefix-list
tags:
- prefix_list
fortios_api_prefix_list:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
      http: socks5://127.0.0.1:9000
  prefixes:
  - name: default_only
    rule:
    - prefix: 0.0.0.0 0.0.0.0
  - name: test_block
    rule:
    - prefix: 10.254.160.0 255.255.240.0
    - prefix: 2.0.0.0 255.0.0.0

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
    'endpoint': ["cmdb", "router", "prefix-list"],
    'list_identifier': 'prefixes',
    'object_identifier': 'name',
    'default_ignore_params': [],
}


def main():
    forti_api = API(prefix_list_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
