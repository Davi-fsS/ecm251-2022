from tkinter import LEFT, PhotoImage
import ttkbootstrap as ttk

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

#Ponto de entrada da interface
base.mainloop()
