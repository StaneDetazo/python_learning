# num 4
a = 0
b = 10

while a < b :
    print(f'a = {a}') # afficher a tant qu'elle sera < b
    a += 1 # incrémenter a
print("--------------")
while b > 0:
    b -= 1  # Décrémenter b
    if b % 2 == 1:  # Vérifier si b est impair
        print(f"b = {b}") # afficher b impaire