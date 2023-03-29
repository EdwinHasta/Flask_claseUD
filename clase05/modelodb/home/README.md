## Comandos utilizados durante la creación del proyecto

### Consideraciones iniciales.

El equipo utilizado tiene instalado OpenSuse Leap 15.4 con python 3.6.15

### Creación del directorio para el proyecto.

``mkdir modelodb `` <br/>
``cd modelodb `` <br/>
``python3 -m venv venv`` <br/>
``. venv/bin/activate `` <br/>
``python3 -m pip install --upgrade pip `` <br/>
``pip install flask `` <br/>
``mkdir home `` <br/>
``cd home `` <br/>
``vi main.py `` <br/>
``mkdir templates `` <br/>
``cd templates ``<br/>
``vi layout.html ``<br/>
``vi index.html ``<br/>
``vi new-user.html ``<br/>

### Ejecución del proyecto 

``export FLASK_APP=main.py `` <br/>
``flask run `` <br/>

### Rutas a probar 

`` http://127.0.0.1:5000 `` <br/>


