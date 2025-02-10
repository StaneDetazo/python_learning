# num 1
# importation de la bibliothèque math
import math
# déclaraion de la variable et l'affectation avec l'entré utilisateur et conversion en décimal
figure = float(input("saisissez un flottant --> "))

if figure >= 0 :
    # affichage de la racine de l'entré utilisateur
    print(f"Racine de {figure} : {math.sqrt(figure)}")
else :
    # saisie incorrect
    print("erreur")


