from tkinter import Button, Canvas, Entry, PhotoImage
from tkinter.tix import ButtonBox
from tkinter.ttk import Style
from turtle import position, width
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk, Image

class Login():

    # Criação da base
    def _initUI(self):

        janela =  ttk.Window(
            title = "Loja Online",
            size= (552,611),
            position=(400,35),
            alpha=1.0,
            themename='darkly'
        )
        janela.resizable(False,False)
        #janela.configure(bg='#3D405B')
        return janela  

    def _criar_box_login(self):
        box = ttk.Window(
            size=(552,611),
            position=(444,199)
        )
        
        return box

    def _label_tela_login(self,texto):
        
        input1 = ttk.Label(
            #self.box_geral,
            text=texto,
            bootstyle="sucess",
        )
        input1.pack(side=TOP)

        return input1

    def _login_input(self, digitado):
        login = ttk.Entry(
            self.base,
            bootstyle="dark",
            width = 35,
            textvariable = digitado
        )
        login.pack(
            side = TOP,
        )
        login.focus()
        return login
    
    def _password_input(self,digitado):
        password = ttk.Entry(
            self.base,
            bootstyle="dark",
            show='*',
            width=35,
            textvariable = digitado
        )
        password.pack(
            side = TOP,
        )
        return password

    def verifica_login(self, digitado):
        if(digitado != "davi"):
            print('vai se foder')

    def _botao_logar(self):
        return ttk.Button(
            self.base,
            text="Entrar",
            command=self.verifica_login
        ).pack(
            side = TOP,
            padx = 20,
            pady = 10
        )

    def __init__(self) -> None:
        self.base = self._initUI()
        #self.box_geral = self._criar_box_login()
        self._valor_digitado1 = ""
        self._valor_digitado2 = ""
        self.label_login = self._label_tela_login("Nome de usuário: ")
        self.box1 = self._login_input(self._valor_digitado1)
        self.label_login = self._label_tela_login("Senha: ")
        self.box1 = self._password_input(self._valor_digitado2)
        self.bot = self._botao_logar()

    def run(self):
        self.base.mainloop()

        
        

if __name__ == '__main__':
    app = Login()
    app.run()