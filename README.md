Mi aplicación web en Render 🚀
Descripción

Este proyecto consiste en una pequeña aplicación web desarrollada con Python y Flask, desplegada en la plataforma Render.

La aplicación muestra un mensaje de bienvenida en su página principal y dispone de una ruta adicional para consultar el estado del servidor mediante datos en formato JSON.

Tecnologías utilizadas
Python
Flask
Gunicorn
GitHub
Render
Estructura del proyecto
text
mi-app-render/
│
├── app.py
├── requirements.txt
└── README.md

Funcionalidades
Página principal (/): muestra un mensaje de bienvenida indicando que la aplicación funciona correctamente.
Estado del servidor (/status): devuelve información del servidor en formato JSON, incluyendo el estado, el nombre del equipo y la versión de Python.
Instalación y ejecución local
Clonar el repositorio:
bash
git clone https://github.com/TU-USUARIO/mi-app-render.git

Entrar en la carpeta:
bash
cd mi-app-render

Instalar las dependencias:
bash
pip install -r requirements.txt

Ejecutar la aplicación:
bash
python app.py

Abrir en el navegador:
text
http://localhost:5000

Despliegue en Render

La aplicación está preparada para desplegarse en Render utilizando los siguientes comandos:

Build Command:

bash
pip install -r requirements.txt


Start Command:

bash
gunicorn app:app


Render permite desplegar automáticamente los cambios realizados en el repositorio de GitHub.

Enlaces del proyecto
Aplicación web: PENDIENTE DE AÑADIR URL DE RENDER.
Repositorio: https://github.com/TU-USUARIO/mi-app-render
Autor

Proyecto realizado como práctica de desarrollo y despliegue de aplicaciones web con Python, Flask y Render.

Proyecto educativo.
