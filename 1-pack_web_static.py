#!/usr/bin/python3
from fabric import api
import os
import datetime
"""A script to pack web_static into a tgz archive"""


def do_pack():
    """Func that will create the tgz archive"""
    curr_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    try:
        if not os.path.isdir("versions"):
            api.local("mkdir versions")
        path = f"versions/web_static_{curr_time}.tgz"
        output = api.local(f"tar -czvf {path} web_static")
        return path
    except Exception:
        return None
