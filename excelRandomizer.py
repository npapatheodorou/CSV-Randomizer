"""
OPEN YOUR TERMINAL AND
pip install tkintertable (if using linux, also apt-get install python3-tk)
pip install numpy
pip install pandas
"""

from tkinter import filedialog
from tkinter import *
import numpy as np
import pandas as pd
import os

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
path, fileName = os.path.split(root.filename)
root.destroy()

inputFile = path + '/' + fileName
splittedFileName = inputFile.split(".")
outputFile = splittedFileName[0] + 'Randomized' + '.' + splittedFileName[1]

df = pd.read_csv(inputFile, header=0,dtype=object,na_filter=False)
df.reindex(np.random.permutation(df.index)).to_csv(outputFile, sep=',',encoding = 'utf-8-sig',index = False)