#pip install numpy
#pip install matplotlib

import random
import matplotlib.pyplot as plt
import numpy as np


# DEFINO LAS CLASES
# CLASE PARA LOS DADOS
class Dado:
    def __init__(self, caras=6):
        self.caras = caras

    def tirar(self):
        return random.randint(1, self.caras)


class JuegoDeDados:
    def __init__(self, num_dados=2):
        self.num_dados = num_dados
        self.dados = [Dado() for _ in range(num_dados)]

    def jugar(self):
        print(
            "¡Bienvenido al juego de dados Argentino! ¡Saca al menos 4 en cada uno y te llevas el loto!"
        )
        input("Presiona Enter para tirar los dados...")

        resultados = [dado.tirar() for dado in self.dados]
        suma_resultados = sum(resultados)

        print("Resultados de los dados:", resultados)
        print("Suma de los resultados:", suma_resultados)

        if suma_resultados == self.num_dados * 4:
            print("¡Bien ahí! Sacaste la máxima puntuación.")
        elif suma_resultados == self.num_dados:
            print("¡Mal ahí! Sacaste la puntuación mínima.")
        else:
            print("¡Jugá mejor la próxima!")


# CLASE PARA LA GRAFICA
class Grafica:
    def graficador_funcion(self):
        funcion_texto = input(
            "Ingrese la función que desea graficar (por ejemplo: 'x**2'): "
        )
        try:
            x = np.linspace(-10, 10, 400)
            y = eval(funcion_texto)
            plt.plot(x, y)
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.title("Gráfico de " + funcion_texto)
            plt.show()
        except Exception as e:
            print("Error:", e)


# CLASE PARA PIEDRA PAPEL TIJERAS
class Manos:
    def __init__(self, opciones=3):
        self.opciones = opciones

    def seleccionar(self):
        return random.randint(1, self.opciones)


class JugarPiedraPapelTijeras:
    def __init__(self, num_manos=2):
        self.manos = [Manos() for _ in range(num_manos)]

    def jugar_piedras_papel_tijeras(self):
        print("¡Bienvenido a piedra, papel o tijeras!")
        input("Presiona Enter para empezar, después de tres...")

        resultados = [mano.seleccionar() for mano in self.manos]
        resultados_jugador1 = resultados[0]
        resultados_jugador2 = resultados[1]

        manosPosibles = ["Piedra", "Papel", "Tijeras"]

        for i, mano in enumerate(manosPosibles):
            print(mano)
            if i + 1 == resultados_jugador1:
                resultado1 = mano
                break

        for i, mano in enumerate(manosPosibles):
            print(mano)
            if i + 1 == resultados_jugador2:
                resultado2 = mano
                break

        print("Resultados del jugador 1:", resultado1)
        print("Resultados del jugador 2:", resultado2)


# CLASE PARA NUM RANDOM


class NumeroRandom:
    def __init__(self):
        self.numrandom = random.randint(1, 10)


class JugarAdivinar:
    def __init__(self):
        print("Bienvenido al juego del azar!")
        self.numjugador = int(input("¡Ingresa un número entre el 1 y el 10! "))
        if self.numjugador > 10 or self.numjugador < 1:
            print(
                "Elegiste un número fuera del rango. Acordate de que más grande el rango, menos chances."
            )
        else:
            self.jugar_azar()

    def jugar_azar(self):
        numero_random = NumeroRandom().numrandom
        if self.numjugador == numero_random:
            print(f"El número que la máquina eligió es el: {numero_random}")
            print("¡Felicidades  Ganaste $300.000!")
        else:
            print(f"El número que la máquina eligió es el: {numero_random}")
            print("¡No acertaste!")


# LLAMO A LA CLASE JuegoDeDados
def jugar_a_los_dados():
    juegoDados = JuegoDeDados()
    juegoDados.jugar()


def piedra_papel_tijeras():
    juegoPPT = JugarPiedraPapelTijeras()
    juegoPPT.jugar_piedras_papel_tijeras()


def jugar_con_azar():
    juegoAzar = JugarAdivinar()
    juegoAzar.jugar_azar()


# GRAFICA
def graficar_funcion():
    graficar = Grafica()
    graficar.graficador_funcion()


def main():
    while True:
        input("Comenzar a jugar?")
        print(
            "Qué está deseando hacer\n1 ¿Jugar a los dados?\n2 ¿Jugar a piedra, papel o tijeras?\n3 ¿Jugar con el azar?\n4 ¿Graficar una función?\n5 ¿Salir?"
        )

        opcion = input("Ingrese el número correspondiente a su elección: ")

        if opcion == "1":
            jugar_a_los_dados()
        elif opcion == "2":
            piedra_papel_tijeras()
        elif opcion == "3":
            jugar_con_azar()
        elif opcion == "4":
            graficar_funcion()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")


if __name__ == "__main__":
    main()
