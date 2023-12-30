import os

from ..command import Command
from ..local_server import serve
from ..utils import PUBLIC_DIR, has_constructionist_site_layout

class Serve(Command):
    def __init__(self, dir, port):
        self.dir = dir
        self.port = port

    def process(self):
        if not has_constructionist_site_layout(self.dir):
            print(f"Directory {dir} doesn't contains a Constructionist site")
        # TODO: Do some checks on the port range (or maybe enforce constraints for it on the argparse level?)
        print(f'Serving content from directory {os.path.join(self.dir, PUBLIC_DIR)} on port {self.port}')
        serve(self.dir, self.port)
