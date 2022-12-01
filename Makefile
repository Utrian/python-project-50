install:
	poetry install

build:
	poetry build

BI:
	poetry build
	poetry install
	python3 -m pip install dist/*.whl

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	python -m pip install --force-reinstall dist/*.whl

.PHONY: all gendiff clean
gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

coverage-missing:
	poetry run pytest --cov-report term-missing --cov=gendiff
