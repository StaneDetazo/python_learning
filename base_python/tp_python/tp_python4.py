# num 2
# variable
first_word = input("saisir le premier mot == ")
second_word = input("saisir le deuxième mot == ")

# afficher le plus petit mot avec l'opération ternaire
min_word = second_word if first_word > second_word else first_word

print(f"le plut petit mot est {min_word}")

