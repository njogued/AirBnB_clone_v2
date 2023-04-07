#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os
"""script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB
Clone repo, using the function do_pack
"""


def do_pack():
    """Function to  archive webstatic folder & contents"""
    try:
        t_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
        if not os.path.isdir("versions"):
            local("mkdir versions")
        file_path = "versions/web_static_{}.tgz".format(t_stamp)
        result = local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception as e:
        return None
