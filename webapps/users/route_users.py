from db.repository.users import create_new_user
from db.session import get_db

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi import responses
from fastapi import status
from fastapi.templating import Jinja2Templates

from schemas.users import UserCreate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from webapps.users.forms import UserCreateForm

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)

"""Este código define dos rutas en un framework web: /register/ para el método GET y el método POST. Cuando se
   accede a la ruta /register/ utilizando el método GET, se renderiza una plantilla HTML que muestra u
   n formulario de registro. Cuando se envía el formulario con el método POST, se procesa la información del
   formulario de registro y, si los datos son válidos, se crea un nuevo usuario y se redirige al usuario a la
   página principal con un mensaje de éxito."""
   

@router.get("/register/")
def register(request: Request):
    """ El método GET de la ruta /register/, que renderiza una plantilla HTML
        que contiene un formulario de registro."""
        
    return templates.TemplateResponse("users/register.html", {"request": request})


@router.post("/register/")
async def register(request: Request, db: Session=Depends(get_db)):
    """La segunda función es para el método POST de la ruta /register/, que recibe datos del formulario
       y la dependencia de la base de datos. La función crea un objeto de formulario, carga los datos del
       formulario y verifica si el formulario es válido. Si es válido, crea un nuevo usuario con los datos
       proporcionados y trata de persistirlo en la base de datos.
       Si el usuario ya existe, agrega un mensaje de error al objeto de formulario y lo devuelve al usuario.
       Si se crea el usuario correctamente, redirige al usuario a la página de inicio con un mensaje de éxito."""
              
    form = UserCreateForm(request)
    await form.load_data()
    if await form.is_valid():
        user = UserCreate(username=form.username, email=form.email, password=form.password)
        
        try:
            user = create_new_user(user=user, db=db)
            return responses.RedirectResponse("/?msg=Usuario creado correctamente", status_code=status.HTTP_302_FOUND)
        except IntegrityError:
            form.__dict__.get("errors").append("El usuario ya existe")
            return templates.TemplateResponse("users/register.html", form.__dict__)
    return templates.TemplateResponse("users/register.html", form.__dict__)
    

