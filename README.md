# hybridPasswordCracker
<h3>Repositorio de la herramienta hybridPasswordCracker. </h3>
<h2>VERSIONES/H2><br>
<b>Version MAR/2019. CEH Final Project.</b> 



<h2>DESCARGO DE RESPONSABILIDAD</H2><br>
Toda la información que se expone a continuación sólo tiene fines educativos y pretende servir como manual del material que se ha visto en clase o como guía para cualquier persona interasada en la seguridad informática desde el punto de vista ofensivo. Como autor de este material, no me hago responsable de cualquier uso indebido que se haga de esta información. Para la mayoría de las pruebas que se enseñan en este manual se requiere autorización legal por escrito del propietario del activo sobre el que se realice la prueba.

    - El código de los ficheros alojados, ha sido redactado por
        el propietario del repositorio.
    - Los documentos que se encuentran en el repositorio, se pueden
        descargar y usar libremente.
    - El autor no se hace repsonsable del mal uso que puedan darse
        a los conocimientos que en este repositorio se comparten.
    - La herramienta ha sido diseñada y programada para generar 
        diccionarios y usarlos en ataques hybridos de contraseña.
    
INFORMACIÓN


    - En próximas versiones se añadiran funcionalidades en las cuales
    se pueda usar el diccionario con el añadido de las herramientas
    que vienen instaladas por defecto en KaliLinux, permitiendo ahorrar
    tiempo a la hora de lanzar la prueba de concepto.
    - Se admiten todo tipo de recomendaciones y aportes 
    para mejorar la herramienta.
    
<h2>FORMA DE USO</H2><br>
<ol>
    <li>Clonar el repositorio: git clone https://github.com/baah-romero/hybridPasswordCracker.git</li>
    <li>Acceder al repositorio: cd hybridPasswordCracker</li>
    <li>Ejecutar la herramienta: python3 hybridPasswordCracker.py</li>
    <li>Introduce el nombre que tendrá el diccionario, se generará en formato TXT</li>
    <li>Añade palabras a la lista del diccionario, usa la cadena :wq para cortar la lista y empezar a generar el diccionario hybrido.</li>
    <li>Al finalizar, mostrará un resumen por cada palabra, así, como del diccionario al completo.</li>
    <li>Usar el diccionario en la PoF que se desee.</li>
</ol>
    
<h2>LICENCIA</H2><br>
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
