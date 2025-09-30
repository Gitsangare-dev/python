class BoiteaOutil:
    
    def __init__(self, outil):
        self.outil = outil
    
    def enlever(self):
        print("enlever")

    def ajouter(self):
        print("ajouter")
        

class Marteaux:

    def __init__(self, marteau, couleur):
        self.marteau = marteau
        self.couleur = couleur
    
    def planter(self):
        print("planter")

    def retire(self):
        print("retire")

    def peindre(self):
        print("peindre")


class Tournevis:

    def __init__(self, taille):
        self.taille = taille
    
    def serrer(self):
        print("serrer")

    def desserrer(self):
        print("desserrer")