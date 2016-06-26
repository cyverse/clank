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
    VIRTUAL_DIR = os.environ["VIRTUAL_ENV"]
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
    from colorama import init, Fore
    import envoy
    import ruamel.yaml
except KeyError:
    sys.exit('''
    Make sure to run within a virtualenv. See README.md.
    ''')
except ImportError:
    sys.exit('''
    Error: missing imports
    pip install -r requirements
    ''')

CUR_DIR = os.path.abspath(os.path.dirname(__file__))

def setup_arguments():
    parser = argparse.ArgumentParser(
        description="Deploys Atmosphere and/or Troposphere according to "
                    "the configuration and overriding arguments.")

    parser.add_argument("--skip-tags",
        type=str,
        default="",
	metavar="TAGS",
        help="Skip the tag list e.g. 'dependencies,atmosphere'")

    parser.add_argument("--tags",
        type=str,
        default="",
        help="Include the tag list e.g. 'dependencies,atmosphere'")

    parser.add_argument("--verbose",
        action='store_true',
        help="Toggle on verbose output for command and shell tasks")

    parser.add_argument("--debug",
        action='store_true',
        help="Print rather than execute ansible")

    parser.add_argument("-e", "--env_file",
        required=True,
        type=str,
        help="The environment file to load when running ansible-playbook")

    return parser

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

    ansible_exec = '{}/bin/ansible-playbook'.format(VIRTUAL_DIR)
    ansible_play = '{}/playbooks/deploy_stack.yml'.format(CUR_DIR)
    command = '{} "{}" --flush-cache -c local -e "@{}" -i "localhost,"'.format(
        ansible_exec, ansible_play, args.env_file
    )

    if args.skip_tags:
       command += ' --skip-tags="%s"' % args.skip_tags
    if args.tags:
        command += ' --tags "%s"' % args.tags  
    if args.verbose:
        command += ' -e"CLANK_VERBOSE=true"'
    if args.debug:
        print "[DEBUG] Command to execute: {}".format(command)
	sys.exit(0)
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
        execute_ansible_playbook(args)
    except Exception as exc:
        print Fore.RED + "Error executing Ratchet: %s" % exc.message
        parser.print_help()
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)

if __name__ == "__main__":
    main()
