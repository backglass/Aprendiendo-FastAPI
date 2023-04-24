# Importamos las librerías necesarias
from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session


from db.repository.jobs import list_jobs
from db.session import get_db
from db.repository.jobs import retrieve_job

#* Creamos una variable templates que permitirá cargar plantillas HTML
templates = Jinja2Templates(directory="templates")


router = APIRouter(include_in_schema=False)

#* Definimos la ruta principal de la API "/"
@router.get("/")
async def home(request: Request, db: Session=Depends(get_db),msg: str = None):

    jobs = list_jobs(db=db)
    print ("jobs: ", jobs)
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request, "jobs": jobs, "msg": msg})


@router.get("/details/{id}")
def job_detail(id: int, request: Request, db: Session=Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    print("job: ")
    return templates.TemplateResponse("jobs/detail.html", {"request": request, "job": job})

""" 
La variable templates se usa para cargar plantillas HTML que se mostrarán en la página web.
La ruta principal de la API es la página de inicio y se define en la ruta "/" usando el método GET.
Esto devuelve una página HTML personalizada que incluye trabajos listados.


Además, existe otra ruta llamada "/details" que se utiliza para mostrar detalles de un trabajo en
particular, siendo id el identificador único de cada trabajo. Cuando el usuario navega a la página
"/details/{id}", se muestra una plantilla HTML personalizada con detalles de ese trabajo. """


