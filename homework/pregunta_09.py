"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    
    import csv
    data = "files/input/data.csv"
    conteos = {}
    with open(data, mode="r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            diccionario_codificado = partes[4]
            claves = [par.split(":")[0] for par in diccionario_codificado.split(",")]
            for clave in claves:
                if clave in conteos:
                    conteos[clave] += 1
                else:
                    conteos[clave] = 1
    conteos_ordenados = dict(sorted(conteos.items()))
    return conteos_ordenados
print(pregunta_09())
            
"""
Retorne un diccionario que contenga la cantidad de registros en que
aparece cada clave de la columna 5.

Rta/
{'aaa': 13,
    'bbb': 16,
    'ccc': 23,
    'ddd': 23,
    'eee': 15,
    'fff': 20,
    'ggg': 13,
    'hhh': 16,
    'iii': 18,
    'jjj': 18}}

"""
