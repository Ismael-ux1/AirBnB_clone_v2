#!/usr/bin/python3
# Fabric script that distributes an archive to your web servers

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['328455-web-01', '328455-web-02']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    """

    # Check if the file at the path archive_path doesn’t exist
    if not os.path.exists(archive_path):
        return False

    # Get the file name without extension
    file_name = os.path.basename(archive_path)
    name, ext = os.path.splitext(file_name)
    dest_dir = "/data/web_static/releases/{}/".format(name)

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder on the web server
        run("mkdir -p {}".format(dest_dir))
        run("tar -xzf /tmp/{} -C {}".format(file_name, dest_dir))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link on the web server
        run("ln -s {} /data/web_static/current".format(dest_dir))

        return True

    except Exception:
        return False
