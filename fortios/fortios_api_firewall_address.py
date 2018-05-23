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
module: fortios_api_firewall_address
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages Firewall address configuration.
description:
    - Manages Firewall address configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Assumes the list of default objects of firewall rules. This list may have to be edited in the library if it changes over time.

options:
    address:
        description:
            - Full list of addresses to be applied to the Firewall. Note that any address not present in the list will be DELETED.
        required: true
        suboptions:
            name:
                description:
                    - Name of the address (must be unique)
                required: true
            type:
                description:
                    - type of the firewall rule
                required: false
                options: ['fqdn','ipmask','iprange']
'''
EXAMPLES = '''
---
- name: set firewall addresses
  fortios_api_firewall_address:
    conn_params:
        fortigate_username: admin
        fortigate_password: test
        fortigate_ip: 1.2.3.4
        port: 10080
        verify: false
        secure: false
        proxies:
            http: socks5://127.0.0.1:9000
    address:
    - name: test
      type: fqdn
      fqdn: test.com
    - name: test2
      type: ipmask
      subnet: 1.1.1.1 255.255.255.255
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
    'endpoint': 'cmdb/firewall/address',
    'list_identifier': 'address',
    'object_identifier': 'name',
    'default_ignore_params': [],
    "ignore_objects": [
        "Adobe Login",
        "FIREWALL_AUTH_PORTAL_ADDRESS",
        "Gotomeeting",
        "SSLVPN_TUNNEL_ADDR1",
        "Windows update 2",
        "adobe",
        "all",
        "android",
        "apple",
        "appstore",
        "auth.gfx.ms",
        "autoupdate.opera.com",
        "citrix",
        "dropbox.com",
        "eease",
        "firefox update server",
        "fortinet",
        "google-drive",
        "google-play",
        "google-play2",
        "google-play3",
        "googleapis.com",
        "icloud",
        "itunes",
        "microsoft",
        "skype",
        "softwareupdate.vmware.com",
        "swscan.apple.com",
        "update.microsoft.com",
        "verisign"
    ]
}


def main():
    forti_api = API(system_global_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
