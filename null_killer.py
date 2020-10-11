# import bibl
import pandas as pd
import csv

# Function read all data from csv(with delimiter '|') and clean up all ';' signs
def Opener(file):
    df = pd.read_csv(file, delimiter='|', comment=';')
    return df

# Function fill all "NaN" in columns which have 'float64' type
def fill_NaN(df):    
    for i in range(df.shape[1]):
        if df.dtypes[i] == 'float64':
            column = df.dtypes.index[i]
            df[column].fillna(0, inplace=True)
    return df

# Function fill all "NaN" in columns which have 'float64' type
def Loader(df):
    df.to_csv(file, sep = '|', mode='w', index_label=False, index=False, header=True)      

# names of files in your derectory. you can input as many names as you wish(in '' and seporated by ',')
files = [r'Path#1', r'Path#2']

# this is a cycle which take name from names array and execute funtions
for file in files:
    step1 = Opener(file)
    step2 = fill_NaN(step1)
    Loader(step2)
