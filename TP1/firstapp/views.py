from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import LivreForm
from . import models
def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            Livre = form.save() # sauvegarde dans la base
            return render(request,"firstapp/affiche.html",{"Livre" : Livre}) #envoie vers une page d'affichage du Livre créé
        else:
            return render(request,"firstapp/ajout.html",{"form": form})
    else:
        form = LivreForm() # création d'un formulaire vide
        return render(request,"firstapp/ajout.html",{"form" : form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        liste_data = list(models.Livre.objects.all())
        return render(request, "firstapp/VUE_affiche_all.html", {"liste": liste_data})
    else:
        return render(request,"firstapp/ajout.html",{"form": lform})

def afficher_all(request):
    liste_data=list(models.Livre.objects.all())
    return render(request,"firstapp/VUE_affiche_all.html",{"liste":liste_data})
def read(request, id):
    Livre = models.Livre.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"firstapp/affiche.html",{"Livre": Livre})

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save(commit=False) # création d'un objet Livre avec les données du formulaire mais sans l'enregistrer dans la base.
        Livre.id = id; # modification de l'id de l'objet
        Livre.save() # mise à jour dans la base puisque l'id du Livre existe déja.
        return HttpResponseRedirect("/firstapp/") # plutot que d'avoir un gabarit pour nous indiquer que cela c'est bien passé, nous repartons sur une autre action qui renvoie vers la page d'index de notre site (celle avec la liste des entrées)
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})