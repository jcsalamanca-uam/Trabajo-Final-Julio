from faker import Faker
import random
import csv

fake = Faker()

def generar_usuarios(num):
    with open('usuarios.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Nombre', 'Email', 'Publicaciones_dia', 'Comentario_reciente'])
        for i in range(num):
            writer.writerow([
                i,
                fake.name(),
                fake.email(),
                random.randint(1, 200),
                fake.sentence()
            ])

if __name__ == '__main__':
    generar_usuarios()
