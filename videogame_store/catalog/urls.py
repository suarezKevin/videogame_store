from django.urls import path
from . import views

#Enrutamiento para las páginas
urlpatterns = [
    path('', views.videogame_list, name='catalog')
]
