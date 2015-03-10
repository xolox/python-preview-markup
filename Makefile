# Makefile for preview-markup.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: March 10, 2015
# URL: https://github.com/xolox/python-preview-markup

WORKON_HOME ?= $(HOME)/.virtualenvs
VIRTUAL_ENV ?= $(WORKON_HOME)/preview-markup
ACTIVATE = . $(VIRTUAL_ENV)/bin/activate

default:
	@echo 'Makefile for preview-markup'
	@echo
	@echo 'Usage:'
	@echo
	@echo '    make install    install the package in a virtual environment'
	@echo '    make reset      recreate the virtual environment'
	@echo '    make publish    publish changes to GitHub/PyPI'
	@echo '    make clean      cleanup all temporary files'
	@echo

install:
	test -d "$(VIRTUAL_ENV)" || virtualenv "$(VIRTUAL_ENV)"
	test -x "$(VIRTUAL_ENV)/bin/pip" || ($(ACTIVATE) && easy_install pip)
	test -x "$(VIRTUAL_ENV)/bin/pip-accel" || ($(ACTIVATE) && pip install pip-accel)
	$(ACTIVATE) && pip uninstall -y preview-markup || true
	$(ACTIVATE) && pip-accel install --editable .

reset:
	rm -Rf "$(VIRTUAL_ENV)"
	make --no-print-directory clean install

publish:
	git push origin && git push --tags origin
	make clean && python setup.py sdist upload

clean:
	rm -Rf *.egg *.egg-info build dist
	find -depth -type d -name __pycache__ -exec rm -Rf {} \;
	find -type f -name '*.pyc' -delete

.PHONY: default install reset publish clean
