import sys
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
while selection != 5:
    selection = int(input(choice))
    if selection == 1:
        item= input("Entrez le noom de l'élément à ajouter à la liste de course : ")
        shoplist.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste")
    elif selection == 2:
        print('ok 2')
    
else:
    print("À bientôt !")
    sys.exit()
# choisi dans la liste avec le numéro

# choix 1
# --> "Entrez le noom de l'élément à ajouter à la liste de course : "
# donne le nom que tu veux exemple: X
# --> "L'élément X a bien été ajouté à la liste"
# Affiche la liste de choix

# choix 2
# --> "Entrez le nom d'un élément à retirer de la liste de course : "
# donne le nom que tu veux exemple: X
# --> "L'élément X a bien été supprimé de la liste"
# Affiche la liste de choix
#
#
# on selectionne de nouveau le chiffre 2
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

# choix 5
# -->"À bientôt"
# quitte le programme
