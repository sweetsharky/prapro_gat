from django.db import models

# Create your models here.
class Mitarbeiter(models.Model):
    vorname = models.CharField(max_length=30)
    nachname = models.CharField(max_length=30)
    profilbild = models.CharField(max_length=30)

    def __str__(self):
        return self.vorname + " " + self.nachname