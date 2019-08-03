# hybridPasswordCracker
Version MAR/2019. CEH Final Project. June of 2019. 

Repositorio de la herramienta hybridPasswordCracker. 

DESCARGO DE RESPONSABILIDAD

    El código de los ficheros alojados, ha sido redactado por el propietario del repositorio.
    Los documentos que se encuentran en el repositorio, se pueden descargar y usar libremente.
    El autor no se hace repsonsable del mal uso que puedan darse a los conocimientos que en este repositorio se comparten.
    La herramienta ha sido diseñada y programada para generar diccionarios y usarlos en ataques hybridos de contraseña.
    
INFORMACIÓN


    En próximas versiones se añadiran funcionalidades en las cuales se pueda usar el diccionario con el añadido de las herramientas que vienen instaladas por defecto en KaliLinux, permitiendo ahorrar tiempo a la hora de lanzar la prueba de concepto.
    Se admiten todo tipo de recomendaciones y aportes para mejorar la herramienta.
    
FORMA DE USO
    
    1. Clonar el repositorio: git clone https://github.com/baah-romero/hybridPasswordCracker.git
    2. Acceder al repositorio: cd hybridPasswordCracker
    3. Ejecutar la herramienta: python3 hybridPasswordCracker.py
    4. Introduce el nombre que tendrá el diccionario, se generará en formato TXT
    5. Añade palabras a la lista del diccionario, usa la cadena :wq para cortar la lista y empezar a generar el diccionario hybrido.
    6. Al finalizar, mostrará un resumen por cada palabra, así, como del diccionario al completo.
    7. Usar el diccionario en la PoF que se desee.
