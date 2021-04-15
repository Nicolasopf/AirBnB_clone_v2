#!/usr/bin/python3
""" Generates a .tgz archive from the contents of the web_static """
from fabric.api import local
from os import path
from datetime import datetime


def do_pack():
    """ Create directory if doesn't exist and backup folder web_static """
    time = str(datetime.now()).split(".")[0].replace(
        ":", "").replace(" ", "").replace("-", "")
    if path.exists("versions"):
        local("tar -czf versions/web_static_{}.tgz web_static".format(time))
    else:
        local("mkdir -p versions")
        local("tar -czf versions/web_static_{}.tgz web_static".format(time))
