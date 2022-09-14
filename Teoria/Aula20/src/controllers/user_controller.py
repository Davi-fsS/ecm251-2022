from models.users import User

class UserController():
    def __init__(self) -> None:
        #Carrega os dados dos usuarios
        self.users = [User(name="")]