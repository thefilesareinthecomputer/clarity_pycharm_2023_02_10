# data_preprocessing


# Import the necessary libraries, such as pandas and os:


import pandas as pd
import os
import openpyxl
import csv

# create a list of all the files in the data directories. There are around 100 files, the files have various names, all unique, and are within the directories /files/data_files/purchases/ and /files/data_files/sales/ and /files/data_files/variances/


directories = ['data_files/purchases', 'data_files/sales', 'data_files/variances']

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
