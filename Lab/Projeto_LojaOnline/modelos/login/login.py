from tkinter import PhotoImage
from turtle import position
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Login():

    def _construir_base(self):
        janela = ttk.Window(
            title = "Loja Online",
            size = (1440,1024),
            minsize = (1440,1024),
            maxsize = (1440,1024),
            alpha = 1.0
        )
        #janela.iconphoto(False,PhotoImage(file='icone-pagina'))
        return janela

    def __init__(self) -> None:
        self.base = self._construir_base()

    def run(self):
        self.base.mainloop()

if __name__ == '__main__':
    app = Login()
    app.run()