import json
import os
from datetime import datetime

import yaml

from Config import Config


def save_setting_data(setting_data: dict):
    file_path = "./setting.json"
    if os.path.exists(file_path):
        if os.path.getsize(file_path):
            with open(file_path, 'a+', encoding='UTF-8') as fp:
                fp.seek(0, 0)
                fp.truncate()
                json.dump(setting_data, fp, sort_keys=True)
    else:
        with open(file_path, 'a+', encoding='UTF-8') as fp:
            fp.seek(0, 0)
            fp.truncate()
            json.dump(setting_data, fp, sort_keys=True)


def get_config_data() -> dict:
    file_path = "./setting.yaml"
    try:
        with open(Config.CONFIG_DATA_FILE, 'r', encoding='UTF-8') as fp:
            file_data = fp.read()
            return yaml.safe_load(file_data)
    except Exception as e:
        return None

def set_config_data(setting_data):
    try:
        with open(Config.CONFIG_DATA_FILE, 'w', encoding='UTF-8') as fp:
            yaml.dump(setting_data,fp)
        return 0
    except Exception as e:
        return None