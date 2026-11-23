from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormContatto
# Create your views here.
def contatti(request):
    #form = FormContatto()
    #Se la richiesta è di tipo POST, possiamo processare i dayi
    if request.method == "POST":
        #Creiamo l'istanza del form e la popoliamo con i dati della POST request (operazione di "binding")
        form=FormContatto(request.POST)
        if form.is_valid():
            #A questo punto possiamo usare i dati validi
            #La funzione .cleaned_data["nome_dato"] ci permette di accedere ai dati validati e convertiti in tipi standard di Python
            print("Il Form è valido!")
            print("NOME:",form.cleaned_data["nome"])
            print("COGNOME:",form.cleaned_data["cognome"])
            print("EMAIL:",form.cleaned_data["email"])
            print("CONTENUTO:",form.cleaned_data["contenuto"])
            #Ringraziamo l'utente per averci contattato (potevamo anche fare un redirect ad un'altra pagina)
            return HttpResponse("<h1>Grazie per averci contattato!<h1>")
    #Se la richiesta ha qualsiasi metodo che non sia POST, allora creo il form di default vuoto
    else:
        form=FormContatto()
    #Arriveremo a questo punto se si tratta della prima volta che la pagina viene richiesta (metodo GET), o se il form non è valido e ha errori
    context ={"form":form}
    return render(request, "forms_app/contatto.html",context)