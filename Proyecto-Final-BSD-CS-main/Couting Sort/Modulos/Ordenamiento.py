import csv
import time

def cargar_desde_csv(nombre_archivo="Personas.csv"):
    personas = []
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        next(reader)  # Saltar encabezado
        for fila in reader:
            id, nombre, edad_str, pais = fila
            edad = int(edad_str)
            personas.append((nombre, edad, pais))
    return personas

def counting_sort_por_edad(personas, edad_maxima=120):
    # Crear lista de listas (una por cada edad)
    conteo = [[] for _ in range(edad_maxima + 1)]
    inicio = time.time()
    
    # Agrupar personas por edad
    for persona in personas:
        edad = persona[1]
        conteo[edad].append(persona)
    
    # Reconstruir la lista ordenada
    resultado = []
    for grupo in conteo:
        resultado.extend(grupo)
    fin = time.time()
    duracion = fin - inicio
    
    return resultado

