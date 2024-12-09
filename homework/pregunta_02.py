"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    
    import csv
    data = "files/input/data.csv"
    contadores = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    with open(data, mode="r", encoding="utf-8") as datos:
        for linea in datos:
            letra = linea.strip().split("\t")[0]  
            if letra in contadores: 
                contadores[letra] += 1
    return sorted(contadores.items())
print(pregunta_02())

    
"""
Retorne la cantidad de registros por cada letra de la primera columna como
la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

Rta/
[('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

"""
