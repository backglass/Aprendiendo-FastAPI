from sqlalchemy import Column, Integer, String,Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship

from db.base_class import Base


class Job(Base):
    #* Este código define una tabla llamada "Job" como una clase en Python usando 
    #* SQLAlchemy. La tabla Job tiene las siguientes columnas:
    
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String,nullable= False)
    company = Column(String,nullable=False)
    company_url = Column(String)
    location = Column(String,nullable = False)
    description = Column(String,nullable=False)
    date_posted = Column(Date)
    is_active = Column(Boolean(),default=True)
    
    #* owner_id - identificador del usuario propietario del trabajo (clave externa).
    #* La relación entre la tabla Job y la tabla User se establece mediante la columna 'owner_id'
    #* mediante el atributo 'ForeignKey("user.id")', que indica que el identificador de la tabla
    #* User es la clave externa para la tabla Job. Finalmente, se define una relación de "back_populates"
    #* a la tabla User para obtener el propietario del trabajo.
    owner_id =  Column(Integer,ForeignKey("user.id"))
    owner = relationship("User",back_populates="jobs")
    