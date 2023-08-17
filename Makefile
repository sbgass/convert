
.PHONY: install install_test_env test clean data

install:
	pip install -e . --index-url https://pypi.python.org/simple

install_test_env:
	pip install -r test/env/requirements.txt --index-url https://pypi.python.org/simple

test: data
	pytest -svv test/

clean:
	rm -rf .pytest_cache __pycache__ src/*.egg-info test/__pycache__ src/convert/__pycache__ test/data/

data:
	python test/generate_test_data.py