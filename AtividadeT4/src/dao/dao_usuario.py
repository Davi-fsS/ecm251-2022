# Davi Fernandes Simões Soares (20.01099-0)

import sqlite3
from src.models.usuario import Usuario

class UsuarioDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = UsuarioDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Usuarios;
        """)
        results = []
        for result in self.cursor.fetchall():
            results.append(Usuario(nome = result[1], email = result[2], senha = result[3], cpf = result[4]))
        self.cursor.close()
        return results

    def insert_user(self, usuario):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Usuarios(nome, email, senha, cpf)
            Values(?,?,?,?);
        """, (usuario.get_nome(), usuario.get_email(), usuario.get_senha(),usuario.get_cpf()))
        self.conn.commit()
        self.cursor.close()

    def update_user(self, usuario):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Usuarios SET
                email = '{usuario.get_email()}',
                senha = '{usuario.get_senha()}'
                WHERE cpf = '{usuario.get_cpf()}'
                
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True