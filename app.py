from flask import Flask, render_template
import mysql.connector
import sqlalchemy
from google.cloud.sql.connector import Connector
import pymysql

# Crear una aplicación Flask
app = Flask(__name__)

# Configura la conexión a Cloud SQL
def get_connection():
    instance_connection_name = "mundofarma:us-central1:sqlmundofarma"
    
    # Usuario, contraseña y nombre de la base de datos en Cloud SQL
    db_user = "root"
    db_pass = "Elekna.24#"
    db_name = "mundofarma"

    # Crea un conector de Cloud SQL
    connector = Connector()

    # Devuelve una conexión a la base de datos usando PyMySQL
    connection = connector.connect(
        instance_connection_name,
        "pymysql",
        user=db_user,
        password=db_pass,
        db=db_name
    )
    return connection

# Ruta para la página principal
@app.route('/')
def mostrar_productos():
    # Obtener una conexión a la base de datos
    connection = get_connection()

    # Crear un cursor para ejecutar consultas
    cursor = connection.cursor()

    # Consulta SQL para obtener los datos
    consulta_sql = "SELECT `ID_Producto`, `Nombre_Producto`, `Componente_Producto` FROM producto;"

    cursor.execute(consulta_sql)

    # Obtener todos los resultados de la consulta
    resultados = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('MundoFarma.html', productos=resultados)

if __name__ == '__main__':
    app.run(debug=True)