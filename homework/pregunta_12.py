"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    import csv
    data = "files/input/data.csv"
    suma_por_letra = {}
    with open(data, mode="r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            letra = partes[0]
            diccionario_codificado = partes[4]
            try:
                valores = [int(par.split(":")[1]) for par in diccionario_codificado.split(",")]
            except (ValueError, IndexError):
                continue
            if letra in suma_por_letra:
                suma_por_letra[letra] += sum(valores)
            else:
                suma_por_letra[letra] = sum(valores)
        suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))
    return suma_por_letra_ordenada
print(pregunta_12())
"""
Genere un diccionario que contengan como clave la columna 1 y como valor
la suma de los valores de la columna 5 sobre todo el archivo.

Rta/
{'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

"""
