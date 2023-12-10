import os

ASSETS_DIR = "_assets"
CONTENT_DIR = "_content"
PUBLIC_DIR = "_public"
TEMPLATES_DIR = "_templates"

def has_constructionist_site_layout(dir):
    dir = os.path.realpath(dir)
    if not os.path.exists(dir) or not os.path.exists(dir):
        return False
    sub_dirs = os.listdir(dir)
    for site_dir in [ASSETS_DIR, CONTENT_DIR, PUBLIC_DIR, TEMPLATES_DIR]:
        if not os.path.isdir(os.path.join(dir, site_dir)) or not site_dir in sub_dirs:
            return False
    return True