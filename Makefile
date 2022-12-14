# Environment =================================================================
.PHONY: environment
## create virtual environment for hierarchical-conf
environment:
	@pyenv install -s 3.7.3
	@pyenv virtualenv 3.7.3 hierarchical-conf
	@pyenv local hierarchical-conf
	@PYTHONPATH=. python -m pip install --upgrade pip

.PHONY: requirements-test
## install test requirements
requirements-test:
	@PYTHONPATH=. python -m pip install -r requirements.test.txt

.PHONY: requirements-lint
## install lint requirements
requirements-lint:
	@PYTHONPATH=. python -m pip install -r requirements.lint.txt

.PHONY: requirements-dev
## install development requirements
requirements-dev:
	@PYTHONPATH=. python -m pip install -U -r requirements.dev.txt

.PHONY: requirements-minimum
## install prod requirements
requirements-minimum:
	@PYTHONPATH=. python -m pip install -U -r requirements.txt

.PHONY: requirements-all
## install all requirements
requirements-all: requirements-test requirements-lint requirements-dev requirements-minimum

.PHONY: requirements-docs
## install docs requirements
requirements-docs:
	@PYTHONPATH=. python -m pip install -r docs/requirements.docs.txt

# Test ========================================================================

.PHONY: tests
## run all unit and integration tests with coverage report
tests:
	@python -m pytest -W ignore::DeprecationWarning --cov-config=.coveragerc --cov=hierarchical_conf --cov-report term --cov-report html:htmlcov --cov-report xml:coverage.xml tests
	@python -m coverage xml -i

.PHONY: unit-tests
## run unit tests with coverage report
unit-tests:
	@echo ""
	@echo "Unit Tests"
	@echo "=========="
	@echo ""
	@python -m pytest -W ignore::DeprecationWarning --cov-config=.coveragerc --cov-report term --cov-report html:unit-tests-cov --cov=hierarchical_conf --cov-fail-under=90 tests/unit

.PHONY: integration-tests
## run integration tests with coverage report
integration-tests:
	@echo ""
	@echo "Integration Tests"
	@echo "================="
	@echo ""
	@python -m pytest -W ignore::DeprecationWarning --cov-config=.coveragerc --cov-report term --cov-report xml:integration-tests-cov.xml --cov=hierarchical_conf --cov-fail-under=60 tests/integration

# Style & Lint ================================================================

.PHONY: style-check
## run code style checks with black
style-check:
	@echo ""
	@echo "Check Style"
	@echo "================"
	@echo ""
	@python -m black --check --exclude="build/|buck-out/|dist/|_build/|pip/|env/|\.pip/|\.git/|\.hg/|\.mypy_cache/|\.tox/|\.venv/|cmake*" . && echo "\n\nSuccess\n" || (echo "\n\nFailure\n\nRun \"make apply-style\" to apply style formatting to your code\n" && exit 1)
	@python -m flake8 --config=setup.cfg hierarchical_conf/

.PHONY: type-check
## run static type checks
type-check:
	@echo ""
	@echo "Mypy"
	@echo "===="
	@echo ""
	@python -m mypy hierarchical_conf

.PHONY: checks
## run all code checks
checks: style-check type-check

.PHONY: apply-style
## run black to fix code style
apply-style:
	@python -m black -t py36 --exclude="build/|buck-out/|dist/|_build/|pip/|env/|\.pip/|\.git/|\.hg/|\.mypy_cache/|\.tox/|\.venv/" .

# Packaging ===================================================================

.PHONY: version
## dump package name into VERSION env variable and show
version:
	@export VERSION=$(grep __version__ setup.py | head -1 | cut -d \" -f2 | cut -d \' -f2)
	@$(info VERSION is [${VERSION}])

.PHONY: package-name
## dump package name into PACKAGE_NAME env variable and show
package-name:
	@PACKAGE_NAME=$(grep __package_name__ setup.py | head -1 | cut -d \" -f2 | cut -d \' -f2 | sed 's/.*/&${build}/')
	@echo $PACKAGE_NAME

.PHONY: package
## build package wheel
package:
	@PYTHONPATH=. python -m setup sdist bdist_wheel

# Documentation ===============================================================

.PHONY: update-docs
## update project API docs
update-docs:
	cd ./docs; rm -rf source/hierarchical_conf.*
	cd ./docs; sphinx-apidoc -T -E -o source/ ../hierarchical_conf
	cd ./docs; make coverage

.PHONY: docs
## generate docs to local test
docs:
	cd ./docs; make clean
	cd ./docs; make html

# Other ===================================================================

.PHONY: clean
## clean unused artifacts
clean:
	@find ./ -type d -name 'dist' -exec rm -rf {} +;
	@find ./ -type d -name 'build' -exec rm -rf {} +;
	@find ./ -type d -name 'hierarchical_conf.egg-info' -exec rm -rf {} +;
	@find ./ -type d -name 'htmlcov' -exec rm -rf {} +;
	@find ./ -type d -name '*-tests-cov' -exec rm -rf {} +;
	@find ./ -type d -name '.pytest_cache' -exec rm -rf {} +;
	@find ./ -type d -name 'spark-warehouse' -exec rm -rf {} +;
	@find ./ -type d -name 'metastore_db' -exec rm -rf {} +;
	@find ./ -type d -name '.ipynb_checkpoints' -exec rm -rf {} +;
	@find ./ -type d -name 'coverage.xml' -exec rm -rf {} +;
	@find ./ -type f -name 'coverage-badge.svg' -exec rm -f {} \;
	@find ./ -type f -name '.coverage' -exec rm -f {} \;
	@find ./ -type f -name '*derby.log' -exec rm -f {} \;
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*.pyo' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')