import pandas as pd

def save_to_csv(dataframe, file_path):
    dataframe.to_csv(file_path, index=False, encoding='utf-8-sig')