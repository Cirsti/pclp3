import matplotlib.pyplot
import numpy as np
import pandas
import matplotlib
import seaborn

#Task_1
print("Task_1:")
my_file = pandas.read_csv('train.csv')
#functia shape returneaza nr de linii si coloane sub forma de tuple
nr_col = my_file.shape[0] #coloane
nr_lin = my_file.shape[1] #linii
data_types = my_file.dtypes #returneaza un series cu numele coloanele si data type ul din fiecare coloana
valorile_lipsa = my_file.isnull().sum()
#.isnull() creeaza un dataframe cu true / false pentru valori lipsa
#.sum() transforma df ul intr-un series si aduna acele valori de True
liniile_duplicate = my_file.duplicated().sum() #duplicated returneaza un series cu numele col si True / False

print(f'Nr_lin: {nr_lin}')
print(f'Nr_col: {nr_col}')
print(f'Nr linii duplicate: {liniile_duplicate}')
print(f'Nr valori lipsa:\n{valorile_lipsa}')
print(f'Data types:\n{data_types}')