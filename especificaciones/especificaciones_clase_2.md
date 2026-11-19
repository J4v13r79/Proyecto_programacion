1. Identificación de la clase

Nombre: CalculadoraVolumen

Objetivo: Realizar el cálculo exacto del volumen de un sólido de revolución mediante el método de arandelas.

Responsabilidad: Procesar las funciones y los límites proporcionados por un objeto SolidoRevolucion y obtener el volumen.

2. Atributos

Atributo

Tipo

Significado

solido

SolidoRevolucion

Objeto con los datos del ejercicio

variable

símbolo matemático

Variable utilizada para integrar

resultado_integral

expresión simbólica

Resultado de la integral

volumen

expresión simbólica

Volumen exacto calculado

3. Constructor init

Recibirá un objeto de tipo SolidoRevolucion.

Inicializará los atributos necesarios para realizar los cálculos.

4. Métodos

calcularIntegral()

Objetivo: Construir y resolver la integral definida.

Entradas: Funciones y límites almacenados en el objeto SolidoRevolucion.

Proceso:

Elevar al cuadrado el radio exterior.

Elevar al cuadrado el radio interior.

Restar ambas expresiones.

Integrar entre los límites establecidos.

Resultado: Integral definida resuelta exactamente.

calcularVolumen()

Objetivo: Obtener el volumen del sólido.

Entradas: Resultado de la integral.

Proceso: Multiplicar el resultado de la integral por pi.

Resultado: Volumen exacto del sólido.

mostrarResultado()

Objetivo: Mostrar los resultados del cálculo.

Resultado: Presentar la integral, el volumen exacto y su aproximación decimal.

5. Reglas que no puede modificar Copilot

La fórmula será V = π ∫[a,b] (R(x)² - r(x)²) dx.

Se utilizará integración simbólica exacta.

Se utilizará la biblioteca SymPy.

No se sustituirá la integración exacta por aproximaciones numéricas.

El resultado deberá expresarse de forma exacta y decimal.