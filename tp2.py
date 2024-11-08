import requests  # Importa la librería para hacer peticiones HTTP.
from bs4 import BeautifulSoup  # Importa la librería para analizar HTML.
from collections import Counter  # Importa la clase Counter para contar elementos.
import pandas as pd  # Importa pandas para manejar datos en tablas.
from openpyxl import load_workbook  # Importa la librería openpyxl para trabajar con archivos Excel.


def asignar_puntaje(lenguajes):
    puntos = [5, 4, 3, 2, 1]  
    return {lenguaje: puntos[i] for i, lenguaje in enumerate(lenguajes)}  


url1 = "https://rootstack.com/es/blog/lenguajes-de-programacion-mas-usados-en-2024"
respuesta1 = requests.get(url1)  # Guardamos en la variable la respuesta de la solicitud HTTP.
contenido1 = BeautifulSoup(respuesta1.text, "html.parser")  # Guardamos el objeto BeautifulSoup con el contenido html.
etiquetas_h3 = contenido1.select(".wysiwyg-purified h3")[:5]  # Obtiene los primeros 5 títulos de los lenguajes.
lista_lenguajes1 = [h3.get_text(strip=True)[3:] for h3 in etiquetas_h3]  # Extrae el texto de esos títulos ignorando los primeros 3 carácteres.

url2 = "https://ruralhack.es/lenguajes-programacion-usados/"
respuesta2 = requests.get(url2)
contenido2 = BeautifulSoup(respuesta2.content, "html.parser")
etiquetas_titulo = contenido2.find_all(class_="elementor-heading-title elementor-size-default")
lista_lenguajes2 = [etiqueta.get_text(strip=True) for i, etiqueta in enumerate(etiquetas_titulo) if i in [0, 1, 4, 5, 6]]  

url3 = "https://keepcoding.io/blog/lenguajes-de-programacion-mas-usados/"
respuesta3 = requests.get(url3)
contenido3 = BeautifulSoup(respuesta3.content, 'html.parser')
elementos_lista = contenido3.select('ol.wp-block-list li')  
lista_lenguajes3 = [li.get_text(strip=True) for li in elementos_lista[:5]]  


puntajes_lenguajes = Counter()  # Contador para poder acumular los puntos.
for lista in [lista_lenguajes1, lista_lenguajes2, lista_lenguajes3]: # Recorremos cada lista.
    puntajes_lenguajes.update(asignar_puntaje(lista))  # Utilizo la función para asignar los puntos a los lenguajes y actualiza el contador.

# Dict crea un diccionario. Most ordena los lenguajes según los puntajes de mayor a menor.
puntajes_lenguajes_ordenados = dict(puntajes_lenguajes.most_common())  

total_puntajes = sum(puntajes_lenguajes_ordenados.values())  # Suma todos los puntos (del nuevo diccionario) para obtener el total.
porcentajes_lenguajes = {lenguaje: (puntos / total_puntajes) * 100 for lenguaje, puntos in puntajes_lenguajes_ordenados.items()}  # Recorremos cada lenguaje del diccionario puntajes_lenguajes_ordenados, calcula su porcentaje en relación al total de puntajes y almacena ese porcentaje en un nuevo diccionario porcentajes_lenguajes.
# EJEMPLO:                            14  / 45               * 100 = 31.11%


# Crear el DataFrame para el Excel con las columnas y los lenguajes usando la biblioteca pandas.
df_lenguajes = pd.DataFrame({
    "Pagina 1": lista_lenguajes1,
    "Pagina 2": lista_lenguajes2,
    "Pagina 3": lista_lenguajes3,
})

# Agregar los datos de posición, porcentaje y puntos al DataFrame.
df_posicion = pd.DataFrame({
    "Posición": list(puntajes_lenguajes_ordenados.keys()),  # Columna con los lenguajes por nombre.
    "Puntos": list(puntajes_lenguajes_ordenados.values()),  # Columna con los puntos acumulados para cada lenguaje.
    "Porcentaje": [f"{porcentajes_lenguajes[l]:.2f}%" for l in puntajes_lenguajes_ordenados.keys()]  # Crea una lista con los porcentajes de cada lenguaje y lo asignamos a una Columna.
})

# Combina las dos tablas en una sola.
df_final = pd.concat([df_lenguajes, df_posicion], axis=1)  # axis=1 significa que se combinan las columnas.

# Guardar el DataFrame en un archivo Excel.
df_final.to_excel("C:/Users/JuanC/Desktop/LenguajesMasUtilizados.xlsx", index=False)  # Guarda el archivo Excel.





# Ajustar el ancho de las columnas.
libro_trabajo = load_workbook("C:/Users/JuanC/Desktop/LenguajesMasUtilizados.xlsx")  # Abre el archivo Excel creado.
hoja_trabajo = libro_trabajo.active
# Establecer un ancho más amplio para las columnas.
columnas = ['A', 'B', 'C', 'D', 'E', 'F']  # Lista de las columnas que queremos ajustar.
for col in columnas:  # Recorre cada columna.
    hoja_trabajo.column_dimensions[col].width = 20  # Ajusta el ancho de cada columna a 20.
libro_trabajo.save("C:/Users/JuanC/Desktop/LenguajesMasUtilizados.xlsx")  # Guarda el archivo Excel con los cambios.


print("Excel generado: LenguajesMasUtilizados.xlsx")  
