<b><h1 align="center">Lenguajes de Programación Más Usados en 2024</h1></b>


<b><h2 align="center">Descripción</h2></b>
<p>Este proyecto se enfoca en la recopilación y análisis de los lenguajes de programación más utilizados en 2024, basándose en información extraída de varios sitios web populares.
Utilizando técnicas de web scraping y procesamiento de datos con bibliotecas de Python, el proyecto obtiene los lenguajes más mencionados en tres páginas web y les asigna una puntuación en función de su aparición.
Los resultados se procesan y se guardan en un archivo Excel, donde se pueden visualizar tanto las posiciones individuales de los lenguajes en cada página como un análisis general con puntuaciones y porcentajes de popularidad.</p>

<b><h2 align="center">Funcionalidades</h2></b>
<p>Extracción de Datos (Web Scraping):

Se realiza scraping en tres sitios web relacionados con los lenguajes de programación más populares en 2024:
Rootstack
RuralHack
KeepCoding
Los lenguajes de programación son extraídos de cada página, prestando atención a las posiciones de los lenguajes en las listas de cada sitio.
Asignación de Puntajes:

Cada lenguaje extraído recibe una puntuación en función de su posición en la lista (1º lugar = 5 puntos, 2º lugar = 4 puntos, etc.).
Se combinan las puntuaciones de los tres sitios para calcular el puntaje total de cada lenguaje.
Análisis y Cálculo de Porcentajes:

Una vez asignados los puntajes, se calculan los porcentajes de popularidad de cada lenguaje con respecto al puntaje total.
Generación de Reporte en Excel:

Los datos obtenidos y procesados se almacenan en un archivo Excel, que incluye:
Las listas de lenguajes extraídos de cada página web.
Las posiciones, puntajes acumulados y porcentajes de cada lenguaje.
Ajuste de Formato en Excel:

El archivo Excel resultante es ajustado para que las columnas tengan un tamaño adecuado, mejorando la legibilidad.
</p>

<b><h2 align="center">Ejecución</h2></b>

<p> Ejecuta el archivo de Python que contiene el código.
El script realizará las siguientes acciones:
Realizará solicitudes HTTP a las páginas web especificadas.
Extraerá los lenguajes de programación más mencionados en cada página.
Asignará puntajes a los lenguajes según su posición.
Calculará los porcentajes de popularidad.
Guardará los resultados en un archivo Excel en la ubicación especificada (C:/Users/JuanC/Desktop/LenguajesMasUtilizados.xlsx).</p>

<b><h2 align="center">Salida</h2></b>
<p>Al finalizar la ejecución del script, se genera un archivo Excel llamado LenguajesMasUtilizados.xlsx en la ubicación especificada. 

<b>- Columnas de las Páginas Web:</b>
Las listas de los lenguajes de programación más mencionados en las tres páginas web analizadas.


<b>- Posición:</b>
El nombre del lenguaje de programación ordenado por su popularidad acumulada.

<b>- Puntos:</b>
La puntuación total de cada lenguaje basada en su posición en cada página.

<b>- Porcentaje:</b>
El porcentaje del total de puntos que representa cada lenguaje.

<b>- Formato Excel:</b>
El archivo Excel tiene un formato ajustado para facilitar la lectura de los datos, con el ancho de las columnas optimizado.</p>


<b><h2 align="center">Conclusión</h2></b>
<p>Según los datos presentados, podemos determinar el ranking de los lenguajes de programación más utilizados y sus respectivas puntuaciones y porcentajes:
- Python: Con un total de 14 puntos y un porcentaje del 31.11%, Python se posiciona como el lenguaje de programación más utilizado en este conjunto de datos. Su amplia presencia en las tres "páginas" analizadas indica una fuerte demanda y popularidad.
- JavaScript: Le sigue muy de cerca JavaScript, con 13 puntos y un 28.89% del total. Su dominio en el desarrollo web lo consolida como un lenguaje fundamental en la industria.
- Java: En el tercer lugar encontramos a Java, con 9 puntos y un 20.00%. Su versatilidad y uso en diversas aplicaciones lo mantienen como una opción sólida para muchos desarrolladores.
- C++: C++ ocupa el cuarto lugar, con 4 puntos y un 8.89%. Su eficiencia y uso en aplicaciones de alto rendimiento lo hacen relevante en ciertos ámbitos.
- C#: C# se ubica en el quinto lugar, con 3 puntos y un 6.67%. Su estrecha relación con Microsoft y su uso en el desarrollo de aplicaciones .NET lo posicionan como una opción popular en ese ecosistema.
- C: Por último, C obtiene 2 puntos y un 4.44%. A pesar de ser un lenguaje más antiguo, sigue siendo utilizado en sistemas embebidos y aplicaciones donde se requiere un alto nivel de control.</p>
