from sqlalchemy.orm import Session
from db.models.users import User



def get_user(username: str, db: Session):
    user = db.query(User).filter(User.email == username).first()
    return user

"""  
Este código define una función llamada "get_user". Esta función recibe dos argumentos:
"username" que es un objeto de tipo string que representa el email del usuario que se 
desea obtener, y "db" que es una sesión de base de datos SQLAlchemy. 

Luego, dentro de la función, se realiza una consulta a la base de datos utilizando el método
"query" de la sesión pasada como argumento. El ".filter" se encarga de buscar en la tabla
"User" aquellos registros cuyo campo email sea igual al valor de "username". Finalmente, el
método "first" devuelve el primer registro encontrado. 

La función retorna una instancia de la entidad User con los valores correspondientes a la fila
encontrada, o retorna "None" si no se encontró un registro que coincida con la consulta
realizada.
"""

#* En resumen, la función "get_user" obtiene un objeto "User" de la base de datos mediante el nombre de
#* usuario proporcionado.