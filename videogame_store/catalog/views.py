from django.shortcuts import render
from catalog.models import Videogame

# Create your views here.
def videogame_list(request):
    videogame = Videogame.objects.all()
    videogame_catalog = {'videogame_list': videogame}
    return render(request, 'catalog/videogame_list.html', videogame_catalog)

