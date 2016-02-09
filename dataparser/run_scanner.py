import argparse
import sys
from queue.scanner import Scanner


def scan_all(workspace, extension, db_path,
             module_search_path):
    for path in module_search_path:
        sys.path.append(path)
    scanner = Scanner()
    scanner.scan(
        workspace=workspace,
        ext=extension,
        db_path=db_path
    )


if __name__ == '__main__':
    c_parser = argparse.ArgumentParser(
        description='Scanning Robot data from system Python')
    c_parser.add_argument(
        'mode',
        choices=['all', 'single'],
        help='Scanning mode: all or single'
    )
    c_parser.add_argument(
        '--workspace',
        help='Root of the folder where data parsing is performed'
    )
    c_parser.add_argument(
        '--extension',
        help='File extension for Robot data, example "robot" or "txt"'
    )
    c_parser.add_argument(
        '--db_path',
        required=True,
        help='Folder where scanning result is saved'
    )
    c_parser.add_argument(
        '--module_search_path',
        nargs='*',
        help='List of paths where libraries are searched when scanning')
    args = c_parser.parse_args()
    module_search_path = []
    if args.module_search_path:
        module_search_path = args.module_search_path
    if args.mode == 'all':
        if not args.workspace:
            raise ValueError('--workspace is needed with mode: {0}'.format(
                args.mode))
        elif not args.extension:
            raise ValueError('--extension is needed with mode: {0}'.format(
                args.mode))
        else:
            scan_all(
                args.workspace,
                args.extension,
                args.db_path,
                module_search_path)
    elif args.mode == 'single':
        """To scan single file"""
        raise ValueError('Not implemented')
