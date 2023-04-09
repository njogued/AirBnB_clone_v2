#!/usr/bin/python3
""" script that distributes an archive to your web servers using Fabric.
"""

from os import path
from fabric import api

web_01 = '54.236.33.171'
web_02 = '54.90.8.140'
api.env.hosts = [web_01, web_02]
api.env.user = 'ubuntu'
api.env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Deploys the code to webservers and decompresses it
    Steps: 1. Check if file path exists
    2. Find the actual archive name w/o extension and store in name_x
    3. Make the directory of the archive (location)
    4. Unarchive the archive
    5. Point symlink to the location
    """
    if path.exists(archive_path) == False:
        return False
    path_f = archive_path.split("/")[-1]
    name_x = path.split(".")[0]

    try:
        location = "/data/web_static/releases/{}/".format(name_x)
        slink = "/data/web_static/current"
        api.put(archive_path, "/tmp/")
        api.run("sudo mkdir -p {}/".format(location))
        api.run("sudo tar -xzf /tmp/{} -C {}/".format(path_f, location))
        api.run("sudo rm -rf /tmp/{}".format(path_f))
        api.run("sudo cp -r {}/web_static/* {}/".format(location, location))
        api.run("sudo rm -rf {}/web_static".format(location))
        api.run("sudo rm -rf {}".format(slink))
        api.run("sudo ln -sf {} {}".format(location, slink))
        return True
    except Exception as e:
        return False
