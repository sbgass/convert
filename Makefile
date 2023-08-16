
.PHONY: install test clean data

install:
	pip install -e . --index-url https://pypi.python.org/simple

test: data
	pytest -svv test/

clean:
	rm -rf .pytest_cache __pycache__ src/*.egg-info test/__pycache__  test/data/

data:
	python test/generate_test_data.py