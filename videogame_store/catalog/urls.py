from django.urls import path
from . import views

#Enrutamiento para las páginas
urlpatterns = [
    path('', views.videogame_list, name='catalog'),
    path('<int:pk>/', views.game_detail, name='game_detail')
]
