import argparse
import markdown
import os
import glob

from .commands import clean, create, construct, serve

def main():
    arg_parser = argparse.ArgumentParser(
        prog="constructionist",
        description="A Static Site Generator in Python"
    )

    subparsers = arg_parser.add_subparsers(title="Commands", dest="command")

    dir_arg_template = {
        "dest": "dir",
        "nargs": "?",
        "type": str,
        "default": "."
    }

    create_parser = subparsers.add_parser("create", help="Create a new static site")
    create_parser.add_argument(
        **dir_arg_template,
        help="The directory to create the static site in (defaults to \".\")")

    clean_parser = subparsers.add_parser("clean", help="Clean up and delete all generated HTML files for a static site")
    clean_parser.add_argument(
        **dir_arg_template,
        help="The directory of the static site (defaults to \".\")")

    construct_parser = subparsers.add_parser("construct", help="Build a static site")
    construct_parser.add_argument(
        **dir_arg_template,
        help="The directory of the static site (defaults to \".\")")
    
    serve_parser = subparsers.add_parser("serve", help="Build and serve a static site on a local port")
    serve_parser.add_argument(
        **dir_arg_template,
        help="The directory of the static site (defaults to \".\")")
    
    serve_parser.add_argument(
        "port",
        nargs="?",
        type=int,
        default=8080,
        help="The port to serve the static site on (default to 8080)")


    args = arg_parser.parse_args()
    
    match args.command:
        case 'clean':
            command = clean.Clean(args.dir)
            command.process()
        case 'create':
            command = create.Create(args.dir)
            command.process()
        case 'construct':
            command = construct.Construct(args.dir)
            command.process()
        case 'serve':
            command = serve.Serve(args.dir, args.port)
            command.process()

if __name__ == '__main__':
    main()