#!/bin/python3

from pathlib import Path

# Global constants
YAML_DATA = "---\n\n\n..."
ANSIBLE_CFG_DATA = "[defaults]\n" \
    "hostfile = inventory\n" \
    "host_key_checking = False\n" \
    "deprecation_warnings=False\n" \
	"stdout_callback = skippy\n\n" \
	"[persistent_connection]\n" \
	"connect_timeout = 100\n" \
	"command_timeout = 80\n" \
    "log_path = /var/log/ansible/ansible.log\n"
PLAYBOOK_DATA = "---\n\n" \
	"- hosts: example_group\n" \
    "  gather_facts: no\n" \
	"  roles:\n" \
    "    - example_role\n\n" \
    "...\n"
EXAMPLE_GROUP = "example_group"
EXAMPLE_GROUP_FILE = "group_vars/" + EXAMPLE_GROUP + ".yml"
GROUP_VARS_DATA = "---\n\n" \
	"ansible_user: 'developer'\n" \
	"ansible_ssh_pass: 'C1sco12345'\n" \
	"ansible_network_os: 'cisco.ios.ios'\n" \
	"ansible_connection: 'network_cli'\n\n" \
	"logging_host_1: 10.10.5.14'\n" \
	"logging_host_2: 20.20.5.14'\n\n" \
	"snmp_server_1: 10.10.10.161'\n" \
	"snmp_server_2: 20.20.20.161'\n\n" \
	"ntp_server_1: 10.10.10.123'\n" \
	"ntp_server_2: 20.20.20.123'\n\n" \
	"...\n"
INVENTORY_DATA = "# Sample inventory file\n\n[" \
	+ EXAMPLE_GROUP + "]\n" \
 	"example-host-1.something.com\n"


def createDirs():
    Path("group_vars").mkdir(exist_ok=True)
    Path("host_vars").mkdir(exist_ok=True)
    # Create Roles folder and sub-folders
    Path("roles/example_role/tasks").mkdir(parents=True, exist_ok=True)
    Path("roles/example_role/templates").mkdir(parents=True, exist_ok=True)
    Path("roles/example_role/vars").mkdir(parents=True, exist_ok=True)
    Path("roles/example_role/handlers").mkdir(parents=True, exist_ok=True)


def createFiles():
	# Create default ansible.cfg
    with open("ansible.cfg", 'w') as f:
        f.write(ANSIBLE_CFG_DATA)

	# Create default inventory
    with open("inventory", 'w') as f:
        f.write(INVENTORY_DATA)

	# Create group_vars/example-group.yml
    with open(EXAMPLE_GROUP_FILE, 'w') as f:
        f.write(GROUP_VARS_DATA)

	# Create default playbook
    with open("playbook.yml", 'w') as f:
        f.write(PLAYBOOK_DATA)

	# Create main.yml for role/tasks
    with open("roles/example_role/tasks/main.yml", 'w') as f:
        f.write(YAML_DATA)

	# Create main.yml for role/vars
    with open("roles/example_role/vars/main.yml", 'w') as f:
        f.write(YAML_DATA)

	# Create main.yml for role/handlers
    with open("roles/example_role/handlers/main.yml", 'w') as f:
        f.write(YAML_DATA)


def main():
    createDirs()
    createFiles()


if __name__ == '__main__':
	main()