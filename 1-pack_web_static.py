#!/usr/bin/python3
# Fabric script that generates a .tgz archive from web_static
from fabric.api import *
from datetime import datetime
import os


# Define the function do_pack
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """

    # Get the current date and time in the format YYYYMMDDHHMMSS
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the file path for the archive
    file_path = "versions/web_static_{}.tgz".format(date)

    # Check if the directory "versions" exists, if not create it
    if not os.path.isdir("versions"):
        local("mkdir versions")

    # Create a .tgz archive of the web_static folder
    local("tar -cvzf {} web_static".format(file_path))

    # Check if the archive was created successfully
    if os.path.exists(file_path):
        # If yes, return the file path
        return file_path
    else:
        # If no, return None
        return None
