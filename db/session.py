#* Este código importa dos módulos de SQLAlchemy: 'create_engine' y 'sessionmaker'. Estas importaciones
#* permiten la creación de una instancia de conexión con una base de datos y la creación de sesiones en
#* esa conexión. 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#* Luego, se importa la variable 'DATABASE_URL' del módulo 'config' que contiene la URL de la base de datos,
#* y se crea una instancia de conexión con la base de datos utilizando 'create_engine'. 
from core.config import settings
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)


#*  Finalmente, se define una clase SessionLocal utilizando sessionmaker para crear una sesión de base
#*  de datos, que permite interactuar con la base de datos a través del motor. Se especifica que la sesión
#*  no se autocommite ni se autoflush, y el motor de la base de datos especificado al vincular la sesión
#*  es el objeto de motor creado anteriormente.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)