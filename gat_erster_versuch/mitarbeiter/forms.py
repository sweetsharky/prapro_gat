from django import forms
from mitarbeiter.models import Mitarbeiter

class MitarbeiterForm(forms.ModelForm):
    #neu
    class Meta:
        model = Mitarbeiter
        fields = ['vorname', 'nachname', 'profilbild']