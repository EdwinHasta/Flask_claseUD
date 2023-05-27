import os
import oracledb
from flask import Flask, request, render_template, url_for
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Identity, create_engine, select, join
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import relationship, backref, sessionmaker, declarative_base
from sqlalchemy import text

import random

app = Flask(__name__)

un = os.environ.get('PYTHON_USERNAME')
pw = os.environ.get('PYTHON_PASSWORD')
dsn = os.environ.get('PYTHON_CONNECTSTRING')

hostname, service_name = dsn.split("/")
port = 1521 

pool = oracledb.create_pool(user=un, password=pw,
                            host=hostname, port=port, service_name=service_name,
                            min=1, max=4, increment=1)

engine = create_engine("oracle+oracledb://", creator=pool.acquire, poolclass=NullPool)

Base = declarative_base()

class ClasificacionesCasos(Base):
    __tablename__ = 'CLASIFICACIONESCASOS'

    # Every SQLAlchemy table should have a primary key named 'id'
    secuencia = Column(Integer, Identity(start=1), primary_key=True)

    codigo = Column(String(20))
    descripcion = Column(String(50))
    

    # Print out a user object
    def __repr__(self):
       return f"ClasificacionesCasos(codigo='{self.codigo}', descripcion='{self.descripcion}')"

class Empleados(Base):
    __tablename__ = 'SPTEMPLEADOSOPORTES'
    secuencia = Column(Integer, Identity(start=1), primary_key=True)
    NOMBRES = Column(String(20))
    PRIMERAPELLIDO = Column(String(20))
    SEGUNDOAPELLIDO = Column(String(20)) 

    def __repr__(self):
        return f"Empleados(NOMBRES='{self.NOMBRES}', PRIMERAPELLIDO='{self.PRIMERAPELLIDO}', SEGUNDOAPELLIDO='{self.SEGUNDOAPELLIDO}')"

class ControlSoportes(Base):
    __tablename__ = 'SPTCONTROLSOPORTES'
    secuencia = Column(Integer, Identity(start=1), primary_key=True)
    codigo = Column(String(20))
    CLASIFICACIONCASO = Column(Integer, ForeignKey('CLASIFICACIONESCASOS.secuencia'))
    clasificacionCasoR = relationship("ClasificacionesCasos", backref=backref('SPTCONTROLSOPORTES'))
    SPTEMPLEADOSOPORTE = Column(Integer, ForeignKey('SPTEMPLEADOSOPORTES.secuencia'))
    empleadoSoporteR = relationship("Empleados", backref=backref('SPTCONTROLSOPORTES'))
    
    def __repr__(self):
        return f"ControlSoportes(codigo='{self.codigo}', Empleado='{self.empleadoSoporteR}')"


@app.route("/")
def index():
    # Create a session to the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query the user that has the e-mail address ed@google.com
    sql = select(ControlSoportes) \
        .select_from(join(ControlSoportes, Empleados )) 
    controlSoporte_todos = session.execute(sql).fetchone()
    print(controlSoporte_todos)
    sqlConteo = text("SELECT COUNT(*) FROM SPTCONTROLSOPORTES") 
    conteoCasos = session.execute(sqlConteo)
    print(conteoCasos)
    return render_template('index.html',conteocasos=conteoCasos)


if __name__ == "__main__":
    app.run(debug=True)