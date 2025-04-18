"""
from django.urls import path, include

from restaurante.views import personas, restaurante, reservas # Importar la vista restaurante
# from . import views
from .views import lista_personas # Importar la vista lista_personas

urlpatterns = [
#    path('personas/', personas, name='personas'), # URL para la vista personas
    path('personas/', lista_personas, name='lista_personas'),
    path('restaurante/', restaurante, name='restaurante'), # URL para la vista restaurante
    path('reservas/', reservas, name='reservas'), # URL para la vista reservas
]
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # URL para la vista de inicio
    path("persona/", views.agregar_persona, name="persona"), # URL para la vista de agregar persona
    path("restaurante/", views.agregar_restaurante, name="restaurante"), # URL para la vista de agregar restaurante
    path("reserva/", views.agregar_reserva, name="reserva"), # URL para la vista de agregar reserva
    path("buscar/", views.buscar_persona, name="buscar"),   # URL para la vista de buscar persona
]
