import os
import json
import platform


PLATFORM = platform.system()


# TODO: Linux 지원
def appdata_path():
    if PLATFORM == 'Windows':
        return os.path.expandvars(r'%LOCALAPPDATA%/Farmland/')
    elif PLATFORM == 'Darwin':
        return os.path.expanduser('~/Library/Farmland/')
    else:
        raise NotImplemented


def save_json(
        data,
        file_name: str,
        folder: str | list[str] = ''
):
    path = os.path.join(appdata_path(), folder)
    if not os.path.exists(path):
        os.makedirs(path)

    path = os.path.join(path, file_name + '.json')
    with open(path, 'w') as f:
        json.dump(data, f)


def load_json(
        file_name: str,
        folder: str | list[str] = '',
        default_value=None
):
    path = os.path.join(appdata_path(), folder, file_name + '.json')
    data = default_value
    if os.path.exists(path):
        with open(path, 'r') as f:
            data = json.load(f)

    return data
