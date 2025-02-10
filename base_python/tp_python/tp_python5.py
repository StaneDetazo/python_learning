# num 3
# déclaration des variable 
p_seuil = 2.3
v_seuil = 7.41

# demande de saisie pour la simulation du comportement
#conversion des entrées en décimal
pression = float(input("veuillez saisir la pression : "))
volume = float(input("veuillez saisir le volume : "))

# simulation
if (volume > v_seuil and volume > p_seuil and pression > p_seuil and pression > v_seuil) :
    print("arrêt immediat")
elif pression > p_seuil :
    new_volume = float(input("Augmenter le volume de l'enceinte "))
    # ecraser l'ancienne valeur du volume
    volume = new_volume
    print("le nouveau volume", volume) # afficher la nouvelle valeur du volume
elif volume > v_seuil :
    new_volume = float(input("Dimunier le volume de l'enceinte "))
    # ecraser l'ancienne valeur du volume
    volume = new_volume
    print("le nouveau volume", volume) # afficher la nouvelle valeur du valeur
else :
    print("tout va bien")

