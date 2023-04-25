
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import HTTPException, status
from jose import jwt, JWTError

from db.session import get_db
from core.hashing import Hasher
from schemas.tokens import Token
from db.repository.login import get_user
from core.security import create_access_token
from core.config import settings

# Nuevos de la parte que se hace la webapp
from fastapi import Response
from apis.utils import OAuth2PasswordBearerWithCookie


router = APIRouter()


def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user(username=username, db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user



@router.post("/token", response_model=Token)
def login_for_access_token(
    response: Response,  form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return {"access_token": access_token, "token_type": "bearer"}



oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/login/token")


def get_current_user_from_token(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        print("payload is ", payload)
        username: str = payload.get("sub")
        print("username/email extracted is ", username)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username=username, db=db)
    if user is None:
        raise credentials_exception
    return user


"""
Este código crea una ruta POST en un API con FastAPI. Esta ruta se encuentra en el endpoint
/token. 

Cuando se realiza una solicitud POST a esta ruta, los siguientes parámetros son requeridos
para ser enviados a través del formulario de solicitud OAuth2:

   - username: nombre de usuario del usuario que quiere logearse.
   - password: contraseña del usuario que quiere logearse.
   
Si las credenciales ingresadas en el formulario coinciden con algún usuario y contraseña
registrado en la base de datos, se genera un token JWT (JSON Web Token) con una fecha de
expiración determinada. Se devuelve el token junto con el tipo de token (bearer) en una
respuesta en formato JSON.

Hay dos métodos implementados en el código que son llamados por la ruta POST:

    - authenticate_user: verifica las credenciales ingresadas con las credenciales
      registradas en la base de datos de usuarios.
    - create_access_token: crea el token de acceso y lo retorna.  
    
Además, hay un método llamado get_current_user_from_token que se utiliza como dependencia para
otras rutas de la API. Este método decodifica el token JWT y luego busca el usuario que
coincide con los datos almacenados en el token. Si el usuario es encontrado, se retorna el
usuario; de lo contrario, se devuelve una excepción HTTP.
"""
