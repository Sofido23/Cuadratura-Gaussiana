# Explicación del Proyecto

Este proyecto tiene como objetivo calcular con precisión la integral definida de funciones utilizando el método de **Cuadratura Gaussiana**, una herramienta potente y eficiente de integración numérica.

## ¿En qué consiste la Cuadratura Gaussiana?

La cuadratura gaussiana es un enfoque numérico para la integración que evalúa la función en puntos específicos dentro del intervalo de integración. Estos puntos son cuidadosamente seleccionados y cada evaluación se pondera con un coeficiente (peso). A diferencia de otros métodos tradicionales como el trapecio o Simpson, **no necesita dividir el intervalo de manera uniforme**, lo que permite obtener resultados más precisos con menos puntos.

La fórmula general de la cuadratura Gauss-Legendre es la siguiente:

\[
\int_{-1}^{1} f(x)\, dx \approx \sum_{i=1}^{N} w_i\, f(x_i)
\]

Donde:

- \( x_i \): Son los puntos donde se evalúa la función (raíces del polinomio de Legendre),
- \( w_i \): Son los pesos correspondientes a cada uno de esos puntos.

## ¿Cómo se aplica al intervalo [a, b]?

El método de Gauss-Legendre está diseñado para funcionar en el intervalo \([-1, 1]\), por lo que, para aplicarlo en otros intervalos como \([a, b]\), es necesario transformar los puntos y los pesos de la siguiente manera:

\[
x' = \frac{1}{2}(b - a)x + \frac{1}{2}(b + a), \quad w' = \frac{1}{2}(b - a)w
\]

Esto asegura que el cálculo de la integral en cualquier intervalo de la forma \([a, b]\) sea posible, manteniendo la precisión del método.

## ¿Qué vamos a calcular?

El proyecto tiene como objetivo calcular la siguiente integral:

\[
\int_0^\pi \sin(x^2)\, dx
\]

Dado que esta integral no tiene una solución analítica exacta, es ideal para aplicar métodos numéricos.

## ¿Cómo funciona el proyecto?

1. Se define la función que se desea integrar, en este caso \( \sin(x^2) \).
2. Se calculan los puntos y pesos de cuadratura para diferentes valores de \(N\), el número de puntos de muestreo.
3. Los puntos y pesos se transforman al intervalo \([0, \pi]\).
4. Se evalúa la integral usando la suma ponderada de la función en esos puntos, lo que permite observar la convergencia numérica del método y elegir el valor adecuado de \(N\) para obtener la precisión deseada.

## ¿Por qué es útil?

- Ofrece resultados muy precisos para funciones suaves y bien comportadas.
- Es útil para resolver integrales que no pueden ser resueltas de manera analítica.
- Es más eficiente que los métodos clásicos cuando se busca alta precisión con menos puntos.
-
