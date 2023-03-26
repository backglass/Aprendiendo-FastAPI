from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    
    class Config():
        """ Esto le dice a Pydantic, cuando se usa esta clase para leer
        datos desde una base de datos, que debe devolver los datos
        en un formato que sea compatible con la mayoría de los ORM
        (Object-Relational Mapping), como SQLAlchemy. """
        orm_mode = True