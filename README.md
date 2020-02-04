# sabescomotedicen
Aplicacion sobre dichos de todo tipo, color, grado


## Pre-task

Correr **pip install -r requerimientos.txt** para instalarse dependencias.

## Correr servidor

**python manage.py runserver**

Deja publicado en el puerto 8000 la api. \
Para cambiar host y puerto agregar **host:port**


## Realizar migraciones

Aplica los cambios en los modelos definios sobre la base de datos que estemos manejando.

Crear migracion: **python manage.py makemigrations** \
Aplicar migracion: **python manage.py migrate**


Archivo settings.py
Se tiene toda la configuracion de la aplicacion, conexion con base de datos y demas.
