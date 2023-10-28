import pandas as pd
import matplotlib.pyplot as plt
import random

class DataLoadingError(Exception):
    pass

def create_random_sales_bar_chart(num_months):
    try:
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        ventas = [random.randint(30000, 80000) for _ in range(num_months)]

        if len(meses) < num_months:
            raise DataLoadingError("No hay suficientes meses disponibles para generar datos aleatorios.")

        data = {'Mes': meses[:num_months], 'Ventas': ventas[:num_months]}
        ventas_df = pd.DataFrame(data)

        plt.figure(figsize=(10, 6))
        plt.barh(ventas_df['Mes'], ventas_df['Ventas'], color='skyblue')

        plt.xlabel('Ventas Totales')
        plt.ylabel('Meses')
        plt.title('Ventas Mensuales por Mes')

        plt.show()

    except DataLoadingError as e:
        print(f"Ocurrió un error inesperado: {e}")

num_months = 12

create_random_sales_bar_chart(num_months)

