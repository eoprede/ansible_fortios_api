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
module: fortios_api_firewall_policy
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages Firewall policy configuration.
description:
    - Manages Firewall policy configuration.
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Assumes the list of default (permanent) objects.

options:
    policies:
        description:
            - Full list of policies to be applied to the Firewall. Note that any policy not present in the list will be DELETED.
              The order in which objects appear in the list is the order in which Firewall will process the rules.
        required: true
        suboptions:
            policyid:
                description:
                    - ID of the policy, must be unique
                required: true
            name:
                description:
                    - Name of the policy. Doesn't exist in 5.2 and isn't required for 5.4 CLI, but required for 5.4 GUI
                required: false
                default: null
            srcintf:
                description:
                    - Source interface.
                required: true
                type: list
            dstintf:
                description:
                    - Destination interface
                required: true
                type: list
            srcaddr:
                description:
                    - Source address.
                required: true
                type: list
            dstaddr:
                description:
                    - Destination address.
                required: true
                type: list
            schedule:
                description:
                    - Schedule.
                required: true
            service:
                description:
                    - Service(s) list.
                required: true
                type: list
            action:
                description:
                    - What to do with the traffic matched by the policy
                required: true
                type: str
                choices: ['accept', 'deny', 'learn']
'''
EXAMPLES = '''
---
name: update firewall policies
fortios_api_firewall_policy:
  conn_params:
        fortigate_username: admin
        fortigate_password: test
        fortigate_ip: 1.2.3.4
        port: 10080
        verify: false
        secure: false
        proxies:
            http: socks5://127.0.0.1:9000
  policies:
  - policyid: 14
    srcintf:
    - name: port4
    dstintf:
    - name: port3
    srcaddr:
    - name: auth.gfx.ms
    dstaddr:
    - name: all
    action: accept
    schedule: always
    service:
    - name: IMAPS
    comments: test_policy
    name: Test policy
    nat: enable
  - policyid: 5
    srcintf:
    - name: port3
    dstintf:
    - name: port5
    srcaddr:
    - name: all
    dstaddr:
    - name: all
    action: accept
    schedule: always
    service:
    - name: IMAPS
    comments: allow_imaps_in
    name: imaps_in
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


fw_api_args = {
    "endpoint": ["cmdb", "firewall", "policy"],
    "list_identifier": 'policies',
    "object_identifier": 'policyid',
    "permanent_objects": [],
    "default_ignore_params": [],
}


