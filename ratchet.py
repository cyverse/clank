#!/usr/bin/env python

import argparse
import json
import os
import shlex
import subprocess
import sys
import traceback
import yaml


try:
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
    from colorama import init, Fore
    import envoy
    import ruamel.yaml
except ImportError:
    sys.exit('''
    Error: missing imports
    Make sure to source the proper virtualenv. See README.md.
    ''')

CUR_DIR = os.path.abspath(os.path.dirname(__file__))

def setup_arguments():
    parser = argparse.ArgumentParser(
        description="Deploys Atmosphere and/or Troposphere according to "
                    "the configuration and overriding arguments.")

    parser.add_argument("--skip-tags",
        type=str,
        default="",
        help="command seperated list e.g. 'dependencies,atmosphere'")

    parser.add_argument("--tags",
        type=str,
        default="",
        help="command seperated list e.g. 'dependencies,atmosphere'")

    parser.add_argument("--vagrant",
        action='store_true',
        help="when present will setup up install for vagrant")

    parser.add_argument("--verbose",
        action='store_true',
        help="Toggle on verbose output for command and shell tasks.")

    parser.add_argument("-i", "--inventory",
	default="{}/hosts".format(CUR_DIR),
        type=str,
        help="The path to the ansible inventory, which defaults to ./hosts.")

    parser.add_argument("-e", "--env_file",
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
    INSTALL_LIST = os.path.join(CUR_DIR, filename)
    with open(INSTALL_LIST) as f:
        commands = f.readlines()
        for command in commands:
            r = envoy.run(command, cwd=CUR_DIR)
            if r.status_code is not 0:
                print Fore.RED + command
                print Fore.RED + "Error Code:" + str(r.status_code)
                print Fore.RED + "Std_out:" + r.std_out
                print Fore.RED + "Std_err:" + r.std_err
                sys.exit(r.status_code)
            else:
                print Fore.GREEN + command

def live_run(command, **kwargs):
    proc = subprocess.Popen(shlex.split(command), **kwargs) 
    out, err = proc.communicate()
    return (out, err, proc.returncode)

def execute_ansible_playbook(args):

    ansible_exec = '{}/clank_env/bin/ansible-playbook'.format(CUR_DIR)
    ansible_play = '{}/playbooks/deploy_stack.yml'.format(CUR_DIR)
    command = '{} "{}" --flush-cache -c local -e "@{}" -i "{}"'.format(
        ansible_exec, ansible_play, args.env_file, args.inventory
    )

    if args.skip_tags:
       command += ' --skip-tags="%s"' % args.skip_tags
    if args.tags:
        command += ' --tags "%s"' % args.tags  
    if args.vagrant:
        command += ' -e"VAGRANT=true"'
    if args.verbose:
        command += ' -e"CLANK_VERBOSE=true"'
    print "COMMAND: %s" % command
    (out, err, returncode) = live_run(command, cwd=CUR_DIR)
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

def main():
    init(autoreset=True)  # init colorama
    parser = setup_arguments()
    args = parser.parse_args()
    try:
        # To be executed prior to running 'ansible-playbook'
        setup_dependencies()
        create_virtualenv()
        execute_ansible_playbook(args)
    except Exception as exc:
        print Fore.RED + "Error executing Ratchet: %s" % exc.message
        parser.print_help()
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)

if __name__ == "__main__":
    main()
