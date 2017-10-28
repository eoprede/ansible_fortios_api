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
module: fortios_api_snmp_community
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages firewall SNMP Community parameters
description:
    - Manages firewall SNMP Community parameters
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Can use all of the parameters supported by Fortigate API

options:
    community:
        description:
            - Set of SNMP Comunity parameters
        required: true
        type: list
        suboptions:
            id:
                description:
                    - ID for object
                required: true
                type: int
            events:
                description:
                    - Events to generate SNMP events
                required: false
                type: str
            hosts:
                description:
                    - List of SNMP hosts for SNMP traps and pulls
                type: list
                required: false
                suboptions:
                    id:
                        description:
                            - ID for object
                        required: true
                        type: int
                    ip:
                        description:
                            - IP address for the host
                        required: true
                        type: str
            name:
                description:
                    - SNMP community name
                required: true
                type: str


'''
EXAMPLES = '''
---
name: set system snmp sysinfo
tags:
- snmp
fortios_api_snmp_sysinfo:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
        http: socks5://127.0.0.1:9000
  sysinfo:
  - status: enable


---
name: set system snmp sysinfo
tags:
- snmp
fortios_api_snmp_community:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
        http: socks5://127.0.0.1:9000
  community:
  - id: 1
    events: cpu-high mem-low log-full intf-ip vpn-tun-up vpn-tun-down ha-switch ha-hb-failure
      ips-signature ips-anomaly av-virus av-oversize av-pattern av-fragmented fm-if-change
      bgp-established bgp-backward-transition ha-member-up ha-member-down ent-conf-change
      av-conserve av-bypass av-oversize-passed av-oversize-blocked ips-pkg-update
      ips-fail-open faz-disconnect fswctl-session-up fswctl-session-down load-balance-real-server-down
    hosts:
    - id: 1
      ip: 10.0.0.1 255.255.255.255
    - id: 2
      ip: 10.0.0.2 255.255.255.255
    name: public
    status: enable
    trap-v1-status: enable
    trap-v2c-status: enable

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
    'endpoint': ['cmdb', 'system.snmp', 'community'],
    'list_identifier': 'community',
    'object_identifier': 'id',
    'default_ignore_params': []}


def main():
    forti_api = API(system_global_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
