from fabric.api import local
from datetime import datetime

def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        print("Error: {}".format(e))
        return None
