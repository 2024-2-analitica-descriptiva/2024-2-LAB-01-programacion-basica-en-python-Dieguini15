"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    import csv
    data = "files/input/data.csv"
    suma_por_letra = {}

    with open(data, mode="r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            letra = partes[0] 
            try:
                valor = int(float(partes[1])) 
            except ValueError:
                continue
            if letra in suma_por_letra:
                suma_por_letra[letra] += valor
            else:
                suma_por_letra[letra] = valor
    resultado = sorted(suma_por_letra.items())
    return resultado
print(pregunta_03())