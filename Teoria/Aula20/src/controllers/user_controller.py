from models.users import User

class UserController():
    def __init__(self) -> None:
        #Carrega os dados dos usuarios
        self.users = [
            User(name="joao",password="arroz",email="joao@mail.com"),
            User(name="joao2",password="arroz2",email="joao2@mail.com"),   
            User(name="tais",password="petacular",email="tais@condida.com")   
        ]

    def checkUser(self,users):
        return users in self.users

    def checkLogin(self,name,password):
        user_test = User(name=name,password=password, email=None)

        for user in self.users:
            if user.name == user_test.name and user.password == user_test.password:
                return True
            return False