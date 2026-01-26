import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime as dt

# Cargar datos
taxis = pd.read_parquet("yellow_tripdata_2025-11.parquet")

# ============= INFORMACIÓN GENERAL =============
print("=" * 60)
print("INFORMACIÓN GENERAL DEL DATASET")
print("=" * 60)

# Columnas con tipos extraños: passenger_count, RatecodeID, store_and_fwd_flag, payment_type, tpep_pickup_datetime, tpep_dropoff_datetime
# Transformación de tipos
taxis['passenger_count'] = taxis['passenger_count'].astype('Int64')
taxis['RatecodeID'] = taxis['RatecodeID'].astype('Int64')
taxis['store_and_fwd_flag'] = taxis['store_and_fwd_flag'].map({'Y':True,'N':False}).astype('boolean')
taxis['tpep_pickup_datetime'] = taxis['tpep_pickup_datetime'].dt.tz_localize('America/New_york', ambiguous="NaT")
taxis['tpep_dropoff_datetime'] = taxis['tpep_dropoff_datetime'].dt.tz_localize('America/New_york', ambiguous="NaT")

# Añadir columnas derivadas
taxis['duracion'] = taxis['tpep_dropoff_datetime'] - taxis['tpep_pickup_datetime']

# Transformar columnas distance de millas a km y valores monetarios de dolar a euro
taxis['trip_distance_km'] = taxis['trip_distance'] * 1.609
taxis['total_amount_euro'] = taxis['total_amount'] * 1.165
taxis['tip_amount_euro'] = taxis['tip_amount'] * 1.165
taxis['tolls_amount_euro'] = taxis['tolls_amount'] * 1.165
taxis['fare_amount_euro'] = taxis['fare_amount'] * 1.165
taxis['Airport_fee_euro'] = taxis['Airport_fee'] * 1.165
taxis['cbd_congestion_fee_euro'] = taxis['cbd_congestion_fee'] * 1.165

print("\nHead:")
print(taxis.head())

print(f"\nNúmero de filas: {len(taxis)}")
print(f"Número de columnas: {len(taxis.columns)}")

print("\nColumnas y tipos de datos:")
print(taxis.dtypes)

print("\nValores faltantes:")
print(taxis.isnull().sum())
print(taxis[taxis["payment_type"] == 0].isna().mean())

# print(taxis["store_and_fwd_flag"].unique())
# print(taxis["congestion_surcharge"].unique())
# print(taxis["improvement_surcharge"].unique())
# print(taxis["payment_type"].unique())


# ============= ESTADÍSTICAS DESCRIPTIVAS =============
print("\n" + "=" * 60)
print("ESTADÍSTICAS DESCRIPTIVAS")
print("=" * 60)
print(taxis.describe())

# ============= ANÁLISIS DE VARIABLES CLAVE =============
print("\n" + "=" * 60)
print("ANÁLISIS DE VARIABLES CLAVE")
print("=" * 60)

print("\nPASSENGER COUNT (Número de pasajeros):")
print(f"  MAX: {taxis['passenger_count'].max()}")
print(f"  MIN: {taxis['passenger_count'].min()}")
print(f"  MEAN: {taxis['passenger_count'].mean():.2f}")
print(f"  MEDIAN: {taxis['passenger_count'].median():.0f}")

print("\nTRIP DISTANCE (Distancia del viaje):")
print(f"  MAX: {taxis['trip_distance'].max():.2f}")
print(f"  MIN: {taxis['trip_distance'].min():.2f}")
print(f"  MEAN: {taxis['trip_distance'].mean():.2f}")
print(f"  MEDIAN: {taxis['trip_distance'].median():.2f}")

print("\nTIP AMOUNT (Propina):")
print(f"  MAX: {taxis['tip_amount'].max():.2f}")
print(f"  MIN: {taxis['tip_amount'].min():.2f}")
print(f"  MEAN: {taxis['tip_amount'].mean():.2f}")
print(f"  MEDIAN: {taxis['tip_amount'].median():.2f}")

print("\nTOTAL AMOUNT (Monto total):")
print(f"  MAX: {taxis['total_amount'].max():.2f}")
print(f"  MIN: {taxis['total_amount'].min():.2f}")
print(f"  MEAN: {taxis['total_amount'].mean():.2f}")
print(f"  MEDIAN: {taxis['total_amount'].median():.2f}")


# ============= TOP 10 VIAJES MÁS LARGOS =============
print("\n" + "=" * 60)
print("TOP 30 VIAJES MÁS LARGOS")
print("=" * 60)

top_10_longest = taxis.nlargest(30, 'trip_distance')
print("\n", top_10_longest)

# PREGUNTA 1: ¿Qué columnas tienen valores outliers y cuáles son? - Anomalias
# PREGUNTA 2: ¿En qué franja horaria suele haber más viajes? - Temporales
# PREGUNTA 3: ¿Qué tipo de pago es el más usado? - Comparativas

print("Cuanto dura el viaje medio")
print("Media: ",taxis['duracion'].mean()) # Agregacion - reducir muchos registros a un solo valor
print("Mediana: ",taxis['duracion'].median())
print("Desviación estandard: ", taxis['duracion'].std())

print("Agrupacion de cantidad a pagar por tipo de pago")
print("Media: ",taxis.groupby('payment_type')['total_amount_euro'].mean()) # Agregacion - reducir muchos registros a un solo valor
print("Mediana: ",taxis.groupby('payment_type')['total_amount_euro'].median())
print("Desviación estandard: ", taxis.groupby('payment_type')['total_amount_euro'].std())

print(taxis.groupby('payment_type')['total_amount_euro'].agg(['count', 'mean']))

print("Agrupar por numero de pasajeros y calcular el coste medio del viaje")
print(taxis.groupby('passenger_count')['total_amount_euro'].agg(['count', 'mean']))
print(taxis[taxis["passenger_count"] == 7])

print(taxis['trip_distance'].quantile([0.25, 0.5, 0.75, 0.95, 0.99, 1]))

print('\nCruce de variables')
print(taxis[['trip_distance', 'duracion']].describe())
print(taxis.groupby('payment_type')['tip_amount'].mean())

# Hipotesis: Los trayectos nocturnos son mas largos
# Define nighttime as 21:00 (9 PM) to 06:00 (6 AM)
print('\n# Hipotesis: Los trayectos nocturnos son mas largos')

taxis['is_night'] = taxis['tpep_pickup_datetime'].dt.hour.between(21, 23) | taxis['tpep_pickup_datetime'].dt.hour.between(0, 5)

print(taxis.groupby('is_night')['trip_distance'].mean())
print(taxis.groupby('is_night')['trip_distance_km'].agg(['count', 'mean', 'median']))

# Hipotesis: Cuando la distancia aumenta, la dispersión de la duración también aumenta
# Definir que es un trayecto corto y largo
# Agrupar y ver los rangos en los que se mueve la variable escogida (duración)
print('\n# Hipotesis: Cuando la distancia aumenta, la dispersión de la duración también aumenta')

taxis['is_long'] = taxis['trip_distance_km'] > taxis['trip_distance_km'].mean()
print(taxis.groupby('is_long')['duracion'].std())