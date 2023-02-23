## Comandos utilizados durante la creación del proyecto

### Consideraciones iniciales.

El equipo utilizado tiene instalado OpenSuse Leap 15.4 con python 3.6.15

### Creación del directorio para el proyecto.

mkdir helloProject
cd helloProject
python3 -m venv venv
. venv/bin/activate
pip install flask
mkdir home
cd home
vi hello.py 

### Ejecución del proyecto 

export FLASK_APP=hello.py
flask run
