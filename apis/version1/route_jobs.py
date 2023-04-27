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
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token




# Creamos una instancia del enrutador
router = APIRouter()

# Creamos la ruta para crear trabajos
@router.post("/create-job", response_model=ShowJob)
def create_job(
    job: JobCreate, # Recibimos los datos requeridos para crear un trabajo 
    db: Session = Depends(get_db), # Dependemos de una conexión a la base de datos 
    current_user: User = Depends(get_current_user_from_token), # Dependemos del usuario autenticado
):
    # Creamos un nuevo trabajo utilizando la función 'create_new_job'
    job = create_new_job(job=job, db=db, owner_id=current_user.id)
    
    # Retornamos el trabajo creado
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
def delete_job(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    job = retrieve_job(id=id, db=db)
    if not job:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with {id} does not exist",
        )
    print(job.owner_id, current_user.id, current_user.is_superuser)
    if job.owner_id == current_user.id or current_user.is_superuser:
        delete_job_by_id(id=id, db=db, owner_id=current_user.id)
        return {"detail": "Successfully deleted."}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not permitted!!!!"
    ) 
     
"""
La primera ruta es una solicitud POST para crear un nuevo trabajo con un propietario especificado.
Retorna el trabajo creado como una respuesta JSON.

La segunda ruta es una solicitud GET para recuperar un trabajo único por su ID. Si el trabajo no
existe, levanta un error 404.

La tercera ruta es una solicitud GET para recuperar una lista de todos los trabajos.

La cuarta ruta es una solicitud PUT para actualizar un trabajo existente con el ID especificado.
Si el trabajo no existe, levanta un error 404.

La quinta ruta es una solicitud DELETE para eliminar un trabajo existente con el ID especificado.
Verifica que el usuario autenticado sea el propietario del trabajo o un superusuario, de lo
contrario, se levanta un error 401 no autorizado.
"""
     