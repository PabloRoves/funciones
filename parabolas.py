"""
Función para graficar una parábola utilizando matplotlib y numpy.

Esta función utiliza numpy para generar un arreglo de valores de x, 
calcula los correspondientes valores de y (y = x**2), y luego utiliza 
matplotlib para graficar la parábola resultante.

Librerías requeridas:
- matplotlib.pyplot como plt
- numpy como np

La gráfica incluye etiquetas para los ejes x e y, ajusta los límites 
de la gráfica a [-5, 5, 0, 10], muestra una cuadrícula y finalmente 
muestra la gráfica.

No devuelve ningún valor.
"""
import matplotlib.pyplot as plt
import numpy as np


def funcion_parabola():
    """
    Genera y muestra una gráfica de una parábola.

    Calcula valores de x y sus correspondientes valores de y = x^2 utilizando 
    numpy.linspace(), y grafica la parábola resultante utilizando matplotlib.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Libraries
    ---------
    - matplotlib.pyplot como plt
    - numpy como np

    Notes
    -----
    Esta función muestra una gráfica de una parábola, con el eje x etiquetado como
    'x axis', el eje y etiquetado como 'y axis', los límites de la gráfica ajustados
    a [-5, 5, 0, 10], y una cuadrícula para una mejor visualización. No devuelve ningún
    valor."""
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
