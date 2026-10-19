from random import randint

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "prova_pratica_1/index.html")
def somma(request):
    var1=randint(1,10)
    var2=randint(1,10)
    somma=var1+var2
    var={'var1':var1,'var2':var2,'somma':somma}
    return render(request, "prova_pratica_1/somma.html",var)

def media(request):
    var=[]
    media=0.0
    for _ in range(1,30):
        var.append(randint(1,10))
    for i in var:
        media+=i
    media=media/len(var)
    dati={'voti':var,'media':media,'soglia':6}
    return render(request, "prova_pratica_1/media.html",dati)

def voti(request):
    var = {'dati':{'studente1': 5, 'studente2': 10, 'studente3': 7,'studente4':8}}
    #my_dict= {'chiave1': 'Valore 1', 'chiave2': 'Valore 2'}
    return render(request, "prova_pratica_1/voti.html",var)