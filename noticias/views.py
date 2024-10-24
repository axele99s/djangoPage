from django.shortcuts import render
from .models import Noticia


def listar_noticias(request):
    noticias = Noticia.objects.all()
    print(noticias)
    return render(request, 'listar_noticias.html',{"noticias": noticias})

