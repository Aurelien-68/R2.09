
from django.urls import path, include
from . import views
from . import views_Modele

urlpatterns = [
    #pour la partie Marque
path('ajoutMarque/', views.ajoutMarque),
path('traitementMarque/', views.traitementMarque), # ajouter la route traitement associé à l'action traitement du fichier views.py
path('afficheMarque/<int:id>/',views.readMarque),
path('Marque_all/', views.afficherMarque_all),
path('updateMarque/<int:id>/',views.updateMarque),
path('sauvegarder_modifMarque/<int:id>/',views.sauvegarder_modifMarque),
path('supprimerMarque/<int:id>/',views.supprimerMarque),

    #Pour la partie Modele
path('ajoutModele/<int:id>/', views_Modele.ajoutModele),
path('traitementModele/<int:id>/', views_Modele.traitementModele),
path('afficheModele/<int:id>/',views_Modele.readModele),
path('updateModele/<int:id>/',views_Modele.updateModele),
path('sauvegarder_modifModele/<int:id>/',views_Modele.sauvegarder_modifModele),
path('supprimerModele/<int:id>/',views_Modele.supprimerModele),

]
