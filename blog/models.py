from django.conf import settings
from django.db import models
from django.utils import timezone
 
class Activity(models.Model):
    id_activ = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=500)
    def __str__(self):
        return self.id_activ
    
class Player(models.Model):
    id_play = models.CharField(max_length=1000, primary_key=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    etat = models.CharField(max_length=50)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_play