.DEFAULT_GOAL := help

# Determine this makefile's path.
# Be sure to place this BEFORE `include` directives, if any.
SHELL := $(shell which bash)
DEFAULT_BRANCH := main
VERSION := 0.0.0
COMMIT := $(shell git rev-parse HEAD)
CDK := node_modules/.bin/cdk

CURRENT_BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
DEFAULT_BRANCH := main
HYBRID_ENV := sandbox
PYTHON_VERSION := 3.10.6
CDK_VERSION := 2.70.0

help: ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

clean-venv: ## re-create virtual env
	[[ -e .venv ]] && rm -rf .venv; \
	( \
       source scripts/enable_pyenv.sh; \
       pyenv local $(PYTHON_VERSION); \
       python3 -m venv .venv; \
       source .venv/bin/activate; \
       pip install --upgrade pip setuptools; \
       pip install -r requirements.txt; \
    )

install-pyenv: ## install pyenv
	-git clone https://github.com/pyenv/pyenv.git ~/.pyenv
	
pylint: ## run pylint on python files
	( \
       . .venv/bin/activate; \
       git ls-files '*.py' | xargs pylint --max-line-length=90; \
    )

black: ## use black to format python files
	( \
       . .venv/bin/activate; \
       git ls-files '*.py' |  xargs black --line-length=79; \
    )

black-check: ## use black to format python files
	( \
       . .venv/bin/activate; \
       git ls-files '*.py' |  xargs black --check --line-length=79; \
    )

shellcheck: ## use black to format python files
	( \
       git ls-files 'scripts/*.sh' |  xargs shellcheck --format=gcc; \
    )

unit-test: ## run test that don't require deployed resources
	( \
       source .venv/bin/activate; \
       python3 -m pytest -v -m "unit" tests/; \
    )

unit-update_golden: ## update test golden files using the current actual results
	( \
       source .venv/bin/activate; \
       python3 -m pytest -v -m "unit" tests/ --update_golden; \
    )

sandbox-test: ## run test that require sandbox credentials
	( \
       source .venv/bin/activate; \
       python3 -m pytest -v -m "sandbox" tests/; \
    )

sandbox-update_golden: ## update test golden files using the current actual results
	( \
       source .venv/bin/activate; \
       python3 -m pytest -v -m "sandbox" tests/ --update_golden; \
    )

dev-test: ## run test that require sandbox credentials
	( \
       source .venv/bin/activate; \
       python3 -m pytest -v -m "dev" tests/; \
    )

dev-update_golden: ## update test golden files using the current actual results
	( \
       source .venv/bin/activate; \
       python3 -m pytest -v -m "dev" tests/ --update_golden; \
    )


static: shellcheck black pylint unit-test ## run all static checks

clean-cache: ## clean python adn pytest cache data
	@find . -type f -name "*.py[co]" -delete -not -path "./.venv/*"
	@find . -type d -name __pycache__ -not -path "./.venv/*" -exec rm -rf {} \;
	@find . -name ".pytest_cache" -exec rm -rf {} \;

git-status: ## require status is clean so we can use undo_edits to put things back
	@status=$$(git status --porcelain); \
	if [ ! -z "$${status}" ]; \
	then \
		echo "Error - working directory is dirty. Commit those changes!"; \
		exit 1; \
	fi

.PHONY: build static test artifact	
