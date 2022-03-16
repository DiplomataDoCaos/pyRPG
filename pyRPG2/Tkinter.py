import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="ok, testando modificações no exemplo,a janela aparentemente aqui é flexível\n\nhahahah")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Dar o fora daqui!",command=tk.destroy)
button.pack(side=BOTTOM)
button = tkinter.Button(frame,text="exit",command=tk.destroy)
button.pack(side=LEFT)
tk.mainloop()

class Pessoa(object):
    def __init__(Nome,Gênero):
        Gênero=Gênero
        Nome=Nome

Fernando=("Fernando","Homem")
Pessoa1=Pessoa(Fernando)
print(Pessoa1)
