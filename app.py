from flask import Flask, render_template
import mysql.connector

# Crear una aplicación Flask
app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def mostrar_productos():
    # Conectar a la base de datos MySQL
    conexion = mysql.connector.connect(
    host="localhost",      # Servidor db
    user="root",           # Usuario db
    password="Elekna.24#.",  # Contraseña db
    database="mundofarma"  # Nombre db
)

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Consulta SQL para obtener los datos
    consulta_sql = " SELECT `ID_Producto`,`Nombre_Producto`,`Componente_Producto` FROM producto;"
    # consulta_sql = " SELECT `ID_Detalle`,`Precio`,`Fecha`,`Farmacia`,`Link`,`ID_Producto` FROM detalleproducto;"

    cursor.execute(consulta_sql)

    # Obtener todos los resultados de la consulta
    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template('MundoFarma.html', productos=resultados)

if __name__ == '__main__':
    app.run(debug=True)