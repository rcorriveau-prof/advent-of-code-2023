dt_txt_to_int = {"one": "1",
                 "two": "2",
                 "three": "3",
                 "four": "4",
                 "five": "5",
                 "six": "6",
                 "seven": "7",
                 "eight": "8",
                 "nine": "9"
                 }

# Extraire les données
with open("input.txt", "r") as fichier:
    ls_inputs = fichier.read().split("\n")

# Extraire les chiffres et les mots
ls_valeurs = []
for input in ls_inputs:
    ls_un_input = []
    chiffres = ""
    for i, car in enumerate(input):
        if car.isnumeric():
            ls_un_input.append((i, car))  # Ajouter le chiffre et sa position dans la chaîne
    for nombre in dt_txt_to_int:
        position = 0  # Pour entrer une fois dans la boucle
        while position != -1:
            position = input.find(nombre, position)  # Attention s'il y a deux fois le même mot ex."twoonetwo"
            if position != -1:
                ls_un_input.append((position, nombre))
                position += 1    # Il faut bouger l'index de +1 pour avancer dans la recherche
    ls_valeurs.append(ls_un_input)



# Trouver le premier et dernier chiffre, convertir en int.
int_ls_valeurs = []
for ls_chaine in ls_valeurs:
    ls_chaine.sort()
    premiere_valeur = ls_chaine[0][1]
    deuxieme_valeur = ls_chaine[-1][1]
    # conversion si c'est des mots
    if premiere_valeur in dt_txt_to_int.keys():
        premiere_valeur = dt_txt_to_int[premiere_valeur]
    if deuxieme_valeur in dt_txt_to_int.keys():
        deuxieme_valeur = dt_txt_to_int[deuxieme_valeur]

    int_ls_valeurs.append(int(premiere_valeur + deuxieme_valeur))

# Calculer la réponse
print(sum(int_ls_valeurs))
