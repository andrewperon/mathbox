from time import sleep
from os import system,name
import pandas as pd
from tkinter import filedialog as fd

# create a clear function

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# create value for numeric table

numerical = 1

# create a tkinter dialogue to select a CSV file, and limit filetypes
# uses user home directory for initial file dialog

csvfiletype = (
    ('CSV files', '*.csv'),
    ('text files', '*.txt')
)

filename = fd.askopenfilename(
    title='Choose a CSV',
    filetypes=csvfiletype,
    initialdir='~/'
)

# debug verify selected CSV is correct

print(filename)

numerical = input('Is this dataset 100% Numeric?\n(Input 1 for Yes): ')

# use input CSV filepath to ingest CSV contents into dataframe

df = pd.read_csv(filename, index_col=0)

# check for data type/clean dataframe and remove NaN values

if numerical == 1:
    mb = df.dropna()
else:
    mb = df

# debug print dataframe contents

print(mb)

sleep(1)
clear()

mbMean = mb.mean(axis=0)

print('Data Frame Statistics:\n')
sleep(1)

print(mb.info())
print(mbMean)