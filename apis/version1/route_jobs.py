from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import create_new_job
from db.repository.jobs import retrieve_job
from db.repository.jobs import list_jobs
"""
Este código define un APIRouter desde la biblioteca FastAPI de Python y define un endpoint
POST "/create-job". Cuando se llama a este endpoint, se crea una nueva tarea en la base de datos
utilizando los datos de entrada proporcionados por el usuario.
Esto se realiza mediante el uso de las clases JobCreate y ShowJob en el archivo "schemas/jobs.py"
para validar los datos de entrada y salida del usuario.
También se usa la clase Job en "db/models/jobs.py" para leer y escribir datos de la base de datos.
La clase create_new_job definida en "db/repository/jobs.py" se utiliza para crear un nuevo trabajo
en la base de datos y, finalmente, se devuelve el trabajo recién creado al usuario.
La clase retrieve_job definida en "db/repository/jobs.py" se utiliza para recuperar un trabajo
"""



router = APIRouter()


@router.post("/create-job", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job, db=db, owner_id=current_user)
    return job


# Crear una ruta GET que recibe un id y retorna un trabajo
@router.get("/get/{id}", response_model=ShowJob)
def read_job(id: int, db: Session = Depends(get_db)):
    # Llamar a la función que buscará el trabajo en la base de datos
    job = retrieve_job(id=id, db=db)
    # Si el trabajo no existe, levantar una excepción 404
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with the id {id} is not available")
    # Si el trabajo existe, retornarlo
    return job


#* Definimos la ruta '/all' y su método GET, especificando que devolverá una lista de
# *ShowJob
@router.get("/all", response_model=list[ShowJob])
def read_jobs(db: Session = Depends(get_db)):
    #* Obtenemos la lista de todos los trabajos
    jobs = list_jobs(db=db)
    
    #* Retornamos la lista de trabajos
    return jobs
