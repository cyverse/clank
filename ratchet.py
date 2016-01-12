#!/usr/bin/env python

import argparse
import json
import os
import sys
import yaml

import envoy

try:
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
except ImportError:
    sys.exit('''
        Configuration required `Jinja2` for template & variable merging.
        Please ensure that the virtualenv for this project have been created
        and activated before running this script.
    ''')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def install_dependencies():
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    INSTALL_LIST = os.path.join(PROJECT_PATH, "install_tasks.txt")
    with open(INSTALL_LIST) as f:
        commands = f.readlines()
        for command in commands:
            r = envoy.run(command, cwd=PROJECT_PATH)
            if r.status_code is not 0:
                print bcolors.FAIL + command
                print "Error Code:" + str(r.status_code)
                print "Std_out:" + r.std_out
                print "Std_err:" + r.std_err + bcolors.ENDC
                sys.exit(1)
            else:
                print bcolors.OKGREEN + command + bcolors.ENDC

def read_and_write_new_varsfile(args):
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    current_vars_file = args.variables_file
    my_vars_dict = json.loads(args.override_args)

    with open(os.path.join(PROJECT_PATH,current_vars_file), "r") as stream:
        dict_from_file = yaml.load(stream)
    
    for key in my_vars_dict.keys():
        dict_from_file[key] = my_vars_dict[key]
  
        

def prepare_ansible_cfg(args):
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    LOADER = FileSystemLoader(PROJECT_PATH)
    ENV = Environment(loader=LOADER,
                      undefined=StrictUndefined)

    template_location = "ansible.cfg.j2"
    output_path = os.path.join(PROJECT_PATH, "ansible.cfg")
    CLANK_ROLES_PATH = os.path.join(PROJECT_PATH, "roles")
    template = ENV.get_template(template_location)
    rendered = template.render(CLANK_ANSIBLE_ROLES=CLANK_ROLES_PATH)
    with open(output_path, 'wb') as fh:
        fh.write(rendered)


def validate_install(args):
    """
    TODO: We may want 'args' to be the 'Merged Python Dict/Object' instead.

    1. Read your config file
    2. Verify that the path you *WANTED* is the path you used.
    3. Verify that the files you *WANTED* are being used in the path they are expected to be.
    More:
    """
    print "NOTE: These next lines are *MEANINGLESS* and can be safely ignored until ratchet is feature-complete"
    from deploy_tests import test_atmosphere
    for func_name in dir(test_atmosphere):
        func = getattr(test_atmosphere, func_name)
        if 'test' in func_name and callable(func):
            result = func({})  #TODO: replace with a dict of 'args' later.
            if result and result[0] == False:
                print result[1]
    pass


def main():
    parser = argparse.ArgumentParser(
        description="Deploys Atmosphere and/or Troposphere according to "
                    "the configuration and overriding arguments.")
    parser.add_argument(
        "--dumpfile",
        type=str,
        help="The dump file to be used when creating the Database. "
             "Can also be set in the config. (Optional)")
    parser.add_argument(
        "--atmosphere-db",
        type=str,
        help="The database name to be used for Atmosphere. "
             "Can also be set in the config. (Optional)")
    parser.add_argument(
        "--troposphere-db",
        type=str,
        help="The database name to be used for Troposphere. "
             "Can also be set in the config. (Optional)")
    parser.add_argument(
        "--atmosphere",
        action='store_true',
        help="Deploy Atmosphere *ONLY* (Default: Deploy both services)")

    parser.add_argument(
        "--troposphere",
        action='store_true',
        help="Deploy Troposphere *ONLY* (Default: Deploy both services)")

    parser.add_argument(
        "--branch",
        type=str,
        default='master',
        help="The branch to use for deploying Atmosphere and/or Troposphere")

    parser.add_argument(
        "--variables-file",
        type=str,
        default="variables.yml",
        help="Define the variables file for which Ansible is used to import")

    parser.add_argument(
        "--override-args",
        help="Pass in json to override variables file")

    args = parser.parse_args()
    # To be executed prior to running 'ansible-playbook'
    read_and_write_new_varsfile(args)

    #install_dependencies()
    #prepare_ansible_cfg(args)
    
    #Override vars
    

    #TODO: At this stage, we should SANITY CHECK:
    #TODO: Print out all variables that have been set (In the env. or the arguments below)
    #TODO: This will allow the user to ensure that things are 'as they should be'.
    #TODO: We should give three second delay before we continue. This gives time to Ctrl+C

    # TODO: Execute ansible-playbook here.
    
    # executed after running 'ansible-playbook'
    #validate_install(args)

if __name__ == "__main__":
  main()
