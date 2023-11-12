import os

folder_path = os. getcwd()

def change_12th_byte(filename, new_byte):
    with open(filename, 'rb') as file:
        content = file.read()

    if len(content) >= 22:
        modified_content = content[:21] + new_byte + content[22:]
        with open(filename, 'wb') as file:
            file.write(modified_content)
        print(f"Modified {filename}: Replaced 12th byte with '{new_byte}'")
    else:
        print(f"Skipped {filename}: File is too short")

def main():
    #folder_path = "chemin/vers/le/dossier"  # Remplacez cela par le chemin du dossier contenant les fichiers
    new_byte = b'C'  # Le nouvel octet (représentant la lettre) à placer à la 12ème position

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            if filename.endswith(".csv"):
                print("fichier csv trouvé ")
            
                change_12th_byte(os.path.join(folder_path, filename), new_byte)

if __name__ == "__main__":
    main()