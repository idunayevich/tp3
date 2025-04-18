from django.shortcuts import render, redirect
from .models import Persona, Restaurante, Reserva # Importar los modelos (models.py)

def home(request):
    return render(request, "restaurante/base.html")


def agregar_persona(request):
    if request.method == "POST": # Verifica si la solicitud es un POST (cliente envia a servidor datos)
        # Si la solicitud es un POST, se procesan los datos del formulario
        # Crear una nueva persona con los datos del formulario y lo envía
        Persona.objects.create(  # Crear una nueva persona con los datos del formulario y lo envía a la base de datos
            nombre=request.POST["nombre"], # Obtener el nombre del formulario
            apellido=request.POST["apellido"], # Obtener el apellido del formulario
            telefono=request.POST["telefono"] # Obtener el teléfono del formulario

        )
        return redirect("home") # Redirigir a la página de inicio después de agregar la persona
    # Si la solicitud no es POST, renderizar el formulario para agregar una persona
    return render(request, "restaurante/agregar_persona.html")

def agregar_restaurante(request):
    if request.method == "POST":
        Restaurante.objects.create(
            nombre=request.POST["nombre"],
            tipo_comida=request.POST["tipo_comida"]
        )
        return redirect("home")
    return render(request, "restaurante/agregar_restaurante.html")

def agregar_reserva(request):
    if request.method == "POST":
        Reserva.objects.create(
            dia=request.POST["dia"],
            hora=request.POST["hora"],
            cant_personas=request.POST["cant_personas"]
        )
        return redirect("home")
    return render(request, 'restaurante/agregar_reserva.html')

def buscar_persona(request):
    personas = []
    if "buscar" in request.GET:
        personas = Persona.objects.filter(nombre__icontains=request.GET["buscar"])
    return render(request, "restaurante/buscar_persona.html", {"personas": personas})


"""
def personas(request): # para cargar personas en la vista manualmente
#        return HttpResponse("hola personas")
        personas_en_lista = [
                {'nombre': 'Juan', 'apellido': 'Pérez', 'telefono': '123456789'},
                {'nombre': 'Ana', 'apellido': 'Gómez', 'telefono': '987654321'},
        ]
        context = {'personas': personas_en_lista}
        # return render(request, 'restaurante/personas.html', context)
        return render(request, 'restaurante/personas.html', context)
        # return render(request, 'restaurante/personas.html')


"""

