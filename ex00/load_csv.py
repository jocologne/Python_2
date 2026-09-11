import os
import pandas as pd


def load(path: str):
    """Load csv dataset from given path"""
    try:
        if not isinstance(path, str):
            raise AssertionError("Path invalid")
        if not path.lower().endswith(".csv"):
            raise AssertionError("Format supported is CSV")
        if not os.path.exists(path):
            raise AssertionError(f"File not found: {path}")
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as error:
        print(f"Error: {error}")
        return None
