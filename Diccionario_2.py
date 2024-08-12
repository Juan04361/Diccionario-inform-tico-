"""
Diccionario Informático

Este diccionario de términos informáticos con definiciones. Permite al usuario buscar definiciones de palabras, agregar nuevas palabras al diccionario, y obtener información sobre el creador del diccionario.
"""

# Definir el diccionario con las palabras y sus definiciones
diccionario_informatico = {
    "ALGORITMO": "Un algoritmo es una secuencia de pasos a seguir para realizar una tarea específica.",
    "CÓDIGO": "Es una secuencia de instrucciones escritas en un lenguaje de programación que una computadora pueda ejecutar para poder realizar tareas específicas.",
    "COMPILADOR": "Es una herramienta que traduce el código fuente escrito en un lenguaje de alto nivel (como C++ o Java) a un lenguaje de bajo nivel o código máquina que puede ser entendido y ejecutado por la computadora.",
    "DEPURACIÓN": "Es el proceso de identificar, aislar y corregir errores o defectos en el código fuente para poder asegurar que el programa funcione correctamente.",
    "VARIABLE": "Es un contenedor que almacena un valor en la memoria y cuyo contenido puede cambiar durante la ejecución del programa. Incluyen variables enteras, flotantes o de texto.",
    "FUNCIÓN": "Bloque de código diseñado para realizar una tarea específica. Puede recibir entradas, procesarlas y devolver un resultado. Las funciones promueven la reutilización y la modularidad del código.",
    "CLASE": "En programación orientada a objetos, una clase es una plantilla que define un tipo de objeto, incluyendo sus atributos (datos) y métodos (funciones).",
    "OBJETO": "Instancia de una clase que contiene atributos y métodos definidos por la clase. Los objetos representan entidades en el programa y pueden interactuar entre sí.",
    "MÉTODO": "Una función que está asociada a una clase en la programación orientada a objetos. Los métodos definen las acciones que los objetos de esa clase pueden realizar.",
    "SINTAXIS": "Conjunto de reglas que define cómo se deben escribir las instrucciones en un lenguaje de programación. La sintaxis incorrecta puede causar errores de compilación o ejecución.",
    "ESTRUCTURA DE CONTROL": "Mecanismos como if, for, while, y switch que determinan el flujo de ejecución del programa, permitiendo decisiones y repeticiones basadas en condiciones.",
    "ARRAY": "Estructura de datos que almacena una colección de elementos del mismo tipo en posiciones consecutivas de memoria, accesibles mediante un índice.",
    "LIBRERÍA": "Conjunto de funciones y procedimientos predefinidos que pueden ser utilizados por programas para realizar tareas comunes sin tener que escribir el código desde cero.",
    "FRAMEWORK": "Conjunto de herramientas y bibliotecas diseñadas para facilitar el desarrollo de aplicaciones, proporcionando una estructura y funcionalidad básica sobre la cual construir.",
    "API": "Conjunto de reglas y herramientas que permite la comunicación entre diferentes software o sistemas. Facilita la integración y el uso de funcionalidades externas.",
    "HERENCIA": "Mecanismo en la programación orientada a objetos que permite a una clase derivada heredar atributos y métodos de una clase base, facilitando la reutilización y extensión del código.",
    "POLIMORFISMO": "Capacidad de diferentes clases para proporcionar una interfaz común para un conjunto de métodos o funciones, permitiendo que se comporten de manera diferente según el tipo de objeto que los invoque.",
    "ENCAPSULAMIENTO": "Concepto de la programación orientada a objetos que oculta los detalles internos de un objeto y expone solo las operaciones permitidas, protegiendo los datos y reduciendo la complejidad.",
    "INTÉRPRETE": "Programa que ejecuta el código fuente línea por línea en tiempo de ejecución, en lugar de compilarlo previamente. Ideal para lenguajes de scripting como Python y JavaScript.",
    "SQL": "Lenguaje estándar para gestionar y manipular bases de datos relacionales, permitiendo operaciones como consultas, inserciones, actualizaciones y eliminaciones de datos.",
    "REPOSITORIO": "Almacenamiento centralizado en el que se guarda el código fuente y otros recursos relacionados con un proyecto de software. Facilita la colaboración y el control de versiones.",
    "VERSIONADO": "Sistema para gestionar y rastrear los cambios en el código fuente a lo largo del tiempo, permitiendo volver a versiones anteriores y colaborar eficientemente en equipos.",
    "GIT": "Sistema de control de versiones distribuido que permite a los desarrolladores colaborar en el desarrollo de software, realizar un seguimiento de los cambios y gestionar múltiples ramas de desarrollo.",
    "MERGE": "Proceso de combinar los cambios realizados en diferentes ramas de un repositorio de código, resolviendo conflictos y creando una versión unificada del código.",
    "BRANCH(RAMA)": "Una línea de desarrollo independiente en un sistema de control de versiones que permite trabajar en características o correcciones separadas sin afectar la rama principal.",
    "DEBUGGING": "Proceso de identificar, aislar y corregir errores en el código fuente. Puede implicar el uso de herramientas de depuración para examinar variables y el flujo de ejecución",
    "IDE": "Aplicación que proporciona herramientas y características como editor de código, depurador y compilador en un solo entorno para facilitar el desarrollo de software.",
    "SCRIPT": "Archivo que contiene un conjunto de instrucciones en un lenguaje de scripting. Los scripts se utilizan para automatizar tareas repetitivas o para ejecutar secuencias de comandos.",
    "KERNEL": "Núcleo del sistema operativo que gestiona los recursos del hardware y proporciona servicios esenciales a otras partes del sistema operativo y aplicaciones.",
    "RECURSIÓN": "Técnica de programación en la que una función se llama a sí misma para resolver un problema, dividiéndolo en subproblemas más pequeños hasta alcanzar un caso base.",
    "ABSTRACCIÓN": "Técnica para simplificar la complejidad mediante la ocultación de detalles innecesarios y la exposición solo de las características relevantes de un objeto o sistema.",
    "CONSTRUCTOR": "Método especial en una clase que se llama automáticamente cuando se crea una instancia de esa clase, inicializando los atributos del objeto.",
    "DESTRUCTOR": "Método especial en una clase que se llama automáticamente cuando un objeto es destruido, utilizado para liberar recursos o realizar tareas de limpieza.",
    "EVENTO": "Acción o suceso que ocurre durante la ejecución de un programa y que puede ser capturado y gestionado mediante un controlador de eventos. Ejemplos incluyen clics de botones o entradas de teclado.",
    "LISTENER": "Objeto o función que espera y responde a eventos específicos, como la pulsación de una tecla o la selección de un elemento en una interfaz de usuario.",
    "MIDDLEWARE": "Software que actúa como intermediario entre diferentes aplicaciones o servicios, facilitando la comunicación y gestión de datos entre ellos.",
    "JIT": "Técnica de compilación que convierte el código fuente en código máquina en tiempo de ejecución, mejorando la velocidad de ejecución al optimizar el código sobre la marcha.",
    "TDD": "Método de desarrollo de software en el que se escriben pruebas automatizadas antes de escribir el código que cumple con esas pruebas, mejorando la calidad del código.",
    "UNIT TEST": "Prueba automatizada que verifica la funcionalidad de la unidad más pequeña de código, como una función o un método, para asegurar que se comporta correctamente en diferentes escenarios.",
    "INTEGRATION TEST": "Prueba que verifica la interacción entre diferentes módulos o componentes de un sistema para asegurar que trabajan juntos correctamente.",
    "MOCK": "Objeto simulado utilizado en pruebas unitarias para imitar el comportamiento de objetos reales, permitiendo probar componentes de forma aislada sin depender de otras partes del sistema.",
    "EXCEPTION": "Mecanismo para manejar errores y condiciones inesperadas durante la ejecución del programa, permitiendo que el código maneje errores de manera controlada.",
    "TRY-CATCH": "Estructura de control que permite capturar y manejar excepciones, evitando que el programa se detenga abruptamente y proporcionando una forma de gestionar errores.",
    "CONCURRENCY": "Capacidad del sistema para realizar múltiples tareas al mismo tiempo, mejorando el rendimiento y la eficiencia en aplicaciones que requieren operaciones simultáneas.",
    "THREAD": "Unidad de ejecución dentro de un proceso que permite realizar múltiples operaciones concurrentemente, compartiendo recursos y memoria con otros hilos.",
    "ASYNCHRONOUS": "Técnica que permite realizar operaciones sin bloquear el flujo de ejecución del programa, facilitando la ejecución de tareas paralelas y mejorando la capacidad de respuesta.",
    "CALLBACK": "Función que se pasa como argumento a otra función y que se ejecuta una vez que se completa una operación, permitiendo la ejecución de código en respuesta a eventos.",
    "LAMBDA": "Función anónima definida en el lugar donde se utiliza, útil para operaciones simples y expresiones funcionales en lenguajes que soportan programación funcional.",
    "PROMISE": "Objeto que representa el resultado eventual de una operación asíncrona y permite manejar el resultado o error de manera estructurada mediante métodos then y catch.",
    "CRUD": "Operaciones básicas realizadas en bases de datos para Crear, Leer, Actualizar y Borrar registros.",
    "SCHEMA": "Estructura que define la organización de una base de datos, incluyendo tablas, relaciones y restricciones, determinando cómo se almacenan y acceden los datos.",
    "NORMALIZATION": "Proceso de estructuración de una base de datos para reducir redundancias y dependencias, dividiendo la información en tablas relacionadas.",
    "DENORMALIZATION": "Proceso de introducir redundancia en una base de datos para mejorar el rendimiento de consultas, agregando datos duplicados para reducir la complejidad de las uniones.",
    "DATA MINING": "Proceso de descubrir patrones, tendencias y relaciones en grandes conjuntos de datos utilizando técnicas estadísticas y algoritmos.",
    "BIG DATA": "Conjuntos de datos extremadamente grandes y complejos que requieren técnicas avanzadas y herramientas para su análisis y gestión.",
    "CLOUD COMPUTING": "Modelo de entrega de servicios informáticos a través de Internet, incluyendo almacenamiento, procesamiento y aplicaciones, permitiendo la escalabilidad y flexibilidad.",
    "INTERFACE": "Contrato que define un conjunto de métodos que una clase debe implementar, permitiendo la interoperabilidad entre diferentes clases y componentes.",
    "ENCRYPTION": "Proceso de codificar información para protegerla de accesos no autorizados, utilizando algoritmos de cifrado que aseguran que solo las partes autorizadas puedan leer los datos.",
    "FRAMEWORK": "Conjunto de herramientas y librerías que proporcionan una estructura básica para desarrollar aplicaciones, facilitando tareas comunes y promoviendo buenas prácticas. Ejemplos incluyen Django para Python y Angular para JavaScript.",
    "REFACTORING": "Proceso de mejorar el diseño del código sin cambiar su comportamiento externo. Facilita la mantenibilidad y legibilidad del código al mejorar su estructura interna.",
    "CODE SMELL": "Indicios de posibles problemas en el código que pueden sugerir la necesidad de refactorización. Ejemplos: métodos demasiado largos o clases con demasiadas responsabilidades.",
    "COMMIT": "Acción de guardar cambios en el sistema de control de versiones, registrando un conjunto de modificaciones en el repositorio junto con un mensaje descriptivo.",
    "XML": "Lenguaje de marcado utilizado para definir y estructurar datos en un formato legible por humanos y máquinas, común en la configuración y transmisión de datos.",
    "OAUTH": "Protocolo de autorización que permite a las aplicaciones obtener acceso a recursos de un usuario en otro servicio sin compartir credenciales, utilizando tokens de acceso.",
    "RACE CONDITION": "Situación en la que el resultado de un programa depende del orden no controlado en que se ejecutan las operaciones concurrentes, lo que puede llevar a errores y comportamientos inesperados.",
    "DATA STRUCTURE": "Forma de organizar y almacenar datos de manera eficiente para facilitar el acceso y la manipulación. Ejemplos incluyen listas, pilas, colas, árboles y grafos.",
    "BINARY TREE": "Estructura de datos en la que cada nodo tiene a lo sumo dos hijos, utilizados en algoritmos y estructuras de datos como árboles de búsqueda binaria y árboles de expresión.",
    "GRAPH": "Estructura de datos compuesta por nodos (vértices) y aristas (arcos) que representan relaciones entre los nodos, utilizada en algoritmos para redes, rutas y más.",
    "GREEDY ALGORITHM": "Algoritmo que toma decisiones locales óptimas en cada paso con la esperanza de encontrar una solución global óptima, utilizado en problemas como el de la mochila y el de la cobertura mínima.",
    "BACKTRACKING": "Técnica de resolución de problemas que intenta construir soluciones incrementales y retrocede cuando se encuentra un estado que no puede llevar a una solución válida.",
    "IF": "Es una estructura de control de flujo que permite ejecutar un bloque de código solo si se cumple una condición específica.",
    "ELIF": "Es una palabra clave en Python que se utiliza dentro de una estructura de control if-elif-else para manejar múltiples condiciones. Es una abreviatura de else if y permite verificar varias condiciones secuenciales de manera eficiente.",
    "BREAK": "Es una instrucción que se utiliza para salir prematuramente de un bucle (for o while) o una estructura de control como un switch en algunos lenguajes. Cuando se ejecuta un break, el flujo de control abandona el bucle o la estructura en la que se encuentra y continúa con la ejecución del código que sigue fuera de esa estructura.",
    "WHILE TRUE": "Es una forma de crear un bucle infinito en el cual el bloque de código dentro del bucle se ejecuta repetidamente sin fin, ya que la condición True siempre es verdadera. Este tipo de bucle se utiliza cuando el número de iteraciones no es conocido de antemano y se espera que el bucle continúe hasta que se cumpla una condición de salida específica dentro del bucle."
}

