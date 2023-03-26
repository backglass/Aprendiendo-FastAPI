from typing import Optional
from pydantic import BaseModel
from datetime import datetime, date

"""
El código define tres clases mediante el uso de herencia. La primera clase es
JobBase que hereda atributos de la clase de modelo pydantic.
La segunda clase llamada JobCreate hereda de JobBase y sobrescribe algunos atributos
con tipos de datos obligatorios en lugar de opcionales.
La última clase es ShowJob que también hereda de JobBase y se utiliza para mostrar los
trabajos en la aplicación. La clase modelo JobCreate se utiliza para crear nuevos trabajos,
mientras que ShowJob se utiliza para mostrar detalles de trabajo en la aplicación.
Además, la clase Config hace que la sintaxis de las bases de datos se adapte.
"""

class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = "remote"
    description: Optional[str] = None
    date_posted: Optional[date] =datetime.now().date()
    

class JobCreate(JobBase):
    title: str
    company: str
    location: str 
    description: str

class ShowJob(JobBase):
    title: str
    company: str
    company_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]
    
    
    class Config():
        orm_mode = True