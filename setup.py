from setuptools import setup

setup(
    name='convert',
    version='0.0.1',
    description="TODO",
    install_requires=[
        'typer'
    ],
    entry_points={
        'console_scripts': [
            'convert = convert.main:cli',
        ]
    }
)