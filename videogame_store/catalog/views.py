from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from catalog.models import Videogame

# Create your views here.
def videogame_list(request):
    videogame = Videogame.objects.all().order_by('id')
    
    paginator = Paginator(videogame, 6) # Show 6 videogames for page
    
    # We obtain the page number from the URL
    page_number = request.GET.get('page')
    
    # We obtain the objects from that page
    page_objects = paginator.get_page(page_number)
    
    videogame_catalog = {'videogame_list': page_objects}
    return render(request, 'catalog/videogame_list.html', videogame_catalog)

def game_detail(request, pk):
    # We obtein the videogame or we show a error 404
    videogame = get_object_or_404(Videogame, pk=pk)
    
    # We create the context that we will pass to the template
    context = {'game': videogame}
    
    # We rendered the detail template
    return render(request, 'catalog/game_detail.html', context)

