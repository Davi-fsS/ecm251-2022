from cgitb import text
from ensurepip import bootstrap
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
        )
        janela.resizable(False,False)
        janela.configure(bg='#3D405B')
        return janela  

    def _criar_box_login(self):
        box = ttk.Window(
            size=(552,611),
            position=(444,199)
        )
        
        return box

    def _label_login(self):
        return(
            ttk.Label(
                #self.box_geral,
                text="Insira seu texto: ",
                background="#3D405B",
                style="light"
            ).pack(
                side=TOP
            )
        )

    def _login_input(self):
        login = ttk.Entry(
            self.base,
            bootstyle="dark",
            width = 35
        )
        login.pack(
            side = TOP,
        )
        login.focus()
        return login
    
    def _password_input(self):
        password = ttk.Entry(
            self.base,
            bootstyle="dark",
            show='*'
        )
        password.pack(
            side = TOP,
            padx = 20,
            pady = 10
        )
        return password

    def _botao_logar(self):
        return ttk.Button(
            self.base,
            text="Entrar"
        ).pack(
            side = TOP,
            padx = 20,
            pady = 10
        )

    def __init__(self) -> None:
        self.base = self._initUI()
        #self.box_geral = self._criar_box_login()
        self.label_login = self._label_login()
        self.box1 = self._login_input()
        self.box1 = self._password_input()
        self.bot = self._botao_logar()

    def run(self):
        self.base.mainloop()

        
        

if __name__ == '__main__':
    app = Login()
    app.run()