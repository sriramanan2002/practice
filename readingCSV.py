#write a python program to read a csv file named test.cv using magic methods __next__ & __iter__ and implement exception handling


import pandas as pd

try:
    a = pd.read_csv("test.csv")
    print(a)
except FileNotFoundError:
    print("The file was not found!,\nEnter the file name properly (its case sensitive)!!")



