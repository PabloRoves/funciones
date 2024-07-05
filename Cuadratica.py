"""ecuaciones_cuadraticas"""

from math import sqrt
from matplotlib import pyplot as plt
import numpy as np


class Cuadratica:
    """clase para graficar funciones cuadraticas"""

    def __init__(self, arga, argb, argc):
        if int(arga) == 0:
            raise ValueError("El primer coeficiente no puede ser 0")

        self.ca = arga
        self.cb = argb
        self.cc = argc

    def obtener_raices(self, arga, argb, argc):
        """
        Resuelve una ecuación cuadrática de la forma ax^2 + bx + c = 0 y devuelve las soluciones.

        Calcula las soluciones de la ecuación cuadrática utilizando la fórmula general:
            x1 = (-b + sqrt(b^2 - 4ac)) / (2a)
            x2 = (-b - sqrt(b^2 - 4ac)) / (2a)

        Parámetros
        ----------
        arga : float
            Coeficiente 'a' de la ecuación cuadrática.
        argb : float
            Coeficiente 'b' de la ecuación cuadrática.
        argc : float
            Coeficiente 'c' de la ecuación cuadrática.

        Returns
        -------
        tuple
            Una tupla que contiene las soluciones de la ecuación cuadrática. Dependiendo del 
            valor del determinante (b^2 - 4ac):
            - Si el determinante es mayor que 0, devuelve las dos soluciones reales distintas (x1, x2).
            - Si el determinante es igual a 0, devuelve una única solución real doble (x1,).
            - Si el determinante es menor que 0, devuelve una tupla vacía () indicando que no hay 
            soluciones reales.

        Librerías
        ---------
        - math.sqrt para calcular la raíz cuadrada.
        """
        determinante = argb**2 - 4*arga*argc

        if determinante > 0:
            x_1 = -argb + sqrt(argb**2 - 4*arga*argc) / (2*arga)
            x_2 = -argb + sqrt(argb**2 - 4*arga*argc) / (2*arga)
            return x_1, x_2

        if determinante == 0:
            x_1 = -argb / (2*arga)
            return (x_1,)

        return tuple()

    def expresion_general(self, ca, cb, cc):
        """
        Solicita al usuario los coeficientes de una ecuación cuadrática, la resuelve 
        y muestra la ecuación en formato estándar.

        Esta función solicita al usuario que ingrese los coeficientes 'a', 'b' y 'c' 
        de una ecuación cuadrática (ax^2 + bx + c = 0), los convierte a enteros, resuelve 
        la ecuación utilizando la función 'resolver_ecuacion()', y luego imprime la 
        solución y la ecuación en formato estándar 'y = ax^2 + bx + c'.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        - Utiliza la función 'resolver_ecuacion()' para obtener las raíces de la ecuación.
        - Muestra la ecuación en formato estándar 'y = ax^2 + bx + c'.
        """

        ecuacion = "y="

        if int(ca) > 1:
            ecuacion += ca
        ecuacion += "x^2"

        if int(cb) > 0:
            ecuacion += "+"
            if int(cb) != 1:
                ecuacion += cb
        elif int(cb) < 0:
            ecuacion += cb

        ecuacion += "x"

        if int(cc) > 0:
            ecuacion += "+"+cc
        elif int(cc) < 0:
            ecuacion += cc

        return ecuacion

    def graficar(self, ca, cb, cc):
        """
        Grafica una función cuadrática de la forma y = ax^2 + bx + c.

        Calcula y grafica la función cuadrática utilizando los coeficientes dados.

        Parameters
        ----------
        ca : float
            Coeficiente 'a' de la ecuación cuadrática (debe ser distinto de 0).
        cb : float
            Coeficiente 'b' de la ecuación cuadrática.
        cc : float
            Término independiente 'c' de la ecuación cuadrática.

        Returns
        -------
        None

        Notes
        -----
        - Esta función utiliza numpy y matplotlib para generar y mostrar la gráfica de la función cuadrática.
        - Si el coeficiente 'a' es igual a 0, imprime un mensaje de advertencia y devuelve sin graficar.
        - Ajusta los límites de la gráfica para mostrar un rango adecuado alrededor del origen.

        Libraries
        ---------
        - matplotlib.pyplot como plt
        - numpy como np
        """

        # RAICES = Cuadratica.obtener_raices(self, ca, cb, cc)

        if ca == 0:
            print("El primer coeficiente no puede ser 0")
            return

        x = np.linspace(-4, 4, 50)
        y = ca*x**2+cb*x+cc
        plt.plot(x, y)
        plt.xlabel("x axis")
        plt.ylabel("y axis")
        v = [-10, 10, -10, 10]
        plt.axis(v)
        # print(x)
        plt.grid()
        plt.show()
