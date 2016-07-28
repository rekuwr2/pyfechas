Instrucciones:
1. Descomprimir zip
2. Crear virtualenv
3. Con virtualenv activado, pip install -r requirements/base.txt desde la raíz del proyecto
4. python manage.py makemigrations; python manage.py migrate para crear la base de datos (embedded SQLite)
5. python manage.py runserver para iniciar el servidor por defecto de Django
6. python manage.py test para ejecutar los tests existentes
7. http://localhost:8000/registro_fechas/search --> Página de inicio, podríamos convertirla en un listado
8. http://localhost:8000/registro_fechas/new --> Formulario donde añadimos el campo fecha, de momento tiene un "Nombre"
9.  TODO: Ejercicio de las diapositivas: Campo fecha que se guarda a partir del formulario,
10. TODO: Comprobar que la fecha sea mayor o igual a la actual
11. TODO: Otras validaciones que podríamos hacer con este campo

Recordad: Primero se escribe el test, lo ejecutamos y falla, y luego implementamos la funcionalidad correspondiente para pasar el test
