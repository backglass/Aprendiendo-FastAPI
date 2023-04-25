from fastapi.security import OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi import Request
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import HTTPException
from fastapi import status

from typing import Optional
from typing import Dict


class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)
    
    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.cookies.get("access_token")
        
        print("authorization: ", authorization)
        
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param
    
"""
El código define una clase llamada OAuth2PasswordBearerWithCookie que hereda de la clase OAuth2 de la
biblioteca fastapi.security. Esta clase extiende la capacidad de autorización de cabecera con una autorización
basada en cookies, en la que el token de acceso se guarda en una cookie.
La clase toma como argumentos el tokenURL, un scheme_name opcional, un diccionario de scopes opcionales y
un booleano auto_error opcional que especifica si se debe generar un error automáticamente si la autorización
falla. 

En el cuerpo de la clase hay un método __call__ que maneja la autorización en una solicitud. Este método
extrae la autorización de la cookie nombrada access_token en la solicitud y verifica si se proporciona un token.
Si no hay autorización o si el esquema de la autorización no es "Bearer", se devuelve un error HTTP 401 por el
medio de una excepción HTTPException. Si el token es válido, el método devuelve un diccionario de parámetros
de autorización.





"""