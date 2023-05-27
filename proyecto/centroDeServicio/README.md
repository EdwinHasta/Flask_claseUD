# Centro de servicio 
#### Un ejemplo de uso de Flask conectando a Oracle Database. 

## Screenshots

![Captura de la página principal!](screenshot_index.png "Centro de servicio")

## Description
Centro de servicio es un proyecto académico que utiliza como base un proyecto estándar en Flask modificando la plantilla en Bootstrap disponible en <a target="_blank" href="https://startbootstrap.com/theme/sb-admin-2">SB Admin 2</a>. Para el almacenamiento de datos se hace uso de una conexión a una base de datos Oracle. Tal conexión se establece utilizando python-oracledb. 

## Comandos utilizados durante la creación del proyecto

### Consideraciones iniciales.

El equipo utilizado tiene instalado OpenSuse Leap 15.4 con python 3.8.16

### Creación del directorio para el proyecto.

``mkdir proyecto `` <br/>
``cd proyecto `` <br/>
``mkdir modelodb `` <br/>
``mkdir centroDeServicio `` <br/>
``cd centroDeServicio `` <br/>
``python3 -m ensurepip --upgrade `` <br/>
``python3 -m venv venv`` <br/>
``. venv/bin/activate `` <br/>
``python3 -m pip install --upgrade pip `` <br/>
``pip install flask `` <br/>
``pip install sqlalchemy `` <br/>
``pip install werkzeug `` <br/>
``# pip install cx_Oracle #No se utilizó`` <br/>
``pip install oracledb `` <br/>
``mkdir home `` <br/>
``cd home `` <br/>
``vi main.py `` <br/>
``mkdir templates `` <br/>
``cd templates ``<br/>
``vi index.html ``<br/>

### Ejecución del proyecto 
``. venv/bin/activate `` <br/>
``export PYTHON_USERNAME=SPT `` <br/>
``export PYTHON_PASSWORD=SPT `` <br/>
``export PYTHON_CONNECTSTRING="192.168.3.47/C02DB01" `` <br/>
``export FLASK_APP=main.py `` <br/>
``cd home `` <br/>
``flask run `` <br/>

### Rutas a probar 

`` http://127.0.0.1:5000 `` <br/>



