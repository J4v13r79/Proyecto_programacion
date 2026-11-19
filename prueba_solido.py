from Clases.Solido_de_revolucion import SolidoRevolucion
from Clases.calculadora_volumen import CalculadoraVolumen

solido = SolidoRevolucion(
    "Ejercicio original",
    "sqrt(25-x**2)",
    "(x+25)/7",
    -4,
    3
)

try:

    solido.validarDatos()

    calculadora = CalculadoraVolumen(solido)

    calculadora.calcularIntegral()

    calculadora.calcularVolumen()

    calculadora.mostrarResultado()

except ValueError as error:

    print("Error:", error)
