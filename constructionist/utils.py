import os
import markdown
from jinja2 import Environment, FileSystemLoader

ASSETS_DIR = "_assets"
CONTENT_DIR = "_content"
PUBLIC_DIR = "_public"
TEMPLATES_DIR = "_templates"
TEMPLATE_EXT = ".jinja"
HTML_EXT = ".html"

def has_constructionist_site_layout(dir):
    dir = os.path.realpath(dir)
    if not os.path.exists(dir) or not os.path.exists(dir):
        return False
    sub_dirs = os.listdir(dir)
    for site_dir in [ASSETS_DIR, CONTENT_DIR, PUBLIC_DIR, TEMPLATES_DIR]:
        if not os.path.isdir(os.path.join(dir, site_dir)) or not site_dir in sub_dirs:
            return False
    return True

# Convert a Markdown file to an HTML string
# TODO: Might be memory-problematic if the file is too large and the resulting HTML string can't fit in memory
def md_to_html(file):
    file = os.path.realpath(file)
    if not os.path.exists(file):
        print(f"Content file {file} not found")
        exit(1)
    
    with open(file, "r") as f:
        md_content = f.read()
        html_content = markdown.markdown(md_content)
        return html_content

def render_template(template_parent_dir, template_name, content):
    environment = Environment(loader=FileSystemLoader(os.path.join(template_parent_dir, TEMPLATES_DIR)))
    template = environment.get_template(template_name + TEMPLATE_EXT)

    path_to_public_dir = os.path.join(template_parent_dir, PUBLIC_DIR)

    if not os.path.exists(path_to_public_dir):
        print(f"Public dir {path_to_public_dir} not found. Creating it right away...")
        os.mkdir(path_to_public_dir)

    generated_html_filename = f"{template_name}" + HTML_EXT
    generated_html_content = template.render(content=content)
    with open(os.path.join(path_to_public_dir, generated_html_filename), "w", encoding="utf-8") as gen_f:
        gen_f.write(generated_html_content)
        print(f"Successfully wrote content to {generated_html_filename}")