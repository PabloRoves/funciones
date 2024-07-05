"""Prueba de funcion lineal"""

# from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def funcion_lineal():
    """Genera y muestra una gráfica de una ecuación lineal utilizando matplotlib.

    Esta función utiliza numpy para generar datos de prueba y matplotlib para 
    graficar una línea roja sólida.

    No devuelve ningún valor. La gráfica se muestra utilizando plt.show()."""
    x = np.arange(-4, 5)
    y = np.arange(-4, 5)

    plt.plot(y, x, color='red', linestyle='solid')
    plt.title('Ecuación lineal')

    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid()
    plt.show()
