#!/usr/bin/python3
# Fabric script that distributes an archive to your web servers.
from fabric.api import env, put, run
from os.path import exists
from datetime import datetime


env.hosts = ['54.209.26.141', '18.215.182.32']
env.user = 'ubuntu'
env.key_filename = '~/larissa/.ssh/id_rsa'

def do_deploy(archive_path):
    """Distribute an archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to the appropriate folder
        archive_filename = archive_path.split('/')[-1]
        release_folder = '/data/web_static/releases/{}'.format(archive_filename[:-4])
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move the contents of the extracted folder to the parent directory
        run('mv {}/web_static/* {}/'.format(release_folder, release_folder))
        run('rm -rf {}/web_static'.format(release_folder))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(release_folder))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Error: {}".format(e))
        return False
