#!/usr/bin/env python

import os.path
import envoy
import subprocess

def run_command(commandList, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                stdin=None, dry_run=False, shell=False):
    """
    NOTE: Use this to run ANY system command, because its wrapped around a loggger
    Using Popen, run any command at the system level and record the output and error streams
    """
    out = None
    err = None
    if type(commandList) == str:
        cmd_str = commandList
    else:
        cmd_str = ' '.join(commandList)
    if dry_run:
        #Bail before making the call
        print "Mock Command: %s" % cmd_str
        return ('','')
    #print "Run Command: %s" % cmd_str
    try:
        if stdin:
            proc = subprocess.Popen(commandList, stdout=stdout, stderr=stderr,
                    stdin=subprocess.PIPE, shell=shell)
        else:
            proc = subprocess.Popen(commandList, stdout=stdout, stderr=stderr,
                    shell=shell)
        out,err = proc.communicate(input=stdin)
    except Exception, e:
        print e
    #if stdin:
    #    print "%s STDIN: %s" % (cmd_str, stdin)
    #print "%s STDOUT: %s" % (cmd_str, out)
    #print "%s STDERR: %s" % (cmd_str, err)
    return (out,err)

def test_directory_installed_correctly(args={}):
    """
    Test that Atmosphere was installed in the correct location.
    """
    #REMOVE hardcode in place of an actual 'args' later.
    args['atmosphere_dir'] = "/opt/dev/atmosphere"

    prev_dir, dirname = os.path.split(args['atmosphere_dir'] )
    r = envoy.run("find %s -type d -name %s -prune -print" % (prev_dir, dirname))
    if r.status_code != 0 or args['atmosphere_dir'] not in r.std_out:
        return (False, "No Atmosphere directory found in expected location: %s"
                       % args['atmosphere_dir'] )

def test_database_installed_correctly(args={}):
    """
    Test that Atmosphere's database is in the correct location.
    """
    #REMOVE hardcode in place of an actual 'args' later.
    args['atmosphere_db'] = "atmosphere"
    out, err = run_command(['su', '-', 'postgres', '-c', 'psql -lqt | cut -d "|" -f 1 | grep "atmosphere"'])
    if args['atmosphere_db'] not in out:
       return (False, "Expected atmosphere database named %s -- Database not found" % args['atmosphere_db'])


def test_crt_key_bundle(args={}):
    """
    Test the final location of 'SSL required files'
    """
    args['ssl_cert'] = "/etc/ssl/certs/ssl_cert.crt"
    args['ssl_key'] = "/etc/ssl/private/ssl_cert.key"
    args['ssl_bundle'] = "/etc/ssl/certs/ssl_bundle.crt"
    for final_file_location in [args['ssl_cert'] , args['ssl_key'] , args['ssl_bundle'] ]:
        if not os.path.exists(final_file_location):
            return (False, "Expected SSL file missing: %s" % final_file_location)

def test_git_branch(args={}):
    """
    Test git branch matches configuration
    """
    args['git_branch'] = "master"
    args['atmosphere_dir'] = "/opt/dev/atmosphere"
    # TEST FOR BRANCH NAME
    r = envoy.run("cat %s/.git/HEAD" % args['atmosphere_dir'])
    if r.status_code != 0 or args['git_branch'] not in r.std_out:
        return (False, "Expected Git Branch of Atmosphere: %s - Output:%s" % (args['git_branch'],r.std_out))

def main():
    args = {
        'git_branch': 'master',
        'atmosphere_dir': '/opt/dev/atmosphere',
        'atmosphere_db': '/opt/dev/atmosphere',
        'ssl_bundle':'/etc/ssl/certs/ssl_bundle.crt',
        'ssl_cert':'/etc/ssl/certs/ssl_cert.crt',
        'ssl_key':'/etc/ssl/private/ssl_cert.key',
    }
    print test_directory_installed_correctly(args)
    print test_database_installed_correctly(args)
    print test_crt_key_bundle(args)
    print test_git_branch(args)
    
if __name__ == "__main__":
  main()
