from flask import Flask, render_template
import sqlalchemy, pymysql, os
from google.cloud.sql.connector import Connector


# Crear una aplicación Flask
app = Flask(__name__)

# Configuración de conexión a Cloud SQL
def get_connection():
    instance_connection_name = os.getenv("INSTANCE_CONNECTION_NAME")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME")

    # Crear conector de Cloud SQL
    connector = Connector()

    # Retornar la conexión a la base de datos
    connection = connector.connect(
        instance_connection_name,
        "pymysql",
        user=db_user,
        password=db_pass,
        db=db_name
    )
    return connection

@app.route('/')
def mostrar_productos():
    connection = get_connection()
    cursor = connection.cursor()
    consulta_sql = "SELECT `ID_Producto`, `Nombre_Producto`, `Componente_Producto` FROM producto;"
    cursor.execute(consulta_sql)
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('MundoFarma.html', productos=resultados)

if __name__ == '__main__':
    app.run(debug=True)