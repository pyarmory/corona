import asyncio
import argparse

from corona import setup, snap


def main(argv=None):
    evt_loop = asyncio.get_event_loop()
    handlers = {
        'setup': setup.command,
        'snap': snap.command,
    }

    parser = setup_argparse()
    arguments = parser.parse_args(argv)

    return evt_loop.run_until_complete(handlers[arguments.command](arguments))


def setup_argparse():
    parser = argparse.ArgumentParser('Website Screenshot CLI Utility')
    subparsers = parser.add_subparsers()
    subparsers.required = True
    subparsers.dest = 'command'

    _ = subparsers.add_parser('setup', help='Downloads required browser')
    ss_parser = subparsers.add_parser('snap', help='Takes a screenshot')
    ss_parser.add_argument('url', type=str, help='Website URL to screenshot')
    ss_parser.add_argument('filename', type=str, help='Path where to save the screenshot')
    ss_parser.add_argument('--viewport-width', type=int, default=1280, help='Browser Width')
    ss_parser.add_argument('--viewport-height', type=int, default=1024, help='Browser Height')
    ss_parser.add_argument('--pyscript', type=str, help='Path to Python extension script')
    ss_parser.add_argument('--auth-username', type=str, help='Basic Auth Username')
    ss_parser.add_argument('--auth-password', type=str, help='Basic Auth Password')
    ss_parser.add_argument('--ignore-http-errors', action='store_true', default=False)
    ss_parser.add_argument('--disable-sandbox', action='store_true', default=False)


    return parser
