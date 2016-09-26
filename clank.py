#!/usr/bin/env python
import argparse
import json
import os
import shlex
import subprocess
import sys
import traceback
from datetime import datetime
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

    parser.add_argument("--dry-run",
        action='store_true',
        help="Just print the command (Do not actually run the command)")

    parser.add_argument("--verbose",
        action='store_true',
        help="toggle on verbose output for command and shell tasks")

    parser.add_argument("--run-virtualenv",
        action='store_true',
        help="Run 'create_release_virtualenvs' utility-playbook, rather than execute deployment playbook")

    parser.add_argument("--run-backup",
        action='store_true',
        help="Run 'perform_backup' utility-playbook, rather than execute deployment playbook")

    parser.add_argument("--debug",
        action='store_true',
        help="print rather than execute deployment playbook")

    parser.add_argument("-e", "--env_file",
        required=True,
        type=str,
        help="the environment file to load when running ansible-playbook")

    parser.add_argument("-x", "--extra",
        required=False,
        action='append', default=[],
        help="This can be used to pass additional extra-vars to ansible-playbook. This is *not* required.")

    return parser

def live_run(command, **kwargs):
    start = datetime.now()
    proc = subprocess.Popen(shlex.split(command), **kwargs)
    out, err = proc.communicate()
    runtime = datetime.now() - start
    return (out, err, runtime, proc.returncode)

def execute_ansible_playbook(args):

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    virtualenv_dir = os.environ["VIRTUAL_ENV"]

    ansible_exec = '{}/bin/ansible-playbook'.format(virtualenv_dir)
    ansible_play = '{}/playbooks/deploy_stack.yml'.format(cur_dir)
    ansible_hosts = '{}/hosts'.format(cur_dir)
    options = ""
    if args.skip_tags:
       options += ' --skip-tags="%s"' % args.skip_tags
    if args.tags:
        options += ' --tags "%s"' % args.tags
    if args.verbose or args.debug:
        options += ' -vvvvv -e"CLANK_VERBOSE=true"'
    if args.debug:
        options += ' --tags print-vars'
    if args.run_backup:
        ansible_play = '{}/playbooks/utils/perform_backup.yml'.format(cur_dir)
    if args.run_virtualenv:
        ansible_play = '{}/playbooks/utils/create_release_virtualenvs.yml'.format(cur_dir)
    if args.extra:
        for extra_arg in args.extra:
            options += ' -e"%s"' % extra_arg

    command = '{} "{}" --flush-cache -c local -e "@{}" -i {} {}'.format(
        ansible_exec, ansible_play, args.env_file, ansible_hosts, options
    )
    if args.dry_run:
        print Fore.GREEN + command
        sys.exit(9)

    (out, err, runtime, returncode) = live_run(command, cwd=cur_dir)
    if returncode is not 0:
        print Fore.RED + "%s" % command
        print Fore.RED + "Total Runtime: %s" % runtime
        print Fore.RED + "Error Code:" + str(returncode)
        if out:
            print Fore.RED + "Std_out:" + out
        if err:
            print Fore.RED + "Std_err:" + err
        sys.exit(returncode)
    else:
        print Fore.GREEN + "Total Runtime: %s" % runtime
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
