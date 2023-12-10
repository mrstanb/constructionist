from ..command import Command

class Construct(Command):
    def __init__(self, dir):
        self.dir = dir

    def process(self):
        print(f'construct {self.dir}')
