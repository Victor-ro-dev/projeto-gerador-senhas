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

alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numeros = '0123456789'
simbolos ='.,;!@#$&*'

#---------------------------Configs básicas------------------

frame_cima = Frame(janela,width=300, height=50, bg = cor2, padx=0, pady=0, relief='flat')
frame_cima.grid(row = 0, column=0, sticky=NSEW)


frame_baixo = Frame(janela,width=300, height=310, bg = cor2, padx=0, pady=0, relief='flat')
frame_baixo.grid(row = 1, column=0, sticky=NSEW)

img = Image.open('imagens/senha.png')
img = img.resize((30, 30), Image.LANCZOS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat',anchor='nw', bg=cor2)
app_logo.place(x=2, y=0)

app_nome = Label(frame_cima,width=20, height=1, text='GERADOR DE SENHAS', padx=0, relief='flat',anchor='nw', bg=cor2, fg=cor1, font='ivy 16 bold')
app_nome.place(x=35, y=3)

app_linha = Label(frame_cima,width=300, height=1, text='', padx=0, relief='flat',anchor='nw', bg=cor3, fg=cor1, font='ivy 1')
app_linha.place(x=0, y=35)

#----------------------Parte superior-------------------

app_senha = Label(frame_baixo,width=26, height=2, text='- - -', padx=0, relief='solid',anchor='center', bg=cor2, fg=cor1, font='ivy 10 bold')
app_senha.grid(row =0, column=0, columnspan=1, sticky=NSEW, padx=7, pady=10)

app_info = Label(frame_baixo,width=26, height=1, text='Número total de caracteres', padx=0, relief='flat',anchor='nw', bg=cor2, fg=cor1, font='ivy 10 bold')
app_info.grid(row =1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_ =0, to=20, width=5, textvariable= var)
spin.grid(row =2, column=0, columnspan=2, sticky=NW, padx=7, pady=8)


frame_caracteres = Frame(frame_baixo,width=300, height=210, bg = cor2, padx=0, pady=0, relief='flat')
frame_caracteres.grid(row = 3, column=0, sticky=NSEW, columnspan=3)

estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var= estado_1, onvalue=alfa_maior, offvalue='off', bg=cor2)
check_1.grid(row = 0, column=0, sticky=NW, padx=2, pady=5)

info_check1 = Label(frame_caracteres,width=26, height=1, text='ABC Letras maiusculas', padx=0, relief='flat',anchor='nw', bg=cor2, fg=cor1, font='ivy 10 bold')
info_check1.grid(row =0, column=1, sticky=NW, padx=2, pady=7)

estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var= estado_2, onvalue=alfa_menor, offvalue='off', bg=cor2)
check_2.grid(row = 1, column=0, sticky=NW, padx=2, pady=5)

info_check2 = Label(frame_caracteres,width=26, height=1, text='abc Letras minusculas', padx=0, relief='flat',anchor='nw', bg=cor2, fg=cor1, font='ivy 10 bold')
info_check2.grid(row =1, column=1, sticky=NW, padx=2, pady=7)

estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var= estado_3, onvalue=numeros, offvalue='off', bg=cor2)
check_3.grid(row = 2, column=0, sticky=NW, padx=2, pady=5)

info_check3 = Label(frame_caracteres,width=26, height=1, text='Números (123456789)', padx=0, relief='flat',anchor='nw', bg=cor2, fg=cor1, font='ivy 10 bold')
info_check3.grid(row =2, column=1, sticky=NW, padx=2, pady=7)

estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var= estado_4, onvalue= simbolos, offvalue='off', bg=cor2)
check_4.grid(row = 3, column=0, sticky=NW, padx=2, pady=5)

info_check4 = Label(frame_caracteres,width=26, height=1, text='Símbolos ([]{}()*;/_-)', padx=0, relief='flat',anchor='nw', bg=cor2, fg=cor1, font='ivy 10 bold')
info_check4.grid(row =3, column=1, sticky=NW, padx=2, pady=7)




estilo = ttk.Style(janela)
estilo.theme_use('clam')
janela.mainloop()