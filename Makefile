install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run python3 -m pytest --cov-report xml --cov=test_files

lint:
	poetry run flake8 gendiff