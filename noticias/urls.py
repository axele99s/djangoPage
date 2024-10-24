from django.urls import path
from .views import listar_noticias

urlpatterns = [
    path('', listar_noticias),
]