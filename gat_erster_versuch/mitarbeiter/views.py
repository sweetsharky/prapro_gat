from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mitarbeiter.forms import AufgabenzettelForm

# Create your views here.
def mitarbeiter(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def create_aufgabenzettel(request):
    method = request.method

    if request.method =='POST':
        form = AufgabenzettelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Daten gespeichert!')
        else:
            return HttpResponse('Fehler')
        print(request.POST)
        return HttpResponse('POST')

    else: #wenn jemand die Seite aufruft(get) und nicht abschickt(post)
        form = AufgabenzettelForm()
        return render(      #render = darstellen lassen
            request,
            'index.html',
            {
                'form': form,
                'tag': 'dienstag',
             }
        )