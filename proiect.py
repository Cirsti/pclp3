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

#Task_2
supravietuitori_percentage = my_file['Survived'].mean() * 100
nesupravietuitori_percentage = 100 - supravietuitori_percentage

class_percentage = my_file['Pclass'].value_counts(normalize='True') * 100
b_f_percentage = my_file['Sex'].value_counts(normalize='True') * 100
#metoda .value_counts() calculeaza de cate ori apare fiecare valoare din coloana respectiva
#normalize='True' transforma numarul de valori intr-o proportie
fig, axs = matplotlib.pyplot.subplots(1, 3, figsize=(18, 6))
axs[0].bar(['Supraviețuitori', 'Non-Supraviețuitori'], [supravietuitori_percentage, nesupravietuitori_percentage], color=['blue', 'orange'])
axs[1].bar(class_percentage.index, class_percentage.values, color=['blue', 'yellow', 'red'])
axs[2].bar(b_f_percentage.index, b_f_percentage.values, color=['lime', 'chocolate'])
#primul parametru reprezinta numele pentru label uri, al doilea reprezinta procentajele folosite in chart
#al treilea este array ul de culori
fig.savefig('grafic_task_2.png')

