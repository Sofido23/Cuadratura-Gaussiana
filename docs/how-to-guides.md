# Guías paso a paso (How-To Guides)

# Guía de Uso

Este documento proporciona instrucciones detalladas sobre cómo implementar la **Cuadratura Gaussiana** para calcular integrales de manera eficiente.

## Cómo calcular una integral con cuadratura gaussiana

Sigue estos pasos si ya conoces el funcionamiento general del proyecto y deseas integrar una función diferente.

### 1. Cambiar los límites de integración

Edita los valores de `a` y `b` en la llamada a `gaussxwab`. Por ejemplo, para integrar de 1 a 2:

```python
x_scaled, w_scaled = gaussxwab(1, 2, x, w)
```

### 2. Modificar la función a integrar

Sustituye la función `integrando(x)` por otra. Por ejemplo, para \( f(x) = e^{-x^2} \):

```python
def integrando(x):
    return np.exp(-x**2)
```

### 3. Ajustar la precisión

Incrementa el número de puntos `N` para mejorar la precisión:

```python
N_valores = np.arange(5, 51)  # Más puntos, mayor precisión
```

### 4. Obtener el resultado de una sola integración

Si no deseas graficar múltiples resultados sino solo obtener un número:

```python
N = 20
x, w = gaussxw(N)
x_scaled, w_scaled = gaussxwab(0, np.pi, x, w)
resultado = np.sum(w_scaled * integrando(x_scaled))
print("Resultado de la integral:", resultado)
```

---

## Cómo agregar nuevas funciones de prueba

Puedes agregar otras funciones para practicar cambiando `integrando(x)` según tu interés:

```python
# f(x) = cos(x^2)
def integrando(x):
    return np.cos(x**2)
```

O crear varias funciones y seleccionar con una variable:

```python
def f1(x): return np.sin(x**2)
def f2(x): return np.exp(-x)
def f3(x): return x**2 + 3*x + 2

integrando = f3
```

---


