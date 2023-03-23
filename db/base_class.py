from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

""" Esta clase se utiliza para crear una clase de modelo de la base de datos.
Los modelos son clases que representan una tabla en la base de datos y sus
campos son variables de clase que representan las columnas. """ 

 
 
@as_declarative()
class Base:
    #* Este código se utiliza como una clase base para la definición de modelos de tablas
    #* en SQLAlchemy. Al heredar de esta clase base, se proporciona automáticamente una tabla
    #* con un nombre por defecto (el nombre de la clase en minúsculas). El atributo id
    #* se utiliza para definir una columna de ID en la tabla.
    id: Any
    __name__: str
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()