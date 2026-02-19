from django.shortcuts import render

#vista de la página de principal
def index(request):
    #Render toma el request y el archivo HTML que queremos mostrar
    return render(request, 'home/index.html')

#vista de la página de contacto
def contacto(request):
    return render(request, 'home/contacto.html')
