import pandas as pd

# 1. Carga del archivo limpio
df = pd.read_csv('siniestros_limpio.csv')

# Preprocesamiento general: filtrar valores "sd" y crear columna de fatalidad
df_analisis = df[df['modo_desplazamiento_victima'] != 'sd'].copy()
df_analisis['fecha_siniestro'] = pd.to_datetime(df_analisis['fecha_siniestro'])
df_analisis['fue_fatal'] = df_analisis['fecha_fallecimiento_victima'].notna()


# --- 2. ANÁLISIS POR MODO DE DESPLAZAMIENTO ---
print("--- Conteo real de víctimas por modo de desplazamiento (Sin 'sd') ---")
print(df_analisis['modo_desplazamiento_victima'].value_counts())

fatalidad_por_modo = (
    df_analisis.groupby('modo_desplazamiento_victima')['fue_fatal']
    .agg(['count', 'sum', 'mean'])
)
fatalidad_por_modo.columns = ['total_siniestros', 'total_fatales', 'tasa_letalidad']
fatalidad_por_modo = fatalidad_por_modo.sort_values(by='tasa_letalidad', ascending=False)

print("\n--- Análisis de Letalidad por Modo de Desplazamiento ---")
print(fatalidad_por_modo)


# --- 3. ANÁLISIS POR RANGO DE EDAD ---
bins = [0, 18, 30, 50, 65, 120]
labels = ['Menores de 18', '18-30', '31-50', '51-65', 'Más de 65']

df_analisis['rango_edad'] = pd.cut(df_analisis['edad_victima'], bins=bins, labels=labels)

edad_fatalidad = (
    df_analisis.groupby('rango_edad', observed=False)['fue_fatal']
    .agg(['count', 'sum', 'mean'])
)
edad_fatalidad.columns = ['total_siniestros', 'total_fatales', 'tasa_letalidad']
edad_fatalidad = edad_fatalidad.sort_values(by='tasa_letalidad', ascending=False)

print("\n--- Análisis de Siniestros y Letalidad por Rango de Edad ---")
print(edad_fatalidad)


# --- 4. ANÁLISIS POR DÍA DE LA SEMANA ---
df_analisis['dia_semana'] = df_analisis['fecha_siniestro'].dt.day_name()

analisis_dias = (
    df_analisis.groupby('dia_semana')['fue_fatal']
    .agg(['count', 'sum', 'mean'])
)
analisis_dias.columns = ['total_siniestros', 'total_fatales', 'tasa_letalidad']

print("\n--- Análisis de Siniestros por Día de la Semana ---")
print(analisis_dias)


# --- 5. ANÁLISIS POR MES ---
df_analisis['mes'] = df_analisis['fecha_siniestro'].dt.month_name()

analisis_meses = (
    df_analisis.groupby('mes')['fue_fatal']
    .agg(['count', 'sum', 'mean'])
)
analisis_meses.columns = ['total_siniestros', 'total_fatales', 'tasa_letalidad']

print("\n--- Análisis de Siniestros por Mes ---")
print(analisis_meses)