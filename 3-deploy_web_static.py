#!/usr/bin/python3
from fabric import api
from os import path
import datetime
"""A script to pack web_static into a tgz archive
using the function do_pack
Execution: fab -f 1-pack_web_static.py do_pack
"""


web_01 = '54.236.33.171'
web_02 = '54.90.8.140'
api.env.hosts = [web_01, web_02]
api.env.user = 'ubuntu'
api.env.key_filename = '~/.ssh/school'


def do_pack():
    """Func that will create the tgz archive
    The file name is web_static_current-time
    """
    try:
        if not path.isdir("versions"):
            api.local("mkdir versions")
        curr_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        path_f = "versions/web_static_{}.tgz".format(curr_time)
        output = api.local("tar -czvf {} web_static".format(path_f))
        return path_f
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploys the code to webservers and decompresses it
    Steps: 1. Check if file path exists
    2. Find the actual archive name w/o extension and store in name_x
    3. Make the directory of the archive (location)
    4. Unarchive the archive
    5. Point symlink to the location
    """
    if path.exists(archive_path) is False:
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


def deploy():
    """Combine archive creation and decompression and deployment"""
    path_f = do_pack()
    if not path_f:
        return False
    else:
        return do_deploy(path_f)
