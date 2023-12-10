import os

from ..command import Command
from ..utils import *

class Create(Command):
    def __init__(self, dir):
        self.dir = dir

    def process(self):
        self.create_site(self.dir)

    def create_site(self, dir):
        # TODO: Maybe also generate some default files in at least some of the directories
        dir = os.path.realpath(dir)
        if has_constructionist_site_layout(dir):
            print(f'Directory {dir} already contains a constructionist site')
            return
        print('Creating constructionist site layout...')
        for site_dir in [ASSETS_DIR, CONTENT_DIR, PUBLIC_DIR, TEMPLATES_DIR]:
            os.makedirs(os.path.join(dir, site_dir))
