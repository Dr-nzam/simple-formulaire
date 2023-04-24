from django.shortcuts import render

# Create your views here.

def formulaire (request):
    nom = request.POST['nom'],
    classe = request.POST['classe'],
    
    
    
    return render (request, 'core/index.html')