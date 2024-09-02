from setuptools import setup

setup(
    name='convert',
    version='0.0.1',
    description="Conversion CLI tool for parquet files",
    install_requires=[
        'typer',
        'pyarrow>=17.0.0'
    ],
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'convert = convert.main:cli',
        ]
    }
)