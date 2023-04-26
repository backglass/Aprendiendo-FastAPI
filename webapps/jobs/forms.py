from typing import List
from typing import Optional

from fastapi import Request


class JobCreateForm:
    def __init__(self,request: Request):
        self.request : Request = request
        self.errors : List = []
        self.title : Optional[str] = None
        self.company : Optional[str] = None
        self.company_url : Optional[str] = None
        self.location : Optional[str] = None
        self.description : Optional[str] = None
        
        
    async def load_data(self):
        form = await self.request.form()
        self.title = form.get("title")
        self.company = form.get("company")
        self.company_url = form.get("company_url")
        self.location = form.get("location")
        self.description = form.get("description")
        
    def is_valid(self):
        if not self.title or not len(self.title) >= 4:
            self.errors.append("Title is required and must be at least 4 characters long")
        if not self.company_url or not (self.company_url.__contains__("http")):
            self.errors.append("Company URL is required and must be a valid URL")
        if not self.company or not len(self.company) >= 1:
            self.errors.append("Company is required and must be at least 1 character long")
        if not self.description or not len(self.description) >= 4:
            self.errors.append("Description is required and must be at least 4 characters long")
        if not self.errors:
            return True
        
        return False
    
""" Este código define una clase llamada JobCreateForm con los siguientes atributos:

    request: un objeto Request FastAPI
    errors: lista de errores que pueden ocurrir al validar la entrada
    title: título del trabajo (opcional)
    company: nombre de la empresa del trabajo (opcional)
    company_url: URL del sitio web de la empresa del trabajo (opcional)
    location: ubicación del trabajo (opcional)
    description: descripción del trabajo (opcional)
    
    
    La clase incluye dos métodos:

        load_data: un método asíncrono que lee los datos del formulario del objeto de solicitud y completa los atributos de JobCreateForm en consecuencia.
        is_valid: un método que verifica si la entrada es válida, según los siguientes criterios
        
            el título es obligatorio y debe contener al menos 4 caracteres
            la URL de la empresa es obligatoria y debe ser una URL válida (http)
            la empresa es obligatoria y debe contener al menos 1 carácter
            la descripción es obligatoria y debe contener al menos 4 caracteres
            
    Si alguno de estos criterios no se cumple, se agrega un mensaje de error a la lista de errores.
    Si la lista de errores está vacía, se considera que la entrada es válida y el método devuelve True,
    de lo contrario devuelve False.

    """