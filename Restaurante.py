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

# Evitar que la pantalla se cierre
aplicacion.mainloop()