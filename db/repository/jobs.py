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



def retrieve_job(id: int, db: Session):
    #* Este código define una función llamada 
    #* retrieve_job
    #* que toma dos argumentos: 
    #* id que es un entero y db que es una sesión SQLAlchemy. La función usa la sesión 
    
    #* db para hacer una consulta a la base de datos para recuperar un trabajo (fila) en la tabla 
    
    #* "Job" donde el ID del trabajo sea igual al argumento id proporcionado.
    #*Luego, la función devuelve la primera fila coincidente obtenida en la consulta.
    job = db.query(Job).filter(Job.id == id).first()
    return job



def list_jobs(db: Session):
    """
    
    Este código define una función llamada 
    list_jobs
    que toma un argumento de base de datos db del tipo Session.
    Dentro de la función, se realiza una consulta a la base de datos para obtener todos los trabajos
    activos (Job.is_active == True) utilizando el método filter. Luego, se utilizó el método all()
    para obtener una lista de todos los trabajos que cumplen la condición establecida en la consulta.
    Finalmente, la función devuelve la lista de trabajos obtenida."""
    
    jobs = db.query(Job).filter(Job.is_active == True).all()
    return jobs
