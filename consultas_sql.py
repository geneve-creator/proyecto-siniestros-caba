import sqlite3
import pandas as pd

# 1. Conexión
conexion = sqlite3.connect('siniestros.db')

# 2. Escribimos nuestra primera consulta SQL con un JOIN
# Queremos unir los hechos con la dimensión de vehículos para ver los nombres reales
consulta = """
    SELECT 
        v.modo_desplazamiento_victima,
        COUNT(f.id_siniestro) as total_siniestros
    FROM fact_victimas f
    JOIN dim_vehiculos v ON f.id_vehiculo = v.id_vehiculo
    WHERE v.modo_desplazamiento_victima != 'sd'
    GROUP BY v.modo_desplazamiento_victima
    ORDER BY total_siniestros DESC
"""

# 3. Ejecutamos la consulta y la cargamos en un DataFrame de Pandas para verla prolija
resultado_sql = pd.read_sql_query(consulta, conexion)

print("--- Resultado de la Consulta SQL (JOIN) ---")
print(resultado_sql)

conexion.close()