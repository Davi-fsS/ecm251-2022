from tkinter import PhotoImage
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class myUI():

    def acao_botao(self):
        print('click')

    def _construir_base(self):
        janela =  ttk.Window(
            title = "Minha GUI maua",
            size= (1024,400),
            position=(100,100),
            minsize=(600,300),
            maxsize=(1800,900),
            alpha=1.0,
        )
        janela.iconphoto(False,PhotoImage(file='calculator.png'))
        return janela

    def __init__(self) -> None:
        self.base = self._construir_base()

        #Criando botao
        ttk.Button(
            self.base,
            text='ola mundo',
            bootstyle='default',
            command=self.ativar_bot
        ).pack(side=LEFT, padx= 10, pady=5)

        # Criando segundo botao
        self.bot2 = ttk.Button(
            self.base,
            text='segundo botao',
            bootstyle=(DANGER, OUTLINE),
            command=self.desativar_bot
        )

        self.bot2.pack(side=LEFT, padx = 10, pady= 5)

    def run(self):
        self.base.mainloop()
    
    def ativar_bot(self):
        print('ligando botao')
        self.bot2.configure(state='enabled')
    
    def desativar_bot(self):
        print('desligando botao')
        self.bot2.configure(state='disabled')

def mostrarNome(nome):
    print(nome)

if __name__ == '__main__':
    f = mostrarNome
    f('Murilo')
    app = myUI()
    app.run()