#!/usr/bin/python3
from fabric import api
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
            api.local("mkdir versions")
        curr_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        path = f"versions/web_static_{curr_time}.tgz"
        output = api.local(f"tar -czvf {path} web_static")
        return path
    except Exception:
        return None
