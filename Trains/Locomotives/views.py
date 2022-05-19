from django.shortcuts import render, HttpResponseRedirect
from .forms import LocomotiveForm
from . import models

def add(request):
    if request.method == "POST":
        form = LocomotiveForm(request)
        return render(request,"Locomotives/Locomotives/add.html",{"form" : form})
    else :
        form = LocomotiveForm()
        return render(request, "Locomotives/Locomotives/add.html", {"form" : form})

def traitement(request):
    lform = LocomotiveForm(request.POST)
    if lform.is_valid():
        locomotive = lform.save()
        return HttpResponseRedirect("../index")
    else :
        return render(request, "Locomotives/Locomotives/add.html", {"form": lform})
    
def index(request):
    liste = list(models.Locomotive.objects.all())
    return render(request, "Locomotives/Locomotives/index.html",{"liste" : liste})

def affiche(request, id):
    locomotives = models.Locomotive.objects.get( pk = id )
    return render(request, "Locomotives/Locomotives/Affiche.html",{"Locomotive": locomotives})

def update(request, id):
    locomotives = models.Locomotive.objects.get( pk = id )
    form = LocomotiveForm(locomotives.dico())
    return render(request, "Locomotives/Locomotives/update.html",{"form" : form, "id" : id})

def updatetraitement(request, id):
    lform = LocomotiveForm(request.POST)
    if lform.is_valid():
        locomotive = lform.save(commit = False)
        locomotive.id = id
        locomotive.save()
        return HttpResponseRedirect("../index")
    else :
        return render(request, "Locomotives/Locomotives/add.html", {"form": lform, "id" : id})

def delete(request, id):
    locomotives = models.Locomotive.objects.get( pk = id )
    locomotives.delete()
    return HttpResponseRedirect("../../index")

def accueil(request):
    return render(request, "Locomotives/accueil.html")
