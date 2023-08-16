import pandas as pd
import numpy as np
from pathlib import Path 

DATA_DIR = Path(__file__).parent / "data"

def generate_test_data()->str: 
    """Creates a parquet file in test/data/ and returns the filename"""
    columns = ["Column1", "Column2", "Column3", "Column4", "Column5", "Column6"]

    # Set the seed for reproducibility
    np.random.seed(42)

    # Create a DataFrame with random numbers
    num_rows = 20
    num_columns = len(columns)

    data = np.random.rand(num_rows, num_columns)
    df = pd.DataFrame(data, columns=columns)
    df['Column2'] = "this is a string"
    df['Column1'] = 2
    df['Column1'] = df['Column1'].astype(np.int8)

    DATA_DIR.mkdir(parents=True,exist_ok=True)
    data_path = DATA_DIR / "data.parquet"
    df.to_parquet(data_path)
    return data_path

if __name__ == "__main__":
    generate_test_data()