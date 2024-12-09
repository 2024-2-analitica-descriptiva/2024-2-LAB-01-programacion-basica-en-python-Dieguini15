"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    import csv
    data = "files/input/data.csv"
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