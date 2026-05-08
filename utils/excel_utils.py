import pandas as pd
import os

def ensure_excel(path: str, headers: list):
    """Create an Excel file with the correct headers if it doesn't exist."""
    if not os.path.exists(path):
        df = pd.DataFrame(columns=headers)
        df.to_excel(path, index=False)

def load_excel(path: str) -> pd.DataFrame:
    """Load an Excel file into a DataFrame."""
    return pd.read_excel(path)

def save_excel(path: str, df: pd.DataFrame):
    """Save a DataFrame back to Excel."""
    df.to_excel(path, index=False)
