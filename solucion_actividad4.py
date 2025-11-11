import pandas as pd
import numpy as np # Necesario para la mediana si fuera el caso, aunque fillna(0) es más directo aquí

# 1. SETUP: DataFrame Base
print("### SETUP Y DATASET BASE ###")
datos = {
    'nombre':   ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'edad':     [25, 30, 22, None, 28],
    'ciudad':   ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'producto': ['Laptop', 'Teléfono', 'Tablet', 'Laptop', 'Tablet'],
    'precio':   [1200, 800, 300, 1150, None],
    'stock':    [10, 15, 5, 8, 0]}

df = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'])
df.to_csv('actividad_semana4.csv', index=True)
print("DataFrame Base Creado (df):")
print(df)
print("-" * 50)

# --- 1) Series — crear y operar ---
print("### 1) SERIES ###")
# Crear Series
s_lista = pd.Series([100, 200, 300], name='Costos')
s_dict = pd.Series({'X': 1, 'Y': 2, 'Z': 3}, name='Coordenadas')

print(f"Series desde diccionario:\n{s_dict}")
print(f"Acceso por índice 'Y': {s_dict['Y']}")

s_lista[0] = 50 # Modificar
s_operacion = s_lista * 2
print(f"Series después de operación (* 2):\n{s_operacion}")
print("-" * 50)

# --- 2) DataFrame — crear y explorar ---
print("### 2) DATAFRAME - CREAR Y EXPLORAR ###")
# Creamos un DF con índice personalizado (ya hecho en el setup, lo mostramos)
df_exploracion = df.copy()

# Acceder a una columna
columna_producto = df_exploracion['producto']
print("Columna 'producto' (Series):\n", columna_producto)

# Acceder a fila por etiqueta ('b')
fila_loc = df_exploracion.loc['b']
print("\nFila con etiqueta 'b' (loc):\n", fila_loc)

# Acceder a fila por posición (índice 3)
fila_iloc = df_exploracion.iloc[3]
print("\nFila en posición 3 (iloc):\n", fila_iloc)
print("-" * 50)

# --- 3) Operaciones básicas ---
print("### 3) OPERACIONES BÁSICAS ###")
df_op = df.copy()

# 3.1 Agrega una columna derivada (precio_descuento = precio * 0.9)
df_op['precio_descuento'] = df_op['precio'] * 0.9
print("Columna 'precio_descuento' agregada:")
print(df_op[['precio', 'precio_descuento']])

# 3.2 Aplicar una operación vectorizada (Incrementar stock en 2)
df_op['stock_incrementado'] = df_op['stock'] + 2
print("\nColumna 'stock' incrementada en 2:")
print(df_op[['stock', 'stock_incrementado']])
print("-" * 50)

# --- 4) Manejo de datos faltantes ---
print("### 4) MANEJO DE FALTANTES ###")
df_nulos = df.copy()

# 4.1 Detecta nulos con isna y cuenta faltantes por columna
print("Conteo de valores faltantes (isna().sum()):")
print(df_nulos.isna().sum())

# 4.2 Completa faltantes
df_nulos['edad'] = df_nulos['edad'].fillna(0)
df_nulos['ciudad'] = df_nulos['ciudad'].fillna('Desconocido')
# Dejamos 'precio' como NaN para el Ejercicio 6, pero lo imprimimos
print("\nDataFrame después de rellenar 'edad' y 'ciudad':")
print(df_nulos)
print("-" * 50)

# --- 5) Selección y filtrado ---
print("### 5) SELECCIÓN Y FILTRADO ###")

# 5.1 Filtra filas con precio > 500
df_precio_alto = df[df['precio'] > 500]
print("Personas con precio > 500:")
print(df_precio_alto)

# 5.2 Filtra productos iguales a 'Laptop' Y stock mayor que 5
filtro_compuesto = (df['producto'] == 'Laptop') & (df['stock'] > 5)
df_laptop_stock = df[filtro_compuesto]
print("\nProductos 'Laptop' y stock > 5:")
print(df_laptop_stock)
print("-" * 50)

# --- 6) Ordenar datos ---
print("### 6) ORDENAR DATOS ###")

# 6.1 Ordena por edad ascendente (los NaN son colocados al final por defecto)
df_edad_ordenada = df.sort_values(by='edad', ascending=True)
print("DataFrame ordenado por 'edad' ascendente:")
print(df_edad_ordenada)

# 6.2 Ordena por precio descendente ignorando nulos (llena temporalmente nulos con 0 para ordenamiento)
# Creamos una columna temporal para el ordenamiento
df_temp_orden = df.copy()
df_temp_orden['precio_relleno'] = df_temp_orden['precio'].fillna(0)
df_precio_desc = df_temp_orden.sort_values(by='precio_relleno', ascending=False)
print("\nDataFrame ordenado por 'precio' descendente (NaN tratados como 0 para orden):")
print(df_precio_desc[['nombre', 'precio', 'precio_relleno']])
print("-" * 50)

# --- 7) Estadísticas básicas ---
print("### 7) ESTADÍSTICAS BÁSICAS ###")

# 7.1 Obtén describe() para columnas numéricas
print("Estadísticas descriptivas (describe()):")
print(df.describe())

# 7.2 Obtén value_counts() para la columna producto
print("\nConteo de valores (value_counts) para 'producto':")
print(df['producto'].value_counts())
print("-" * 50)

# --- 8) Leer y guardar datos ---
print("### 8) LEER Y GUARDAR DATOS ###")

# 8.1 Lee el CSV creado (actividad_semana4.csv)
df_leido = pd.read_csv('actividad_semana4.csv', index_col=0) # Usamos index_col=0 para leer el índice
print("CSV Leído (actividad_semana4.csv):\n", df_leido.head(2))

# 8.2 Guarda un nuevo CSV con columnas seleccionadas (nombre, producto, precio)
df_leido[['nombre', 'producto', 'precio']].to_csv('inventario_reducido.csv', index=False)
print("\nCSV 'inventario_reducido.csv' guardado.")
print("-" * 50)

# --- 9) Ejercicio integrado ---
print("### 9) EJERCICIO INTEGRADO (Final) ###")
df_final = df.copy()

# 1. Aplica descuento del 10% a precio
df_final['precio_descuento'] = df_final['precio'] * 0.9

# 2. Filtra productos con stock > 5
df_filtrado_final = df_final[df_final['stock'] > 5]

# 3. Ordena por precio_descuento descendente (NaN se maneja por defecto)
df_ordenado_final = df_filtrado_final.sort_values(by='precio_descuento', ascending=False)

# 4. Guarda como inventario_procesado.csv
df_ordenado_final.to_csv('inventario_procesado.csv', index=True)

print("Resultado final (Stock > 5, ordenado por descuento):")
print(df_ordenado_final)
print("El resultado se guardó en 'inventario_procesado.csv'.")