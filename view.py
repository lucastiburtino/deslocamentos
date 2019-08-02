#! usr/bin/python3

from tkinter import *
# from tkinter import Menu  // ATENÇÃO: descomentar caso necessário


window = Tk()

window.title('deslocamentos 0.0.1') # Version: 0.0.1 Work in progress

WIDTH = '600'
HEIGHT = '500'

window.geometry(WIDTH + 'x' + HEIGHT)

menu = Menu(window)

request = Menu(menu)

# TODO: acrescentar função assim:
# request.add_command(label='blablabla', command=minhafunção)

request.add_command(label='Cadastrar Deslocamento') 

request.add_command(label='Alterar Deslocamento')

request.add_command(label='Acompanhar solicitação')

menu.add_cascade(label='Solicitação', menu=request)

report = Menu(menu)

report.add_command(label='Abertas')

report.add_command(label='Passadas')

menu.add_cascade(label='Prestação de contas', menu=report)

window.config(menu=menu)

window.mainloop()
