from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class Formulaire_Marque(ModelForm):
    class Meta:
        model = models.Marque
        fields = ['nom', 'date_creation', 'createur','autre']
        labels = {
            'nom': _('Nom '),
            'date_creation': _('Date_creation '),
            'createur': _('createur '),
            'autre': _('Autre information '),
        }

class Formulaire_Modele(ModelForm):
    class Meta:
        model = models.Modele
        fields = ['nom', 'annee_creation', 'puissance','poid','autre']
        labels = {
            'nom': _('Nom '),
            'annee_creation': _('annee_creation '),
            'puissance': _('puissance '),
            'poid': _('poid '),
            'autre': _('Autre information '),
        }
