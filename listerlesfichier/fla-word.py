#########################""
# Author: Alexandre LEMAIRE
# Date: 12/11/2023
#
#Projet: Generer automatiquement la feuille de match
#########################################
import os
import pandas
import csv

DF_liste_joueur = pandas.DataFrame()


folder_path = os. getcwd()
print( "Dossier de travail: "+ folder_path)


folder_data_path = "G:\\Mon Drive\\03 - Foot\\2023 - 2024 Paris Clichy FC\\Licence"

print(folder_data_path)

for path, dirs, files in os.walk(folder_data_path):
    
    for filename in files:
        print(filename)
        
        liste_filename = filename.split("_")
        
        if len(liste_filename) == 2:
            liste_filename.append(0)
        elif len(liste_filename) == 1:
            break
        
        data = {
            #'ID': [filename],
            'Nom': [liste_filename[0]],
            'Prenom': [liste_filename[1]],
            'Numero': [liste_filename[2]],
            }
        
        df1 = pandas.DataFrame(data)
        DF_liste_joueur = pandas.concat([ DF_liste_joueur, df1], ignore_index=True)
        
DF_liste_joueur.to_csv( "listejoueurs.csv")      