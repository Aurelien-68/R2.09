from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class Formulaire_Marque(ModelForm):
    class Meta:
        model = models.Marque
        fields = ['nom', 'date_creation', 'autre']
        labels = {
            'nom': _('Nom '),
            'date_creation': _('Date_creation '),
            'createur': _('createur '),
            'autre': _('Autre information '),
        }
