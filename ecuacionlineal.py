"""Prueba de funcion lineal"""

# from math import sqrt
from matplotlib import pyplot as plt
import numpy as np


def funcion_lineal():
    x = np.arange(-4, 5)
    y = np.arange(-4, 5)
    plt.plot(y, x, color='red', linestyle='solid')
    plt.title('Ecuación lineal')

    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid()
    plt.show()
