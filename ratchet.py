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

def prepare_ansible_env_file(args):
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    current_vars_file = args.env_file
    my_vars_dict = json.loads(args.override_args)

    with open(os.path.join(PROJECT_PATH,current_vars_file), "r") as stream:
        dict_from_file = yaml.load(stream)
    
    for key in my_vars_dict.keys():
        if type(my_vars_dict[key]) == dict:
            vars_dict = my_vars_dict[key]
            dict_from_file[key].update(vars_dict)
        else:
            dict_from_file[key] = my_vars_dict[key]
  
    new_env_file = os.path.join(PROJECT_PATH, args.dynamic_env_file)
    with open(new_env_file,'w') as the_file:
        the_file.write(yaml.safe_dump(dict_from_file, default_flow_style=False,  encoding='utf-8', allow_unicode=True))


#def prepare_ansible_env_file(args):
#    """
#    INPUT: arguments (Including args.env_file)
#    OUTPUT: A new env file that includes *EVERYTHING* in args.env_file + overriding arguments!
#    This file will be called 'dynamic_ratchet_ansible_env'
#    """
#    if not args.env_file:
#        raise Exception("Missing env_file! Check your filepath and re-run with an env_file!")
#    with open(args.env_file,'r') as the_file:
#        python_obj = yaml.load(the_file)
#    arg_map = map_arguments(args)
#    python_obj.update(arg_map)
#    new_env_file = os.path.join(os.getcwd(), "dynamic_ratchet_ansible_env")
#    with open(new_env_file,'w') as the_file:
#        the_file.write(
#            yaml.dump(python_obj, default_flow_style=False)
#        )

def execute_ansible_playbook(args):
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    command = '%s/clank/clank_env/bin/ansible-playbook --flush-cache "%s/clank/playbooks/deploy_stack.yml" -c local -e @"%s/clank/%s" -i "%s/clank/local_inventory" --skip "troposphere"' % (args.workspace, args.workspace, args.workspace, args.dynamic_env_file, args.workspace)
    print command
    r = envoy.run(command, cwd=PROJECT_PATH)
    if r.status_code is not 0:
        print bcolors.FAIL + command
        print "Error Code:" + str(r.status_code)
        print "Std_out:" + r.std_out
        print "Std_err:" + r.std_err + bcolors.ENDC
        sys.exit(1)
    else:
        print bcolors.OKGREEN + command + bcolors.ENDC    
 
def map_arguments(args):
    """
    Takes a 'args NameSpace'
    Returns a Python dict with 'Ansible-ized' names!
    """
    return {
        'TROPOSPHERE_BRANCH': args.branch,
        'ATMOSPHERE_BRANCH': args.branch,
    }

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
        help="The dump file to be used when creating the Atmosphere database. "
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

    parser.add_argument("--override-args",
        default="{}",
        help="Pass in json to override variables file")
    
    parser.add_argument("--dynamic-env-file",
        type=str,
        default="dynamic_ratchet_ansible_env.yml",
        help="The environment file to be renamed as which will be loaded in to ansible-playbook")

    #POSITIONAL ARGUMENTS:
    parser.add_argument("workspace",
        type=str,
        help="The workspace from which files will be used to get ansible to run")
    parser.add_argument("env-file",
        type=str, 
        help="The environment file to load when running ansible-playbook")
    

    args = parser.parse_args()

    # To be executed prior to running 'ansible-playbook'

    try:
        install_dependencies()
        prepare_ansible_cfg(args)
        prepare_ansible_env_file(args)
        #TODO: At this stage, we should SANITY CHECK:
        #TODO: Print out all variables that have been set (In the env. or the arguments below)
        #TODO: This will allow the user to ensure that things are 'as they should be'.
        #TODO: We should give three second delay before we continue. This gives time to Ctrl+C

        # TODO: Execute ansible-playbook here.
        execute_ansible_playbook(args)
        # executed after running 'ansible-playbook'
        validate_install(args)
    except Exception as exc:
        print "Error executing Ratchet: %s" % exc.message
        parser.print_help()

if __name__ == "__main__":
  main()
