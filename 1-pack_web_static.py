#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
"""script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB
Clone repo, using the function do_pack
"""


def do_pack():
    """Function to  archive webstatic folder & contents"""
    now = datetime.now()
    t_stamp = now.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")

    file_path = f"versions/web_static_{t_stamp}.tgz"

    cmd = f"tar -cvzf {file_path} web_static"

    result = local(cmd)

    if result.succeeded:
        return file_path
    else:
        return None
