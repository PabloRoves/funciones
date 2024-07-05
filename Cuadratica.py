"""ecuaciones_cuadraticas"""

from math import sqrt
from matplotlib import pyplot as plt
import numpy as np


class Cuadratica:
    """clase para graficar funciones cuadraticas"""

    def obtenerx(self, arga, argb, argc):
        """Calculo los posibles X y los devuelvo"""

        determinante = argb**2 - 4*arga*argc
        if determinante > 0:
            x_1 = (-argb - sqrt(argb**2 - 4*arga*argc)) / (2*arga)
            x_2 = (-argb + sqrt(argb**2 - 4*arga*argc)) / (2*arga)
            return x_1, x_2
        if determinante == 0:
            x_1 = -argb / (2*arga)
            return x_1
        return tuple()

    def mostrarEcuacion(self, cA, cB, cC):
        """Arma la ecuación y la devuelve como string"""
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

    # def graficar(self, cA, cB, cC):
    #     valores = Cuadratica.obtenerX(cA, cB, cC)

    #     if cA == 0:
    #         print("El primer coeficiente no puede ser 0")
    #         return

    #     x = np.linspace(-4, 4, 50)
    #     y = cA*x**2+cB*x+cC
    #     plt.plot(x, y)
    #     plt.xlabel("x axis")
    #     plt.ylabel("y axis")
    #     v = [-10, 10, -10, 10]
    #     plt.axis(v)
    #     # print(x)
    #     plt.grid()
    #     plt.show()
