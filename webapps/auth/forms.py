from typing import Optional
from typing import List

from fastapi import Request


class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.username: Optional[str] = None
        self.password: Optional[str] = None
    
    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("email")
        self.password = form.get("password")
        
    async def is_valid(self):
        if not self.username or not (self.username.__contains__("@")):
            self.errors.append("El nombre de usuario debe ser un correo electrónico")
        if not self.password or not len(self.password) >= 4:
            self.errors.append("La contraseña debe tener al menos 4 caracteres")
        if not self.errors:
            return True
        return False
    
"""
Este código define la clase LoginForm, que tiene un constructor inicializado con una instancia de Request
y que tiene como atributos una lista de errores, un objeto opcional username y un objeto opcional password. 

La clase tiene dos métodos asincrónicos. El método load_data, que utiliza la instancia de Request para cargar
los datos del formulario y define los valores username y password.

El método is_valid, que valida los datos ingresados en el formulario y agrega cualquier error correspondiente
a la lista self.errors. Si no hay errores, este método devuelve True. Si hay uno o más errores, devuelve False.
"""