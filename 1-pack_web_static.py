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
    year, month, day = now.year, now.month, now.day
    hour, minute, second = now.hour, now.minute, now.second

    if not os.path.exists("versions"):
        os.makedirs("versions")
    _path = f"versions/web_static_{year}{month}{day}{hour}{minute}{second}.tgz"

    cmd = f"tar -cvf {_path} web_static"

    result = local(cmd)

    if result.failed:
        return None
    else:
        return _path
