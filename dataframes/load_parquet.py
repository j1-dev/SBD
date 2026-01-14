import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Cargar datos
df_parquet = pd.read_parquet("yellow_tripdata_2025-11.parquet")

# ============= INFORMACIÓN GENERAL =============
print("=" * 60)
print("INFORMACIÓN GENERAL DEL DATASET")
print("=" * 60)

print("\nHead:")
print(df_parquet.head())

print(f"\nNúmero de filas: {len(df_parquet)}")
print(f"Número de columnas: {len(df_parquet.columns)}")

print("\nColumnas y tipos de datos:")
print(df_parquet.dtypes)

print("\nValores faltantes:")
print(df_parquet.isnull().sum())

# ============= ESTADÍSTICAS DESCRIPTIVAS =============
print("\n" + "=" * 60)
print("ESTADÍSTICAS DESCRIPTIVAS")
print("=" * 60)
print(df_parquet.describe())

# ============= ANÁLISIS DE VARIABLES CLAVE =============
print("\n" + "=" * 60)
print("ANÁLISIS DE VARIABLES CLAVE")
print("=" * 60)

print("\nPASSENGER COUNT (Número de pasajeros):")
print(f"  MAX: {df_parquet['passenger_count'].max()}")
print(f"  MIN: {df_parquet['passenger_count'].min()}")
print(f"  MEAN: {df_parquet['passenger_count'].mean():.2f}")
print(f"  MEDIAN: {df_parquet['passenger_count'].median():.0f}")

print("\nTRIP DISTANCE (Distancia del viaje):")
print(f"  MAX: {df_parquet['trip_distance'].max():.2f}")
print(f"  MIN: {df_parquet['trip_distance'].min():.2f}")
print(f"  MEAN: {df_parquet['trip_distance'].mean():.2f}")
print(f"  MEDIAN: {df_parquet['trip_distance'].median():.2f}")

print("\nTIP AMOUNT (Propina):")
print(f"  MAX: {df_parquet['tip_amount'].max():.2f}")
print(f"  MIN: {df_parquet['tip_amount'].min():.2f}")
print(f"  MEAN: {df_parquet['tip_amount'].mean():.2f}")
print(f"  MEDIAN: {df_parquet['tip_amount'].median():.2f}")

print("\nTOTAL AMOUNT (Monto total):")
print(f"  MAX: {df_parquet['total_amount'].max():.2f}")
print(f"  MIN: {df_parquet['total_amount'].min():.2f}")
print(f"  MEAN: {df_parquet['total_amount'].mean():.2f}")
print(f"  MEDIAN: {df_parquet['total_amount'].median():.2f}")


# ============= TOP 10 VIAJES MÁS LARGOS =============
print("\n" + "=" * 60)
print("TOP 10 VIAJES MÁS LARGOS")
print("=" * 60)

top_10_longest = df_parquet.nsmallest(30, 'total_amount')
print("\n", top_10_longest)

# ============= VISUALIZACIONES =============
# print("\n" + "=" * 60)
# print("Generando gráficos...")
# print("=" * 60)

# # Configurar estilo
# sns.set_style("whitegrid")
# plt.rcParams['figure.figsize'] = (15, 12)

# # Crear figura con múltiples subplots
# fig = plt.figure(figsize=(16, 12))

# # 1. Distribución de Distancia del Viaje
# ax1 = plt.subplot(3, 3, 1)
# df_parquet['trip_distance'].hist(bins=50, edgecolor='black', ax=ax1)
# ax1.set_title('Distribución de Distancia del Viaje', fontsize=12, fontweight='bold')
# ax1.set_xlabel('Distancia (millas)')
# ax1.set_ylabel('Frecuencia')

# # 2. Distribución de Monto Total
# ax2 = plt.subplot(3, 3, 2)
# df_parquet['total_amount'].hist(bins=50, edgecolor='black', ax=ax2, color='orange')
# ax2.set_title('Distribución de Monto Total', fontsize=12, fontweight='bold')
# ax2.set_xlabel('Monto ($)')
# ax2.set_ylabel('Frecuencia')

# # 3. Distribución de Propina
# ax3 = plt.subplot(3, 3, 3)
# df_parquet['tip_amount'].hist(bins=50, edgecolor='black', ax=ax3, color='green')
# ax3.set_title('Distribución de Propina', fontsize=12, fontweight='bold')
# ax3.set_xlabel('Propina ($)')
# ax3.set_ylabel('Frecuencia')

# # 4. Número de Pasajeros
# ax4 = plt.subplot(3, 3, 4)
# passenger_counts = df_parquet['passenger_count'].value_counts().sort_index()
# ax4.bar(passenger_counts.index, passenger_counts.values, color='steelblue', edgecolor='black')
# ax4.set_title('Número de Pasajeros por Viaje', fontsize=12, fontweight='bold')
# ax4.set_xlabel('Cantidad de Pasajeros')
# ax4.set_ylabel('Frecuencia')

