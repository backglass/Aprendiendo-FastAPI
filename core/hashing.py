#* El código importa la librería "CryptContext" de la librería "passlib". Crea una instancia de
#* "CryptContext" con un esquema de cifrado "bcrypt" y con una opción de "deprecated" que
#* se establece automáticamente.
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher():
    @staticmethod
    def veryfy_password(plain_password, hashed_password):
        """verify_password" recibe una contraseña en texto plano y una contraseña cifrada, y 
        utiliza el objeto "pwd_context" de la instancia de "CryptContext" para verificar
        si la contraseña en texto plano coincide con la contraseña cifrada
        def veryfy_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)"""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        """ El método "get_password_hash" recibe una contraseña en texto plano y devuelve la
        versión cifrada de esa contraseña utilizando el objeto "pwd_context" de la
        instancia de "CryptContext". """
        return pwd_context.hash(password)
    
    #! Estamos creando métodos estáticos. Un método estático es aquel que no requiere de una instancia
    #! de la clase para ser llamado. Podemos llamar directamente a estos métodos como "Hasher.verify_password".
    #! Queda mas bonito llamar a los metodos empezando por Haser.verify_password o Haser.get_password_hash