from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt

from core.config import settings

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return encode_jwt

""" El código anterior define una función llamada 
create_access_token: que recibe dos argumentos, "data" que es un diccionario que representa los
datos que se van a codificar en el token y "expires_delta" que es un objeto del tipo "timedelta"
opcional que representa el período de tiempo después del cual el token caducará.
 
En el código, se importan algunos módulos y clases, como "datetime" y "timedelta" de la librería
datetime, Optional de la librería typing y JWTError y jwt de la librería jose.
Además, también se hace una importación desde otro módulo llamado core, de la variable settings.

Todas estas importaciones son necesarias para el correcto funcionamiento de la función
create_access_token:
Dentro de la función, se hace una copia del diccionario data en una variable llamada to_encode.
Luego, si el argumento expires_delta está presente, se calcula la fecha y hora de expiración
del token expire, sumando la fecha y hora actuales con la duración expires_delta.
Si expires_delta no está presente, se toma la duración especificada en la variable ACCESS_TOKEN_EXPIRE_MINUTES
que se define en el archivo de configuración settings. 
Después se actualiza el diccionario to_encode con una clave "exp" cuyo valor es la fecha y
hora de expiración calculada. Finalmente, se llama la función encode para codificar los datos
en un token JWT usando la llave secreta definida en SECRET_KEY y el algoritmo especificado en
la variable ALGORITHM de settings.
El código retorna el token generado. """

