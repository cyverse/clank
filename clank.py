#!/usr/bin/env python
import argparse
import json
import os
import shlex
import subprocess
import sys
import traceback

try:
    from colorama import init, Fore
except ImportError:
    sys.exit('''
    Error: missing imports
    pip install -r requirements
    ''')


def setup_arguments():
    parser = argparse.ArgumentParser(
        description="Deploys Atmosphere and/or Troposphere according to "
                    "the configuration and overriding arguments.")

    parser.add_argument("--skip-tags",
        type=str,
        default="",
	metavar="TAGS",
        help="skip the tag list e.g. 'dependencies,atmosphere'")

    parser.add_argument("--tags",
        type=str,
        default="",
        help="include the tag list e.g. 'dependencies,atmosphere'")

    parser.add_argument("--verbose",
        action='store_true',
        help="toggle on verbose output for command and shell tasks")

    parser.add_argument("--debug",
        action='store_true',
        help="print rather than execute ansible")

    parser.add_argument("-e", "--env_file",
        required=True,
        type=str,
        help="the environment file to load when running ansible-playbook")

    return parser

def live_run(command, **kwargs):
    proc = subprocess.Popen(shlex.split(command), **kwargs) 
    out, err = proc.communicate()
    return (out, err, proc.returncode)

def execute_ansible_playbook(args):

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    virtualenv_dir = os.environ["VIRTUAL_ENV"]
    ansible_exec = '{}/bin/ansible-playbook'.format(virtualenv_dir)
    ansible_play = '{}/playbooks/deploy_stack.yml'.format(cur_dir)
    ansible_hosts = '{}/hosts'.format(cur_dir)
    command = '{} "{}" --flush-cache -c local -e "@{}" -i {}'.format(
        ansible_exec, ansible_play, args.env_file, ansible_hosts
    )

    if args.skip_tags:
       command += ' --skip-tags="%s"' % args.skip_tags
    if args.tags:
        command += ' --tags "%s"' % args.tags  
    if args.verbose or args.debug:
        command += ' -vvvvv -e"CLANK_VERBOSE=true"'
    if args.debug:
        command += ' --tags print-vars'
    (out, err, returncode) = live_run(command, cwd=cur_dir)
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
        os.environ["VIRTUAL_ENV"]
    except KeyError:
        sys.exit('''
        Make sure to run within a virtualenv. See README.md.
        ''')
    try:
        execute_ansible_playbook(args)
    except Exception as exc:
        print Fore.RED + "Error executing clank: %s" % exc.message
        parser.print_help()
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)

if __name__ == "__main__":
    main()
