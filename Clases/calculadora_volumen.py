from sympy import symbols, integrate, pi, N, simplify


class CalculadoraVolumen:

    def __init__(self, solido):

        self.solido = solido
        self.variable = solido.x
        self.resultado_integral = None
        self.volumen = None

    def calcularIntegral(self):

        self.solido.validarDatos()

        x = self.variable

        radio_exterior = self.solido.radio_exterior
        radio_interior = self.solido.radio_interior

        # Elevar los radios al cuadrado
        exterior_cuadrado = radio_exterior**2
        interior_cuadrado = radio_interior**2

        # Construir la expresión de la integral
        expresion = exterior_cuadrado - interior_cuadrado

        # Resolver la integral definida exactamente
        self.resultado_integral = integrate(
            expresion,
            (x, self.solido.limite_inferior,
             self.solido.limite_superior)
        )

        return simplify(self.resultado_integral)

    def calcularVolumen(self):

        if self.resultado_integral is None:
            self.calcularIntegral()

        # Multiplicar el resultado por pi
        self.volumen = simplify(pi * self.resultado_integral)

        return self.volumen

    def mostrarResultado(self):

        if self.volumen is None:
            self.calcularVolumen()

        print("\n----- RESULTADO DEL SOLIDO -----")

        print(f"Ejercicio: {self.solido.nombre_ejercicio}")

        print(f"Radio exterior: {self.solido.radio_exterior}")

        print(f"Radio interior: {self.solido.radio_interior}")

        print(
            f"Integral resuelta: {self.resultado_integral}"
        )

        print(f"Volumen exacto: {self.volumen}")

        print(f"Volumen aproximado: {N(self.volumen, 8)}")

        print("--------------------------------")
