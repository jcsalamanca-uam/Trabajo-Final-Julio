import csv
import time

# palabras sospechosas
PALABRAS_CLAVE = ['hack', 'bot', '$$', 'malware', 'phishing', 'virus']

def es_sospechoso(usuario):
    
    publicaciones = int(usuario['Publicaciones_dia'])
    comentario = usuario['Comentario_reciente'].lower()

    if publicaciones > 150:
        return True

    for palabra in PALABRAS_CLAVE:
        if palabra in comentario:
            return True

    return False

def buscar_sospechosos(ruta_csv='usuarios.csv', mostrar_resultado=True):
   
    sospechosos = []
    comparaciones = 0
    inicio = time.time()

    
    with open(ruta_csv, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
            
        #Parte importente :)
        for usuario in lector:
            comparaciones += 1
            if es_sospechoso(usuario):
                sospechosos.append(usuario)

    fin = time.time()
    duracion = fin - inicio

    if mostrar_resultado:
        print(f"\n Usuarios sospechosos encontrados: {len(sospechosos)}")
        print(f" Tiempo total: {duracion:.4f} segundos")
        print(f" Comparaciones realizadas: {comparaciones}")

    return sospechosos
