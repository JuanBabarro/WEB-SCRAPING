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
Al finalizar la ejecución del script, se genera un archivo Excel llamado LenguajesMasUtilizados.xlsx en la ubicación especificada. Este archivo contiene los siguientes datos:

- Columnas de las Páginas Web:

Las listas de los lenguajes de programación más mencionados en las tres páginas web analizadas.
Columnas de Análisis:

Posición: El nombre del lenguaje de programación ordenado por su popularidad acumulada.
Puntos: La puntuación total de cada lenguaje basada en su posición en cada página.
Porcentaje: El porcentaje del total de puntos que representa cada lenguaje.
Formato Excel:

El archivo Excel tiene un formato ajustado para facilitar la lectura de los datos, con el ancho de las columnas optimizado.