# # 5. Boxplot de Distancia
# ax5 = plt.subplot(3, 3, 5)
# ax5.boxplot(df_parquet['trip_distance'], vert=True)
# ax5.set_title('Boxplot: Distancia del Viaje', fontsize=12, fontweight='bold')
# ax5.set_ylabel('Distancia (millas)')

# # 6. Boxplot de Monto Total
# ax6 = plt.subplot(3, 3, 6)
# ax6.boxplot(df_parquet['total_amount'], vert=True)
# ax6.set_title('Boxplot: Monto Total', fontsize=12, fontweight='bold')
# ax6.set_ylabel('Monto ($)')

# # 7. Relación Distancia vs Monto Total
# ax7 = plt.subplot(3, 3, 7)
# ax7.scatter(df_parquet['trip_distance'], df_parquet['total_amount'], alpha=0.3, s=10)
# ax7.set_title('Distancia vs Monto Total', fontsize=12, fontweight='bold')
# ax7.set_xlabel('Distancia (millas)')
# ax7.set_ylabel('Monto Total ($)')

# # 8. Relación Distancia vs Propina
# ax8 = plt.subplot(3, 3, 8)
# ax8.scatter(df_parquet['trip_distance'], df_parquet['tip_amount'], alpha=0.3, s=10, color='green')
# ax8.set_title('Distancia vs Propina', fontsize=12, fontweight='bold')
# ax8.set_xlabel('Distancia (millas)')
# ax8.set_ylabel('Propina ($)')

# # 9. Proporción de Propina
# ax9 = plt.subplot(3, 3, 9)
# df_parquet['tip_ratio'] = df_parquet['tip_amount'] / (df_parquet['total_amount'] + 1)
# ax9.hist(df_parquet['tip_ratio'], bins=50, edgecolor='black', color='purple', alpha=0.7)
# ax9.set_title('Proporción de Propina (Propina/Total)', fontsize=12, fontweight='bold')
# ax9.set_xlabel('Ratio Propina')
# ax9.set_ylabel('Frecuencia')

# plt.tight_layout()
# plt.savefig('eda_taxis.png', dpi=300, bbox_inches='tight')
# print("\n✓ Gráfico guardado como 'eda_taxis.png'")
# plt.show()

# # ============= ANÁLISIS DE CORRELACIÓN =============
# print("\n" + "=" * 60)
# print("ANÁLISIS DE CORRELACIÓN")
# print("=" * 60)

# # Seleccionar columnas numéricas
# numeric_cols = df_parquet.select_dtypes(include=[np.number]).columns
# correlation_matrix = df_parquet[numeric_cols].corr()

# print("\nMatriz de correlación:")
# print(correlation_matrix)

# # Visualizar matriz de correlación
# fig, ax = plt.subplots(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
#             center=0, square=True, ax=ax, cbar_kws={'label': 'Correlación'})
# ax.set_title('Matriz de Correlación - Variables Numéricas', fontsize=14, fontweight='bold')
# plt.tight_layout()
# plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
# print("\n✓ Matriz de correlación guardada como 'correlation_matrix.png'")
# plt.show()

# print("\n" + "=" * 60)
# print("EDA COMPLETADO")
# print("=" * 60)


# ============= RESPUESTAS A LAS PREGUNTAS =============
print("\n" + "=" * 80)
print("RESPUESTAS A LAS PREGUNTAS DEL EJERCICIO")
print("=" * 80)

# PREGUNTA 1: Qué columnas tienen valores outliers y cuáles son?
print("\n" + "=" * 80)
print("PREGUNTA 1: ¿Qué columnas tienen valores outliers y cuáles son?")
print("=" * 80)

def find_outliers_iqr(data, column):
    """Encuentra outliers usando el método IQR (Rango Intercuartílico)"""
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

numeric_columns = df_parquet.select_dtypes(include=[np.number]).columns

for col in numeric_columns:
    outliers, lower, upper = find_outliers_iqr(df_parquet, col)
    print(f"\n{col.upper()}:")
    print(f"  Límite inferior: {lower:.2f}")
    print(f"  Límite superior: {upper:.2f}")
    print(f"  Número de outliers: {len(outliers)} ({len(outliers)/len(df_parquet)*100:.2f}%)")
    
    if len(outliers) > 0:
        print(f"  Rango de outliers: [{outliers[col].min():.2f}, {outliers[col].max():.2f}]")
        if len(outliers) <= 5:
            print(f"  Ejemplos de outliers:")
            print(outliers[[col]].head())

# PREGUNTA 2: Qué se podría hacer con los valores nulos?
print("\n" + "=" * 80)
print("PREGUNTA 2: ¿Qué se podría hacer con los valores nulos?")
print("=" * 80)

print("\nAnálisis de valores nulos:")
missing_data = df_parquet.isnull().sum()
missing_percent = (df_parquet.isnull().sum() / len(df_parquet)) * 100

