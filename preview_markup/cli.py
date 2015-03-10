# Command line interface for the live-preview program.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: March 9, 2015
# URL: https://github.com/xolox/python-preview-markup

"""
Usage: preview-markup [OPTIONS] [TEXT_FILE]

Supported options:

  -v, --verbose  make more noise
  -q, --quiet    make less noise
  -h, --help     show this message and exit
"""

# Standard library modules.
import getopt
import logging
import os
import sys

# External dependencies.
import coloredlogs

# Modules included in our package.
from preview_markup.converter import find_readme_file
from preview_markup.server import start_webserver

# Initialize a logger for this module.
logger = logging.getLogger(__name__)

def main():
    """Command line interface for the ``preview`` program."""
    # Initialize logging to the terminal.
    coloredlogs.install()
    # Parse the command line arguments.
    try:
        options, arguments = getopt.getopt(sys.argv[1:], 'vqh', [
            'verbose', 'quiet', 'help'
        ])
        for option, value in options:
            if option in ('-v', '--verbose'):
                coloredlogs.increase_verbosity()
            elif option in ('-q', '--quiet'):
                coloredlogs.decrease_verbosity()
            elif option in ('-h', '--help'):
                usage()
                return
            else:
                assert False, "Unhandled option!"
        if not arguments:
            arguments = ['.']
        elif len(arguments) > 1:
            raise Exception("Only one positional argument may be given!")
    except Exception as e:
        print("Failed to parse command line arguments! (%s)" % e)
        print("")
        usage()
        sys.exit(1)
    try:
        if os.path.isdir(arguments[0]):
            start_webserver(find_readme_file(arguments[0]))
        elif os.path.isfile(arguments[0]):
            start_webserver(arguments[0])
        else:
            raise Exception("Input doesn't exist!")
    except KeyboardInterrupt:
        sys.stderr.write('\r')
        logger.error("Interrupted by Control-C, terminating ..")
        sys.exit(1)
    except Exception:
        logger.exception("Encountered an unhandled exception, terminating!")
        sys.exit(1)

def usage():
    """Print a friendly usage message to the terminal."""
    print(__doc__.strip())
