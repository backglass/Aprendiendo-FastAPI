from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import create_new_job
from db.repository.jobs import retrieve_job
from db.repository.jobs import list_jobs
from db.repository.jobs import update_job_by_id
from db.repository.jobs import delete_job_by_id
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



# Definimos la ruta y el verbo HTTP correspondiente
@router.put("/update/{id}")
def update_job(id: int, job: JobCreate, db: Session = Depends(get_db)):
    # Obtenemos el usuario actual
    current_user = 1
    # Llamamos a la función de actualización de trabajos
    message = update_job_by_id(id=id, job=job, db=db, owner_id=current_user)
    # Si la función devuelve un valor falso, lanzamos una excepción 404
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with the id {id} is not available")
    # Devolvemos un mensaje de éxito
    return {"msg": "Successfully updated job"}


@router.delete("/delete/{id}")
def delete_job(id: int, db: Session = Depends(get_db)):
    """ Este código define una ruta en un router utilizando el método HTTP DELETE y un parámetro de ruta llamado "id".
    El controlador de ruta llama a una función llamada "delete_job_by_id" pasando el id del trabajo y la base de datos como argumentos.
    También se define la variable current_user como 1, la cual se utiliza como argumento en la función delete_job_by_id a través del 
    asignación owner_id=current_user. Si la función devuelve un mensaje exitoso, el controlador de ruta devuelve un mensaje de éxito en formato JSON.
    Si la función devuelve "None" porque no se encontró ningún trabajo con la id especificada, se devuelve una excepción del tipo HTTPException
    con un código de estado 404 y un mensaje detallando que el trabajo no fue encontrado."""

    current_user = 1
    message = delete_job_by_id(id=id, db=db, owner_id=current_user)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with the id {id} is not found")
    return {"msg": "Successfully deleted job"}
    
            
 
 
     
     