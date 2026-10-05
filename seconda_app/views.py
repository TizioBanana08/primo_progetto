from django.shortcuts import render
import datetime
# Create your views here.
def es_if(request):
    var ={'var1': 5, 'var2': 10, 'var3': 15}
    return render(request, "seconda_app/es_if.html",var)
def if_else_elif(request):
    var ={'var1': 5, 'var2': 10, 'var3': 15}
    return render(request, "seconda_app/if_else_elif.html",var)
def es_for(request):
    dic={'list1':[1,datetime.date(2024, 6, 1),'Do Not Give Up!'], 'list2':[1,datetime.date(2024, 6, 1),'Do Not Give Up!'], 'my_dict': {'chiave1': 'Valore 1', 'chiave2': 'Valore 2'}}
    return render(request, "seconda_app/es_for.html",dic)