import sys
import os
import json
choice ="""
choisissez parmi les 5 options suivantes:
1: Ajouter un élément à la liste de courses
2: Retirer un élément de la liste de courses
3: Afficher les éléments de la liste de courses
4: Vider la liste de courses
5: Quitter le programme
👉 Votre choix :
"""

selection = 0
shoplist =[]
CHECK_FILE = os.path.exists("liste.json")
if not CHECK_FILE:
    with open("liste.json","x") as shoplist:
        shoplist.write("[]")

CUR_DIR=os.path.dirname(__file__)
CUR_FILE = os.path.join(CUR_DIR,"liste.json")
# print(CUR_FILE)



while selection != 5:
    with open(CUR_FILE,"r") as f:
        shoplist=json.load(f)
    selection = int(input(choice))
    if selection == 1: # Ajouter un élément
        item= input("Entrez le noom de l'élément à ajouter à la liste de course : ")
        shoplist.append(item)
        with open(CUR_FILE, "w") as f:
            json.dump(shoplist,f,indent=4)
        print(f"L'élément {item} a bien été ajouté à la liste")
    elif selection == 2: # Retirer un élément
        item= input("Entrez le nom d'un élément à retirer de la liste de course : ")
        for eachitem in shoplist:
            if eachitem == item:
                item_index=shoplist.index(item)
                shoplist.pop(item_index)
                with open(CUR_FILE, "w") as f:
                     json.dump(shoplist,f,indent=4)
                print(f"L'élément {item} a bien été supprimé de la liste")
                break
        else:
            print(f"L'élément {item} n'est pas dans la liste")
    elif selection == 3:
        print("Voici le contenu de votre liste : ")
        for i,eachitem in enumerate(shoplist):
            print(f"{i+1}.{eachitem}")
    elif selection == 4:
        shoplist.clear()
        with open(CUR_FILE, "w") as f:
            json.dump(shoplist,f,indent=4)
        print("La liste a été vidée de son contenu")
else:
    with open(CUR_FILE, "w") as f:
        json.dump(shoplist,f,indent=4)
    print("À bientôt !")
    sys.exit()