import sqlite3

# Conectar a la base de datos (asegúrate de que tu base de datos SQLite3 exista en el mismo directorio o proporciona la ruta correcta)
conn = sqlite3.connect('tu_base_de_datos.db')
# Crear un cursor
cursor = conn.cursor()
# Ejecutar la consulta SQL
cursor.execute("SELECT name, pass FROM users")
# Recuperar los resultados
resultados = cursor.fetchall()
# Cerrar la conexión a la base de datos
conn.close()
# Procesar los resultados
for row in resultados:
    nombre = row[0]  # Obtener el valor de la columna 'name'
    contraseña = row[1]  # Obtener el valor de la columna 'pass'
    print(f"Nombre: {nombre}, Contraseña: {contraseña}")
