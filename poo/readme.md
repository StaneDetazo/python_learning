objet = état + comportement

état == attribut
comportement == méthode

objet.mon_attribut
objet.maFonction()

meme concept car objet et classe ont tous les deux attribut et fonction

classe est un modèle décrivant les état et comportement d'un objet
objet est une représentation abstraite d'un classe.

_ = protected (non modifiable par les classes fille héritant de la classe mère mais modifiable par les instance de la classe mere) -> self._name
__ = private (modifiable par les instances de la classe mais pas accessible dans les classes fille) -> self.__name