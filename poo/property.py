# ENCAPSULATION
# déclaration de classe
class Personne:
    # constructeur
    def __init__(self, nom:str, age:int=0):
        # initialisation des attributs
        self.__nom = nom
        self.__age = age
    # nom
    # getter
    def get_nom(self):
        return self.__nom
    # setter
    def set_nom(self, nom):
        self.__nom = nom

    # age
     # getter
    def get_age(self):
        return self.__age
    # setter
    def set_age(self, age):
        self.__age = age

    # déclarer une variable publique utilisant le property pour regrouper le getter et le setter
    nom = property(get_nom, set_nom)
    age = property(get_age, set_age)

p = Personne("azazel", 39)
print(f"nom et age d'origine : {p.nom}, {p.age}")

p.nom = "samael"
p.age = 20
print(f"nouveau nom et age : {p.nom}, {p.age}")
