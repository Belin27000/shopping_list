import sys
CHOICE ="""
choisissez parmi les 5 options suivantes:
1: Ajouter un élément à la liste de courses
2: Retirer un élément de la liste de courses
3: Afficher les éléments de la liste de courses
4: Vider la liste de courses
5: Quitter le programme
👉 Votre choix :
"""

SELECTION = 0
shoplist =[]
while SELECTION != 5:
    SELECTION = int(input(CHOICE))
    if SELECTION == 1: # Ajouter un élément
        item= input("Entrez le noom de l'élément à ajouter à la liste de course : ")
        shoplist.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste")
    elif SELECTION == 2: # Retirer un élément
        item= input("Entrez le nom d'un élément à retirer de la liste de course : ")
        for eachitem in shoplist:
            if eachitem == item:
                item_index=shoplist.index(item)
                shoplist.pop(item_index)
                print(f"L'élément {item} a bien été supprimé de la liste")
                break
        else:
            print(f"L'élément {item} n'est pas dans la liste")
    elif SELECTION == 3: # Afficher la liste
        print("Voici le contenu de votre liste : ")
        for i,eachitem in enumerate(shoplist):
            print(f"{i+1}.{eachitem}")
    elif SELECTION == 4: # Vider la liste
        shoplist.clear()
        print("La liste a été vidée de son contenu")
else:
    print("À bientôt !")
    sys.exit()
# choisi dans la liste avec le numéro

# choix 1 - OK
# --> "Entrez le nom de l'élément à ajouter à la liste de course : "
# donne le nom que tu veux exemple: X
# --> "L'élément X a bien été ajouté à la liste"
# Affiche la liste de choix

# choix 2 - OK
# --> "Entrez le nom d'un élément à retirer de la liste de course : "
# donne le nom que tu veux exemple: X
# --> "L'élément X a bien été supprimé de la liste"
# Affiche la liste de choix
#
#
# on SELECTIONne de nouveau le chiffre 2 - OK
# --> "Entrez le nom d'un élément à retirer de la liste de course : "
# essaye de supprimer un élément déjà supprimé
# --> "L'élément X n'est pas dans la liste"

# choix 3
# --> "Voici le contenu de votre liste : "
# 1:  X   le numéro s'ajoute automatiquement devant le nom de l'élément
# Affiche la liste de choix


# choix 4
# --> "La liste a été vidée de son contenu"
# Affiche la liste de choix

# choix 5 - OK
# -->"À bientôt"
# quitte le programme
