# Site para baixar icones: https://icons8.com/icons/set/password
# https://icons8.com/icons/set/password ou https://icon-icons.com/pt/icones/busca/?filtro=money  =  Site para baixar icones que vao dentro do app  == (xxx.png)
# pip install pillow


# * Pelo fato do gerador ter como foco, gerar senhas fortes, é necessário marcar a 1º opção de letras maiúsculas para o exito do programa, as outras opções são opcionais.


from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image  # Pillow
from tkinter import messagebox

# import para senhas
import string
import random


# cores ---------------------
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul


janela = Tk()
janela.title('Gerador')
# janela.geometry('295x360')
janela.configure(bg=cor2)
# Bloquia a tela cheia e deixa como nao redirecionamento
janela.resizable(width=False, height=False)
janela.iconbitmap('senha.ico')  # icon do app


estilo = ttk.Style(janela)
estilo.theme_use('clam')


# Dividindo a tela em dois frames ---------------------------
frame_cima = Frame(janela, width=295, height=50, bg=cor2,
                   pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310,
                    bg=cor2, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)


# Trabalhando no frame_Cima do nome e da imagem do app --------------------------
img = Image.open('senha.PNG')
img = img.resize((30, 30), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT,
                 padx=10, relief='flat', anchor='nw', bg=cor2)
app_logo.place(x=2, y=-1)

app_nome = Label(frame_cima, text='GERADOR DE SENHAS', width=20, height=1,
                 padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold'), bg=cor2, fg=cor1)
app_nome.place(x=35, y=2)

app_linha = Label(frame_cima, text='', width=295, height=1, padx=0,
                  relief='flat', anchor='nw', font=('Ivy 1'), bg='#3080f0', fg=cor1)
app_linha.place(x=0, y=35)


# -----------Função Gerar Senha -------------

def criar_senha():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '[]{}()*;/,_-'

    global combinar

    # condição para Maiuscula

    if estado_1.get() == alfabeto_maior:
        combinar = alfabeto_maior
    else:
        messagebox.showwarning(
            'Atenção!', 'Almejando senhas fortes, o primeiro campo deve estar sempre selecionado para o restante funcionar')
        return

    # condição para Minuscula

    if estado_2.get() == alfabeto_menor:
        combinar = combinar + alfabeto_menor
    else:
        pass

    # condição para Numero

    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    # condição para Simbolos

    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    comprimento = int(spin.get())
    senha = ''.join(random.sample(combinar, comprimento))

    app_senha['text'] = senha


# ---------- Função Copiar Senha -----------


    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo('Sucesso', 'A senha foi copiada com sucesso')

    botao_gerar_senha = Button(frame_baixo, command=copiar_senha, text='Copiar', width=7, height=2, padx=0,
                               relief='raised', overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor1)
    botao_gerar_senha.grid(row=0, column=1, sticky=NW,
                           padx=5, pady=7, columnspan=1)


# Trabalhando no frame_baixo --------------------------

app_senha = Label(frame_baixo, text='- - - - -', width=21, height=2, padx=0,
                  relief='solid', anchor='center', font=('Ivy 12 bold'), bg=cor2, fg=cor1)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_baixo, text='Numero total de caracteres na senha', height=1,
                 padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor2, fg=cor1)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)


# Criando a Spin Box -----------------
var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)


# Senhas -----------------

alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '[]{}()*;/,_-'

frame_caracteres = Frame(frame_baixo, width=295,
                         height=210, bg=cor2, pady=0, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)


# Caixas de acesso ----------------

# estado_1 = StringVar()
# estado_1.set(False)
# check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfabeto_maior, offvalue='off', relief='flat', bg=cor2)
# check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)


# ---------------- Letras maiúsculas ----------------

estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1,
                      onvalue=alfabeto_maior, offvalue='off', relief='flat', bg=cor2)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)

# é o que vai escrito do lado da caixa de opção
app_info = Label(frame_caracteres, text='ABC Letras maiusculas', height=1,
                 padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor2, fg=cor1)
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)


# ---------------- Letras minúsculas ----------------

estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2,
                      onvalue=alfabeto_menor, offvalue='off', relief='flat', bg=cor2)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)

# é o que vai escrito do lado da caixa de opção
app_info = Label(frame_caracteres, text='ABC Letras minúsculas', height=1,
                 padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor2, fg=cor1)
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)


# ---------------- Números ----------------

estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3,
                      onvalue=numeros, offvalue='off', relief='flat', bg=cor2)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)

# é o que vai escrito do lado da caixa de opção
app_info = Label(frame_caracteres, text='123 Numeros', height=1, padx=0,
                 relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor2, fg=cor1)
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5)


# ---------------- Símbolos ----------------

estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4,
                      onvalue=simbolos, offvalue='off', relief='flat', bg=cor2)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)

# é o que vai escrito do lado da caixa de opção
app_info = Label(frame_caracteres, text='Símbolos', height=1, padx=0,
                 relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor2, fg=cor1)
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5)


# ---------------- Botao Gerar Senha ----------------

botao_gerar_senha = Button(frame_caracteres, command=criar_senha, text='Gerar Senha', width=34, height=1, padx=0,
                           relief='flat', overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg='#3080f0', fg=cor2)
botao_gerar_senha.grid(row=5, column=0, sticky=NSEW,
                       padx=5, pady=11, columnspan=5)


# * Centralizando o arquivo

# Dimensoes da janela
largura = 295
altura = 360

# Resolução do nosso sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()
# print(largura_screen, altura_screen)  # para saber as dimensoes do monitor


# Posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

# Definir a geometria
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


janela.mainloop()
