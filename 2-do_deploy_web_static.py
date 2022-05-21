#!/usr/bin/python3
"""script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy"""

from threading import local
from fabric.api import run, put, env
from datetime import datetime
import os
env.hosts = ['104.196.101.1', '3.94.111.32']


def do_pack():
    """ Function to generate a tgz from web_static"""
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        tgz_file = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(tgz_file))
        return tgz_file
    except:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to your web servers. """

    if os.path.exists(archive_path):
        path = "/data/web_static/releases/"
        name = archive_path.split('.')[0].split('/')[1]
        dest = path + name

        try:
            put(archive_path, '/tmp')
            run('mkdir -p {}'.format(dest))
            run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
            run('rm -f /tmp/{}.tgz'.format(name))
            run('mv {}/web_static/* {}/'.format(dest, dest))
            run('rm -rf {}/web_static'.format(dest))
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(dest))

            return True

        except:
            return False
    else:
        return False
