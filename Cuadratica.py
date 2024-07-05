"""ecuaciones_cuadraticas"""

from math import sqrt
from matplotlib import pyplot as plt
import numpy as np


class Cuadratica:

    # Calculo los posibles X y los devuelvo
    def obtenerX(argA, argB, argC):
        determinante = argB**2 - 4*argA*argC

        if determinante > 0:
            x_1 = (-argB - sqrt(argB**2 - 4*argA*argC)) / (2*argA)
            x_2 = (-argB + sqrt(argB**2 - 4*argA*argC)) / (2*argA)
            return x_1, x_2
        elif determinante == 0:
            x_1 = -argB / (2*argA)
            return (x_1)
        else:
            return tuple()

    # Arma la ecuación y la devuelve como string
    def mostrarEcuacion(cA, cB, cC):
        ECUACION = "y="

        if cA != 1:
            ECUACION += str(cA)
        ECUACION += "x^2"

        if cB > 0:
            ECUACION += "+"
            if cB != 1:
                ECUACION += str(cB)
            ECUACION += "x"

        elif cB < 0:
            ECUACION += str(cB) + "x"

        if cC > 0:
            ECUACION += "+" + str(cC)
        elif cC < 0:
            ECUACION += str(cC)

        return ECUACION

    def graficar(cA, cB, cC):
        valores = Cuadratica.obtenerX(cA, cB, cC)

        if cA == 0:
            print("El primer coeficiente no puede ser 0")
            return

        x = np.linspace(-4, 4, 50)
        y = cA*x**2+cB*x+cC
        plt.plot(x, y)
        plt.xlabel("x axis")
        plt.ylabel("y axis")
        v = [-10, 10, -10, 10]
        plt.axis(v)
        # print(x)
        plt.grid()
        plt.show()
