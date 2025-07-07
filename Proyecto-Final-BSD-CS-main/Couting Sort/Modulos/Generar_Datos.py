from faker import Faker
import random
import csv
fake = Faker()

def generar_nombre():
    nombres = ["Ana", "Luis", "Carlos", "María", "Juan", "Pedro", "Lucía", "Jorge", "Elena", "José"]
    return random.choice(nombres)

def generar_pais():
    paises = ["Nicaragua", "Costa rica", "Honduras", "Estados unidos", "Panama"]
    return random.choice(paises)

def generar_datos(num):
    with open('Personas.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Nombre', 'Edad', 'Pais'])
        for i in range(num):
            writer.writerow([
                i,
                fake.name(),
                random.randint(0, 98),
                generar_pais()
            ])

if __name__ == '__main__':
    generar_datos()

def guardar_en_csv(personas, nombre_archivo="personas.csv"):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Nombre", "Edad", "Pais"])  # Encabezados
        writer.writerows(personas)