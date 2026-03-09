from django.urls import path
from . import views

#Enrutamiento para las páginas
urlpatterns = [
    path('log-in', views.log_in_view, name='log-in'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('log-out/', views.log_out_view, name='log-out'),
    path('profile/', views.profile_view, name='profile')
]