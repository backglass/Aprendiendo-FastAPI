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



def update_job_by_id(id: int, job: JobCreate, db: Session, owner_id):
    """ Este código define una función llamada update_job_by_id que toma cuatro argumentos. Los argumentos son:

    id: un identificador entero de trabajo.
    job: un objeto JobCreate.
    db: un objeto de sesión SQLAlchemy.
    owner_id: el identificador del propietario del trabajo.

    La función busca un trabajo existente con el id proporcionado en la base de datos. Si no se encuentra un
    trabajo, la función devuelve 0. Si se encuentra un trabajo, los valores del objeto job se convierten en
    un diccionario, luego se actualiza el diccionario añadiendo owner_id. Se actualiza el trabajo existente
    en la base de datos con los valores actualizados, y se guarda en la base de datos con db.commit().
    Finalmente, la función devuelve 1. 
    """
    existing_job = db.query(Job).filter(Job.id == id) # Selecciona el trabajo existente con el id proporcionado.
    if not existing_job.first(): # Si no se encuentra un trabajo existente con el id proporcionado, devuelve un 0.
        return 0
    job_dict = job.dict() # Convierte el objeto 'job' en un diccionario.
    job_dict.update(owner_id=owner_id) # Actualiza el 'owner_id' en el diccionario.
    existing_job.update(job_dict) # Actualiza el trabajo existente con la información actualizada.
    db.commit() # Confirma los cambios en la base de datos.
    return 1 # Devuelve un 1 si la actualización fue exitosa.



def delete_job_by_id(id: int, db: Session, owner_id):
    
    """ Este código define una función llamada delete_job_by_id que elimina un trabajo específico de la base de datos en función de su id. 
    La función toma tres argumentos: 

    id: un entero que representa el id del trabajo que se desea eliminar.
    db: una sesión de la base de datos.
    owner_id: el id del usuario propietario del trabajo.

    Primero, la función consulta la base de datos para obtener el trabajo con el id especificado, y si no existe, devuelve 0. Si el trabajo 
    existe, se elimina y se realiza un commit para confirmar los cambios en la base de datos. Finalmente, la función devuelve 1 para indicar
    que el trabajo ha sido eliminado con éxito. 
    El parámetro synchronize_session del método delete se establece en False. Esto dice a SQLAlchemy que no
    intente sincronizar la sesión de objeto (en este caso, la sesión db) con la base de datos después de la eliminación,
    lo que puede ser más eficiente en algunos casos. """

    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    existing_job.delete(synchronize_session=False)
    db.commit()
    return 1