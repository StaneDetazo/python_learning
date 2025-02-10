liste = ["diane", "fabio", 2, 3.23]
liste2 = ["diane", "fabio", 2, 3.23]
liste3 = [2, 3.2]
liste4 = [
    ["licifer", 30],
    ["gabriel", 42],
    ["zael", 26]
]

liste3.append('groom')
liste3.insert(0, 'Detazo')
print("taille de la liste 1 : ", len(liste))
print(liste + liste2)
print(liste[1])
print(liste3 + ['Terre'])
print(liste4[1][1])