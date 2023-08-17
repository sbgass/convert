from pathlib import Path
from typing import Type 

import pyarrow.parquet as pq
import pandas as pd
import typer 
import json 

app = typer.Typer() 

def split_data_from_metadata(filename:Type[Path])->None:
    """ Saves parquet data to CSV and metadata to JSON"""
    parquet_file = pq.ParquetFile(filename)
    metadata_summary = parquet_file.metadata.to_dict()
    with open(filename.with_stem(filename.stem + "_metadata").with_suffix(".json"), "w") as f:
        json.dump(metadata_summary, f, indent=4, sort_keys=True,  default=str) 

    df = pd.read_parquet(filename)
    df.to_csv(filename.with_suffix(".csv"), index=False)


def convert_all_parquet_files(directory_path:Type[Path])-> None:
    """ Calls convert_pq_to_csv() on all parquet files in the directory """
    directory = Path(directory_path)
    for filepath in directory.rglob('*'):
        if filepath.is_file() and filepath.suffix == ".parquet":
            split_data_from_metadata(filepath)

@app.command(help="This is the help menu")
def main(target_dir:str = "./", recursive:bool=True):
    convert_all_parquet_files(target_dir)


def cli():
    app()

if __name__ == "__main__":
    cli() 