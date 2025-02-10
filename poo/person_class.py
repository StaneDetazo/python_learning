# création de class
class Person:
    # déclaration des variable
    nom : str
    age : int

# instanciation
p = Person()
# affectation
p.nom = "Samael"
p.age = 36
# afficher les valeurs
print(p.nom, "a", p.age, "ans")