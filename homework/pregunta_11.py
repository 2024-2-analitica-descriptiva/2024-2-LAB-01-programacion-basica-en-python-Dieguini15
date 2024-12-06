"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    import csv
    data = r"C:\analiticadescriptiva\2024-2-LAB-01-programacion-basica-en-python-Dieguini15\data.csv"
    suma_letras = {}

    with open(data, mode="r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            try:
                valor_columna_2 = int(float(partes[1]))
                letras_columna_4 = partes[3].split(",")
            except ValueError:
                continue
            for letra in letras_columna_4:
                if letra in suma_letras:
                    suma_letras[letra] += valor_columna_2
                else:
                    suma_letras[letra] = valor_columna_2
    suma_letras_ordenada = dict(sorted(suma_letras.items()))
    return suma_letras_ordenada
print(pregunta_11())
    
"""
Retorne un diccionario que contengan la suma de la columna 2 para cada
letra de la columna 4, ordenadas alfabeticamente.

Rta/
{'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


"""
