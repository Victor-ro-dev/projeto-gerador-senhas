from tkinter import*
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk, Image
import string
import random

cor1 = "#0a0a0a"  # Preta
cor2 = "#fafcff"  # Branca
cor3 = "#21c25c"  # Verde
cor4 = "#eb463b"  # Vermelha
cor5 = "#dedcdc"  # Cinza
cor6 = "#3080f0"  # Azul

janela = Tk()
janela.geometry("300x350")
janela.config(bg=cor2)
janela.resizable(width=False, height=False)





estilo = ttk.Style(janela)
estilo.theme_use('clam')
janela.mainloop()