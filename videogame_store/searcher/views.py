from django.shortcuts import render
from catalog.models import Videogame
from django.core.paginator import Paginator
from django.db.models import Q

def search_games(request):
    query = request.GET.get('q','')# we obtain the search term

    #Filter by name or platform containing the query
    response = Videogame.objects.filter(
        Q(name__icontains=query) | Q(platform__icontains=query)
        ).order_by('id')
    
    paginator = Paginator(response, 6)# Six games for page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'query':query, 'videogame_list': page_obj}
    return render(request, 'searcher/search_results.html', context)
