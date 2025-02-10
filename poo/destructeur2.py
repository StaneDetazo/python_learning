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

    def del_nom(self):
        del self.__nom

    # déclarer une variable publique utilisant le property pour regrouper le getter et le setter
    nom = property(get_nom, set_nom, del_nom)
    age = property(get_age, set_age)

p = Personne("azazel", 39)
p.nom = "Thanos"
del p.nom
# print(p.nom)
p.nom = "Ragnarok"
print(p.nom)