class FirewallAPI(API):

    def __init__(self, module):
        super(FirewallAPI, self).__init__(module)
        self._validate_policies()
        self._object_map = []

    def _validate_policies(self):
        policy_specification = self._get_argument_spec()
        if not self._update_config:
            return

        types = {
            'str': str,
            'list': list,
            'dict': dict,
            'int': int,
        }

        required = [k for k in policy_specification if policy_specification[
            k].get('necessary')]
        for i, policy in enumerate(self._update_config):
            missing = []
            unrecognized = []
            wrong_type = ""

            for k in required:
                if k not in policy:
                    missing.append(k)

            if missing:
                self.fail(msg="Missing required arguments '%s' in policy #%s" % (
                    ", ".join(missing), str(i)))

            try:
                for k, v in policy.items():
                    if k not in policy_specification:
                        unrecognized.append(k)
                    else:
                        value_type = type(v)
                        required_type = policy_specification[k].get('type')
                        if v is not None and value_type != types[required_type]:
                            wrong_type += ("Wrong type %s for argument '%s' in policy #%s. Requires %s.\n" % (
                                value_type, k, str(i), required_type))
            except AttributeError:
                for k, v in policy.items():
                    if k not in policy_specification:
                        unrecognized.append(k)
                    else:
                        value_type = type(v)
                        required_type = policy_specification[k].get('type')
                        if v is not None and value_type != types[required_type]:
                            wrong_type += ("Wrong type %s for argument '%s' in policy #%s. Requires %s.\n" % (
                                value_type, k, str(i), required_type))

            if wrong_type:
                self.fail(wrong_type)

            if unrecognized:
                self.fail(msg="Unrecognized arguments '%s' in policy #%s" %
                          (", ".join(unrecognized), str(i)))

    def apply_configuration_to_endpoint(self):
        self._execute_config_changes()
        self._build_object_map()
        self._move_existing_policies()
        if not self._check_mode:
            message, changed, failed = self._process_response()
            changed = changed or self._order_changed()
        else:
            message = "Check Mode"
            original_match, update_match = self._original_or_update_match_current_configuration()
            changed = not update_match or self._order_changed()
            failed = False

        self._module.exit_json(msg=message, changed=changed, failed=failed,
                               existing=self._fortigate_current_config, proposed=self._update_config, new=self._diff_configs())

    def _order_changed(self):
        try:
            return any([True for i, o in enumerate(self._fortigate_original_config)
                        if o[self._object_identifier] != self._fortigate_current_config[i][self._object_identifier]])
        except IndexError:
            return True

    def _identify_highest_distance_move(self):
        index = None
        highest = 0
        for i, policy_info in enumerate(self._object_map):
            if policy_info:
                move_distance = policy_info[2]
                if move_distance > highest:
                    index = i
                    highest = move_distance
        return index

    def _get_policy_index_from_object_map(self, target_policy_id):
        index = None
        for i, policy_info in enumerate(self._object_map):
            policy_id = policy_info[1]
            if policy_id == target_policy_id:
                index = i
                break
        return index

    def _move_existing_policies(self):
        mpol_target_index = self._identify_highest_distance_move()
        while mpol_target_index is not None:
            self._move_policy(mpol_target_index)
            mpol_target_index = self._identify_highest_distance_move()

    def _move_policy(self, mpol_target_index):
        # move policy is the one going to its final position
        mpol_info = self._object_map[mpol_target_index]
        mpol_cur_index = mpol_info[0]
        mpol_id = mpol_info[1]

        target_index_id = self._fortigate_current_config[
            mpol_target_index]['policyid']

        if mpol_target_index > mpol_cur_index:
            self._fortigate_current_config.insert(
                mpol_target_index + 1, self._fortigate_current_config[mpol_cur_index])
            del self._fortigate_current_config[mpol_cur_index]
            if not self._check_mode:
                self._edit('/'.join([self._endpoint, str(mpol_id)]),
                           params={"action": "move", "after": str(target_index_id), "vdom": self._vdom})
        else:
            self._fortigate_current_config.insert(
                mpol_target_index, self._fortigate_current_config[mpol_cur_index])
            del self._fortigate_current_config[mpol_cur_index + 1]
            if not self._check_mode:
                self._edit('/'.join([self._endpoint, str(mpol_id)]),
                           params={"action": "move", "before": str(target_index_id), "vdom": self._vdom})

        self._build_object_map()

    def _find_policy_index_in_current_config_by_id(self, policy_id):
        for i, p in enumerate(self._fortigate_current_config):
            if p['policyid'] == policy_id:
                return i
        return False

    def _get_index_of_matching_object(self, forti_object):
        found = False
        existing_index = 0
        existing_object_count = len(self._fortigate_current_config)

        while not found and existing_index < existing_object_count:
            if not self._diff_unknown(self._fortigate_current_config[existing_index], forti_object):
                return existing_index
            existing_index = existing_index + 1
        return None

    def _build_object_map(self):
        self._get_current_configuration()
        if not self._update_config:
            self._object_map = [None] * len(self._fortigate_current_config)
        else:
            self._object_map = []
            for desired_index, forti_object in enumerate(self._update_config):
                existing_index = self._get_index_of_matching_object(
                    forti_object)
                if existing_index is not None:
                    self._object_map.append((existing_index,
                                             self._fortigate_current_config[
                                                 existing_index][self._object_identifier],
                                             abs(existing_index - desired_index)))
                else:
                    self._object_map.append(None)


def main():
    forti_api = FirewallAPI(fw_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
