from ..command import Command

class Clean(Command):
    def __init__(self, dir):
        self.dir = dir

    def process(self):
        print(f'clean {self.dir}')
