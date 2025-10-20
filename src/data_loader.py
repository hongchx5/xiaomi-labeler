import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)