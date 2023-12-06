from django.shortcuts import render
from django.http import HttpResponse
from aufgabenzettel.forms import AufgabenzettelForm

# Create your views here.
def create_aufgabenzettel(request):
    context= {}
    method = request.method

    if request.method =='POST':
        form = AufgabenzettelForm(request.POST)
        if form.is_valid():
            form.save()         #hier werden die eingegebenen Inputs in Aufgabenzettel() in db (SQLite) gespeichert,ahhhh
            return HttpResponse('Daten gespeichert!')
        else:
            return HttpResponse('Fehler')
        print(request.POST)
        return HttpResponse('POST')

    else: #wenn jemand die Seite aufruft(get) und nicht abschickt(post)
        form = AufgabenzettelForm()
        return render(request,'aufgabenbereich.html', {'form': form,'tag': 'dienstag',} )
    
    return render(request=request, template_name='aufgabenbereich.html', context=context) #lieber mit return render(), anstatt HttpResponse 
   #return render(request,'index.html', context) ist das gleiche wie eine Zeile drüber, nur kürzer
