"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    import csv
    data = "files/input/data.csv"
    letras = ['A', 'B', 'C', 'D', 'E']
    maximos = [-float('inf')] * 5 
    minimos = [float('inf')] * 5  
    with open(data, mode="r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            letra, valor = partes[0], partes[1]
            try:
                valor = float(valor)
            except ValueError:
                continue
            for i in range(len(letras)):
                if letra == letras[i]:
                    maximos[i] = max(maximos[i], valor)
                    minimos[i] = min(minimos[i], valor)
                    break
    resultados = list(zip(letras, map(int, maximos), map(int, minimos)))
    return resultados
print(pregunta_05())
    
    
"""
Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
por cada letra de la columa 1.

Rta/
[('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

"""
