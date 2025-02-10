# déclaration de classe
class Personne:
    # constructeur
    def __init__(self, nom:str, age:int=0):
        # initialisation des attributs
        self.__nom = nom
        self.__age = age
    # getter
    @property
    def nom(self):
        return self.__nom
    # setter
    @nom.setter
    def nom(self, name):
        self.__nom = name
    # deleter
    @nom.deleter
    def nom(self):
        del self.__nom

p = Personne("charline", 21)
print(f"nom d'origine : {p.nom}")
p.nom = "Walcia"
print(f"nouveau nom : {p.nom}")