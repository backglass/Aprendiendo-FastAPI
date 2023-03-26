from sqlalchemy.orm import Session

from schemas.users import UserCreate
from db.models.users import User
from core.hashing import Hasher
""" El código define una función llamada 'create_new_user', que toma dos
argumentos: 'user', un objeto de la clase 'UserCreate', y 'db', una
instancia de 'Session' de SQLAlchemy.  """



def create_new_user(user: UserCreate, db: Session):
    #* Se crea una nueva instancia de la clase 'User' a partir de los
    #* datos proporcionados por 'user'. En esta instancia, el atributo
    #* 'hashed_password' se codifica utilizando la función
    #* 'get_password_hash' de la clase 'Hasher'. 


    user = User(username=user.username,
                email=user.email,
                hashed_password=Hasher.get_password_hash(user.password),
                is_active=True,
                is_superuser=False)
    
    #* Luego, se agrega el objeto 'user' a la sesión actual 'db', se
    #* confirman los cambios con 'commit()', se actualiza la instancia
    #* con 'refresh()', y finalmente se devuelve el objeto 'user'.
    db.add(user)
    db.commit()
    db.refresh(user)
    return user