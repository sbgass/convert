from pathlib import Path
from typing import Type 

import pandas as pd
import typer 

app = typer.Typer() 

def create_csv_copy(filename:Type[Path])->None:
    """ """
    df = pd.read_parquet(filename)
    df.to_csv(filename.with_suffix(".csv"), index=False)


def convert_all_parquet_files(directory_path:Type[Path])-> None:
    """ Calls convert_pq_to_csv() on all parquet files in the directory """
    directory = Path(directory_path)
    for filepath in directory.rglob('*'):
        if filepath.is_file() and filepath.suffix == ".parquet":
            create_csv_copy(filepath)

@app.command(help="This is the help menu")
def main(target_dir:str = "./", recursive:bool=True):
    convert_all_parquet_files(target_dir)


def cli():
    app()

if __name__ == "__main__":
    cli() 