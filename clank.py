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
        description="Deploys Atmosphere and/or Troposphere according to the "
                    "configuration and overriding arguments. Any arguments "
                    "that Clank doesn't recognize will be passed on to the "
                    "resulting ansible-playbook command.")

    parser.add_argument("--skip-tags",
        type=str,
        default="",
	metavar="TAGS",
        help="skip the tag list e.g. 'dependencies,atmosphere'")

    parser.add_argument("--rebuild",
        action='store_true',
        help="Dramatically speed-up the time it takes to run clank by skipping one-time build steps")

    parser.add_argument("--limit",
        type=str,
        default="",
        help="(For remote deployments) tell clank what host to execute on")

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

    parser.add_argument("--playbook",
        type=str,
        help="Run a specific playbook, rather than the default deployment playbook")

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

    parser.add_argument("-b", "--become",
        required=False,
        action='store_true',
        help="This can be used to run operations with become. This is *not* required.")

    return parser

def live_run(command, **kwargs):
    start = datetime.now()
    proc = subprocess.Popen(shlex.split(command), **kwargs)
    out, err = proc.communicate()
    runtime = datetime.now() - start
    return (out, err, runtime, proc.returncode)

def execute_ansible_playbook(args, extra_ansible_playbook_args):

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    virtualenv_dir = os.environ["VIRTUAL_ENV"]

    ansible_exec = '{}/bin/ansible-playbook'.format(virtualenv_dir)
    ansible_play = '{}/playbooks/deploy_stack.yml'.format(cur_dir)
    ansible_hosts = '{}/hosts'.format(cur_dir)
    options = ""
    if args.skip_tags:
       options += ' --skip-tags="%s"' % args.skip_tags
    options += ' --limit "%s"' % args.limit if args.limit else ' -c local --limit localhost'
    if args.tags:
        options += ' --tags "%s"' % args.tags
    if args.rebuild:
        options += ' --skip-tags "clone-repo,data-load,npm,pip-install-requirements,apt-install"'
    if args.verbose or args.debug:
        options += ' -vvvvv -e"CLANK_VERBOSE=true"'
    if args.debug:
        options += ' --tags print-vars'
    if args.playbook:
        ansible_play = args.playbook
    if args.extra:
        for extra_arg in args.extra:
            options += ' -e"%s"' % extra_arg
    if args.become:
        options += ' -b'
    if extra_ansible_playbook_args:
        for arg in extra_ansible_playbook_args:
            options += ' %s' % arg

    command = '{} "{}" --flush-cache -e "@{}" -i {} {}'.format(
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
    args, extra_ansible_playbook_args = parser.parse_known_args()
    try:
        os.environ["VIRTUAL_ENV"]
    except KeyError:
        sys.exit('''
        Make sure to run within a virtualenv. See README.md.
        ''')
    try:
        execute_ansible_playbook(args, extra_ansible_playbook_args)
    except Exception as exc:
        print Fore.RED + "Error executing clank: %s" % exc.message
        parser.print_help()
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)

if __name__ == "__main__":
    main()

