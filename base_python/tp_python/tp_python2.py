# declaration des variable
student_nb = 2
valuation_nb = 3

# déclaration de all_student pour stocker tous les etudiants
all_student = []

# déclaration de fonction noteEntry pour la saisie des notes et le calcule de leur moyenne
def noteEntry() :
    # une boucle pour parcourir le nombre des etudiants
    for i in range(1, student_nb+1) :
        student_name = input(f"le nom de l'étucdiant {i} -->") # entré au clavier du nom de l'etudiant
        # déclaration de liste de note pour l'etudiant actif
        notes = []
        # parcour des notes
        for j in range(1, valuation_nb+1) :
            note = float(input(f"saisir la note {j} de {student_name} >")) # convertion des entrées en décimal
            while note < 0 or note > 20 : # controle des notes
                print("la note doit être compris entre 0 et 20")
                note = float(input(f"saisir la note {j} de {student_name}"))
            notes.append(note) # ajout de la note à la liste de notes pour l'etudiant actif

        average_note = sum(notes) / valuation_nb  # calcul de la moyenne des notes de l'etudiant actif
        # Ajout des informations (nom et moyenne) dans la liste (all_student) sous forme de dictionnaire
        all_student.append({"nom": student_name, "moyenne": average_note})
        
    average_list = []
    for i in range(len(all_student)) :
        average_list = all_student[i]["moyenne"]
        # print(all_student[i]["moyenne"])
    max_average = max(average_list)
    print(max_average)
    print(all_student)
    print(average_note)


noteEntry()