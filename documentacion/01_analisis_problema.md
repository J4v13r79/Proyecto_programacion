Análisis del problema

1.1 Nombre del problema

Cálculo de volúmenes de sólidos de revolución mediante el método de arandelas.

1.2 Asignatura

Cálculo Integral.

1.3 Descripción del problema

El problema consiste en calcular el volumen de un sólido generado al girar una región limitada por dos funciones matemáticas alrededor del eje X. Para resolverlo se utiliza el método de arandelas, que permite obtener el volumen mediante la diferencia entre el radio exterior y el radio interior.

1.4 Justificación

Se desarrollará una aplicación en Python que permita realizar estos cálculos de manera automática, mostrando el procedimiento matemático y el resultado exacto. También permitirá guardar diferentes ejercicios y consultar los resultados anteriores.

1.5 Entradas

Primera función matemática.

Segunda función matemática.

Límite inferior de integración.

Límite superior de integración.

1.6 Procesos

Se utilizará el método de arandelas con la siguiente fórmula:

V = π ∫[a,b] (R(x)² - r(x)²) dx

Donde R(x) representa el radio exterior y r(x) el radio interior.

El programa identificará los radios, elevará ambas funciones al cuadrado, calculará su diferencia y resolverá la integral definida mediante integración simbólica exacta.

1.7 Salidas esperadas

Funciones ingresadas.

Límites de integración.

Integral planteada.

Resultado de la integral.

Volumen exacto.

Aproximación decimal del volumen.

1.8 Alcance

La aplicación permitirá ingresar dos funciones, establecer los límites de integración, calcular el volumen de revolución alrededor del eje X, guardar varios resultados y consultar un historial de operaciones.

1.9 Herramientas

Python.

Visual Studio Code.

Git y GitHub.

GitHub Copilot.

Biblioteca SymPy.

1.10 Ejemplo original resuelto

Se utilizará un ejercicio previamente realizado en
Cálculo Integral para comprobar los resultados de la aplicación.

Primera función:

x² + y² = 25

f(x) = √(25 - x²)

Segunda función:

x - 7y + 25 = 0

g(x) = (x + 25) / 7

Límites de integración:

a = -4
b = 3

Método: Arandelas alrededor del eje X.

Radio exterior:

R(x) = √(25 - x²)

Radio interior:

r(x) = (x + 25) / 7

Fórmula:

V = π ∫[-4,3] (R(x)² - r(x)²) dx

Resultado exacto:

V = 175π / 3

Resultado aproximado:

V = 183.259571 unidades cúbicas.

Este resultado se utilizará como referencia
para comprobar el funcionamiento del programa.