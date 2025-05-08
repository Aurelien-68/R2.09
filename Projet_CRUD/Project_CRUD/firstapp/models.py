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