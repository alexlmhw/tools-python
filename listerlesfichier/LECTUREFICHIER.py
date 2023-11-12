# coding: utf-8

import os

folder_path = "C:/Users/alexa/Desktop/PYTHON TEST/4"
liste = []


fichier = open("data.txt", "a")


for path, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".csv"):
            print("fichier csv trouvé ")
            #print(filename)
            liste.append(filename)
            fichier.write(filename)
            fichier.write("\n")

        

nombredefichier = len(liste)
print(nombredefichier)
fichier.close()
