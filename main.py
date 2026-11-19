from Clases.Solido_de_revolucion import SolidoRevolucion
from Clases.calculadora_volumen import CalculadoraVolumen


historial = []


def calcularNuevoSolido():

    print("\n--- NUEVO SOLIDO DE REVOLUCION ---")

    nombre = input("Nombre del ejercicio: ")

    radio_exterior = input("Funcion del radio exterior: ")

    radio_interior = input("Funcion del radio interior: ")

    try:
        limite_inferior = float(input("Limite inferior: "))
        limite_superior = float(input("Limite superior: "))

        solido = SolidoRevolucion(
            nombre,
            radio_exterior,
            radio_interior,
            limite_inferior,
            limite_superior
        )

        solido.validarDatos()

        calculadora = CalculadoraVolumen(solido)

        calculadora.calcularIntegral()
        calculadora.calcularVolumen()
        calculadora.mostrarResultado()

        historial.append(calculadora)

        print("\nEjercicio guardado correctamente.")

    except Exception as error:

        print(f"\nNo se pudo realizar el calculo: {error}")


def consultarHistorial():

    print("\n--- HISTORIAL DE CALCULOS ---")

    if len(historial) == 0:

        print("No hay ejercicios registrados.")

    else:

        for i, calculadora in enumerate(historial):

            print(f"\nEjercicio {i + 1}")

            print(f"Nombre: {calculadora.solido.nombre_ejercicio}")

            print(f"Volumen: {calculadora.volumen}")


def mostrarMenu():

    while True:

        print("\n================================")
        print(" CALCULADORA DE SOLIDOS")
        print("       DE REVOLUCION")
        print("================================")

        print("1. Calcular nuevo solido")
        print("2. Consultar historial")
        print("3. Salir")

        opcion = input("\nSelecciona una opcion: ")

        if opcion == "1":

            calcularNuevoSolido()

        elif opcion == "2":

            consultarHistorial()

        elif opcion == "3":

            print("\nGracias por utilizar el programa.")
            break

        else:

            print("\nOpcion no valida. Intenta nuevamente.")


if __name__ == "__main__":

    mostrarMenu()