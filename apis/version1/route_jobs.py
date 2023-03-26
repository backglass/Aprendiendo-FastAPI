from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import create_new_job
"""
Este código define un APIRouter desde la biblioteca FastAPI de Python y define un endpoint
POST "/create-job". Cuando se llama a este endpoint, se crea una nueva tarea en la base de datos
utilizando los datos de entrada proporcionados por el usuario.
Esto se realiza mediante el uso de las clases JobCreate y ShowJob en el archivo "schemas/jobs.py"
para validar los datos de entrada y salida del usuario.
También se usa la clase Job en "db/models/jobs.py" para leer y escribir datos de la base de datos.
La clase create_new_job definida en "db/repository/jobs.py" se utiliza para crear un nuevo trabajo
en la base de datos y, finalmente, se devuelve el trabajo recién creado al usuario.
"""



router = APIRouter()


@router.post("/create-job", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job, db=db, owner_id=current_user)
    return job