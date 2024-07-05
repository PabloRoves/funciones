"""Prueba de funcion Cuadrática"""

from math import sqrt

# Crear una función para resolver una ecuación cuadrática.
# a*x^2 + b* + c = 0
# a, b, c


# print("Función cuadratica")
def obtener_raices(arga, argb, argc):
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


def mostrar_ecuacion():
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
    print("Ingresa los coeficientes")
    ca = input()
    cb = input()
    cc = input()
    print(obtener_raices(int(ca), int(cb), int(cc)))

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

    print(ecuacion)


mostrar_ecuacion()
