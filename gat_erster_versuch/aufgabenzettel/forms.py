from django import forms
from aufgabenzettel.models import Aufgabenzettel

class AufgabenzettelForm(forms.ModelForm):
    #neu
    class Meta:
        model = Aufgabenzettel
        fields = ['überschrift', 'beschreibung']

