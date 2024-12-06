"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
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
                asociaciones[valor].add(letra)
            else:
                asociaciones[valor] = {letra}
    resultados = sorted((valor, sorted(list(letras))) for valor, letras in asociaciones.items())
    return resultados
print(pregunta_08())
    
    
    
    
"""
Genere una lista de tuplas, donde el primer elemento de cada tupla
contiene  el valor de la segunda columna; la segunda parte de la tupla
es una lista con las letras (ordenadas y sin repetir letra) de la
primera  columna que aparecen asociadas a dicho valor de la segunda
columna.

Rta/
[(0, ['C']),
    (1, ['B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E']),
    (4, ['B', 'E']),
    (5, ['B', 'C', 'D', 'E']),
    (6, ['A', 'B', 'C', 'E']),
    (7, ['A', 'C', 'D', 'E']),
    (8, ['A', 'B', 'D', 'E']),
    (9, ['A', 'B', 'C', 'E'])]

"""
