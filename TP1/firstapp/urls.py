from django.urls import path

from . import views

urlpatterns = [
path('ajout/', views.ajout),
path('traitement/', views.traitement),
path('affiche/<int:id>/',views.read),
path('affiche_all/',views.afficher_all),
#path('/update/<int:id>/',views.update),
]