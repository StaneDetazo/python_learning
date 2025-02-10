# déclaration de classe
class MaClasse: 
    # déclaration des attributs
    x = 23
    y = x + 5
    # méthode pour afficher les valeur
    def affiche(self):
        self.z = 42
        print(f"y = {self.y} et z = {self.z}")
# instanciation de la classe
ma_classe = MaClasse()
ma_classe.affiche() # accès au méthode d'affichage

