"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    import csv
    data = r"C:\analiticadescriptiva\2024-2-LAB-01-programacion-basica-en-python-Dieguini15\data.csv"
    x=open(data).readlines()
    x=[i.split("\t")   for i in x]
    x=[int(i[1]) for i in x]
    x=sum(x)
   
    return x
print(pregunta_01())
##dadd
"""
Retorne la suma de la segunda columna.

Rta/
214

"""
