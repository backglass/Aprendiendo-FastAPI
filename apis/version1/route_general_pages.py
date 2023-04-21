from fastapi import APIRouter 
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#* esto inicializa una instancia de Jinja2Templates y especifica el directorio donde se
#* encuentran las plantillas. Si no se especifica ningún directorio, por
#* defecto Jinja2 buscará las plantillas en un directorio llamado "templates" al nivel del
#* directorio principal de la aplicación
#! Será inutilizado cuando se construya la appweb porque esta ruta se manejara desde otro lado.
templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()



@general_pages_router.get("/")
async def home(request: Request):
    #* Este código define una ruta de la página principal ("/") para una aplicación web utilizando el framework FastAPI.
 
    #* Cuando un usuario accede a esa ruta, se ejecuta la función "home"
    #* , que toma como argumento un objeto Request y retorna una respuesta con una plantilla HTML
    #* (ubicada en el archivo "general_pages/homepage.html") y un objeto que contiene información sobre la solicitud
    #* del usuario (el objeto Request que se le pasó como argumento).
    #* La respuesta devuelve una plantilla HTML renderizada utilizando el paquete Jinja2,
    #* que es una biblioteca de software libre para hacer templates o plantillas. 
    
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request})
