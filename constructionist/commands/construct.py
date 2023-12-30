from ..command import Command
from ..utils import md_to_html, render_template
import glob

class Construct(Command):
    def __init__(self, dir):
        self.dir = dir

    def process(self):
        for f in glob.iglob(self.dir + "/_content/*.md"):
            md_content = md_to_html(f)
            render_template(self.dir, "index", md_content)
