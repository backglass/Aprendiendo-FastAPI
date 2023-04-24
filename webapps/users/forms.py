from typing import Optional
from typing import List

from fastapi import Request

""" La clase UserCreateForm es una clase que se utiliza para validar y cargar los datos de un formulario de
registro de usuario. A continuación, se describe cada método: """




class UserCreateForm:
    """ es el constructor de la clase y recibe un objeto Request. En el constructor se inicializan algunos
        atributos importantes como errors, username, email y password. """
    
    def __init__(self, request: Request):
        self.request : request = request
        self.errors : List = []
        self.username : Optional[str] = None
        self.email : Optional[str] = None
        self.password : Optional[str] = None
        
        
    async def load_data(self):
        """Este método es llamado después de la creación del objeto UserCreateForm.
           Permite cargar los datos del formulario, obteniendo los valores del formulario mediante una
           petición asíncrona del objeto Request. Los datos como el nombre de usuario, correo electrónico y
           contraseña se obtienen y se asignan a los atributos correspondientes."""
           
        form = await self.request.form()
        self.username = form.get("username")
        self.email = form.get("email")
        self.password = form.get("password")
        print ("form: ", form)
        
        
    async def is_valid(self):
        """ Este método se utiliza para validar los datos del formulario. Se comprueba si el username es nulo
            o su longitud es menor o igual a 3, en tal caso se agrega un mensaje de error a la lista de errores.
            Se comprueba si el correo electrónico contiene el símbolo @, en caso contrario también se agrega un
            mensaje de error a la lista de errores. Y finalmente, se verifica si la contraseña es nula o su
            longitud es menor o igual a 4, de ser así, también se agrega un mensaje de error a la lista de
            errores. En el caso de que no haya errores, devuelve True, lo que indica que los datos son válidos
            para crear un nuevo usuario, en caso contrario, se devolverá False."""
            
        if not self.username or not len(self.username) > 3:
            self.errors.append("El nombre de usuario debe tener más de 3 caracteres")
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("El email es inválido")
        if not self.password or not len(self.password) > 4:
            self.errors.append("La contraseña debe tener más de 4 caracteres")
        if not self.errors:
            return True
        return False