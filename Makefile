.PHONY: help requirements requirements_test lint test run

APP := __MY_APP__
WORKON_HOME ?= .venv/$(APP)
VENV_ACTIVATE := $(WORKON_HOME)/bin/activate
PYTHON := ${WORKON_HOME}/bin/python3

.DEFAULT: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/\n\t/'

venv:	## create virtualenv
	@if [ ! -d "$(WORKON_HOME)" ]; then \
		virtualenv -p python3 $(WORKON_HOME); \
	fi

requirements:	## install requirements
requirements: venv
	@echo Install requirements
	@${PYTHON} -m pip install -r requirements.txt > /dev/null

requirements_test:	## install test requirements
requirements_test: requirements
	@echo Install test requirements
	@${PYTHON} -m pip install -r requirements_test.txt > /dev/null

lint:	## run pycodestyle
lint: requirements_test
	@echo Running linter
	@${PYTHON} -m pycodestyle ${APP} test
	@${PYTHON} -m flake8 ${APP} test
	@${PYTHON} -m mypy --ignore-missing-imports ${APP} test

test:	## run tests and show report
test: lint
	@echo Running tests
	@${PYTHON} -m coverage run -m unittest discover
	@${PYTHON} -m coverage report -m

run:	## run project
run: requirements
	${PYTHON} -m ${APP}
