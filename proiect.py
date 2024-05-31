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

#Task_3
coloane_cu_numere = my_file.select_dtypes(include=['int64', 'float64'])
nr = 1
for coloana in coloane_cu_numere:
    matplotlib.pyplot.figure(figsize=(8, 6)) #8 in latime si 6 in inaltime
    matplotlib.pyplot.figure(figsize=(8, 6))
    matplotlib.pyplot.hist(my_file[coloana], bins=20, color='skyblue', edgecolor='black')
    matplotlib.pyplot.title(f"{coloana}")
    matplotlib.pyplot.xlabel('Valoare')
    matplotlib.pyplot.ylabel('Frecvență')
    matplotlib.pyplot.savefig(f"grafic_task_3_{nr}.png")
    nr += 1

#Task_4
print("\nTask_4:")
coloane_cu_valori_lipsa = my_file.columns[my_file.isnull().any()].tolist()
#my_file.isnull().any() seteaza cu True coloanele care au elemente lipsa
#pasand valoarea ca argument la my_file.columns, selectam doar acele coloane din lista de coloane
#metoda .tolist() transforma lista pandas intr-o lista python
for coloana in coloane_cu_valori_lipsa:
    valori_lipsa = my_file[coloana].isnull().sum()
    valori_lipsa_percentage = my_file[coloana].isnull().mean() * 100
    print(f'Col "{coloana}": {valori_lipsa} valori lipsa, procentaj {valori_lipsa_percentage:.2f}%')
for coloana in coloane_cu_valori_lipsa:
    supravietuitori = my_file[my_file['Survived'] == 1][coloana].isnull().mean() * 100
    nonsupravietuitori = 100 - supravietuitori
    print(f'Col "{coloana}": supravietuitori: {supravietuitori:.2f}%')
    print(f'Col "{coloana}": nonsupravietuitori: {nonsupravietuitori:.2f}%')

#Task_5
varsta_maxima = my_file['Age'].max()
labels = ['0-20', '21-40', '41-60', '61+']
bins = [0, 20, 40, 60, varsta_maxima]
my_file['categorie-varsta'] = pandas.cut(my_file['Age'], bins=bins,  labels = labels)
#metoda cut este folosita pentru a imparti coloana Age in bin uri, cu labeluri din labels
persoane_pe_categorie = my_file['categorie-varsta'].value_counts()
matplotlib.pyplot.bar(persoane_pe_categorie.index, persoane_pe_categorie.values, color='skyblue')
matplotlib.pyplot.title('Nr persoane')
matplotlib.pyplot.xlabel('Categorie varsta')
matplotlib.pyplot.ylabel('Nr persoane')
matplotlib.pyplot.savefig('grafic_task_5.png')

#Task_6
#Gruparea persoanelor in functie de categoria de varsta si separarea dupa gen
persoane_pe_categorie = my_file.groupby(['categorie-varsta', 'Sex'], observed=False)['Survived'].mean() * 10    0
#Reorganizarea datelor pentru a fi afisate
persoane_pe_categorie = persoane_pe_categorie.unstack()
#Realizarea graficului
persoane_pe_categorie.plot(kind='bar', color=['blue', 'orange'], figsize=(10, 6))
matplotlib.pyplot.title('Procent supravietuire')
matplotlib.pyplot.xlabel('Categorie varsta')
matplotlib.pyplot.ylabel('Procent supravietuire')
matplotlib.pyplot.xticks(rotation=45)
matplotlib.pyplot.legend(title='Sex')
matplotlib.pyplot.savefig('grafic_task_6.png')
