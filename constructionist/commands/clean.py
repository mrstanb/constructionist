import os

from ..command import Command
from ..utils import *

class Clean(Command):
    def __init__(self, dir):
        self.dir = dir

    def process(self):
        self.clean_dir(self.dir)

    def clean_dir(self, dir):
        if not has_constructionist_site_layout(dir):
            print(f"Directory {dir} does not contain a constructionist website")
            return
        public_dir_path = os.path.join(dir, PUBLIC_DIR)
        print(f"Cleaning directory {public_dir_path}")
        for root, dirs, files in os.walk(public_dir_path, topdown=False):
            for name in files:
                os.remove(os.path.join(public_dir_path, name))
            for name in dirs:
                os.rmdir(os.path.join(public_dir_path, name))