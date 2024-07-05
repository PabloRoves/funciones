"""ecuaciones_cuadraticas"""

from math import sqrt
from matplotlib import pyplot as plt
import numpy as np


class Cuadratica:
    """clase para graficar funciones cuadraticas"""

    def __init__(self, arga, argb, argc):
        try:
            self.ca = int(arga)
            self.cb = int(argb)
            self.cc = int(argc)

        except ValueError as exc:
            raise ValueError("Los coéficientes deben ser números.") from exc

        if self.ca == 0:
            raise ValueError("El primer coeficiente no puede ser 0.")

    def obtener_raices(self):
        """
        Calcula las raíces de una ecuación cuadrática de la forma ax^2 + bx + c = 0 y devuelve las soluciones.

        Utiliza los coeficientes 'ca', 'cb' y 'cc' almacenados en el objeto actual (self) para calcular las raíces 
        de la ecuación cuadrática utilizando la fórmula general:
            x1 = (-b + sqrt(b^2 - 4ac)) / (2a)
            x2 = (-b - sqrt(b^2 - 4ac)) / (2a)

        Returns
        -------
        tuple
            Una tupla que contiene las soluciones de la ecuación cuadrática. Dependiendo del valor del determinante (b^2 - 4ac):
            - Si el determinante es mayor que 0, devuelve las dos soluciones reales distintas (x1, x2).
            - Si el determinante es igual a 0, devuelve una única solución real doble (x1, x1).
            - Si el determinante es menor que 0, devuelve una tupla vacía () indicando que no hay soluciones reales.
        """

        ca = self.ca
        cb = self.cb
        cc = self.cc

        determinante = cb**2 - 4*ca*cc

        if determinante > 0:
            x_1 = (-cb + sqrt(cb**2 - 4*ca*cc)) / (2*ca)
            x_2 = (-cb - sqrt(cb**2 - 4*ca*cc)) / (2*ca)
            y_1 = ca*x_1**2+cb*x_1+cc
            y_2 = ca*x_2**2+cb*x_2+cc

            return ([x_1, y_1], [x_2, y_2])

        if determinante == 0:
            x = -cb / (2*ca)
            y = ca*x**2+cb*x+cc
            return ([x, y])

        return tuple()

    def expresion_general(self):
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
        ca = self.ca
        cb = self.cb
        cc = self.cc

        ecuacion = "y="

        if ca > 1:
            ecuacion += str(ca)
        ecuacion += "x^2"

        if cb > 0:
            ecuacion += "+"
            if cb != 1:
                ecuacion += str(cb)
        elif cb < 0:
            ecuacion += str(cb)

        ecuacion += "x"

        if cc > 0:
            ecuacion += "+"+str(cc)
        elif cc < 0:
            ecuacion += str(cc)

        return ecuacion

    def graficar(self):
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
        ca = self.ca
        cb = self.cb
        cc = self.cc

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
