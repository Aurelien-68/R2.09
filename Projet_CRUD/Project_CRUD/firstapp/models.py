from django.db import models

class Marque(models.Model):
    nom=models.CharField(max_length=100,blank=False)
    date_creation=models.IntegerField(blank=False)
    autre=models.TextField(null = True, blank = True)

    def __str__(self):
        str_retournee = f'<ul>' \
                        f'<li>Nom : <span>{self.nom}</span></li>' \
                        f'<li>Date de création :<span>{self.date_creation}</span></li>' \
                        f'<li>Autre information :<span>{self.autre}</span></li>' \
                        f'</ul>'
        return str_retournee