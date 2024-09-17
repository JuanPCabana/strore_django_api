# Django REST Framework Project - Centribal

Este proyecto es una API RESTful construida con Django y Django REST Framework.

## Requisitos previos

Antes de empezar, asegúrate de tener instalados los siguientes componentes:

- Python 3.9+
- pip (gestor de paquetes de Python)
- virtualenv (opcional, pero recomendado)
- Docker (opcional, para despliegue en contenedores)

## Instalación

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone git@github.com:JuanPCabana/strore_django_api.git
cd strore_django_api
```

### 2. Crear y activar un entorno virtual (opcional pero recomendado)

Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

### 3. Instalar las dependencias

Instala las dependencias del proyecto usando `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configuración de variables de entorno

El proyecto requiere algunas variables de entorno para configurarse correctamente. Crea un archivo `.env` en la raíz del proyecto y añade las siguientes variables con los valores que correspondan:

```env
DB_NAME=store_db

DB_USER=root

DB_SECRET=root

DB_HOST=db

DB_PORT=3306

DEBUG=False
```

- `DEBUG`: Define si el modo de depuración está activado. Usa `True` para desarrollo y `False` para producción.

### 5. Migraciones de la base de datos

Aplica las migraciones a la base de datos para crear las tablas necesarias:

```bash
python manage.py migrate
```

### 6. Crear un superusuario

Crea un superusuario para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor de desarrollo

Levanta el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

La API debería estar disponible en `http://localhost:8000/`.

## Uso de Docker (Opcional)

Si prefieres usar Docker, puedes levantar el proyecto dentro de un contenedor.

### 1. Construir la imagen de Docker

```bash
docker-compose up --build
```

### 2. Crear super usuario para entrar en el django admin

```bash
docker exec -ti django_app python manage.py createsuperuser
```

El proyecto estará disponible en `http://localhost:8000/`.
El Django Admin estara disponible en `http://localhost:8000/admin` (se debera ingresar con el super usuario creado previamente para gestionar los productos y ordenes)

## Testing

Para ejecutar las pruebas unitarias:

```bash
python manage.py test
```

Desde docker:

```bash
docker exec -ti django_app python manage.py test
```

## Documentación de la API

Una vez levantado el proyecto puedes acceder a la documentación de la API con Swagger en:

```
http://localhost:8000/api/v1/docs/

ó

http://localhost:8000/api/v1/redocs/
```

## Despliegue

Para desplegar el proyecto en un entorno de producción, asegúrate de:

1. Configurar `DEBUG=False` en tu archivo `.env`.
2. Utilizar un servidor WSGI como Gunicorn.
3. Configurar adecuadamente tu servidor web (nginx, apache, etc.).
