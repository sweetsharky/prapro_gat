from django.contrib import admin
from mitarbeiter.models import Mitarbeiter

# Register your models here.
admin.site.register(Mitarbeiter) #jetzt ist das model auch sichtbar auf der admin-Seite
