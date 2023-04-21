from webapps.jobs import route_jobs
from fastapi import APIRouter

""" Este código importa la función route_jobs del módulo webapps.jobs y la asocia con una instancia de la clase
APIRouter de FastAPI para crear y configurar rutas de la API web. Luego, se incluye esta ruta dentro de otra
ruta (en este caso, prefix="" indica que no hay prefijo de ruta) y se le asigna un tag ("job-webapp")
que se utilizará para organizar y documentar la API. """

api_router = APIRouter()
api_router.include_router(route_jobs.router, prefix="", tags=["job-webapp"])