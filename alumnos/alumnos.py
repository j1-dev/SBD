import pandas as pd

df = pd.read_csv('alumnos.csv')
print(df.dtypes)

print("--Clase 1A (Slice)")
print(df[df['Clase']=='1A'].describe())

print("\n--Diferencias entre 1A y 1B en Matemáticas y Física durante los primeros días (Dice)")
print(df[(df['Clase'].isin(['1A','1B'])) & 
         (df['Asignatura'].isin(['Matemáticas','Física'])) & 
         (df['Fecha'].between('2026-01-05','2026-01-30'))].head())

print("\n--Rendimiento promedio de cada estudiante por asignatura (Drill-Down)")
print(df.groupby(['Estudiante','Asignatura'])['Nota'].mean())

print("\n--Promedio de notas por clase y asignatura durante toda la semana (Roll-up)")
print(df.groupby(['Clase','Asignatura'])['Nota'].mean())

print("\n--Reorganizar datos para comparar clases y asignaturas (Pivot)")
print(df.pivot_table(values='Nota', index='Asignatura', columns='Clase', aggfunc='mean'))