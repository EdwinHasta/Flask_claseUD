## Comandos utilizados durante la creación del proyecto

### Consideraciones iniciales.

El equipo utilizado tiene instalado OpenSuse Leap 15.4 con python 3.6.15

### Creación del directorio para el proyecto.

``mkdir helloProject `` <br/>
``cd helloProject `` <br/>
``python3 -m venv venv`` <br/>
``. venv/bin/activate `` <br/>
``pip install flask `` <br/>
``mkdir home `` <br/>
``cd home `` <br/>
``vi hello.py `` <br/>

### Ejecución del proyecto 

``export FLASK_APP=hello.py `` <br/>
``flask run `` <br/>
