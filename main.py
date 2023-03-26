# Archivo principal del proyecto

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles #* Este módulo permite servir archivos estáticos como imágenes, CSS, JavaScript, etc. asincronamente.
from core.config import settings

from db.session import engine #engine de db.session, que es una instancia de SQLAlchemy que permite conectar con la base de datos a través de funciones para crear, insertar, modificar y eliminar registros.
from db.base import Base #Base que a su vez esta en de db.base_class
from apis.base import api_router  #Importa las Rutas de la API

""" Este código importa el objeto general_pages_router del módulo route_homepage que se encuentra en la carpeta 
apis.general_pages
. Presumiblemente, este objeto es una instancia de un enrutador que maneja las rutas relacionadas
con la página de inicio para una API. """



app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

def include_router(app):
    #* Básicamente, lo que esta función hace es agregar un conjunto predeterminado de rutas y controladores al
    #* objeto app para que pueda ser utilizado por un servidor web.
    app.include_router(api_router)

def configure_static(app):
    #* Este código configura el servidor para que sirva archivos estáticos (como imágenes, hojas de estilo y archivos de JavaScript)
    #* en una ruta determinada en lugar de siempre devolver una respuesta HTTP al procesar una petición.
    app.mount("/static", StaticFiles(directory="static"), name="static")
    
def create_tables():
    #* Este código se utiliza para crear todas las tablas en una base de datos utilizando los modelos de SQLAlchemy.
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)


def start_application():
    #* Esta función inicializa fastapi con la configuración de la aplicación importada desde settings.py
    #* y usa la funcion include_router para agregar las rutas predeterminadas a la aplicación.
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()
    return app

app = start_application()