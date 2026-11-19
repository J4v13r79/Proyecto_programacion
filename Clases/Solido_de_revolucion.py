from sympy import (
    symbols, sympify, Interval, S,
    solve_univariate_inequality
)


class SolidoRevolucion:

    def __init__(self, nombre_ejercicio, radio_exterior,
                 radio_interior, limite_inferior, limite_superior):

        self.x = symbols('x')

        self.nombre_ejercicio = nombre_ejercicio
        self.radio_exterior = sympify(radio_exterior, locals={'x': self.x})
        self.radio_interior = sympify(radio_interior, locals={'x': self.x})

        self.limite_inferior = sympify(limite_inferior)
        self.limite_superior = sympify(limite_superior)

    def mostrarDatos(self):

        print(f"\nNombre del ejercicio: {self.nombre_ejercicio}")
        print(f"Radio exterior: {self.radio_exterior}")
        print(f"Radio interior: {self.radio_interior}")
        print(f"Límite inferior: {self.limite_inferior}")
        print(f"Límite superior: {self.limite_superior}")

    def validarDatos(self):

        if not self.limite_inferior.is_number or not self.limite_superior.is_number:
            raise ValueError("Los límites deben ser números.")

        if self.limite_inferior.is_real is not True or self.limite_superior.is_real is not True:
            raise ValueError("Los límites deben ser números reales.")

        if self.limite_inferior >= self.limite_superior:
            raise ValueError("El límite inferior debe ser menor que el superior.")

        intervalo = Interval(self.limite_inferior, self.limite_superior)

        # Comprobar que ambos radios sean no negativos
        try:
            for radio in [self.radio_exterior, self.radio_interior]:

                valores_negativos = solve_univariate_inequality(
                    radio < 0,
                    self.x,
                    relational=False,
                    domain=intervalo
                )

                if valores_negativos != S.EmptySet:
                    raise ValueError("Los radios no pueden ser negativos.")

            # Comprobar que el radio exterior sea mayor o igual
            diferencia = self.radio_exterior - self.radio_interior

            valores_invalidos = solve_univariate_inequality(
                diferencia < 0,
                self.x,
                relational=False,
                domain=intervalo
            )

            if valores_invalidos != S.EmptySet:
                raise ValueError("El radio exterior no puede ser menor que el interior.")

        except NotImplementedError:
            raise ValueError(
                "SymPy no pudo comprobar las funciones en todo el intervalo."
            )

        return True
