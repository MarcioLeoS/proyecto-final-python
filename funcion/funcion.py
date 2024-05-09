import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk

#Creamos la ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Graficador de funciones')
# ventana.iconbitmap('./prueba/python.ico') # Esta línea produce un error si el icono no existe, comentada temporalmente

# Ajusto para obtener el valor y procesarlo
entrada_funcion = tk.StringVar(value='')
entrada_1 = ttk.Entry(ventana, width=30, textvariable=entrada_funcion)
entrada_1.grid(row=0, column=0)

def recibir():
    funcion_texto = entrada_funcion.get()
    print('Función recibida:', funcion_texto)
    try:
        x = np.linspace(-10, 10, 400)
        y = eval(funcion_texto)  # esto evalúa la función ingresada por el usuario
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfico de ' + funcion_texto)
        plt.show()
    except Exception as e:
        print('Error:', e)

boton_1 = ttk.Button(ventana, text='Recibir', command=recibir)
boton_1.grid(row=0, column=1)

# Inicialización
ventana.mainloop()


