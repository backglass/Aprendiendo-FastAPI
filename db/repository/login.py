from sqlalchemy.orm import Session
from db.models.users import User



def get_user(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    return user

""" Este código define una función llamada "get_user" que toma dos parámetros de entrada: "username"
que es el nombre de usuario y "db" que es un objeto de sesión que representa una conexión a la base
de datos.

La función utiliza el objeto "db" para acceder a la base de datos y buscar un objeto "User" cuyo nombre
de usuario es igual al valor de "username". 

Luego, la función devuelve el primer objeto "User" que coincide con la consulta.  """

#* En resumen, la función "get_user" obtiene un objeto "User" de la base de datos mediante el nombre de
#* usuario proporcionado.