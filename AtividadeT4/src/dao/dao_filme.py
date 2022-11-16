# Davi Fernandes Simões Soares (20.01099-0)

import sqlite3
from src.models.filme import Filme

class FilmeDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = FilmeDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Filmes;
        """)
        results = []
        for result in self.cursor.fetchall():
            results.append(Filme(nome = result[0], preco = result[1], url = result[2], saldo = result[3]))
        self.cursor.close()
        return results

    def insert_filme(self, filme):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                INSERT INTO Filmes Values(
                    '{filme.get_nome()}',
                    {filme.get_preco()},
                    '{filme.get_url()}',
                    {filme.get_saldo()}
                );
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def update_filme(self, filme):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Filmes SET
                saldo = {filme.get_saldo()}
                WHERE nome = '{filme.get_nome()}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
