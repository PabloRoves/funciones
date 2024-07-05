"""
Archivo de ejemplo para graficar una función lineal utilizando matplotlib y numpy.

Este archivo contiene una función llamada funcion_lineal que genera y muestra
una gráfica de una ecuación lineal utilizando las bibliotecas matplotlib y numpy.

Bibliotecas requeridas:
- matplotlib
- numpy

Funciones definidas:
- funcion_lineal(): Genera y muestra una gráfica de una ecuación lineal.

Este archivo se puede ejecutar para visualizar la gráfica de la función lineal.

Ejemplo de uso:
>>> python archivo_ejemplo.py

"""
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
