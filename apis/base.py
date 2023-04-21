""" Este código importa tres módulos: 
    APIRouter de FastAPI, y dos módulos personalizados (rutas para páginas generales
    y rutas para usuarios) desde el paquete version1 ubicado en apis.
    
Luego se crea una instancia de APIRouter() y se le agrega dos rutas usando el método
.include_router(): una para páginas generales y otra para usuarios,
cada una con su propio prefijo y etiquetas.

Por último, la instancia completa del router se asigna a la variable api_router. """


from fastapi import APIRouter
from apis.version1 import route_general_pages
from apis.version1 import route_users
from apis.version1 import route_jobs
from apis.version1 import route_login

api_router = APIRouter()


api_router = APIRouter()
#! Eliminado api_router.include_router(route_general_pages.general_pages_router,prefix="",tags=["general_pages"])
api_router.include_router(route_users.router,prefix="/users",tags=["users"])
api_router.include_router(route_jobs.router,prefix="/jobs",tags=["jobs"])
api_router.include_router(route_login.router,prefix="/login",tags=["login"])