# création de class
class Student :
    # crétion de méthode d'initialisation 
    def initialize(self, name, age) :
        # déclaration des attributs
        self.name = name
        self.age = age

# déclaration des objet
student_1 = Student()
student_2 = Student()
student_3 = Student()
# initialisation des objet 
student_1.initialize("tazo", 21)
student_2.initialize("détazo", 23)
student_3.initialize("stallone", 12)
# afficher les information des objets
print(student_1.name, student_1.age)
print(student_2.name, student_2.age)
print(student_3.name, student_3.age)
