# Instrucciones para ejecutar este proyecto

- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/coder-live-class/django-coderhouse-project.git

cd django-coderhouse-project

git checkout class_22

```

- Crear y activar entorno virtual (Windows)
```bash
C:\>python -m venv c:\ruta\al\entorno\virtual
C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat
```

- Crear y activar entorno virtual (Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```
- Instalar Django
```bash
pip install Django
```

- Crear base de datos con los Modelos (hacer migraciones y migrar)
```bash
python manage.py makemigrations app_coder

python manage.py migrate
```

- Crear super-usuario
```bash
python manage.py createsuperuser
```

- Ejecutar proyecto
```bash
python manage.py runserver
```
# Comandos básicos para Git

## Git clone
Git clone es un comando para descargarte el código fuente existente desde un repositorio remoto (como Github, por ejemplo). Descarga la última versión de tu proyecto en un repositorio y la guarda en tu ordenador
```bash
git clone <https://link-con-nombre-del-repositorio>
```

## Git branch
- Creando una nueva rama:
```bash
git branch <nombre-de-la-rama>

```
- Visualización de ramas:
```bash
git branch
git branch --list
```
- Borrar una rama:
```bash
git branch -d <nombre-de-la-rama>
```

## Git checkout
- Para cambiarte a una rama existente
```bash
git checkout <nombre-de-la-rama>
```
- Para crear y cambiarte a esa rama al mismo tiempo
```bash
git checkout -b <nombre-de-tu-rama>

```

## Git status
El comando de git status nos da toda la información necesaria sobre la rama actual:
- Si la rama actual está actualizada
- Si hay algo para confirmar, enviar o recibir (pull).
- Si hay archivos en preparación (staged), sin preparación(unstaged) o que no están recibiendo seguimiento (untracked)
- Si hay archivos creados, modificados o eliminadosstatus
```bash
git status
```

## Git add
- Añadir un único archivo:
```bash
git add <archivo>
```

- Añadir todo de una vez:
```bash
git add -A
git add .
```
***Importante: El comando ``git add`` almacena en el ``stage`` los cambios de los archivos sin embargo aún no quedan registrados en el repositorio hasta que se utilice el comando de confirmación ``git commit`` para registrar un punto de control de los cambios.***

## Git commit
Git commit establece un punto de control al cual puedes volver más tarde si es necesario.
Resulta muy aconsejable escribir un mensaje corto para explicar qué hemos desarrollado o modificado en el código fuente.

```bash
git commit -m "mensaje de confirmación"
```

## Git push
Después de haber confirmado tus cambios, el siguiente paso que quieres dar es enviar tus cambios al servidor remoto. Git push envía tus commits al repositorio remoto.
```bash
git push <nombre-remoto> <nombre-de-tu-rama>
git push origin <nombre-de-tu-rama>
```
***Importante: Git push solamente carga los cambios que han sido confirmados con un ``git commit``.***

## Git pull
El comando git pull se utiliza para recibir actualizaciones del repositorio remoto.
```bash
git pull <nombre-remoto> <nombre-de-tu-rama>
git pull origin master
```
## Git remote
Sirve para cambiar la dirección url del repositorio que tenemos por origin.
```bash
git remote set-url origin <url_de_tu_repositorio_en_GitHub>
git remote set-url origin https://github.com/coder-live-class/django-coderhouse-project.git
```