## Comandos utilizados durante la creación del proyecto

### Consideraciones iniciales.

El equipo utilizado tiene instalado OpenSuse Leap 15.4 con python 3.6.15

### Creación del directorio para el proyecto.

``mkdir rutasProject `` <br/>
``cd rutasProject `` <br/>
``python3 -m venv venv`` <br/>
``. venv/bin/activate `` <br/>
``pip install flask `` <br/>
``mkdir home `` <br/>
``cd home `` <br/>
``vi main.py `` <br/>
``mkdir templates `` <br/>
``cd templates ``<br/>
``vi hello.html ``<br/>

### Ejecución del proyecto 

``export FLASK_APP=hello.py `` <br/>
``flask run `` <br/>

### Rutas a probar 

`` http://127.0.0.1:5000 `` <br/>
`` http://127.0.0.1:5000/magic `` <br/>
`` http://127.0.0.1:5000/person/edwin `` <br/>
`` http://127.0.0.1:5000/template  `` <br/>
`` http://127.0.0.1:5000/login?name=juan&password=12345 `` <br/>

