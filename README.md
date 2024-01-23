# Gestión de Socios

El Sistema de Gestión de Información para Socios de San Francisco está diseñado para optimizar y facilitar la gestión de datos relacionados con los miembros de la comunidad.

## Backend

El backend está construido con Django Rest Framework 4.1 y Python 3.10.

### Pasos para la creación del backend

#### Instalación de [Python 3.10](https://www.python.org/downloads/)
1. Descargar y seguir los pasos de la documentación.

#### Instalación de [Django Rest Framework](https://www.django-rest-framework.org/)
1. Instalar un entorno virtual para el proyecto de Django con `python -m venv`.
2. Activar el entorno virtual de esta forma: `.\venv\Scripts\activate` o de esta forma: `source env/Scripts/activate`.
3. Ejecutar `pip list` para ver los paquetes por defecto.
4. Instalar Django con `pip install django==4.1.*`, recomendado en la documentación para evitar inconvenientes.
5. Ejecutar `pip list` para verificar los paquetes correctos.
6. Instalar Django Rest Framework con `pip install djangorestframework`.
7. Crear el proyecto Django con `django-admin startproject app`.
8. Iniciar el servidor con `python app/manage.py runserver`.

### Iniciar el Proyecto
1. Instalar un entorno virtual para el proyecto de Django con `python -m venv venv`.
2. Activar el entorno virtual de esta forma: `.\venv\Scripts\activate` o de esta forma : `source venv/Scripts/activate` si usamos la consola git bash.
3. Instalar los paquetes ejecutando `pip install -r requirements.txt`.
4. Ejecutar las migraciones con este comando `python app/manage.py migrate`.
5. Crear un usuario para ingresar al administrador de Django `python app/manage.py createsuperuser`.
6. Ejecutar el backend con `python app/manage.py runserver`.

## Frontend

El frontend está construido con Vue3.

### Pasos para la creación del frontend

#### Instalación de [Vue](https://vuejs.org/guide/quick-start)
1. Verificar la versión de yarn con `yarn --version`. Si no tiene ninguna versión, instalar con `npm install --global yarn`, siguiendo las sugerencias recomendadas en la documentación de [yarn](https://yarnpkg.com/getting-started/install) para prevenir posibles errores.
2. Desde la consola ingresar al proyecto app creado anteriormente con Django y seguir los siguientes pasos.
3. Ejecutar `yarn create vue@latest` y seguir las recomendaciones de instalación de [Vue](https://vuejs.org/guide/quick-start).
4. Si hay problemas de instalación, ejecutar `npx create-vue@latest` para crear el proyecto de forma local.
5. Desde la consola ingresar a la carpeta vue y ejecutar `yarn` para instalar los paquetes necesarios.
6. Ejecutar `yarn dev`, ingresar a la URL `http://localhost:5173/` desde el navegador y debería mostrar la página de Vue.
7. Agregar el `.gitignore` para node_modules, dist y cache.

#### Configurar el frontend
Esto es necesario para poder ejecutar los comandos de yarn desde la raíz del proyecto.
  1. Copiar `package.json`, `vite.config.js`, `yarn.lock` y `node_modules` a la raíz del proyecto.
  2. Ejecutar otra vez `yarn dev` y el proyecto debería seguir funcionando correctamente.

### Iniciar el Proyecto
1. Ejecutar `yarn` en la raíz del proyecto.
2. Ejecutar `yarn dev` en la raíz del proyecto.
3. Ingresar a la URL `http://localhost:5173/`.