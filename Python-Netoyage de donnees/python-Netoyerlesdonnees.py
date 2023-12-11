# import des librairies dont nous aurons besoin
import pandas as pd
import numpy as np
import re

# chargement et affichage des données
data = pd.read_csv('course+-+Quiz+P2.csv')
print(data)

print(data["Dept"].unique())
print(data.isnull().sum())

data['Temps new'] = pd.to_datetime(data['Temps'], format='%H/%M/%S', errors='coerce')
print(data.isnull().sum())

print(data)