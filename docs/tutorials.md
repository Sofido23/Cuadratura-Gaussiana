# Guía de Uso

En este tutorial, se explica cómo utilizar la **cuadratura de Gauss** para aproximar la integral de la función \( \sin(x^2) \) en el intervalo \([0, \pi]\).

## Paso 1: Importación de librerías

Primero, es necesario importar las funciones previamente definidas y las bibliotecas estándar:

```python
from Gaussian_Cuadrature.Cuadrature import gaussxw, gaussxwab, integrando
import numpy as np
import matplotlib.pyplot as plt
```

## Implementación del Método de Cuadratura Gaussiana

A continuación, se presentan las instrucciones para implementar el método de cuadratura gaussiana paso a paso.

### Paso 2: Definición de las funciones de cuadratura

Primero, definimos las funciones necesarias para la cuadratura gaussiana. La función `gaussxw` calcula los puntos de muestreo y los pesos para la cuadratura de Gauss-Legendre, y la función `gaussxwab` escala estos valores al intervalo deseado.

```python
def gaussxw(N):
    """
    Calcula los puntos de muestreo y pesos de Gauss-Legendre.

    Parameters:
        N (int): Número de puntos de muestreo.

    Returns:
        tuple: Dos arrays, `x` y `w`, con los puntos y pesos.

    Example:
        >>> x, w = gaussxw(2)
        >>> np.allclose(x, [-1/np.sqrt(3), 1/np.sqrt(3)])                                                                 True
        >>> np.allclose(w, [1.0, 1.0])
        True
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """
    Escala los puntos y pesos de Gauss-Legendre al intervalo [a, b].

    Parameters:
        a (float): Límite inferior.
        b (float): Límite superior.
        x (array): Puntos originales en [-1, 1].
        w (array): Pesos originales.

    Returns:
        tuple: Nuevos puntos y pesos escalados al intervalo [a, b].

    Example:
        >>> x = np.array([-1.0, 0.0, 1.0])
        >>> w = np.array([1.0, 4.0, 1.0])
        >>> x_new, w_new = gaussxwab(0, np.pi, x, w)
        >>> np.allclose(x_new, [0.0, np.pi/2, np.pi])
        True
        >>> np.allclose(w_new, [np.pi/2, 2*np.pi, np.pi/2])
        True
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


def integrando(x):
    """
    Define la función a integrar.

    Parameters:
        x (float or array): Valor o arreglo de valores de entrada.

    Returns:
        float or array: Resultado de evaluar sin(x^2).

    Example:
        >>> integrando(0)
        0.0
        >>> round(integrando(1), 5)
        0.84147
        >>> np.allclose(integrando(np.array([0, 1])), [0.0, np.sin(1)])
        True
    """
    return np.sin(x**2)
N_valores = np.arange(2, 21)
resultados = []

for N in N_valores:
    x, w = gaussxw(N)
    x_scaled, w_scaled = gaussxwab(0, np.pi, x, w)
    integral = np.sum(w_scaled * integrando(x_scaled))
    resultados.append(integral)
import matplotlib.pyplot as plt

plt.plot(N_valores, resultados, 'o-')
plt.xlabel('N (Número de puntos de muestreo)')
plt.ylabel('Valor de la integral')
plt.title('Cuadratura Gaussiana para la integral de sin(x^2) de 0 a pi')
plt.grid(True)
plt.show()

