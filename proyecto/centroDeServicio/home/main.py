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

def consultarCaso(session):
    sql = select(ControlSoportes) \
        .select_from(join(ControlSoportes, Empleados )) 
    resultado = session.execute(sql).fetchone()
    #resultado = session.scalars(sql)
    return resultado

def consultarUsuario(session): 
    sql = text("SELECT NOMBRES||' '||PRIMERAPELLIDO||' '||SEGUNDOAPELLIDO FROM SPTEMPLEADOSOPORTES WHERE NUMERODOCUMENTO = 38")
    resultado = session.execute(sql).fetchone()
    return resultado

def consultarCantidadCasos(session):
    sql = text("SELECT COUNT(*) FROM SPTCONTROLSOPORTES") 
    resultado = session.execute(sql).fetchone()
    #resultado = session.scalars(sqlConteo)
    return resultado

def consultarCantidadCasosPropios(session):
    sql = text("SELECT COUNT(*) FROM SPTCONTROLSOPORTES CS, SPTEMPLEADOSOPORTES E WHERE CS.SPTEMPLEADOSOPORTE = E.SECUENCIA AND E.NUMERODOCUMENTO = 38") 
    resultado = session.execute(sql).fetchone()
    #resultado = session.scalars(sqlConteo)
    return resultado

def consultarPorcentajeAvance(session):
    sql = text("SELECT ROUND((((SUM(CS.TOTALTIEMPOENTERO)*60+SUM(CS.TOTALTIEMPOFRACCION))-MOD((SUM(CS.TOTALTIEMPOENTERO)*60+SUM(CS.TOTALTIEMPOFRACCION)),60))/60)/(240-32)*100,0) P FROM SPTCONTROLSOPORTES CS, SPTEMPLEADOSOPORTES E WHERE CS.SPTEMPLEADOSOPORTE = E.SECUENCIA AND E.NUMERODOCUMENTO = 38 AND CS.HORAINICIO BETWEEN TRUNC(SYSDATE,'MM') AND LAST_DAY(SYSDATE) ")
    resultado = session.execute(sql).fetchone()
    return resultado

def consultarCasosPausados(session):
    sql = text("SELECT COUNT(*) FROM SPTCONTROLSOPORTES CS, SPTEMPLEADOSOPORTES E WHERE CS.SPTEMPLEADOSOPORTE = E.SECUENCIA AND E.NUMERODOCUMENTO = 38 AND CS.ESTADO IN ('I', 'P') ")
    resultado = session.execute(sql).fetchone()
    return resultado

@app.route("/")
def index():
    #Session = sessionmaker(bind=engine)
    #session = Session()
    #controlSoporte_todos = consultarCaso(session)
    #session.commit()
    #print(controlSoporte_todos)

    Session = sessionmaker(bind=engine)
    session = Session()
    nombreUsuario = consultarUsuario(session)
    session.commit()
    print(nombreUsuario)

    Session = sessionmaker(bind=engine)
    session = Session()
    conteoCasos = consultarCantidadCasos(session)
    session.commit()
    print(conteoCasos)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    conteoCasosPropios = consultarCantidadCasosPropios(session)
    session.commit()
    print(conteoCasosPropios)

    Session = sessionmaker(bind=engine)
    session = Session()
    porcentajeAvance = consultarPorcentajeAvance(session)
    session.commit()
    print(porcentajeAvance)

    Session = sessionmaker(bind=engine)
    session = Session()
    casosPausados = consultarCasosPausados(session)
    session.commit()
    print(casosPausados)

    return render_template('index.html',nombreusuario=nombreUsuario, conteocasos=conteoCasos, casospropios=conteoCasosPropios, porcentajeavance=porcentajeAvance, casospausados=casosPausados)


if __name__ == "__main__":
    app.run(debug=True)