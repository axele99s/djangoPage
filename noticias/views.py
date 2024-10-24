# noticias/views.py
from django.shortcuts import render, redirect
from .models import Noticia

def listar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'listar_noticias.html', {"noticias": noticias})

def agregar_noticia(request):
    if request.method == 'POST':
        # Recoger los datos del formulario
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')

        # Crear la nueva noticia y guardarla en la base de datos
        nueva_noticia = Noticia(titulo=titulo, descripcion=descripcion)
        nueva_noticia.save()  # Guardar en la base de datos PostgreSQL

        # Redirigir a la página de lista de noticias
        return redirect('noticias:listar_noticias')

    # Si no es POST, renderizar el formulario para agregar la noticia
    return render(request, 'crear_noticia.html')

