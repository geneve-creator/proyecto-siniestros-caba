import pandas as pd

#Archivo CSV en la memoria
df = pd.read_csv('siniestros_viales_victimas.csv', sep=';', low_memory=False)
df.columns = df.columns.str.lower().str.replace(' ', '_')

#Limpieza de columnas de texto
df['sexo_victima'] = df['sexo_victima'].str.lower().str.strip()
df['modo_desplazamiento_victima'] = df['modo_desplazamiento_victima'].str.lower().str.strip()
df['rol_victima'] = df['rol_victima'].str.lower().str.strip()
df['gravedad_victima'] = df['gravedad_victima'].str.lower().str.strip()
df['edad_victima'] = pd.to_numeric(df['edad_victima'], errors='coerce')

#Limpieza datetime
df['fecha_siniestro'] = pd.to_datetime(df['fecha_siniestro'])
df['fecha_fallecimiento_victima'] = pd.to_datetime(df['fecha_fallecimiento_victima'], errors='coerce')

print("--- Tipos de datos de cada columna ---")
print(df.dtypes)

#Guardado
df.to_csv('siniestros_limpio.csv', index=False)

print("¡Archivo limpio guardado exitosamente como 'siniestros_limpio.csv'!")