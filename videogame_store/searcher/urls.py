from django.urls import path
from . import views

#Enrutamiento para las páginas
urlpatterns = [
    path('', views.search_games, name='searcher'),#llama a la vista searcher
]