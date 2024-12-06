"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    import csv
    data = r"C:\analiticadescriptiva\2024-2-LAB-01-programacion-basica-en-python-Dieguini15\data.csv"
    asociaciones = {}  
    with open(data, mode="r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            
            letra, valor = partes[0], partes[1]
            try:
                valor = int(float(valor)) 
            except ValueError:
                continue
            if valor in asociaciones:
                asociaciones[valor].append(letra)
            else:
                asociaciones[valor] = [letra]
                
    resultados = sorted((valor, letras) for valor, letras in asociaciones.items())
    return resultados
print(pregunta_07())
"""
Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
contiene un valor posible de la columna 2 y una lista con todas las letras
asociadas (columna 1) a dicho valor de la columna 2.

Rta/
[(0, ['C']),
    (1, ['E', 'B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E', 'E', 'D']),
    (4, ['E', 'B']),
    (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
    (6, ['C', 'E', 'A', 'B']),
    (7, ['A', 'C', 'E', 'D']),
    (8, ['E', 'D', 'E', 'A', 'B']),
    (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

"""