missing_df = pd.DataFrame({
    'Columna': missing_data.index,
    'Valores_Nulos': missing_data.values,
    'Porcentaje': missing_percent.values
})
missing_df = missing_df[missing_df['Valores_Nulos'] > 0].sort_values('Valores_Nulos', ascending=False)

if len(missing_df) == 0:
    print("\n✓ ¡EXCELENTE! No hay valores nulos en el dataset.")
else:
    print("\nColumnas con valores nulos:")
    print(missing_df.to_string(index=False))
    
    print("\n📋 RECOMENDACIONES PARA MANEJAR VALORES NULOS:")
    print("""
    1. ELIMINACIÓN DE FILAS:
       - Si el porcentaje de valores nulos es muy bajo (< 5%), se pueden eliminar esas filas.
       - Útil cuando los valores nulos son esporádicos y no afectan mucho al análisis.
    
    2. IMPUTACIÓN (RELLENAR VALORES):
       - Media/Mediana: Para columnas numéricas, se puede usar la media o mediana.
       - Moda: Para columnas categóricas, se puede usar la categoría más frecuente.
       - Forward Fill: Para datos de series temporales, rellenar con el valor anterior.
       - Regresión/KNN: Métodos más avanzados que usan otras variables para predecir.
    
    3. CREAR VARIABLE INDICADORA:
       - Crear una columna binaria que indique si el valor era nulo.
       - Luego imputar el valor con la media/mediana.
    
    4. ANÁLISIS POR SEPARADO:
       - Analizar separately los registros con y sin valores nulos.
       - Pueden representar un patrón importante.
    """)

# PREGUNTA 3: Transformar columnas datetime en una sola columna llamada tpep_duration?
print("\n" + "=" * 80)
print("PREGUNTA 3: ¿Convendría transformar tpep_pickup_datetime y tpep_dropoff_datetime")
print("            en una sola columna llamada tpep_duration?")
print("=" * 80)

# Convertir a datetime si no lo están
if df_parquet['tpep_pickup_datetime'].dtype == 'object':
    df_parquet['tpep_pickup_datetime'] = pd.to_datetime(df_parquet['tpep_pickup_datetime'])
if df_parquet['tpep_dropoff_datetime'].dtype == 'object':
    df_parquet['tpep_dropoff_datetime'] = pd.to_datetime(df_parquet['tpep_dropoff_datetime'])

# Crear columna de duración
df_parquet['tpep_duration'] = (df_parquet['tpep_dropoff_datetime'] - df_parquet['tpep_pickup_datetime']).dt.total_seconds() / 60

print("\n✓ SÍ, ES RECOMENDABLE crear la columna tpep_duration por las siguientes razones:")
print("""
VENTAJAS:
---------
1. REDUCCIÓN DE DIMENSIONALIDAD:
   - Convertir 2 columnas en 1 simplifica el dataset.
   - Menos variables = modelos más simples y eficientes.

2. INFORMACIÓN MÁS RELEVANTE:
   - La duración es más útil que dos timestamps separados para análisis.
   - Permite entender el comportamiento de viajes de forma directa.

3. CÁLCULOS MÁS FÁCILES:
   - Facilita análisis como "viajes cortos vs viajes largos".
   - Permite crear categorías (ej: viajes < 5 min, 5-15 min, > 15 min).

4. MEJOR PARA MODELOS:
   - Los modelos de ML típicamente necesitan la duración, no los timestamps.
   - Reduce la complejidad temporal del modelo.

ESTADÍSTICAS DE DURACIÓN (en minutos):
""")

print(f"  Media: {df_parquet['tpep_duration'].mean():.2f} min")
print(f"  Mediana: {df_parquet['tpep_duration'].median():.2f} min")
print(f"  Desv. Estándar: {df_parquet['tpep_duration'].std():.2f} min")
print(f"  Mínimo: {df_parquet['tpep_duration'].min():.2f} min")
print(f"  Máximo: {df_parquet['tpep_duration'].max():.2f} min")

# Visualizar distribución de duración
# fig, ax = plt.subplots(figsize=(12, 5))
# df_parquet['tpep_duration'].hist(bins=50, edgecolor='black', ax=ax, color='steelblue')
# ax.set_title('Distribución de Duración de Viajes (en minutos)', fontsize=14, fontweight='bold')
# ax.set_xlabel('Duración (minutos)')
# ax.set_ylabel('Frecuencia')
# plt.tight_layout()
# plt.savefig('duration_distribution.png', dpi=300, bbox_inches='tight')
# print("\n✓ Gráfico de distribución de duración guardado como 'duration_distribution.png'")
# plt.show()

# Guardar el dataframe actualizado con la nueva columna
# df_parquet.to_parquet('yellow_tripdata_2025-11_con_duration.parquet', index=False)
# print("✓ Dataset actualizado guardado como 'yellow_tripdata_2025-11_con_duration.parquet'")

print("\n" + "=" * 80)
print("ANÁLISIS COMPLETADO")
print("=" * 80)

