from django.shortcuts import render

# Create your views here.

def formulaire (request):
    
    return render (request, 'core/index.html')