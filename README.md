# ansible_fortios_api
Fortios API module for Ansible


## Installation
Copy content of fortios folder to ansible/lib/ansible/modules/network/fortios

Copy content of module_utils folder to ansible/lib/ansibe/module_utils

Run Ansible playbook as you would normally do.


## Usage
It's no different than any other Ansible module. If you have a Fortigate VM with code 5.4 at 192.0.2.5 accepting HTTP connections
with username admin and password test, then you can simply run example playbooks like this:

ansible-playbook fw_inventory_example.json -i test_inventory --extra-vars "pw=test"

ansible-playbook fw_example.json -i test_inventory

fw_example playbook goes through all of the modules and demonstrates how they can be used

fw_inventory_example playbook goes through some configuration and shows one of the ways this module can be used with inventory files


## How this module works
This module serves as the interface between Ansible and Fortios API. It can take any parameter that API accepts and send it over.
It's very important to note that this module takes the end-state config on the object level. I.e. if you have policies 1, 2 and 3
configured on the Firewall and you run a playbook that has policies 4 and 5, the end configuration on the firewall will have
policies 4 and 5 configured, while policied 1-3 will be deleted.

Within the object, only the values that are specified will be changed. I.e. if you have configured policy 1 and run a playbook
that has policy 1 with only a value of "comment=test comment", then only the comment field of the policy will be changed.

To simplify onboarding of existing devices, you can run playbook with print_current_config:true option (see fw_example.json),
which will run module in check mode and write a local file with current config of the specified firewall API endpoint.


## fortios_api arbitrary module
While the rest of the modules have hard-coded API path, this module is written to accept any arbitrary API endpoint and any arbitrary
set of variables. It will query the API to build an argument spec (which values can be assigned and what is the format for them) for
the given API endpoint. In some cases it fails, so you may need to edit "convert_type_str" function in module_utils/fortios_api.py
to solve the issue.

You can see examples of how this module can be used in the module itself (for setting static routes) or in the fw_example.json
(for managing VRRP interfaces)


## Parameters
Hopefully most of the parameters are self-explanatory and don't need any additional clarifcation, but there are some I want to clarify.
```endpoint_information - dictionary with information about API endpoint. You will see it only with fortios_api module
    endpoint - the API endpoint path
    list_identifier - the name of the list from which module will take objects
    object_identifier - if the list has multiple objects, module needs to know how this objects are identified in API (usually by name or id)
print_current_config - false by default, if set to true will run module in check mode (no changes) and write a file with currect config
conn_params - connection parameters, how to reach firewall and how to communicate with it
    fortigate_username - username
    fortigate_password - password
    fortigate_ip - ip or FQDN of the firewall
    secure - use HTTPS if true, use HTTP if false
    port - which port to use (default to 80 or 443 depending on secure)
    verify - verify validity of the cert if true
    proxies - if proxy is needed, specify it in the requests format (i.e. http: socks5://127.0.0.1:9000), see module code for example
list_of_objects - this is the list referenced in list_identifier. Its name and content changes based on the module. Note that this value
                  must be list all of the times, even if it is a list of 1 element.
permanent_objects - objects by ID that can not be deleted. Instead, when they are not present in the end state config, module will try to
                    reset them to defaults. Currently used only in the interface module.
ignore_objects - objects by ID that will be ignored by the module. Useful if you don't want your module to mess with management interface,
                 also can be used to not mess with built-in firewall addresses or services (see example playbooks).```

## Known gotchas
This module will write some files in the folder you are running it from (specifically it will write argument spec and current config if
you request it). I have not tested how it will work if it is run on a remote host. If the API changes at some point, you may need to
delete the local files so that argument spec is renegarated and can accept new values.

Module requires requests library to function. If you want to use socks proxy, make sure you install socks support for requests as well.

## Why is it in private repo and not submitted to Ansible?
I tried, they didn't take it. Ansible wants all of the modules to have defined argument spec, while this module builds it dynamically
based on the API endpoint. I personally believe that the ability to use effectively the same code to communicate with different API endpoints
is the point of using APIs, but I can see why Ansible wants modules to be better defined as well.
Regardless, I currently don't have much desire or time to effectively reduce the module functionality in order for Ansible to accept it.