from django.db import models

# Create your models here.
class Aufgabenzettel(models.Model):
    überschrift = models.CharField(max_length=30)
    beschreibung = models.CharField(max_length=100)
    


    def __str__(self):
        return self.überschrift + ": " + self.beschreibung #Return a string representation of the model instance