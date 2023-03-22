# Archivo principal del proyecto

from fastapi import FastAPI
from core.config import settings

""" Este código importa el objeto general_pages_router del módulo route_homepage que se encuentra en la carpeta 
apis.general_pages
. Presumiblemente, este objeto es una instancia de un enrutador que maneja las rutas relacionadas
con la página de inicio para una API. """
from apis.general_pages.route_homepage import general_pages_router #Rutas predeterminadas


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

def include_router(app):
    #* Básicamente, lo que esta función hace es agregar un conjunto predeterminado de rutas y controladores al
    #* objeto app para que pueda ser utilizado por un servidor web.
    
    app.include_router(general_pages_router)
    

def start_application():
    #* Esta función inicializa fastapi con la configuración de la aplicación importada desde settings.py
    #* y usa la funcion include_router para agregar las rutas predeterminadas a la aplicación.
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    return app

app = start_application()