def mostrar_definicion():
    """
    Solicita al usuario ingresar una palabra y muestra la definición correspondiente si la palabra está en el diccionario.
    """
    palabra = input("Ingrese una palabra para ver su definición: ").strip().upper()
    if palabra in diccionario_informatico:
        print(f"\n{palabra}: {diccionario_informatico[palabra]}")
    else:
        print("La palabra no se encuentra en el diccionario.")

def agregar_palabra():
    """
    Permite al usuario agregar una nueva palabra y su definición al diccionario.
    """
    palabra = input("Ingrese la nueva palabra: ").strip().upper()
    definicion = input("Ingrese la definición de la palabra: ").strip()
    diccionario_informatico[palabra] = definicion
    print(f"\nLa palabra '{palabra}' ha sido añadida al diccionario.")

def mostrar_acerca_de_mi():
    """
    Muestra información sobre el creador del diccionario.
    """
    print("\n" + "*" * 160)
    print("Me llamo Edwin Juan Pablo Sebastian Cuc. Soy estudiante de 4to de Computación en el Colegio Howard W. Hunter.")
    print("Este diccionario fue creado con la intención de ayudar a los nuevos estudiantes de computación a entender los conceptos y términos usados en programación.")
    print("*" * 160 + "\n")

# Menú de opciones
while True:
    print("\n" + "$" * 38)
    print("Bienvenido al Diccionario Informático")
    print("$" * 38)
    print("1. Ver definición de una palabra")
    print("2. Agregar una nueva palabra")
    print("3. Acerca de mí")
    print("4. Salir")
    print("$" * 38)
    eleccion = input("Seleccione una opción:").strip()
    print("$" * 38)

    if eleccion == "1":
        mostrar_definicion()
    elif eleccion == "2":
        agregar_palabra()
    elif eleccion == "3":
        mostrar_acerca_de_mi()
    elif eleccion == "4":
        print("\nSaliendo del programa. Hasta luego")
        break
    else:
        print("Opción no válida. Por favor, seleccione 1, 2, 3 o 4.")


