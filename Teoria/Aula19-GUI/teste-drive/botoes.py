from tkinter import PhotoImage
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

base = ttk.Window(
    title = "Minha GUI maua",
    size= (1024,400),
    position=(100,100),
    minsize=(600,300),
    maxsize=(1800,900),
    alpha=1.0,
)
base.iconphoto(False,PhotoImage(file='calculator.png'))

def acao_botao():
    print('click')


#Criando botao
ttk.Button(
    base,
    text='ola mundo',
    bootstyle='default',
    command=acao_botao
).pack(side=LEFT, padx= 10, pady=5)

# Criando segundo botao
bot2 = ttk.Button(
    base,
    text='segundo botao',
    bootstyle=(DANGER, OUTLINE),
    command=acao_botao
)

bot2.pack(side=RIGHT, padx = 10, pady= 5)

#Ponto de entrada da interface
base.mainloop()
