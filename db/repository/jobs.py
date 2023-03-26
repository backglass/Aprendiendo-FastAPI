"""
El código importa la clase Session del módulo sqlalchemy.orm
y las clases JobCreate  y Job de los módulos schemas.jobs y 
db.models.jobs
"""

from sqlalchemy.orm import Session

from schemas.jobs import JobCreate
from db.models.jobs import Job

def create_new_job(job: JobCreate, db: Session, owner_id: int):
    #* Acepta tres argumentos: 
    #* job
    #* db
    #* owner_id
    #* El parámetro job es objeto de tipo JobCreate que se utiliza para crear un nuevo Job
    #* (trabajo) en la base de datos.
    #* El parámetro db  es objeto de tipo Session, utilizado para interactuar con la base
    #* de datos. Y, finalmente, el parámetro owner_id es un número entero que representa
    #* el id del dueño del trabajo.

    job_objet = Job(**job.dict(), owner_id=owner_id)
    db.add(job_objet)
    db.commit()
    db.refresh(job_objet)
    return job_objet
