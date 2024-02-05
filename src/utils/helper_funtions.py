import os
import json


def load_db_config():
    """TODO need to implement the basedir"""

    json_file_path = "resources/db_config.json"

    with open(json_file_path, 'r') as fr:
        content = json.loads(fr.read())

    return content
