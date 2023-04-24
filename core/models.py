from django.db import models

# Create your models here.

class enregistrement (models.Model):
    nom = models.CharField(max_length=128,)
    classe = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nom