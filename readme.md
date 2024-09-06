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

El proyecto requiere algunas variables de entorno para configurarse correctamente. Crea un archivo `.env` en la raíz del proyecto y añade las siguientes variables:

```env
DB_NAME=store_db

DB_USER=root

DB_SECRET=root

DB_HOST=54.167.246.98

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
docker build -t nombre_imagen .
```

### 2. Ejecutar el contenedor

```bash
docker run -d -p 8000:8000 --env-file .env --name nombre_contenedor nombre_imagen
```

El proyecto estará disponible en `http://localhost:8000/`.

## Testing

Para ejecutar las pruebas unitarias:

```bash
python manage.py test
```

## Documentación de la API

Puedes acceder a la documentación de la API en:

```
https://documenter.getpostman.com/view/21621812/2sAXjRVUdV
```

## Despliegue

Para desplegar el proyecto en un entorno de producción, asegúrate de:

1. Configurar `DEBUG=False` en tu archivo `.env`.
2. Utilizar un servidor WSGI como Gunicorn.
3. Configurar adecuadamente tu servidor web (nginx, apache, etc.).
