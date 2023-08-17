# convert
pip installable CLI to convert parquet files to human-readable formats.  

## Installation  
This package isn't published on pypi, but is installable from source. The package was written in python 3.11 and should be compatible with python >=3.8. 
### Install from source 
From inside the top-level repo directory, run `pip install .`

For Developers: 

Phony Makefile commands have are available for developer convenience. To install the package in edittable mode, run `make install` in the same directory as the `Makefile`. 

## Using the CLI 

The CLI defaults to the current directory. To run the main function, simply run `convert` with no arguments to convert all parquet files in the current directory into CSVs of the data and JSONs of the metadata. 

## Runs Test

Test data is generated at test-time for all unit level tests. To run the tests, first install the test environment by runnning `make install_test_env` in the same virtual environment that you installed the package. Then run the tests with `make test`. 

## Clean 
To clean the repo after installing and running tests, run `make clean`. This will tidy up any cached data left behind by the tests. 