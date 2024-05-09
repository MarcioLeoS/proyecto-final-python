import random
import matplotlib.pyplot as plt
import numpy as np

# Comentado por GPT:


class Dado:
    """Representa un dado con un número específico de caras."""

    def __init__(self, caras=6):
        """Inicializa el dado con un número específico de caras."""
        self.caras = caras

    def tirar(self):
        """Simula el lanzamiento del dado y devuelve el resultado."""
        return random.randint(1, self.caras)


class JuegoDeDados:
    """Representa un juego de dados donde se lanzan múltiples dados y se suman sus resultados."""

    def __init__(self, num_dados=2):
        """Inicializa el juego con un número específico de dados."""
        self.num_dados = num_dados
        self.dados = [Dado() for _ in range(num_dados)]

    def jugar(self):
        """Inicia el juego de dados."""
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


class Grafica:
    """Representa una herramienta para graficar funciones matemáticas."""

    def graficador_funcion(self):
        """Solicita al usuario una función y grafica su representación."""
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
            plt.grid(
                True, linestyle=":", linewidth=0.5, color="gray", alpha=0.7
            )  # Mostrar cuadrícula, GPT AYUDO PORQUE NO MOSTRABA CUADRICULA
            plt.show()
        except (SyntaxError, NameError, ValueError) as e:
            print("Error al graficar la función:", e)


class Manos:
    """Representa las opciones de piedra, papel o tijeras."""

    def __init__(self, opciones=3):
        """Inicializa el juego con un número específico de opciones."""
        self.opciones = opciones

    def seleccionar(self):
        """Simula la selección de una opción entre piedra, papel o tijeras."""
        return random.randint(1, self.opciones)


class JugarPiedraPapelTijeras:
    """Representa el juego de piedra, papel o tijeras."""

    def __init__(self, num_manos=2):
        """Inicializa el juego con un número específico de jugadores."""
        self.manos = [Manos() for _ in range(num_manos)]

    def jugar_piedras_papel_tijeras(self):
        """Inicia el juego de piedra, papel o tijeras."""
        print("¡Bienvenido a piedra, papel o tijeras!")
        input("Presiona Enter para empezar, después de tres...")

        resultados = [mano.seleccionar() for mano in self.manos]
        resultados_jugador1 = resultados[0]
        resultados_jugador2 = resultados[1]

        manosPosibles = ["Piedra", "Papel", "Tijeras"]

        resultado1 = manosPosibles[resultados_jugador1 - 1]
        resultado2 = manosPosibles[resultados_jugador2 - 1]

        print("Resultados del jugador 1:", resultado1)
        print("Resultados del jugador 2:", resultado2)


class NumeroRandom:
    """Representa un número aleatorio entre 1 y 10."""

    def __init__(self):
        """Inicializa el número aleatorio."""
        self.numrandom = random.randint(1, 10)


class JugarAdivinar:
    """Representa el juego de adivinar un número aleatorio."""

    def __init__(self):
        """Inicializa el juego."""
        print("Bienvenido al juego del azar!")
        self.numjugador = int(input("¡Ingresa un número entre el 1 y el 10! "))
        if self.numjugador > 10 or self.numjugador < 1:
            print(
                "Elegiste un número fuera del rango. Acordate de que más grande el rango, menos chances."
            )
        else:
            self.jugar_azar()

    def jugar_azar(self):
        """Inicia el juego de adivinar el número aleatorio."""
        numero_random = NumeroRandom().numrandom
        print(f"El número que la máquina eligió es el: {numero_random}")
        if self.numjugador == numero_random:
            print("¡Felicidades! Ganaste $300.000!")
        else:
            print("¡No acertaste!")


def jugar_a_los_dados():
    """Inicia el juego de dados."""
    juegoDados = JuegoDeDados()
    juegoDados.jugar()


def piedra_papel_tijeras():
    """Inicia el juego de piedra, papel o tijeras."""
    juegoPPT = JugarPiedraPapelTijeras()
    juegoPPT.jugar_piedras_papel_tijeras()


def jugar_con_azar():
    """Inicia el juego de adivinar un número aleatorio."""
    juegoAzar = JugarAdivinar()
    juegoAzar.jugar_azar()


def graficar_funcion():
    """Inicia el proceso de graficar una función matemática."""
    graficar = Grafica()
    graficar.graficador_funcion()


def main():
    """Función principal que controla el flujo del programa."""
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
