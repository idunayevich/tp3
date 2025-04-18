Sistema de reservas de Restaurante

Este proyecto es una web en Django estilo blog muy sencilla, utilizando el patrón MVT de Django y herencia de plantillas, utilizando patrón MVT y Herencia de plantillas, con un modelo de 3 clases:
Modelos:
1. Persona: Nombre, Apellido, Telefono
2. Restaurante: Nombre, Tipo de comida
3. Reserva: dia, hora, cant de personas

Debe contar con un formulario para ingresar datos y otro para buscar personas.
Al no ser parte del curso, se tomaron html de chatgpt.

La aplicación dentro del proyecto es: restaurante

Funcionalidades

- Agregar persona
- Agregar restaurante
- Agregar reserva
- Buscar personas por nombre

Archivos modificados:
urls.py (URLs), views.py (funciones), settings.py (variables), models.py (clases), templates/restaurante (html)

Pruebas

1. Descargar el proyecto (clonar).
$ git clone https://github.com/....
$ cd proyecto
2. Activar enorno virtual:
$ python3 -m venv .venv
$ source .venv/bin/activate

3. Ejecutá las migraciones (especialmente para actualizar el modelo de base de datos a partir de los models.py):
$ python manage.py makemigrations # define, crea los scripts
$ python manage.py migrate # implementa

3. Iniciar el servidor:
python manage.py runserver

4. Probar las páginas:
- `/` Página principal
- `/persona/` Agregar persona
- `/restaurante/` Agregar restaurante
- `/reserva/` Agregar reserva
- `/buscar/` Buscar persona
- `/admin/` panel de administración (crear superusuario con  python manage.py createsuperuser)

4.1 registrar persona

4.2 registrar restaurante

4.3 registrar una reserva

4.4 buscar una persona

4.5 verificar en admin lo realizado

