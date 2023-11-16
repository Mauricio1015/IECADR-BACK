from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Ruta de ejemplo para obtener datos
@app.route('/login', methods=['GET'])
def login():
    # Conectar a la base de datos (asegúrate de que tu base de datos SQLite3 exista en el mismo directorio o proporciona la ruta correcta)
    con = sqlite3.connect('iecadr.db')
    # Crear un cursor
    cursor = con.cursor()
    # Ejecutar la consulta SQL
    cursor.execute("SELECT name, pass FROM users")
    # Recuperar los resultados
    resultados = cursor.fetchall()
    # Cerrar la conexión a la base de datos
    con.close()
    # Procesar los resultados
    datos = []
    for row in resultados:
        nombre = row[0]  # Obtener el valor de la columna 'name'
        contraseña = row[1]  # Obtener el valor de la columna 'pass'
        datos.append({'name': nombre, 'pass': contraseña})
    
    return jsonify(datos)

@app.route('/datos')
def recibir_datos():
    # Obtén los parámetros de consulta de la URL
    parametro1 = request.args.get('parametro1')
    parametro2 = request.args.get('parametro2')

    # Haz algo con los datos recibidos
    resultado = f'Parámetro 1: {parametro1}, Parámetro 2: {parametro2}'
    return resultado

if __name__ == '__main__':
    app.run(debug=True)
