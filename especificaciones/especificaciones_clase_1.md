1. Identificación de la clase

Nombre: SolidoRevolucion

Objetivo: Almacenar los datos necesarios para calcular el volumen de un sólido de revolución mediante el método de arandelas alrededor del eje X.

Responsabilidad: Guardar las dos funciones matemáticas y los límites de integración de cada ejercicio.

2. Atributos

Atributo

Tipo

Significado

nombre

str

Nombre del ejercicio

radio_exterior

expresión simbólica

Función del radio exterior

radio_interior

expresión simbólica

Función del radio interior

limite_inferior

número

Inicio de la integración

limite_superior

número

Final de la integración

3. Constructor init

Recibirá el nombre del ejercicio, las dos funciones y los límites de integración.

Inicializará todos los atributos utilizando self.

4. Métodos

mostrarDatos()

Objetivo: Mostrar la información almacenada del sólido.

Entradas: Ninguna.

Proceso: Consultar los atributos del objeto e imprimir sus valores.

Resultado: Mostrar el nombre, las funciones y los límites de integración.

validarDatos()

Objetivo: Comprobar que los datos introducidos sean válidos.

Validaciones:

El límite inferior debe ser menor que el superior.

Las funciones deben ser expresiones matemáticas válidas.

Los radios deben representar valores no negativos en el intervalo de integración.

El radio exterior debe ser mayor o igual al interior en el intervalo considerado.

5. Reglas que no puede modificar Copilot

El sólido siempre girará alrededor del eje X.

Se utilizará el método de arandelas.

Se trabajará con dos funciones.

El radio exterior será R(x).

El radio interior será r(x).

Los límites de integración deberán ser válidos.

La aplicación utilizará integración simbólica exacta.