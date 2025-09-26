from keyword import iskeyword

print("CALCULATRICE")

print("Entrez un premier chiffre")  #on utilise la fonction print pour afficher des caractère
nombre_1 = input(" : ")             # fonction input pour demander a l'utlisateur d'effectuer une saisie et on initialise la reponse dans la variable nombre_1  
print("Entrez un second chiffre")
nombre_2 = input(" : ")

nb_1 = nombre_1.isnumeric()        #on initilise la variable nb_1 avec nombre_1 et la fonction isnumeric() pour verifier ci cest bien un numero
nb_2 = nombre_2.isnumeric()

if nb_1 and nb_2 != True:          # on dit que si nb_1 et nb_2 son different de true que le programme s'arrete
    raise SystemExit("fin du programme")
elif nb_1 and nb_2 == True:        # mais si il est egal a true
    nb_1_conv = int(nombre_1)      # on convertie la chaine de caractère en int
    nb_2_conv = int(nombre_2)

print("Quel signe souhaitez vous utilisez?")
operation = input("Addition, Soustraction, Multiplaction ou Division ? : ")

operation_verif = operation.isascii()             

if operation_verif != True:
    raise SystemExit("fin du programme erreur operateur")    # On applique le meme principe que plus haut
elif operation == "+":
    resultat = nb_1_conv + nb_2_conv
    print(f" {resultat} est le resultat d'addition. ")      #on dit que si operation egal au signe + nb_1_conv et nb_2_conv s'addition et initialise la variable resultat puis on l'affiche dans print la meme si dessous  
elif operation == "-":
    resultat = nb_1_conv - nb_2_conv
    print(f" {resultat} est le resultat de la soustraction. ")
elif operation == "*":
    resultat = nb_1_conv * nb_2_conv
    print(f" {resultat} est le resultat de la multiplication. ")
elif operation == "/" and nb_2_conv == 0:
    raise SystemExit("nombre ne peu etre diviser part 0")        #on ne peu diviser un nombre part zero donc on va lui demander de verifier si nb_2_conv et egal a zero de sortir de la boucle
elif operation == "/" and nb_2_conv != 0:
    resultat = nb_1_conv / nb_2_conv
    r_resultat = round(resultat)                                 # et si cest ok de faire la divisition et initial une variable r_resulat qui egal a round(resultat) c'est a dire le resultat a roundi
    print(f" {r_resultat} est le resultat de la division . ")
else:
    raise SystemExit("fin du programme erreur calculatrice")