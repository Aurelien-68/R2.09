
from django.shortcuts import render, HttpResponseRedirect
from .forms import Formulaire_Modele
from . import models
from django.shortcuts import get_object_or_404



def ajoutModele(request, id):
    form=Formulaire_Modele
    return render(request,"modele/ajout_Modele.html", {"form":form, "id":id})

def traitementModele(request, id):
    marque=models.Marque.objects.get(pk=id)
    lform = Formulaire_Modele(request.POST)
    if lform.is_valid():
        Modele = lform.save(commit=False)
        Modele.marque= marque
        Modele.marque_id= id
        Modele.save()
        return render(request,"modele/affiche_Modele.html",{"Modele" : Modele})
    else:
        return render(request,"modele/ajout_Modele.html",{"form": lform})

def readModele(request, id):
    Modele = models.Modele.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"modele/affiche_Modele.html",{"Modele": Modele})



def updateModele(request, id):
    data = models.Modele.objects.get(pk=id)
    dico = data.make_dico()
    formulaire_avant_modif = Formulaire_Modele(dico)
    return render(request, "modele/update_Modele.html", {"form": formulaire_avant_modif, "id": id})

def sauvegarder_modifModele(request, id):
    # 1. On récupère le Modele existant
    modele = get_object_or_404(models.Modele, pk=id)

    # 2. On passe l'instance au formulaire pour que Django fasse la mise à jour
    formulaire_avec_modif = Formulaire_Modele(request.POST, instance=modele)

    if formulaire_avec_modif.is_valid():
        # 3. Le champ 'marque' est déjà rempli, on n'a pas besoin de le re-remplir
        formulaire_avec_modif.save()
        return HttpResponseRedirect("/modele/Marque_all/")
    else:
        return render(request, "modele/update_Modele.html", {
            "formulaire": formulaire_avec_modif,
            "id": id
        })



def supprimerModele(request, id):
    data = get_object_or_404(models.Modele, pk=id)
    data.delete()
    return HttpResponseRedirect("/marque/Marque_all/")