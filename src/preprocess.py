import pandas as pd
import os

# Paths
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
RAW_FILES = [
    "GreenAI_Dataset.csv",
    "farmer_advisor_dataset.csv",
    "market_researcher_dataset.csv"
]

PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)

def load_data(file_path):
    """Load a CSV into a pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Loaded {file_path} with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except FileNotFoundError:
        print(f"⚠️ File not found: {file_path}")
        return pd.DataFrame()

def clean_data(df):
    """Basic preprocessing: drop duplicates, handle missing values."""
    if df.empty:
        return df
    
    df = df.drop_duplicates()
    df = df.fillna(method="ffill").fillna(method="bfill")  # forward/backward fill
    return df

def preprocess():
    for file in RAW_FILES:
        raw_path = os.path.join(DATA_DIR, file)
        df = load_data(raw_path)

        if not df.empty:
            df_clean = clean_data(df)

            save_path = os.path.join(PROCESSED_DIR, f"processed_{file}")
            df_clean.to_csv(save_path, index=False)
            print(f"💾 Saved cleaned file: {save_path}")

if __name__ == "__main__":
    preprocess()
