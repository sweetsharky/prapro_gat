from django.shortcuts import render
from django.http import HttpResponse
from mitarbeiter.forms import MitarbeiterForm
from .models import Mitarbeiter

# Create your views here.

def erstelle_mitarbeiter(request): 
    context= {}
    method = request.method

    if request.method =='POST':
        form = MitarbeiterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Daten gespeichert!')
        else:
            return HttpResponse('Fehler')
        print(request.POST)
        return HttpResponse('POST')

    else: #wenn jemand die Seite aufruft(get) und nicht abschickt(post)
        form = MitarbeiterForm()
        return render(      #render = darstellen lassen
            request,
            'mitarbeiterbereich.html',
            {
                'form_Mitarbeiter': form,
                'tag': 'dienstag',
             }
        )
    return render(request=request, template_name='mitarbeiterbereich.html', context=context) #lieber mit return render(), anstatt HttpResponse 
   #return render(request,'index.html', context) ist das gleiche wie eine Zeile drüber, nur kürzer


def mitarbeiter(request):
    alle_mitarbeiter = Mitarbeiter.objects.all().values()           #Objekt mit allen Werten des Member-models wird erstellt
    context = {
        'alle_mitarbeiter' : alle_mitarbeiter,                        
    }
    return render(request,'alle_mitarbeiter.html', context)


def details(request, id):
    mitarbeiter = Mitarbeiter.objects.get(id=id)
    context = {
        'mitarbeiter': mitarbeiter, 
    }   
    return render(request, 'details.html', context)