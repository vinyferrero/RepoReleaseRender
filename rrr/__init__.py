# __init__.py
import os
import sys

__version__ = '0.0.1'

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rrr.releasereporender import ReleaseRepoRender

def generate_release_environment(filepath, dirpath):
    b_is_file = False
    b_is_dir = False
    b_is_empty = False
    if os.path.isfile(filepath):
        b_is_file = True
    else:
        print(f"the file: {filepath} does not exist.")
    if os.path.isdir(dirpath):
        b_is_dir = True

        if not os.listdir(dirpath):
            b_is_empty = True
        else:
            print(f"The directory '{dirpath}' is not empty.")
    else:
        print(f"the directory: {dirpath} does not exist.")
        
    if b_is_file and b_is_dir and b_is_empty:
        env = ReleaseRepoRender(filepath, dirpath)
        env.prepare_repositories()
        del env