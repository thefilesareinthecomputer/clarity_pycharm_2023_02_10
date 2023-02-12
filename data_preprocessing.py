import pandas as pd
import os
import openpyxl
import csv

directories = ['data_files/purchases/', 'data_files/sales/', 'data_files/variances/']

def create_dataframe(directories):
    dataframes = []
    for directory in directories:
        for filename in os.listdir(directory):
            if filename.endswith(".xlsx"):
                file_path = os.path.join(directory, filename)
                df = pd.read_excel(file_path)
                dataframes.append(df)
    return pd.concat(dataframes)

df = create_dataframe(directories)

df.dropna(inplace=True)
