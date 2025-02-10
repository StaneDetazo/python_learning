# num 11
import easygui

# Initialisation de la liste avec 5 entiers
liste = [5, 10, 15, 20, 25]

# Première saisie avec integerbox
entier_saisi = easygui.integerbox("Entrez un entier pour rechercher dans la liste :")

# Recherche de l'entier dans la liste avec une boucle for
for x in liste:
    if x == entier_saisi:
        easygui.msgbox(f"L'entier {entier_saisi} a été trouvé dans la liste.")
        break
else:
    easygui.msgbox(f"L'entier {entier_saisi} n'est pas dans la liste.")

# Deuxième saisie avec integerbox
entier_saisi_positif = easygui.integerbox("Entrez un entier positif pour vérifier s'il est premier :")

# Vérification si l'entier est premier avec une boucle while
if entier_saisi_positif > 1:  # Assurez-vous que l'entier est positif
    diviseur = 2
    while diviseur <= entier_saisi_positif // 2:
        if entier_saisi_positif % diviseur == 0:
            easygui.msgbox(f"L'entier {entier_saisi_positif} n'est pas premier. Son premier diviseur est {diviseur}.")
            break
        diviseur += 1
    else:
        easygui.msgbox(f"L'entier {entier_saisi_positif} est un nombre premier.")
else:
    easygui.msgbox("Veuillez entrer un entier positif supérieur à 1.")
