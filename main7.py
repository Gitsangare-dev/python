def salaire_mensuel(salaire_annuel):
    resultat = salaire_annuel / 12
    return resultat

def salaire_hebdomadaire(salaire_mensuel):
    resultat = salaire_mensuel / 4
    return resultat

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    resultat = salaire_hebdomadaire / heures_travaillees
    return resultat

salaire_a = input("combien gagner vous part années ? ")
n_salaire_a = float(salaire_a)

heure_t = input("combien de temp travailler vous par jours ? ")
n_heure_t = float(heure_t)

r_salaire_a = salaire_mensuel(n_salaire_a)
r_salaire_h = salaire_hebdomadaire(r_salaire_a)
r_heure_t = salaire_horaire(r_salaire_h, n_heure_t)

print(f"Vous gagnez {r_salaire_a} euros par mois, {r_salaire_h} euros salaire par jours et {r_heure_t} euros par heure!")


