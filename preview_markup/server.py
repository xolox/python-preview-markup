# Simple Flask based HTTP server for the preview-markup program.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: April 3, 2015
# URL: https://github.com/xolox/python-preview-markup

# Standard library modules.
import random
import webbrowser

# External dependencies.
from flask import Flask, Markup, render_template

# Modules included in our package.
from preview_markup.converter import convert_to_html, extract_document_title

# Initialize the Flask application.
app = Flask('preview_markup')

def start_webserver(input_file):
    """Simple shortcut to start Flask's development server."""
    host = '127.0.0.1'
    # Pick a random "ephemeral" port number that's (most likely) not in use. See
    # also: http://en.wikipedia.org/wiki/Port_(computer_networking)#Common_port_numbers
    port = random.randint(49152, 65535)
    webbrowser.open('http://%s:%i' % (host, port))
    # Here is a nasty way to communicate the document that is to be rendered
    # from the user input (explicit or implicit command line argument) to the
    # Flask application.
    app.config['INPUT_FILE'] = input_file
    # Start the Flask development webserver (we don't need high performance or
    # anything like that, so this will do fine for now).
    app.run(host=host, port=port)

@app.route('/')
def index():
    """Flask view to render live previews of Markdown/reStructuredText documents."""
    head, body = convert_to_html(app.config['INPUT_FILE'])
    return render_template('preview.html',
                           title=extract_document_title(body),
                           head=Markup(head),
                           body=Markup(body))
