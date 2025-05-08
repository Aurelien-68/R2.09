
from django.shortcuts import render, HttpResponseRedirect
from .forms import Formulaire_Marque
from . import models
def ajoutMarque(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = Formulaire_Marque(request)
        if form.is_valid(): # validation du formulaire.
            Marque = form.save() # sauvegarde dans la base
            return render(request,"marque/affiche_Marque.html",{"Marque" : Marque})
        else:
            return render(request,"marque/ajout_Marque.html",{"form": form})
    else:
        form = Formulaire_Marque()
        return render(request,"marque/ajout_Marque.html",{"form" : form})

def traitementMarque(request):
    lform = Formulaire_Marque(request.POST)
    if lform.is_valid():
        Marque = lform.save()
        return render(request,"marque/affiche_Marque.html",{"Marque" : Marque})
    else:
        return render(request,"marque/ajout_Marque.html",{"form": lform})

def readMarque(request, id):
    Marque = models.Marque.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"marque/affiche_Marque.html",{"Marque": Marque})

def afficherMarque_all(request):
    liste_data = list(models.Marque.objects.all())
    return render(request, "marque/afficher_allMarque.html", {"liste": liste_data})

def updateMarque(request, id):
    data = models.Marque.objects.get(pk=id)
    dico = data.make_dico()
    formulaire_avant_modif = Formulaire_Marque(dico)
    return render(request, "marque/ajout_Marque.html", {"form": formulaire_avant_modif, "id": id})

def sauvegarder_modifMarque(request, id):
    formulaire_avec_modif = Formulaire_Marque(request.POST)
    if formulaire_avec_modif.is_valid():
        sauvegarde = formulaire_avec_modif.save(commit=False)
        sauvegarde.id = id
        sauvegarde.save()
        return HttpResponseRedirect("/marque/Marque_all/")
    else:
        return render(request, "/marque/ajout_Marque.html", {"formulaire": formulaire_avec_modif , "id": id})



def supprimerMarque(request, id):
    data = models.Marque.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect("/marque/Marque_all/")