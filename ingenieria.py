import pandas as pd
import sqlite3

# 1. Cargamos el archivo limpio evitando la advertencia de tipos mixtos
df = pd.read_csv('siniestros_limpio.csv', low_memory=False)

# Creamos la conexión a la base de datos SQLite
conexion = sqlite3.connect('siniestros.db')

# 2. Creamos y guardamos la Tabla Dimensión de Vehículos
dim_vehiculos = df[['modo_desplazamiento_victima']].drop_duplicates().reset_index(drop=True)
dim_vehiculos['id_vehiculo'] = dim_vehiculos.index + 1
dim_vehiculos.to_sql('dim_vehiculos', conexion, if_exists='replace', index=False)

# ¡NUEVO! Exportamos la dimensión a CSV para Power BI
dim_vehiculos.to_csv('dim_vehiculos.csv', index=False)
print("--- Tabla 'dim_vehiculos' creada en SQLite y exportada a CSV ---")

# 3. Armamos la Tabla de Hechos (Fact Table)
df_con_id = df.merge(dim_vehiculos, on='modo_desplazamiento_victima', how='left')

fact_victimas = df_con_id[[
    'id_siniestro', 
    'fecha_siniestro', 
    'anio_siniestro', 
    'id_vehiculo', 
    'sexo_victima', 
    'edad_victima', 
    'gravedad_victima', 
    'rol_victima', 
    'fecha_fallecimiento_victima'
]]

# 4. Guardamos la Tabla de Hechos en SQLite
fact_victimas.to_sql('fact_victimas', conexion, if_exists='replace', index=False)

# ¡NUEVO! Exportamos los hechos a CSV para Power BI
fact_victimas.to_csv('fact_victimas.csv', index=False)
print("--- Tabla 'fact_victimas' creada en SQLite y exportada a CSV ---")

print("\n¡Ingeniería completa! Base de datos y archivos CSV listos para Power BI.")