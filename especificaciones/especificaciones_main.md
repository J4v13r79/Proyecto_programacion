1. Objetivo

Controlar el funcionamiento de la aplicación mediante un menú de opciones y permitir al usuario realizar diferentes cálculos de volúmenes de sólidos de revolución.

2. Menú principal

El programa mostrará las siguientes opciones:

Calcular nuevo sólido de revolución.

Consultar historial de cálculos.

Mostrar información de un ejercicio.

Salir del programa.

3. Objetos a crear

Un objeto de tipo SolidoRevolucion para almacenar los datos del ejercicio.

Un objeto de tipo CalculadoraVolumen para realizar las operaciones.

4. Secuencia de operaciones

Mostrar el menú principal.

Solicitar una opción al usuario.

Si selecciona calcular, solicitar las dos funciones y los límites de integración.

Crear un objeto SolidoRevolucion.

Validar los datos introducidos.

Crear un objeto CalculadoraVolumen.

Calcular la integral y el volumen exacto.

Mostrar el procedimiento y el resultado.

Guardar el ejercicio en una lista de historial.

Permitir consultar los cálculos anteriores.

5. Condiciones de salida

El programa continuará mostrando el menú mediante un ciclo while hasta que el usuario seleccione la opción de salir.

6. Validaciones

No aceptar funciones matemáticas inválidas.

No aceptar límites donde el inferior sea mayor o igual al superior.

Validar que los radios sean adecuados para el método de arandelas.

No permitir opciones inexistentes en el menú.