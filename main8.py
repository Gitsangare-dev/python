numerateur = input("Entrez le numerateur : ")
denominateur = input("Entrez le denominateur : ")

try:
    resultat = int(numerateur) / int(denominateur)
    print(f"le resultat est {resultat}")
except ZeroDivisionError:
    print("Erreur : division par zero")
except ValueError:
    print("Erreur : de type incorrecte")