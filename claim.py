#!/usr/bin/env python3

""" Text files created on DOS/Windows machines have different line endings than
    files created on Unix/Linux. DOS uses carriage return and new line ("\r\n")
    as a line ending, while Unix uses just new line ("\n"). The purpose of this
    script is to have a quick, on the go, shell friendly solution to convert one
    to the other.
"""

import sys
import argparse


def main():
    """ Removes error traceback clutter and converts files specified.
    """

    sys.tracebacklimit = 0
    args = commands()

    for filename in args.filenames:
        convert(filename, args.dos)


def commands():
    """ Sets up command line arguments and improper argument error handling.
    
        Returns:
            parser (object)
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-dos', action='store_true',
                        help="converts file to DOS")
    parser.add_argument('filenames', metavar='filename',
                        type=str, nargs='+', help="file to be converted")
    return parser.parse_args()


def convert(filename, flag):
    """ Converts the file's line endings appropriately.

        Args:
            filename (string): the file being converted
            flag (bool): defaults to UNIX. If flag is true, converts line endings to DOS
    """

    unix, dos = '\n', '\r\n'
    format = 'UNIX'

    with open(filename, 'rb') as f:
        content = f.read().decode('UTF-8')
        if flag:
            format = 'DOS'
            content = content.replace(unix, dos)
        else:
            content = content.replace(dos, unix)

    with open(filename, 'wb') as f:
        f.write(content.encode('UTF-8'))

    print("converting file '{}' to {} ...".format(filename, format))


if __name__ == '__main__':
    main()
