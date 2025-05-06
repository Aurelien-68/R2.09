from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class Formulaire_Marque(ModelForm):
    class Meta:
        model = models.Marque
        fields = ['nom', 'date_creation', 'autre']
        labels = {
            'nom': _('Nom : '),
            'date_creation': _('date_creation : '),
            'autre': _('autre information : '),
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'class_css_input', 'placeholder': 'Votre nom…'}),
            'date_creation': forms.TextInput(attrs={'class': 'class_css_input', 'placeholder': 'Date de creation…'}),
            'autre': forms.EmailInput(attrs={'class': 'class_css_input', 'placeholder': 'Autre informations …'}),
        }