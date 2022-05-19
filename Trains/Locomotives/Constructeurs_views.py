from django.shortcuts import render, HttpResponseRedirect
from .forms import ConstructeurForm
from . import models

def add(request):
    if request.method == "POST":
        form = ConstructeurForm(request)
        return render(request,"Locomotives/Constructeurs/add.html",{"form" : form})
    else :
        form = ConstructeurForm()
        return render(request, "Locomotives/Constructeurs/add.html", {"form" : form})

def traitement(request):
    cform = ConstructeurForm(request.POST)
    if cform.is_valid():
        Constructeur = cform.save()
        return HttpResponseRedirect("../indexc")
    else :
        return render(request, "Locomotives/Constructeurs/add.html", {"form": cform})
    
def index(request):
    liste = list(models.Constructeur.objects.all())
    return render(request, "Locomotives/Constructeurs/index.html",{"liste" : liste})

def affiche(request, id):
    Constructeurs = models.Constructeur.objects.get( pk = id )
    return render(request, "Locomotives/Constructeurs/Affiche.html",{"Constructeur": Constructeurs})

def update(request, id):
    Constructeurs = models.Constructeur.objects.get( pk = id )
    form = ConstructeurForm(Constructeurs.dico())
    return render(request, "Locomotives/Constructeurs/update.html",{"form" : form, "id" : id})

def updatetraitement(request, id):
    cform = ConstructeurForm(request.POST)
    if cform.is_valid():
        Constructeur = cform.save(commit = False)
        Constructeur.id = id
        Constructeur.save()
        return HttpResponseRedirect("../indexc")
    else :
        return render(request, "Locomotives/Constructeurs/add.html", {"form": cform, "id" : id})

def delete(request, id):
    Constructeurs = models.Constructeur.objects.get( pk = id )
    Constructeurs.delete()
    return HttpResponseRedirect("../../indexc")