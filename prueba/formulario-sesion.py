#Imports
#import pandas as pd
#from tkinter import ttk as tk
import tkinter as tk
from tkinter import ttk

#Objects
ventana = tk.Tk()

#Tamaño ventana
ventana.geometry('600x400')

#Nombre ventana e icono
ventana.title('Jugando')
ventana.iconbitmap('./python.ico')

#Creamos botón y evento click
# def evento_click():
#     boton_1.config(text='Botón presionado')
#     print('Ejecusión del evento_click')


#Formulario

entrada_usuario = tk.StringVar(value='Valor por default')
entrada_contraseña = tk.StringVar(value='Valor por default')
entrada_1 = ttk.Entry(ventana, width=30, textvariable=entrada_usuario)
entrada_2 = ttk.Entry(ventana, width=30, textvariable=entrada_contraseña)
entrada_1.grid(row=0, column=0)
entrada_2.grid(row=1, column=0)



#Evento
def enviar():
    boton_1.config(text=entrada_usuario.get())
    print('Info recibida')

    entrada_usuario.set('Cambio...')

    print(entrada_usuario.get())

boton_1 = ttk.Button(ventana, text='Enviar', command=enviar)

#Mostar botón
#boton_1.pack()
boton_1.grid(row=0, column=1)

#Inicialización

ventana.mainloop()




