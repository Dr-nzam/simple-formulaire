from django.urls import path
from .views import formulaire

urlpatterns = [
    path('',formulaire, name='formulaire')
]

