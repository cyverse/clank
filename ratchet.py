#!/usr/bin/env python

import os
import sys

import envoy

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
              print bcolors.FAIL + command + bcolors.ENDC
          else:
              print bcolors.OKGREEN + command + bcolors.ENDC
      
 
def setup_ansible_cfg():
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

def main():
    install_dependencies()

if __name__ == "__main__":
  main()
