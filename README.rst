preview-markup: Live preview Markdown and reStructuredText files
================================================================

The ``preview-markup`` program takes a text file with lightweight markup
(Markdown_ and reStructuredText_ are supported) and shows a live preview of the
markup rendered to HTML in your web browser. When you save your text file the
preview is automatically updated within a couple of seconds. That's all there
is to it!

.. contents::
   :local:

Installation
------------

The ``preview-markup`` program is written in Python and is available on PyPI_
which means installation should be as simple as::

  $ pip install preview-markup

There's actually a multitude of ways to install Python packages (e.g. the `per
user site-packages directory`_, `virtual environments`_ or just installing
system wide) and I have no intention of getting into that discussion here, so
if this intimidates you then read up on your options before returning to these
instructions ;-).

Getting started
---------------

To get started you simply run the command ``preview-markup``. If you give it a
filename as an argument then that file will be previewed, otherwise the
``README.md`` or ``README.rst`` file in the current working directory is
previewed.

If you want to run ``preview-markup`` in the background then you probably won't
appreciate the logging to the terminal that is enabled by default. In this case
I suggest you use the following command line::

  $ preview-markup -q &

The ``-q`` is short for ``--quiet`` and the ``&`` instructs your shell to run
the program in the background. If you want to kill the program later on just
run the ``fg`` command (this will bring the program back to the foreground) and
then press Control-C (this will kill the program).

Why this project?
-----------------

Different variations of ``preview-markup`` have lived in my private dotfiles
repository for years now (I track ``~/bin`` in my dotfiles repository). Over
those years the program has had several names and very similar yet slightly
different purposes. By the time I decided to clean up these "variations on a
similar theme" I was using several different shell and Python scripts working
together to do the same things that ``preview-markup`` now does. I decided to
merge, cleanup, document and publish that mess of Python and shell scripts for
multiple reasons:

1. I wanted to merge all of the features that I'd grown to appreciate into a
   single coherent piece of software that was easy and intuitive to use (and
   written in Python so I could more easily maintain it :-).

2. I wanted to manage the installation of that software as a Python package
   with properly specified dependencies where a single ``pip install`` was
   enough to get things going.

3. Last but not least: Given the effort I'd already put into it, it seemed a
   shame not to share my work with the world.

Similar projects
~~~~~~~~~~~~~~~~

I created ``preview-markup`` because I couldn't find a tool that provided live
previews of Markdown_ *and* reStructuredText_ markup and just because it was
fun to work on, however *this is clearly an itch that dozens of developers have
scratched over the years* :-). Here are some similar projects that I've run
into and/or used in the past:

`restview <https://mg.pov.lt/restview/>`_
 Live preview of reStructuredText_ files. A personal favorite of mine, simple
 and sweet, does exactly what is promises. Written in Python.

`markdown-live <https://github.com/mobily/markdown-live>`_
 Live preview of Markdown files. Written in JavaScript (using Node.js).

`github-markdown-preview <https://github.com/dmarcotte/github-markdown-preview>`_
 Live preview of Markdown files. Makes it an explicit goal to render things
 just like GitHub does. Written in Ruby.

Contact
-------

The latest version of ``preview-markup`` is available on PyPI_ and GitHub_. For
bug reports please create an issue on GitHub_. If you have questions,
suggestions, etc. feel free to send me an e-mail at `peter@peterodding.com`_.

License
-------

This software is licensed under the `MIT license`_.

© 2015 Peter Odding.

.. External references:
.. _GitHub: https://github.com/xolox/python-preview-markup
.. _Markdown: http://en.wikipedia.org/wiki/Markdown
.. _MIT license: http://en.wikipedia.org/wiki/MIT_License
.. _per user site-packages directory: https://www.python.org/dev/peps/pep-0370/
.. _peter@peterodding.com: peter@peterodding.com
.. _PyPI: https://pypi.python.org/pypi/preview-markup
.. _reStructuredText: http://en.wikipedia.org/wiki/ReStructuredText
.. _virtual environments: http://docs.python-guide.org/en/latest/dev/virtualenvs/
