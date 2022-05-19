from django.db import models

class Locomotive(models.Model):
    nom = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    pays_origine = models.CharField(max_length = 100)
    date_creation =  models.CharField(max_length = 4, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    Constructeur = models.ForeignKey("Constructeur", on_delete=models.CASCADE, default = None)

    def __str__(self):
        chaine = f"Locomotive : {self.nom}, Type de Motorisation : {self.type}, Pays d'origine : {self.pays_origine}, Première Livraison : {self.date_creation}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "type" : self.type, "pays_origine" : self.pays_origine, "date_creation" : self.pays_origine, "date_creation" : self.date_creation, "description" : self.description, "Constructeur" : self.Constructeur}

class Constructeur(models.Model):
    nom = models.CharField(max_length = 100)
    siege_social = models.CharField(max_length = 100)
    pays_origine = models.CharField(max_length = 100)
    date_creation =  models.CharField(max_length = 4, null = True, blank = True)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"Constructeur : {self.nom}, Siège social basé à : {self.siege_social}, Pays d'origine : {self.pays_origine}, crée en : {self.date_creation}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "siege_social" : self.siege_social, "pays_origine" : self.pays_origine, "date_creation" : self.pays_origine, "date_creation" : self.date_creation, "description" : self.description}