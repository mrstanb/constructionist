from ..command import Command

class Serve(Command):
    def __init__(self, dir, port):
        self.dir = dir
        self.port = port

    def process(self):
        print(f'serve {self.dir} {self.port}')
