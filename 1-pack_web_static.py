#!/usr/bin/python3
# script that generates a .tgz archive from the
# contents of the web_static folder of your AirBnB
# Clone repo, using the function do_pack

# Import requisite modules
from fabric.api import *
import os
from datetime import datetime


def do_pack():
    """Function to  archive webstatic folder & contents"""
    now = datetime.now()
    t_stamp = now.strftime('%Y%m%d%H%M%S')

    if not os.path.exists("versions"):
        os.makedirs("versions")

    file_name = f"versions/web_static_{t_stamp}.tgz"

    cmd = f"tar -cvzf {file_name} web_static"

    result = local(cmd)

    if result.return_code != 0:
        return None
    else:
        return file_name
