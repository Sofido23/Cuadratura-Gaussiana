# Explicación Conceptual del Proyecto

Este proyecto tiene como objetivo calcular de manera precisa la integral definida de funciones mediante el método de **Cuadratura Gaussiana**, una técnica eficiente de integración numérica.

## ¿Qué es la Cuadratura Gaussiana?

La cuadratura gaussiana es un método de integración que evalúa una función en ciertos puntos óptimos dentro del intervalo de integración y pondera estas evaluaciones con coeficientes específicos. A diferencia de métodos como el trapecio o Simpson, **no requiere una división uniforme del intervalo**, lo que permite **una mayor precisión con menos puntos**.

La fórmula general de cuadratura de Gauss-Legendre es:

\[
\int_{-1}^{1} f(x)\, dx \approx \sum_{i=1}^{N} w_i\, f(x_i)
\]

Donde:

- \( x_i \): Puntos de muestreo (raíces del polinomio de Legendre de grado \(N\))
- \( w_i \): Pesos correspondientes a cada punto

## ¿Cómo se aplica al intervalo [a, b]?

Como esta fórmula aplica solo al intervalo \([-1, 1]\), es necesario escalar los puntos y pesos para integrales en cualquier otro intervalo \([a, b]\):

\[
x' = \frac{1}{2}(b - a)x + \frac{1}{2}(b + a), \quad w' = \frac{1}{2}(b - a)w
\]

Este cambio de variable garantiza que la integral en \([a, b]\) se pueda resolver con los mismos principios.

## ¿Qué calcula este proyecto?

La integral:

\[
\int_0^\pi \sin(x^2)\, dx
\]

Esta integral no tiene una solución analítica, por lo que es ideal para métodos numéricos.

## ¿Cómo funciona el proyecto?

1. Se define la función que se desea integrar.
2. Se calcula una serie de puntos y pesos de cuadratura para distintos valores de \(N\) (número de puntos de muestreo).
3. Se transforman esos puntos y pesos al intervalo \([0, \pi]\).
4. Se evalúa la suma ponderada de la función en esos puntos.
5. Se grafica cómo evoluciona el valor de la integral conforme aumenta \(N\).

Esto permite ver la convergencia numérica del método y elegir un \(N\) adecuado para una precisión deseada.

## ¿Por qué es útil?

- Es extremadamente preciso para funciones suaves.
- Permite estudiar integrales que no pueden resolverse analíticamente.
- Es más eficiente que métodos clásicos cuando se desea alta precisión.

---
