import logging
import json
import os
LOGGER = logging.getLogger()
from constant import DOSSIER_DATA

# Ajout d'un commentaire pour actualiser mon code

liste = []

def affiche_menu():
    print("Choisissez une option : ")
    print("1- Ajouter un nom\n2- Afficher la liste des noms\n3- Supprimer un nom\n4- Sauvgarder")
    choix_menu()
    

def choix_menu():
    choix = input("Choisissez votre option : ")
    choix = int(choix)
    
    if choix == 1:
        def ajouter ():
            personne = []
            nom = input("Entrez le nom : ")
            email = input("Entrez l'email : ")
            tel = input("Entrez le téléphone: ")
            # personne = {
            #     "nom": f"{nom}",
            #     "email": f"{email}",
            #     "tel": f"{tel}",
            # }
            personne = f"{nom} - {email} - {tel}"
            liste.append(personne)
            print(liste)
            affiche_menu()
            return True
        ajouter()
    
    elif choix == 2:
        def afficher ():
            print("Liste des noms")
            for element in liste[0]:
                print(f" - {element}")
        afficher()
        affiche_menu()
    
    
    elif choix == 3:
        element = input("Entrez le nom à supprimer : ")
        def enlever ():
            if element in liste:
                liste.remove(element)
                print(f"{element} a été supprimé avec succès")
                return True
            else:
                print(f"{element} n'existe pas")
                return False
        enlever()
        affiche_menu()
        
    elif choix == 4:
        def sauvegarder ():
            chemin = os.path.join(DOSSIER_DATA, "user.txt")
            if not os.path.exists(DOSSIER_DATA):
                os.makedirs(DOSSIER_DATA)
                
            with open(chemin, "a") as f:
                # json.dump(liste, f, indent=4)
                for el in liste:
                    f.write(f"{el}\n")
            return True
        sauvegarder()

if __name__ == "__main__":
    affiche_menu()