<b><h1 align="center">Lenguajes de Programación Más Usados en 2024</h1></b>


<b><h2 align="center">Descripción</h2></b>
<p>Este proyecto se enfoca en la recopilación y análisis de los lenguajes de programación más utilizados en 2024, basándose en información extraída de varios sitios web populares.
Utilizando técnicas de web scraping y procesamiento de datos con bibliotecas de Python, el proyecto obtiene los lenguajes más mencionados en tres páginas web y les asigna una puntuación en función de su aparición.
Los resultados se procesan y se guardan en un archivo Excel, donde se pueden visualizar tanto las posiciones individuales de los lenguajes en cada página como un análisis general con puntuaciones y porcentajes de popularidad.</p>

<b><h2 align="center">Funcionalidades</h2></b>
<p>Extracción de Datos (Web Scraping):

Se realiza scraping en tres sitios web relacionados con los lenguajes de programación más populares en 2024:<br>
Rootstack <br>
RuralHack <br>
KeepCoding <br>
Los lenguajes de programación son extraídos de cada página, prestando atención a las posiciones de los lenguajes en las listas de cada sitio.
<br>
- Asignación de Puntajes:

Cada lenguaje extraído recibe una puntuación en función de su posición en la lista (1º lugar = 5 puntos, 2º lugar = 4 puntos, etc.).
Se combinan las puntuaciones de los tres sitios para calcular el puntaje total de cada lenguaje.
Análisis y Cálculo de Porcentajes:

Una vez asignados los puntajes, se calculan los porcentajes de popularidad de cada lenguaje con respecto al puntaje total.
- Generación de Reporte en Excel:

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


##  Conclusión

###  Ranking de Lenguajes de Programación

Basado en los datos analizados, podemos establecer el siguiente ranking de los lenguajes de programación más utilizados en este proyecto:

1. **Python:** Con 14 puntos (31.11%), Python lidera claramente. Su amplia presencia en el proyecto indica una alta demanda y popularidad.
2. **JavaScript:** Muy cerca de Python, con 13 puntos (28.89%). Su dominio en el desarrollo web lo consolida como un lenguaje fundamental.
3. **Java:** En tercer lugar, Java obtiene 9 puntos (20.00%). Su versatilidad lo mantiene a lo largo del tiempo como una opción sólida.
4. **C++:** Con 4 puntos (8.89%), C++ se posiciona en cuarto lugar. Su eficiencia lo hace ideal para aplicaciones de alto rendimiento.
5. **C#:** C# obtiene 3 puntos (6.67%). Su estrecha relación con Microsoft lo posiciona como una opción popular en ese ecosistema.
6. **C:** Por último, C obtiene 2 puntos (4.44%). A pesar de ser más antiguo, sigue siendo relevante en sistemas embebidos.

