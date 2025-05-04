import numpy as np
from scipy.special import legendre
import matplotlib.pyplot as plt

def gaussxw(N):
    """
    Calcula los puntos y pesos para la cuadratura de Gauss-Legendre en el intervalo [-1, 1].

    Parameters
    ----------
    N : int
        Número de puntos de muestreo (nodos) para la cuadratura.

    Returns
    -------
    x : ndarray
        Arreglo de puntos (raíces del polinomio de Legendre).
    w : ndarray
        Arreglo de pesos correspondientes a cada punto.

    Examples
    --------
    >>> x, w = gaussxw(2)
    >>> np.allclose(x, [-1/np.sqrt(3), 1/np.sqrt(3)])
    True
    >>> np.allclose(w, [1.0, 1.0])
    True
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """
    Transforma los puntos y pesos de la cuadratura de Gauss del intervalo [-1, 1] al intervalo [a, b].

    Parameters
    ----------
    a : float
        Límite inferior del nuevo intervalo.
    b : float
        Límite superior del nuevo intervalo.
    x : ndarray
        Puntos originales en el intervalo [-1, 1].
    w : ndarray
        Pesos originales en el intervalo [-1, 1].

    Returns
    -------
    x_scaled : ndarray
        Puntos transformados al intervalo [a, b].
    w_scaled : ndarray
        Pesos ajustados para el intervalo [a, b].

    Examples
    --------
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
    Función a integrar: sin(x^2).

    Parameters
    ----------
    x : float or ndarray
        Valor o arreglo de valores donde evaluar la función.

    Returns
    -------
    float or ndarray
        Resultado de sin(x^2) evaluado en x.

    Examples
    --------
    >>> float(integrando(0))
    0.0
    >>> float(np.round(integrando(1), 5))
    0.84147
    >>> np.allclose(integrando(np.array([0, 1])), [0.0, np.sin(1)])
    True
    """
    return np.sin(x**2)

# Valores de N para probar diferentes cantidades de puntos de muestreo
N_valores = np.arange(2, 21)
resultados = []

# Aproximación de la integral ∫₀^π sin(x²) dx usando cuadratura gaussiana
for N in N_valores:
    x, w = gaussxw(N)
    x_scaled, w_scaled = gaussxwab(0, np.pi, x, w)
    integral = np.sum(w_scaled * integrando(x_scaled))
    resultados.append(integral)

# Gráfica de convergencia de la integral con respecto a N
plt.plot(N_valores, resultados, 'o-')
plt.xlabel('N (Número de puntos de muestreo)')
plt.ylabel('Valor de la integral ∫₀^π sin(x²) dx')
plt.title('Cuadratura Gaussiana para ∫₀^π sin(x²) dx')
plt.grid(True)
plt.show()
