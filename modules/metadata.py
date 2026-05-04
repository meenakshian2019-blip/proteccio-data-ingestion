import os
import getpass
from datetime import datetime


def get_metadata(filepath, source_type="File Upload"):
    stats = os.stat(filepath)

    return {
        "source_name": os.path.basename(filepath),
        "source_type": source_type,
        "owner": getpass.getuser(),
        "file_name": os.path.basename(filepath),
        "file_type": filepath.split(".")[-1].lower(),
        "file_size_bytes": stats.st_size,
        "created_time": str(datetime.fromtimestamp(stats.st_ctime)),
        "modified_time": str(datetime.fromtimestamp(stats.st_mtime))
    }