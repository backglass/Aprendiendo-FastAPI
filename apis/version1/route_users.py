""" Este código define un enrutador API utilizando la biblioteca FastAPI y utiliza
la dependencia de SQLAlchemy para la sesión de base de datos. También importa
el esquema de creación de usuario y la función para crear un nuevo usuario
a través de "create_new_user" """

from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.users import UserCreate, ShowUser
from db.session import get_db
from db.repository.users import create_new_user

router = APIRouter()

""" El método create_user:
se define como HTTP POST y toma un objeto de usuario creado con UserCreate
y una sesión de base de datos obtenida a través de get_db. """
@router.post("/", response_model=ShowUser) #!  "response_model" se utiliza para validar los datos de entrada y salida de la respuesta.
                                           #!   En este caso se usa para que la respuesta no incluya la contraseña del usuario.
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    #* la función create_new_user
    #* para crear un nuevo usuario en la base de datos y devuelve el usuario
    #* recién creado en formato JSON como respuesta HTTP.
    user = create_new_user(user, db)
    return user