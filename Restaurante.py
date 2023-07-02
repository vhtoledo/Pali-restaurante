from tkinter import *

# Iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# Evitar maximizar
aplicacion.resizable(0, 0)

# Titulo de la ventana
aplicacion.title("Pali RestoBar - Sistema de Facturación")

# Color de fondo de la ventana
aplicacion.config(bg='DarkGrey')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiquieta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4',
                        font=('Dosis', 47), bg='DarkGrey', width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='DarkGrey')
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='DarkGrey')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='DarkGrey')
panel_botones.pack()

# lista de productos
lista_comidas = ['pollo', 'coredero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# generar items comida
variables_comida = []
contador = 0
for comida in lista_comidas:
    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador])

    comida.grid(row=contador,
                column=0,
                sticky=W,)
    contador += 1

# generar items bebidas
variables_bebida = []
contador = 0
for bebida in lista_bebidas:
    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador])

    bebida.grid(row=contador,
                column=0,
                sticky=W,)
    contador += 1

# generar items postres
variables_postre = []
contador = 0
for postre in lista_postres:
    # crear checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador])

    postre.grid(row=contador,
                column=0,
                sticky=W,)
    contador += 1

# Evitar que la pantalla se cierre
aplicacion.mainloop()