"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    import csv
    data = "files/input/data.csv"
    resultado = []
    with open(data, mode="r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            letra = partes[0]
            columna_4 = partes[3].split(",")
            columna_5 = partes[4].split(",")
            cantidad_columna_4 = len(columna_4)
            cantidad_columna_5 = len(columna_5)
            resultado.append((letra, cantidad_columna_4, cantidad_columna_5))
    return resultado
print(pregunta_10())
    



    
    
"""
Retorne una lista de tuplas contengan por cada tupla, la letra de la
columna 1 y la cantidad de elementos de las columnas 4 y 5.

Rta/
[('E', 3, 5),
    ('A', 3, 4),
    ...
    ('E', 2, 3),
    ('E', 3, 3)]


"""
