#!/usr/bin/python3
"""
script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the
function do_deploy
Distributes an archive to your web servers using Fabric.
"""

import os
from fabric.api import run, put, env

env.hosts = ['54.175.228.113', '54.236.26.145']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ftn deploys code and decompresses it"""
    if not os.path.isfile(archive_path):
        return False

    """extract filename of archive from its path"""
    comp_file = archive_path.split("/")[-1]

    """removing the file extension .tgz"""
    no_suffix = comp_file.split(".")[0]

    try:
        """remote dir where the code will be deployed"""
        remote_dir = "/data/web_static/releases/{}/".format(no_suffix)

        """symbolic link; will point to latest version of the code"""
        symbolic_link = "/data/web_static/current"

        """uploading archive to /tmp/ in server"""
        put(archive_path, "/tmp/")

        """create remote directory if not exists"""
        run("sudo mkdir -p {}".format(remote_dir))

        """extracts contents of archive to remote dir"""
        run("sudo tar -xvzf /tmp/{} -C {}".format(comp_file, remote_dir))

        """delete archive from server"""
        run("sudo rm /tmp/{}".format(comp_file))

        """move contents of webstatic to remote dir"""
        run("sudo mv {}/web_static/* {}".format(remote_dir, remote_dir))

        """delete the webstatic dir from remote dir"""
        run("sudo rm -rf {}/web_static".format(remote_dir))

        """removes symbolic link to previous code version"""
        run("sudo rm -rf /data/web_static/current")

        """create new symbolic link to new code version"""
        run("sudo ln -sf {} {}".format(remote_dir, symbolic_link))
        return True
    except Exception as e:
        return False
