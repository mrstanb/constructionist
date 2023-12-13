import http.server
import socketserver
import os
from .utils import PUBLIC_DIR

def http_server_from_dir(directory):
    def _init(self, *args, **kwargs):
        return http.server.SimpleHTTPRequestHandler.__init__(self, *args, directory=self.directory, **kwargs)
    return type(f'HandlerFrom<{dir}>',
                (http.server.SimpleHTTPRequestHandler,),
                {'__init__': _init, 'directory': directory})

def serve(dir, port):
    dir = os.path.join(dir, PUBLIC_DIR)
    with socketserver.TCPServer(("", port), http_server_from_dir(dir)) as httpd:
        print("Serving site at port", port)
        httpd.serve_forever()