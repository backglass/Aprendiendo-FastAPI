from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    #* que sirve como modelo para una tabla de usuarios en una base de datos.
    #* Utiliza la librería SQLAlchemy para trabajar con el motor de la base de datos.
    
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean(),default=True)
    is_superuser = Column(Boolean(),default=False)

    jobs = relationship("Job",back_populates="owner")
    
    """
    Este código define una relación entre dos tablas de una base de datos en SQLAlchemy.
    La tabla en la que se define este código es la tabla "User", y la tabla con la que se relaciona es
    la tabla "Job". La relación se establece mediante la propiedad "jobs", que es una lista
    de objetos de la clase "Job". 

    El parámetro "back_populates" se utiliza para establecer la relación inversa entre las dos tablas.
    En este caso, "back_populates" se establece en "owner", lo que significa que cada objeto de la clase
    "Job" tendrá un atributo "owner" que apunta al objeto de la clase "User" al que está asociado. 

    En resumen, este código establece una relación bidireccional uno a muchos entre la tabla "User" y
    la tabla "Job", lo que permite acceder a los trabajos asociados a un usuario determinado o al usuario
    que es dueño de un trabajo determinado.
    """