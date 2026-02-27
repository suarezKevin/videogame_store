from django.shortcuts import render
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

