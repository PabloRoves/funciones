"""Prueba de funcion Cuadrática"""

from math import sqrt
from matplotlib import pyplot as plt
import numpy as np

# Crear una función para resolver una ecuación cuadrática.
# a*x^2 + b* + c = 0
# a, b, c


# print("Función cuadratica")
def resolver_ecuacion(argA, argB, argC):
    determinante = argB**2 - 4*argA*argC

    if determinante > 0:
        x_1 = -argB + sqrt(argB**2 - 4*argA*argC) / (2*argA)
        x_2 = -argB + sqrt(argB**2 - 4*argA*argC) / (2*argA)
        return x_1, x_2
    elif determinante == 0:
        x_1 = -argB / (2*argA)
        return (x_1,)
    else:
        return tuple()


def mostrar_ecuacion():

    print("Ingresa los coeficientes")
    cA = input()
    cB = input()
    cC = input()
    print(resolver_ecuacion(int(cA), int(cB), int(cC)))

    ECUACION = "y="

    if int(cA) > 1:
        ECUACION += cA
    ECUACION += "x^2"

    if int(cB) > 0:
        ECUACION += "+"
        if int(cB) != 1:
            ECUACION += cB
    elif int(cB) < 0:
        ECUACION += cB

    ECUACION += "x"

    if int(cC) > 0:
        ECUACION += "+"+cC
    elif int(cC) < 0:
        ECUACION += cC

    print(ECUACION)


def funcion_parabola():
    x = np.linspace(-4, 4, 100)
    y = (x**2)
    plt.plot(x, y)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    v = [-5, 5, 0, 10]
    plt.axis(v)
    print(x)
    plt.grid()
    plt.show()


# mostrar_ecuacion()
# funcion_lineal()
funcion_parabola()
