from django.shortcuts import render

# Create your views here.
def es_if(request):
    var ={'var1': 5, 'var2': 10, 'var3': 15}
    return render(request, "seconda_app/es_if.html",var)
def if_else_elif(request):
    var ={'var1': 5, 'var2': 10, 'var3': 15}
    return render(request, "seconda_app/if_else_elif.html",var)