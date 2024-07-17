# Project of Mathematical Functions

This Python project enables working with mathematical functions, specifically linear and quadratic equations. It utilizes the matplotlib, numpy, and math libraries for plotting functions and calculating roots of quadratic equations.

## Installation and Setup

To use this project, make sure you have the following libraries installed:

```bash
pip install matplotlib numpy
```

## Usage

### Linear Functions

In lineal.py, the funcion_lineal function generates and displays plots of linear equations. Below is an example of how to use it:

```python
import lineal as Lineal

# Plot a linear function
Lineal.funcion_lineal()
```

### Quadratic Functions

In cuadratica.py, the Cuadratica class allows working with quadratic equations. Here's an example of using this class from main.py:

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

### Execution

To run the main.py file and see the results, simply execute the following command:

```bash
python main.py
```

## Project Structure

The project is organized into three main files:

- lineal.py: Contains a function to plot linear equations.
- cuadratica.py: Defines the Cuadratica class for working with quadratic equations, including methods to calculate roots, obtain the general expression, and plot the function.
- main.py: Main file for testing and utilizing both lineal.py and cuadratica.py.

## Credits

This project uses the matplotlib, numpy, and math libraries for mathematical operations and plotting.

## Contribution

We welcome contributions to improve this project! Please create pull requests on GitHub.

## License

This project is licensed under the MIT License.
