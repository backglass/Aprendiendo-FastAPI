from apis.version1.route_login import login_for_access_token
from db.session import get_db

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from webapps.auth.forms import LoginForm

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.post("/login")
async def login(request: Request, db: Session=Depends(get_db)):
    """
    La función carga los datos recibidos desde el formulario de inicio de sesión (si los hay) y en caso de
    ser válidos la función intenta realizar el inicio de sesión verificando los datos en la base de datos
    (en este caso, la base de datos ya está conectada).
    
    Si el inicio de sesión es correcto, la función muestra la plantilla de la página de inicio de sesión,
    actualiza la información del formulario de inicio de sesión para mostrar que el inicio de sesión es
    correcto y llama a otra función login_for_access_token para generar un token de acceso para usar en otras
    partes de la aplicación.
    
    Si los datos no son correctos, la función muestra la misma página de inicio de sesión con un mensaje de
    error.
    """
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Inicio de sesión correcto")
            response = templates.TemplateResponse("auth/login.html", form.__dict__)
            login_for_access_token(response=response, form_data=form, db=db)
            return response
        except HTTPException:
            form.__dict__.update(errors="")
            form.__dict__.get("errors").append("Nombre de usuario o contraseña incorrectos")
            return templates.TemplateResponse("auth/login.html", form.__dict__)
    return templates.TemplateResponse("auth/login.html", form.__dict__)
        