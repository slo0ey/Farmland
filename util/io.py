import os
import pickle
import platform


PLATFORM = platform.system()


# TODO: Linux 지원
def appdata_path():
    if PLATFORM == 'Windows':
        return os.path.expandvars(r'%LOCALAPPDATA%/Farmland')
    elif PLATFORM == 'Darwin':
        return os.path.expanduser('~/Library/Farmland')
    else:
        raise NotImplemented


# def load_file(
#         file_name: str,
#         extension: str = 'txt'
# ):
#
