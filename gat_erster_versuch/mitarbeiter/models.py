from django.db import models

# Create your models here.
class Mitarbeiter(models.Model):
    vorname = models.CharField(max_length=30)
    nachname = models.CharField(max_length=30)
    profilbild = models.ImageField(upload_to='images/')  # 'images/' is the upload directory --> in settings.py muss dafür MEDIA_ROOT und MEDIA_URL angelegt werden --> außerdem muss dafür pillow zur venv heruntergeladen werden = eine library, die image processing capabilities bietet

    def __str__(self):
        return self.vorname + " " + self.nachname     

