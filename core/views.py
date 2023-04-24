from django.shortcuts import render

from .models import Enregistrement

# Create your views here.

def formulaire (request):
    nom = request.POST['nom'],
    classe = request.POST['classe'],
    
    NewEnregistrement = Enregistrement.objects.create(nom=nom, classe= classe)
    NewEnregistrement.save()
    
    
    return render (request, 'core/index.html')