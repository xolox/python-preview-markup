# Easily preview text documents as HTML in a web browser.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: March 10, 2015
# URL: https://github.com/xolox/python-preview-markup

# Standard library modules.
import codecs
import logging
import os

# External dependencies.
from BeautifulSoup import BeautifulSoup
from docutils.core import publish_parts
from humanfriendly import Timer, format_size
from markdown import markdown

# Initialize a logger for this module.
logger = logging.getLogger(__name__)

# Known filename extensions for Markdown and reStructuredText files.
MARKDOWN_EXTENSIONS = ('.md', '.mkd', '.markdown')
RESTRUCTUREDTEXT_EXTENSIONS = ('.rst',)
SUPPORTED_EXTENSIONS = MARKDOWN_EXTENSIONS + RESTRUCTUREDTEXT_EXTENSIONS

def convert_to_html(filename, input_encoding='UTF-8'):
    """
    Convert a file with Markdown or reStructuredText markup to HTML.

    :param filename: The filename of the text file to convert (a string).
    :param encoding: The encoding of the text file (a string).
    :returns: The converted HTML (a string).
    """
    # Determine the filename extension.
    extension = get_filename_extension(filename)
    # Read the input file into a Unicode string.
    with codecs.open(filename, encoding=input_encoding) as handle:
        text = handle.read()
    # Convert the input file.
    timer = Timer()
    if extension in MARKDOWN_EXTENSIONS:
        logger.debug("Filename extension of input file (%s) indicates Markdown.", extension)
        html = markdown(text)
    elif extension in RESTRUCTUREDTEXT_EXTENSIONS:
        logger.debug("Filename extension of input file (%s) indicates reStructuredText.", extension)
        parts = publish_parts(source=text,
                              writer_name='html',
                              settings_overrides=dict(doctitle_xform=False))
        html = parts['html_body']
    else:
        msg = "Input file not supported! (filename extension %s not recognized)"
        raise ValueError(msg % extension)
    logger.debug("Converted %s input text to %s HTML in %s.",
                 format_size(len(text)), format_size(len(html)), timer)
    return html

def extract_document_title(html):
    """
    Extract the text of the first level one heading in a string of HTML.

    :param html: The HTML to extract the title from (a string).
    :returns: The extracted title (a string) or ``None``.
    """
    tree = BeautifulSoup(html, convertEntities=BeautifulSoup.ALL_ENTITIES)
    elements = tree.findAll('h1')
    if elements:
        return ''.join(elements[0].findAll(text=True))

def find_readme_file(directory):
    """
    Find a supported ``README.*`` in the given directory.

    :param directory: The pathname of a directory (a string).
    :returns: The filename of a readme file (a string).
    :raises: :py:exc:`AssertionError` when zero or more than one readme file is
             found.
    """
    matched_files = []
    for filename in os.listdir(directory):
        pathname = os.path.join(directory, filename)
        if os.path.isfile(pathname):
            extension = get_filename_extension(filename)
            if extension in SUPPORTED_EXTENSIONS:
                matched_files.append(pathname)
    assert len(matched_files) > 0, "Failed to find README!"
    assert len(matched_files) == 1, "Found more than one README file?!"
    return matched_files[0]

def get_filename_extension(filename):
    """
    Get the lowercase extension of a filename.

    :param filename: The filename to extract the extension from (a string).
    :returns: The lowercase filename extension (a string).
    """
    basename, extension = os.path.splitext(filename)
    return extension.lower()
