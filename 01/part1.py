# Extraire les données
with open("input.txt", "r") as fichier:
    ls_inputs = fichier.read().split("\n")

# Extraire les chiffres
ls_valeurs = []
for input in ls_inputs:
    chiffres = ""
    for car in input:
        if car.isnumeric():
            chiffres += car
    ls_valeurs.append(int(chiffres[0] + chiffres[-1]))

# Calculer la réponse
print(sum(ls_valeurs))
