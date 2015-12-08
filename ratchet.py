#!/usr/bin/env python

import os
import sys

import envoy

try:
    from jinja2 import Environment, FileSystemLoader, meta, StrictUndefined, \
                       TemplateNotFound
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
          r = envoy.run(command)
          if r.status_code is not 0:
              print bcolors.FAIL + command 
              print "Error Code:" + str(r.status_code)
              print "Std_out:" + r.std_out
              print "Std_err:" + r.std_err + bcolors.ENDC
              sys.exit(1)
          else:
              print bcolors.OKGREEN + command + bcolors.ENDC
      
 
def setup_ansible_cfg():
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

def main():
    install_dependencies()
    setup_ansible_cfg()

if __name__ == "__main__":
  main()
