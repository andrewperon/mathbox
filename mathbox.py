import time
import pandas as pd
from tkinter import filedialog as fd

# create a tkinter dialogue to select a CSV file, and limit filetypes

csvfiletype = (
    ('CSV files', '*.csv'),
    ('text files', '*.txt')
)

filename = fd.askopenfilename(
    title='Choose a CSV',
    filetypes=csvfiletype
)

# debug verify selected CSV is correct

print(filename)

# use input CSV filepath to ingest CSV contents into dataframe

df = pd.read_csv(filename, index_col=0)

# debug print dataframe contents

print(df)