# Proyecto de Funciones Matemáticas

Este proyecto en Python permite trabajar con funciones matemáticas, específicamente ecuaciones lineales y cuadráticas. Utiliza las bibliotecas matplotlib, numpy y math para graficar funciones y calcular raíces de ecuaciones cuadráticas.

## Estructura del Proyecto

El proyecto está organizado en tres archivos principales:

- lineal.py: Contiene una función para graficar ecuaciones lineales.
- cuadratica.py: Define la clase Cuadratica para trabajar con ecuaciones cuadráticas, incluyendo métodos para calcular raíces, obtener la expresión general y graficar la función.
- main.py: Archivo principal donde se realizan pruebas y se utiliza tanto lineal.py como cuadratica.py.

## Instalación de Dependencias

Para utilizar este proyecto, asegúrate de tener instaladas las siguientes bibliotecas:

```bash
pip install matplotlib numpy
```

## Uso del Proyecto

### Funciones Lineales

En lineal.py, se encuentra la función funcion_lineal que genera y muestra gráficas de ecuaciones lineales. A continuación, un ejemplo de cómo utilizarla:

```python
import lineal as Lineal

# Graficar una función lineal
Lineal.funcion_lineal()
```

### Funciones Cuadráticas

En cuadratica.py, se define la clase Cuadratica que permite trabajar con ecuaciones cuadráticas. Aquí tienes un ejemplo de cómo utilizar esta clase desde main.py:

```python
from cuadratica import Cuadratica

# Crear una instancia de Cuadratica
ca = int(input("Ingresa el coeficiente a: "))
cb = int(input("Ingresa el coeficiente b: "))
cc = int(input("Ingresa el término independiente c: "))

cuadratica1 = Cuadratica(ca, cb, cc)

# Obtener las raíces de la ecuación cuadrática
print("Raíces de la ecuación cuadrática:", cuadratica1.obtener_raices())

# Obtener la expresión general de la ecuación cuadrática
print("Expresión general de la ecuación cuadrática:", cuadratica1.expresion_general())

# Graficar la función cuadrática
cuadratica1.graficar()
```

### Ejecución

Para ejecutar el archivo main.py y ver los resultados, simplemente ejecuta el siguiente comando:

```bash
python main.py
```

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Clona el repositorio a tu máquina local.
3. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
4. Haz tus cambios y haz commit de ellos (git commit -am 'Añade nueva funcionalidad').
5. Sube los cambios a tu repositorio fork (git push origin feature/nueva-funcionalidad).
6. Envía un pull request para revisar los cambios.

## Créditos

Este proyecto utiliza las bibliotecas matplotlib, numpy y math para realizar operaciones matemáticas y gráficas.

## Licencia

Este proyecto está licenciado bajo Licencia MIT.
