from django.urls import path
from .views import home,articoloDetailView,listaArticoliView,queryBase

app_name="news"

urlpatterns =[
    path('',home,name="homeview"),
    path("articoli/<int:pk>",articoloDetailView, name="articolo_detail"),
    path("lista_articoli/", listaArticoliView, name="lista_articoli"),
    path("lista_articoli/<int:pk>",listaArticoliView, name="lista_articoli_giornalista"),
    path("query_base",queryBase,name="query_base")
    ]