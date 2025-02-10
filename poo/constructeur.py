class Person:
    # déclaration du constructeur
    def __init__(self, nom:str, age:int):
        self.nom = nom
        self.age = age

p = Person("azazel", 123)
# p.nom = "azazel"
# p.age = 14

print(p.nom, p.age, "ans")