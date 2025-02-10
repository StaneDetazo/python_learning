# num 6
string = input("veuillez saisir une chaine de caractère : ") # permettre la saisie d'un chaine
list = ['samael', 3, {"hobby": "foot", "work": "commercial"}]

# boucle for pour parcourir la chaine
for i in string :
    print(i, end="-") # afficher chaque caractère de la chaine accompagner d'un trait

print('') # saut de ligne

for i in range(len(list)) : # parcourir la liste
    print(list[i]) # afficher les valeur de la liste