from django.urls import path
from .views import listar_noticias, agregar_noticia

app_name = 'noticias'  # Esto establece un namespace para la aplicación

urlpatterns = [
    path('', listar_noticias, name='listar_noticias'),
    path('agregar/', agregar_noticia, name='agregar_noticia'),  # Ruta para agregar noticia
]