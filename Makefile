
.PHONY: install test clean

install:
	pip install -e . --index-url https://pypi.python.org/simple

test: 
	pytest -svv -m "unit" test/

clean:
	rm -rf .pytest_cache __pycache__ src/*.egg-info test/__pycache__ 