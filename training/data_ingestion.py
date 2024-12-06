import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Loads data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("Data successfully loaded.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise