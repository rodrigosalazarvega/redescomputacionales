# redescomputacionales
Trabajo Integrador sobre Algoritmo Bellman-Ford
Alumno: Rodrigo Salazar Vega 
Código: 20171406

INSTRUCCIONES

ANTES de ejecutar:

- Colocar en la terminal que se usará para ejecutar el codigo lo siguiente:

	pip install texttable
	pip install qprompt
	pip install tabulate

DURANTE la ejecución:

- Al ejecutar el programa aparecerá un menú con distintas opciones ( Agregar Nodo, Agregar Arista, Bellman Ford, Mostrar, Salir)
- Para llamar a cada una de estas funciones se tendra que escribir en el terminal el número que aparece entre paréntesis. Por ejemplo: [?] Enter menu selection: 4. Esto me mostrará los nodos y aristas que haya insertado hasta el momento. 

Observaciones:

- En caso se coloque dos veces el mismo nodo, el programa no lo añadirá y lo tomará como ya existente
- En caso se coloque una arista para los mismos nodos, el programa avisará al usuario que ya hay una arista existente
- En caso se coloque un peso negativo, al ejecutar la opción 3 (Bellman-Ford), el programa nos avisará que no hay solución y existen pesos negativos

FINALIZAR la ejecución:

-Para terminar la ejecución del programa basta con colocar el valor de 5. Enter menu selection: 5
- Al finalizar la ejecución aparecera el tiempo total de ejecución. 
