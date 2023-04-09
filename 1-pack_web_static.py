#!/usr/bin/python3
from fabric.api import local
import os
import datetime
"""A script to pack web_static into a tgz archive
using the function do_pack
Execution: fab -f 1-pack_web_static.py do_pack
"""


def do_pack():
    """Func that will create the tgz archive
    The file name is web_static_current-time
    """
    try:
        if not os.path.isdir("versions"):
            local("mkdir versions")
        curr_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        path = "versions/web_static_{}.tgz".format(curr_time)
        output = local("tar -czvf {} web_static".format(path))
        return path
    except Exception:
        return None
