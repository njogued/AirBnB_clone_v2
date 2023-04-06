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
    comp_file = archive_path.split("/")[-1]
    no_suffix = comp_file.split(".")[0]
    
    try:
       remote_dir = "/data/web_static/releases/{}/".format(no_suffix)
       symbolic_link = "/data/web_static/current"
       put(archive_path, "/tmp/")
       run("sudo mkdir -p {}".format(remote_dir))
       run("sudo tar -xvzf /tmp/{} -C {}".format(comp_file, remote_dir))
       run("sudo rm /tmp/{}".format(comp_file))
       run("sudo mv {}/web_static/* {}".format(remote_dir, remote_dir))
       run("sudo rm -rf {}/web_static".format(remote_dir))
       run("sudo rm -rf /data/web_static/current")
       run("sudo ln -sf {} {}".format(remote_dir, symbolic_link))
       return True
    except Exception as e:
       return False
