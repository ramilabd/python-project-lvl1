install:
	poetry install

run:
	poetry run brain-games

#test:
#	poetry run pytest hexlet_python_package tests

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck lint    # add a test later

build: check
	poetry build

publish: check
	poetry build
	poetry publish -r testpypi

.PHONY: install test lint selfcheck check build
