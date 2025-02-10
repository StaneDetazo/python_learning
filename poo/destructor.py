# déclaration de classe
class Personne:
    # constructeur
    def __init__(self, nom:str, age:int=0):
        # initialisation des attributs
        self.__nom = nom
        self.__age = age

    def __del__(self):
        print("destructeur appelé")

p = Personne("test", 12)
del p