"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_04():
    import csv
    data = r"C:\analiticadescriptiva\2024-2-LAB-01-programacion-basica-en-python-Dieguini15\data.csv"
    meses = [f"{i:02}" for i in range(1, 13)]
    conteos = [0] * 12 
    with open(data, mode="r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")
            fecha = partes[2]  
            try:
                mes = fecha.split("-")[1]
                for i in range(len(meses)):
                    if mes == meses[i]:
                        conteos[i] += 1
                        break
            except IndexError:
                print(f"No válido '{linea.strip()}'")
                continue
    resultados = list(zip(meses, conteos))
    return resultados
print(pregunta_04())
