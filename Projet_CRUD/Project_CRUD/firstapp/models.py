from django.db import models

class Marque(models.Model):
    nom=models.CharField(max_length=100,blank=False)
    date_creation=models.IntegerField(blank=False)
    createur=models.CharField(max_length=100,blank=False)
    autre=models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"La marque {self.nom} a été crée en {self.date_creation} par {self.createur} "
        return chaine