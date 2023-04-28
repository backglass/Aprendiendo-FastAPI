# Importamos las librerías necesarias
from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session


from db.repository.jobs import list_jobs
from db.session import get_db
from db.repository.jobs import retrieve_job
from db.repository.jobs import search_job

from db.models.users import User
from apis.version1.route_login import get_current_user_from_token
from webapps.jobs.forms import JobCreateForm
from schemas.jobs import JobCreate
from db.repository.jobs import create_new_job
from fastapi import responses, status
from fastapi.security.utils import get_authorization_scheme_param

from typing import Optional


#* Creamos una variable templates que permitirá cargar plantillas HTML
templates = Jinja2Templates(directory="templates")


router = APIRouter(include_in_schema=False)

#* Definimos la ruta principal de la API "/"
@router.get("/")
async def home(request: Request, db: Session=Depends(get_db),msg: str = None):
    """Se llama a la función list_jobs() que lista todos los trabajos en la base de datos.
       Luego, la plantilla HTML 'homepage.html' se inserta con la lista de trabajos y un mensaje opcional."""
    
    jobs = list_jobs(db=db)
    print ("jobs: ", jobs)
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request, "jobs": jobs, "msg": msg})


@router.get("/details/{id}")
def job_detail(id: int, request: Request, db: Session=Depends(get_db)):
    """Toma un parámetro de "id" que especifica el trabajo a mostrar. Luego llama a la función retrieve_job()
       que busca el trabajo en la base de datos utilizando el "id" especificado. Finalmente, se carga la
       plantilla HTML 'detail.html' y se muestra el trabajo en la página."""
       
    job = retrieve_job(id=id, db=db)
    print("job: ")
    return templates.TemplateResponse("jobs/detail.html", {"request": request, "job": job})

@router.get("/post-a-job")
def create_job(request: Request, db: Session=Depends(get_db)):
    """un controlador para la página de creación de trabajos. Simplemente carga la plantilla HTML
      'create_job.html' y muestra el formulario para crear trabajos."""
      
    return templates.TemplateResponse("jobs/create_job.html", {"request": request})

@router.post("/post-a-job")
async def create_job(request: Request, db: Session=Depends(get_db)):
    """se llama cuando el usuario presenta un formulario de creación de trabajo. En primer lugar, se carga el
       formulario con los datos presentados por el usuario.
       Luego, se verifica si el formulario es válido (por ejemplo, si se proporcionaron todos los campos
       obligatorios).
       Si el formulario es válido, se verifica la autenticación del usuario a través del token de acceso que
       se encuentra en las cookies de la solicitud. Se llama a la función get_current_user_from_token()
       para obtener información del usuario del token de acceso. Si se encuentra un usuario válido,
       se crea un nuevo trabajo con la información del formulario de creación de trabajo y se agrega a la
       base de datos utilizando la función create_new_job().
       Finalmente, se redirige al usuario a la página de detalles del trabajo recién creado.
       Si ocurre algún error, se muestra el formulario de creación de trabajo con los errores apropiados."""
       
    
    # Se crea un objeto formulario para crear un trabajo
    form = JobCreateForm(request)

    # Se carga la información enviada en el formulario
    await form.load_data()

    # Si el formulario es válido
    if form.is_valid():

        try:
            # Se obtiene el token de acceso de las cookies de la solicitud
            token = request.cookies.get("access_token")

            # Se obtiene el emblema de autorización y los parámetros del token de acceso
            scheme, param = get_authorization_scheme_param(token)

            # Se obtiene al usuario actual a través del token de acceso
            current_user : User = get_current_user_from_token(token=param, db=db)

            # Se crea una nueva oferta de trabajo con los datos enviados del formulario
            job = JobCreate(**form.__dict__)

            # Se asigna el propietario de la oferta de trabajo
            job = create_new_job(job=job, db=db, owner_id=current_user.id)

            # Se redirecciona a la página de detalles de la nueva oferta de trabajo creada
            return responses.RedirectResponse(f"/details/{job.id}", status_code=status.HTTP_302_FOUND)

        except Exception as e:
            # En caso de que no se pueda crear una nueva oferta de trabajo, se muestra un mensaje de error
            print(e)
            form.__dict__.get("errors").append("You are not logged in")

            # Se devuelve una plantilla de respuesta de formulario HTML para que el usuario corrija los errores
            return templates.TemplateResponse("jobs/create_job.html", form.__dict__)

    # Si el formulario no es válido, se devuelve una plantilla de respuesta de formulario HTML para que el usuario corrija los errores
    return templates.TemplateResponse("jobs/create_job.html", form.__dict__)

@router.get("/delete-job/")
def show_jobs_to_delete(request: Request, db: Session=Depends(get_db)):
    """Se muestra una lista de trabajos que el usuario puede eliminar. Se carga la plantilla HTML
       'show_jobs_to_delete.html' con la lista de trabajos."""
       
    jobs = list_jobs(db=db)
    return templates.TemplateResponse("jobs/show_jobs_to_delete.html", {"request": request, "jobs": jobs})



@router.get("/search/")
def search(request: Request, db: Session=Depends(get_db), query: Optional[str] = None):
    """"request" que representa la solicitud HTTP.
        "db" que es una instancia de la sesión de la base de datos.
        "query" que es un parámetro opcional que se utiliza para determinar qué datos deben ser buscados
        en la base de datos.
        
        La función utiliza el parámetro "query" para buscar trabajos en la base de datos llamando a otra
        función llamada "search_job". Luego, la función devuelve una respuesta HTTP renderizando un archivo
        de plantilla HTML llamado "homepage.html" que se encuentra en una carpeta llamada "general_pages"
        junto con los trabajos encontrados.
        """
    jobs = search_job(query, db=db)
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request, "jobs": jobs})

#! Explicar de nuevo lo de abajo con codeGpt
""" 
Este código crea un API Router utilizando FastAPI y define varias rutas para crear, leer y actualizar trabajos
en una base de datos. También se utiliza Jinja2Templates para cargar plantillas HTML. El código proporciona
funciones para listar trabajos, obtener detalles de trabajos, crear nuevos trabajos y mostrar formularios para
crear y editar trabajos. Cada ruta define su propia lógica para interactuar con la base de datos y/o
formularios. Las funciones también dependen de una sesión de base de datos. Adicionalmente, se implementa 
la seguridad con tokens de usuario. """


