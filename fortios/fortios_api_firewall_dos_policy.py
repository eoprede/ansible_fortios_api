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
module: fortios_api_firewall_dos_policy
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages firewall DoS policy configuration.
description:
    - Manages firewall DoS policy configuration.
author:
    - Will Wagner (@willwagner602)
    - Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Can use all of the parameters supported by Fortigate API
    - The FortiOS API has a bug that rejects creating objects at this endpoint on an initial request.
      As a temporary workaround, simply setup your playbook to immediately re-attempt the configuration.
      A permanent workaround will require a fix to the API by the vendor.

options:
    dos_policies:
        description:
            - DoS policy parameters, must be a list of firewall DoS policy objects.
'''
EXAMPLES = '''
# It appears that you MUST submit full anomaly list with all the configuration parameters,
# API will not assume any default values for anomaly list
fortios_api_firewall_dos_policy:
  endpoint_information:
  conn_params: '{{ test_fw }}'
  dos_policies:
  - interface: "port3"
    srcaddr:
    - name: "all"
    dstaddr:
    - name: "all"
    service:
    - name: "ALL"
    policyid: 1
    anomaly:

    - name: "tcp_syn_flood"
      status: enable
      log: enable
      threshold: 2000

    - name: "tcp_port_scan"
      status: disable

    - name: "tcp_src_session"
      status: enable
      log: enable
      threshold: 5000

    - name: "tcp_dst_session"
      status: enable
      log: enable
      threshold: 5000

    - name: "udp_flood"
      status: enable
      log: enable
      action: block
      threshold: 20000

    - name: "udp_scan"
      status: enable
      log: enable
      threshold: 2000

    - name: "udp_src_session"
      status: enable
      log: enable
      threshold: 5000

    - name: "udp_dst_session"
      status: enable
      log: enable
      threshold: 5000

    - name: "icmp_flood"
      status: enable
      log: enable
      threshold: 250

    - name: "icmp_sweep"
      status: enable
      log: enable
      threshold: 100

    - name: "icmp_src_session"
      status: enable
      log: enable
      threshold: 300

    - name: "icmp_dst_session"
      status: enable
      log: enable
      threshold: 1000

    - name: "ip_src_session"
      status: enable
      log: enable
      threshold: 5000

    - name: "ip_dst_session"
      status: enable
      log: enable
      threshold: 5000

    - name: "sctp_flood"
      status: enable
      log: enable
      threshold: 2000

    - name: "sctp_scan"
      status: enable
      log: enable
      threshold: 1000

    - name: "sctp_src_session"
      status: enable
      log: enable
      threshold: 5000

    - name: "sctp_dst_session"
      status: enable
      log: enable
      threshold: 5000
'''

RETURN = '''
proposed:
    description: k/v pairs of parameters passed into module and sent to the device for changes
    returned: always
    type: list
    sample: '[{"anomaly": [
                {"log": "enable", "name": "tcp_syn_flood", "status": "enable", "threshold": 2000},
                {"name": "tcp_port_scan", "status": "disable"},
                {"log": "enable", "name": "tcp_src_session", "status": "enable", "threshold": 5000},
                {"log": "enable", "name": "tcp_dst_session", "status": "enable", "threshold": 5000},
                {"action": "block", "log": "enable", "name": "udp_flood", "status": "enable", "threshold": 20000},
                {"log": "enable", "name": "udp_scan", "status": "enable", "threshold": 2000},
                {"log": "enable", "name": "udp_src_session", "status": "enable", "threshold": 5000},
                {"log": "enable", "name": "udp_dst_session", "status": "enable", "threshold": 5000},
                {"log": "enable", "name": "icmp_flood", "status": "enable", "threshold": 250},
                {"log": "enable", "name": "icmp_sweep", "status": "enable", "threshold": 100},
                {"log": "enable", "name": "icmp_src_session", "status": "enable", "threshold": 300},
                {"log": "enable", "name": "icmp_dst_session", "status": "enable", "threshold": 1000},
                {"log": "enable", "name": "ip_src_session", "status": "enable", "threshold": 5000},
                {"log": "enable", "name": "ip_dst_session", "status": "enable", "threshold": 5000},
                {"log": "enable", "name": "sctp_flood", "status": "enable", "threshold": 2000},
                {"log": "enable", "name": "sctp_scan", "status": "enable", "threshold": 1000},
                {"log": "enable", "name": "sctp_src_session", "status": "enable", "threshold": 5000},
                {"log": "enable", "name": "sctp_dst_session", "status": "enable", "threshold": 5000}],
              "dstaddr": [{"name": "all"}],
              "interface": "port3",
              "policyid": 1,
              "service": [{"name": "ALL"}],
              "srcaddr": [{"name": "all"}]}]'
existing:
    description: k/v pairs of existing configuration
    returned: always
    type: list
    sample: '[]'
end_state:
    description: k/v pairs of configuration after module execution
    returned: always
    type: list
changed:
    description: Whether a change was required for the device configuration.
    returned: always
    type: boolean
    sample: true
msg:
    description: A short description of the success of the change and status of the device.
    returned: always
    type: str
    sample: "Configuration updated."
'''

from ansible.module_utils.fortios_api import API

router_ospf_ospf_interface_args = {
    "endpoint": ['cmdb', 'firewall', 'DoS-policy'],
    "list_identifier": 'dos_policies',
    "object_identifier": "policyid",
    "permanent_objects": [],
    "default_ignore_params": [],
    "match_ignore_params": []
}


def main():
    forti_api = API(router_ospf_ospf_interface_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
