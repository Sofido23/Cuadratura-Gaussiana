# Referencia 

---

## `gaussxw(N)`

Devuelve los puntos de muestreo y pesos para la cuadratura de Gauss-Legendre estándar en el intervalo \([-1, 1]\).

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
        >>> np.allclose(x, [-1/np.sqrt(3), 1/np.sqrt(3)])
        True
        >>> np.allclose(w, [1.0, 1.0])
        True
    """
```

---

## `gaussxwab(a, b, x, w)`

Transforma los puntos y pesos de la cuadratura de Gauss-Legendre desde el intervalo \([-1, 1]\) al intervalo \([a, b]\).

```python
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
```

---

## `integrando(x)`

Función que se desea integrar, definida inicialmente como \( f(x) = \sin(x^2) \). Puedes modificarla según tu necesidad.

```python
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
```

---
