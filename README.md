Calculadora de Volúmenes de Sólidos de Revolución

1. Descripción del proyecto

Este proyecto consiste en desarrollar una aplicación en Python capaz de calcular el volumen de sólidos de revolución mediante el método de arandelas y utilizando integración exacta.

El programa permite ingresar las funciones del radio exterior e interior, establecer los límites de integración, validar los datos ingresados y calcular el volumen del sólido utilizando la biblioteca SymPy.

Además, cuenta con un menú que permite realizar nuevos cálculos y consultar un historial de ejercicios durante la ejecución del programa.

2. Objetivo

Desarrollar una aplicación utilizando programación orientada a objetos que permita resolver problemas de volúmenes de sólidos de revolución, aplicando conceptos de integración definida y utilizando herramientas de Python para la manipulación simbólica de expresiones matemáticas.

3. Funcionalidades

Ingresar las funciones del radio exterior e interior.

Establecer los límites de integración.

Validar los datos ingresados.

Calcular la integral definida de manera exacta.

Obtener el volumen del sólido de revolución.

Mostrar el resultado exacto y aproximado.

Registrar diferentes ejercicios durante la ejecución.

Consultar el historial de cálculos.

Mostrar mensajes de error cuando los datos no sean válidos.

4. Método matemático utilizado

La aplicación utiliza el método de arandelas para calcular el volumen de sólidos de revolución.

La fórmula utilizada es:

V = π ∫[a,b] (R(x)² - r(x)²) dx

Donde:

V: volumen del sólido.

R(x): función del radio exterior.

r(x): función del radio interior.

a: límite inferior de integración.

b: límite superior de integración.

π: constante pi.

La integración se realiza utilizando SymPy, lo que permite obtener resultados exactos cuando la integral puede resolverse simbólicamente.

5. Tecnologías utilizadas

Python: lenguaje de programación utilizado para desarrollar la aplicación.

SymPy: biblioteca para realizar operaciones matemáticas simbólicas e integración exacta.

Git: sistema de control de versiones.

GitHub: plataforma para almacenar y gestionar el proyecto.

Visual Studio Code: editor utilizado durante el desarrollo.

GitHub Copilot: herramienta de asistencia utilizada durante la implementación y revisión del código