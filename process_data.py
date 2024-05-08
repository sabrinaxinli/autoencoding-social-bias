import pandas as pd
import tarfile
import os
import matplotlib.pyplot as plt
import seaborn as sns
import math

def extract_tgz(tgz_path, extract_path):
    try:
        with tarfile.open(tgz_path, 'r:gz') as tar:
            tar.extractall(path=extract_path)
        return True
    except Exception as e:
        print(f"Error occurred while extracting the file: {e}")
        return False

def read_tgz_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")
        return None

tgz_path = '/Users/sabrina/Computational Social Science/final-project/SBIC.v2.tgz'
extract_path = '/Users/sabrina/Computational Social Science/final-project/extracted'

# Extract the tgz file

# Assuming there is a specific file you want to read, you will need to know the name of this file
data_file_path = os.path.join(extract_path, 'SBIC.v2.tst.csv') # Replace 'your_data_file.csv' with the actual file name

if not os.path.exists(data_file_path):
    extract_tgz(tgz_path, extract_path)

tgz_data = read_tgz_data(data_file_path)

if tgz_data is not None:
    print(f"Data len: {len(tgz_data)}")
    print("Data stats:")
    print(tgz_data.describe())
    
    

