from django.db import models

class Marque(models.Model):
    nom=models.CharField(max_length=100,blank=False)
    date_creation=models.IntegerField(blank=False)
    createur=models.CharField(max_length=100,blank=False)
    autre=models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f" {self.nom}  "
        return chaine

    def make_dico(self):
        return {"nom": self.nom, "date_creation":self.date_creation,"createur":self.createur, "autre": self.autre}

class Modele(models.Model):
    nom=models.CharField(max_length=100,blank=False)
    anne_creation=models.IntegerField(blank=False)
    puissance=models.IntegerField(blank=False)
    poid=models.IntegerField(blank=False)
    autre = models.TextField(null=True, blank=True)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE, default=None)
    def __str__(self):
        chaine = f" {self.nom}  "
        return chaine

    def make_dico(self):
        return {"nom": self.nom, "annee_creation":self.date_creation,"puissance":self.createur, "poid":self.poid,"autre": self.autre, "marque":self.marque}