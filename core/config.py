
#* El código comienza importando el módulo 'os', que proporciona una forma sencilla de trabajar con variables de entorno
#* y el módulo 'load_dotenv' de la biblioteca 'python-dotenv' para cargar variables en un archivo .env en el entorno.
import os
from dotenv import load_dotenv

#* Luego, se utiliza el módulo 'pathlib' para crear una ruta hacia el archivo .env,
#* que se encuentra en el mismo directorio del archivo principal.
from pathlib import Path 
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    #* La clase 'Settings' define un conjunto de variables que se usan en el proyecto, incluidos
    #* el nombre del proyecto, la versión del proyecto y las credenciales necesarias para conectarse
    #* a la base de datos PostgreSQL. 
    
    PROJECT_NAME: str = "Trabajos FastAPI"
    PROJECT_VERSION: str = "1.0.0"
    
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT",5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
    #Datos para token JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
       
settings = Settings() # Importa esta configuración en tu archivo principal


"""
En resumen, este código carga las credenciales de la base de datos y otra información de 
configuración desde un archivo .env en el entorno y los hace accesibles en el archivo principal
para un proyecto que utiliza la biblioteca FastAPI.
"""