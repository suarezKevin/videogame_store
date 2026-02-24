from django.shortcuts import render

# Create your views here.
def videogame_list(request):
    videogame = [
        {
            'name':'Dogo Racing', 'price': 30.00, 'platform': 'PC,PS5,Xbox,Series X'
        },
        {
            'name':'Platform', 'price': 14.99, 'platform': 'PC,PS5,Xbox,Series X'
        },
        {
            'name':'Urban Darkness', 'price': 39.99, 'platform': 'PC,PS5,Xbox,Series X'
        },
        {
            'name':'Highspeed', 'price': 49.99, 'platform': 'PC,PS5,Xbox,Series X'
        },
        {
            'name':'Night Mode', 'price': 19.99, 'platform': 'PC,PS5,Xbox,Series X'
        },
        {
            'name':'The Grand Thief', 'price': 59.99, 'platform': 'PC,PS5,Xbox,Series X'
        },
        {
            'name':'Sunset Vibe', 'price': 24.99, 'platform': 'PC,PS5,Xbox,Series X'
        },
        {
            'name':'Dark Whispers', 'price': 34.99, 'platform': 'PC,PS5,Xbox,Series X'
        },
        {
            'name':'Space Zero', 'price': 44.99, 'platform': 'PC,PS5,Xbox,Series X'
        },
        {
            'name':'Medieval Saga', 'price': 54.99, 'platform': 'PC,PS5,Xbox,Series X'
        }
    ]
    videogame_catalog = {'videogame_list': videogame}
    return render(request, 'catalog/videogame_list.html', videogame_catalog)

