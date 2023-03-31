from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import HTTPException, status

from db.session import get_db
from core.hashing import Hasher
from schemas.tokens import Token
from db.repository.login import get_user
from core.security import create_access_token
from core.config import settings


router = APIRouter()

def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username=username, db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}

""" Este código es una API escrita con FastAPI para permitir la autenticación de usuario y devolver
un token de acceso. La API utiliza la biblioteca "OAuth2PasswordBearer" para manejar el flujo del
OAuth2 para autenticar al usuario.

El primer paso en el código es crear una instancia de la clase "APIRouter()" para configurar el enrutador
para la API. Luego, definimos una función "authenticate_user" que recibe un nombre de usuario, contraseña
y una sesión de base de datos. La función busca al usuario en la base de datos correspondiente y verifica
su contraseña. Si las credenciales son correctas, la función devuelve el objeto del usuario; de lo
contrario, devuelve incorrecto.

A continuación, definimos una ruta POST con decorador "@router.post("/token", response_model=Token)".
Esta ruta sirve para el inicio de sesión y se espera que un usuario ingrese un usuario válido y una
contraseña. La función "login_for_access_token" utiliza la función "authenticate_user" para verificar
las credenciales de inicio de sesión y, si son válidas, devuelve un token de acceso con la duración 
especificada en los parámetros de configuración de la API. """

#* En resumen, este código es una API en FastAPI que ofrece una ruta para la autenticación de usuario
#* y devuelve un token de acceso válido para el consumo de otros recursos.
        
