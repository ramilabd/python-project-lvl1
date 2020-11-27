install:
	poetry install

package-install: build
	python3 -m pip install --user dist/*.whl

run:
	poetry run brain-games

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

publish: check
	poetry build
	poetry publish -r testpypi

.PHONY: install test lint selfcheck check build
