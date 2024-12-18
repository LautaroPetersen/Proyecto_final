from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "App/index.html")

# Página "Sobre la aplicación"
def sobre_aplicacion(request):
    return render(request, 'app/sobre_aplicacion.html')

# Página "Sobre mí"
def sobre_mi(request):
    return render(request, 'app/sobre_mi.html')