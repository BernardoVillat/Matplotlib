import pandas as pd
import matplotlib.pyplot as plt
import random

class DataGenerationError(Exception):
    pass

def create_random_area_chart(num_students):
    try:
        estudiantes = list(range(1, num_students + 1))

        examen1 = [random.randint(50, 100) for _ in estudiantes]
        examen2 = [random.randint(50, 100) for _ in estudiantes]

        if len(examen1) != num_students or len(examen2) != num_students:
            raise DataGenerationError("Error en la generación de datos.")
        
        data = {'Estudiantes': estudiantes, 'Examen1': examen1, 'Examen2': examen2}
        df = pd.DataFrame(data)

        plt.figure(figsize=(10, 6))
        plt.stackplot(df['Estudiantes'], [df['Examen1'], df['Examen2']], labels=['Examen1', 'Examen2'], alpha=0.5)
        plt.xlabel('Estudiantes')
        plt.ylabel('Puntajes')
        plt.title('Relación entre Puntajes en Examen1 y Examen2')
        plt.legend(loc='upper left')

        plt.show()

    except DataGenerationError as e:
        print(f"Error en la generación de datos: {e}")

num_students = 20  

create_random_area_chart(num_students)
