from os import makedirs
import os
import requests
from bs4 import BeautifulSoup

from Colors import Colors

def fetchData(link):
    datas = []
    response = requests.get(link)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        coursename_tags = soup.find_all(class_="coursename")
        for tag in coursename_tags:
            datas.append(tag.text.strip())
            
        print(f"{Colors.OKGREEN}{response.status_code}{Colors.ENDC} - Récupération des données réussie")
        print(f"Nombre de dossiers récupérés : {len(datas)}")
        
    else:
        print(f"{Colors.FAIL}{response.status_code}{Colors.ENDC} - Récupération des données échouée")

    return datas

def sanitize(name):
    # Replace any characters not allowed in file names with underscore
    return "".join(c if c.isalnum() or c in " .-_" else "_" for c in name)

def rightDirectory(base_dir, datas):
    print("Création des dossiers dans le repertoire :" + Colors.OKGREEN + base_dir + Colors.ENDC)
    for data in datas:
        sanitized_data = sanitize(data)
        dir_path = os.path.join(base_dir, sanitized_data)
        makedirs(dir_path, exist_ok=True)
        tp_dir = os.path.join(dir_path, "tp")
        td_dir = os.path.join(dir_path, "td")
        cours_dir = os.path.join(dir_path, "cours")
        makedirs(tp_dir, exist_ok=True)
        makedirs(td_dir, exist_ok=True)
        makedirs(cours_dir, exist_ok=True)
        print(f" > {Colors.OKGREEN}{sanitized_data}{Colors.ENDC}")

if __name__ == "__main__":
    link = input("Entrez le lien de récupération de répertoires : ")
    datas = fetchData(link)
    dir = input("Entrez le chemin du répertoire où vous voulez créer les dossiers : ")
    print(datas)
    rightDirectory(dir, datas)
