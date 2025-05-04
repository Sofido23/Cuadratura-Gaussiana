# Guía de Uso 

En este tutorial, aprenderás cómo utilizar la **cuadratura de Gauss** para aproximar la integral de la función \( \sin(x^2) \) en el intervalo \([0, \pi]\)

## Paso 1: Importar las librerías necesarias


El primer paso es importar las funciones que ya tenemos definidas en el código.
```python
from Gaussian_Cuadrature.Cuadrature import gaussxw, gaussxwab, integrando
import numpy as np
import matplotlib.pyplot as plt
```

## Paso 2: Definir funciones de cuadratura


Estas funciones generan los puntos y pesos necesarios para la integración:

```python
def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w
```
## Paso 3: Definir la función a integrar

```python
def integrando(x):
    return np.sin(x**2)
```
## Paso 4: Aplicar el método

```python
N_valores = np.arange(2, 21)
resultados = []

for N in N_valores:
    x, w = gaussxw(N)
    x_scaled, w_scaled = gaussxwab(0, np.pi, x, w)
    integral = np.sum(w_scaled * integrando(x_scaled))
    resultados.append(integral)
```
## Paso 5: Visualizar los resultados

```python
plt.plot(N_valores, resultados, 'o-')
plt.xlabel('N (Número de puntos de muestreo)')
plt.ylabel('Valor de la integral')
plt.title('Cuadratura Gaussiana para la integral de sin(x^2) de 0 a pi')
plt.grid(True)
plt.show()
```
