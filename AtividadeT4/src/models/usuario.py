# Davi Fernandes Simões Soares (20.01099-0)

class Usuario():
    def __init__(self, nome, email, senha, cpf):
        self._email = email
        self._nome = nome
        self._senha = senha
        self._cpf = cpf

    def get_senha(self):
        return self._senha

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def get_cpf(self):
        return self._cpf

    def __str__(self)->str:
        return f'Usuario(nome:{self.get_nome()}, email:{self.get_email()}, senha:{self.get_senha()} cpf:{self.get_cpf()}'