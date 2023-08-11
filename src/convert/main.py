from pathlib import Path
from typing import Type 

import pyarrow.parquet as pq
import pandas as pd
import typer 

app = typer.Typer() 

def convert(filename:Type[Path]):
    """ """
    parquet_table = pq.read_table(filename)
    df = parquet_table.to_pandas()
    df.to_csv(csv_file_path, index=False)


def iterate_files(directory_path:Type[Path], recursive:bool):
    """ """
    directory = Path(directory_path)
    for filepath in directory.rglob('*'):
        if filepath.is_file() and filepath.suffix == ".parquet":
            convert(filepath)

@app.command(help="This is the help menu")
def main(target_dir:str = ".", recursive:bool=True):
    print(target_dir)
    iterate_files(target_dir, recursive)


def cli():
    print("hello")
    app()

if __name__ == "__main__":
    cli() 