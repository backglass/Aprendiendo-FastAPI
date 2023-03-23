from db.base_class import Base
from db.models.jobs import Job
from db.models.users import User


""" El código importa tres clases de módulos diferentes relacionados con una base de datos. La expresión "from db.base_class import Base"
importa la clase "Base" del módulo "base_class" ubicado en la carpeta "db".
La clase Base es una clase de SQLAlchemy, una herramienta de mapeo objeto-relacional (ORM) muy popular en Python. 


Luego se importan dos clases más, "Job" y "User", desde otros dos módulos diferentes, "jobs" y "users", respectivamente.
Estas dos clases son modelos de datos que se utilizarán para interactuar con la base de datos. Al importar estas clases,
el código las hace disponibles para su uso posterior. """