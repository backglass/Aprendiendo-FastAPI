# Importamos las librerías necesarias
from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

#* Importamos la función list_jobs de la carpeta jobs del archivo repository y la función get_db de session del archivo db
from db.repository.jobs import list_jobs
from db.session import get_db

#* Creamos una variable templates que permitirá cargar plantillas HTML
templates = Jinja2Templates(directory="templates")

#* Creamos una variable router que nos permitirá definir rutas para nuestra API
router = APIRouter(include_in_schema=False)

#* Definimos la ruta principal de la API "/"
@router.get("/")
async def home(request: Request, db: Session=Depends(get_db)):
    #* Llamamos a la función list_jobs para obtener una lista de trabajos desde nuestra base de datos
    jobs = list_jobs(db=db)
    
    #* Devolvemos una respuesta utilizando una plantilla HTML llamada "homepage.html", junto con una variable "jobs" que contiene la lista de trabajos obtenida anteriormente
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request, "jobs": jobs})



# Este código crea una ruta en una API de FastAPI, que hace una solicitud GET al directorio raíz.
# Cuando se accede al directorio raíz, se ejecuta la función home que utiliza la dependencia get_db() para
# obtener una conexión de base de datos.

# La función home llama a list_jobs() que es una función de un módulo denominado jobs que se encarga de listar
# todos los trabajos disponibles.
# Los trabajos se pasan como un contexto a la plantilla HTML llamada "general_pages/homepage.html", junto
# con una solicitud request.

# En resumen, lo que hace este código es listar los trabajos disponibles en una página web en el directorio raíz
# de la API de FastAPI