#!/usr/bin/env python

import argparse
import json
import os
import shlex
import subprocess
import sys
import traceback
import yaml

from colorama import init, Fore
import envoy
import ruamel.yaml

try:
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
except ImportError:
    sys.exit('''
        Configuration required `Jinja2` for template & variable merging.
        Please ensure that the virtualenv for this project have been created
        and activated before running this script.
    ''')

FILE_PATH = os.path.abspath(os.path.dirname(__file__))

def setup_arguments():
    parser = argparse.ArgumentParser(
        description="Deploys Atmosphere and/or Troposphere according to "
                    "the configuration and overriding arguments.")
    parser.add_argument(
        "--dumpfile",
        type=str,
        help="The dump file to be used when creating the Atmosphere database. "
             "Can also be set in the config. (Optional)")
    parser.add_argument(
        "--atmosphere_db",
        type=str,
        help="The database name to be used for Atmosphere. "
             "Can also be set in the config. (Optional)")
    parser.add_argument(
        "--troposphere_db",
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

    parser.add_argument("--skip",
        type=str,
        default="",
        help="command seperated list e.g. 'dependencies,atmosphere'")

    parser.add_argument(
        "--branch",
        type=str,
        default='master',
        help="The branch to use for deploying Atmosphere and/or Troposphere")

    parser.add_argument("--override_args",
        default="{}",
        help="Pass in json to override variables file")

    parser.add_argument("--dynamic_env_file",
        type=str,
        default="dynamic_ratchet_ansible_env.yml",
        help="The environment file to be renamed as which will be loaded in to ansible-playbook")

    parser.add_argument("--workspace",
        required=True,
        type=str,
        help="The workspace from which files will be used to get ansible to run")

    parser.add_argument("--env_file",
        required=True,
        type=str,
        help="The environment file to load when running ansible-playbook")

    return parser

def setup_dependencies():
    # Check to see if ansible is not installed and redis
    ansible_check = envoy.run("which ansible")
    redis_check = envoy.run("which redis-server")
    if ansible_check.status_code is not 0 or redis_check.status_code is not 0:
        run_tasks_in_file("install_dependencies.txt")

def create_virtualenv():
    run_tasks_in_file("create_virtualenv.txt")

def run_tasks_in_file(filename):
    INSTALL_LIST = os.path.join(FILE_PATH, filename)
    with open(INSTALL_LIST) as f:
        commands = f.readlines()
        for command in commands:
            r = envoy.run(command, cwd=FILE_PATH)
            if r.status_code is not 0:
                print Fore.RED + command
                print Fore.RED + "Error Code:" + str(r.status_code)
                print Fore.RED + "Std_out:" + r.std_out
                print Fore.RED + "Std_err:" + r.std_err
                sys.exit(r.status_code)
            else:
                print Fore.GREEN + command

def prepare_ansible_env_file(args):
    current_vars_file = args.env_file
    my_vars_dict = json.loads(args.override_args)

    with open(current_vars_file, "r") as stream:
        dict_from_file = yaml.load(stream)

    for key in my_vars_dict.keys():
        if type(my_vars_dict[key]) == dict:
            vars_dict = my_vars_dict[key]
            dict_from_file[key].update(vars_dict)
        else:
            dict_from_file[key] = my_vars_dict[key]
    dumper = yaml.RoundTripDumper
    dumper.MAX_SIMPLE_KEY_LENGTH = 999
    file_content = ruamel.yaml.dump(dict_from_file, Dumper=dumper)

    new_env_file = os.path.join(FILE_PATH, args.dynamic_env_file)
    with open(new_env_file,'w') as the_file:
        the_file.write(file_content)


def live_run(command, **kwargs):
    proc = subprocess.Popen(shlex.split(command), **kwargs) 
    out, err = proc.communicate()
    return (out, err, proc.returncode)

def execute_ansible_playbook(args):

    command = '%s/clank/clank_env/bin/ansible-playbook %s/clank/playbooks/deploy_stack.yml --flush-cache -c local -e "@%s/clank/%s" -i "%s/clank/local_inventory"' % (args.workspace, args.workspace, args.workspace, args.dynamic_env_file, args.workspace)

    #Optional commands that cause errors if left empty:
    if args.skip:
       command += ' --skip "%s"' % args.skip
    (out, err, returncode) = live_run(command, cwd=FILE_PATH)
    if returncode is not 0:
        print Fore.RED + "%s" % command
        print Fore.RED + "Error Code:" + str(returncode)
        if out:
            print Fore.RED + "Std_out:" + out
        if err:
            print Fore.RED + "Std_err:" + err
        sys.exit(returncode)
    else:
        print Fore.GREEN + command 

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
    LOADER = FileSystemLoader(FILE_PATH)
    ENV = Environment(loader=LOADER,
                      undefined=StrictUndefined)

    template_location = "ansible.cfg.j2"
    output_path = os.path.join(FILE_PATH, "ansible.cfg")
    CLANK_ROLES_PATH = os.path.join(FILE_PATH, "roles")
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
    parser = setup_arguments()
    args = parser.parse_args()
    try:
        # To be executed prior to running 'ansible-playbook'
        setup_dependencies()
        create_virtualenv()
        prepare_ansible_cfg(args)
        prepare_ansible_env_file(args)

        # TODO: At this stage, we should SANITY CHECK:
        #       Print out all variables that have been set (In the env. or the arguments below)
        #       This will allow the user to ensure that things are 'as they should be'.
        #       We should give three second delay before we continue. This gives time to Ctrl+C

        execute_ansible_playbook(args)
        # TODO: Tests that can be executed after running 'ansible-playbook'
        # validate_install(args)
    except Exception as exc:
        print Fore.RED + "Error executing Ratchet: %s" % exc.message
        parser.print_help()
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)

if __name__ == "__main__":
    init(autoreset=True)  #init colorama
    main()
