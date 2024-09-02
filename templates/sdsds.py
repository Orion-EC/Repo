import mysql.connector

from mysql.connector import Error

try:
    # Conectar a la base de datos MySQL
    connection = mysql.connector.connect(
        host='localhost',          # Cambia por la dirección de tu servidor MySQL
        database='mundofarma',      # Nombre de la base de datos a la que deseas conectar
        user='root',         # Tu usuario de MySQL
        password='Elekna.24#'   # La contraseña de tu usuario de MySQL
    )

    if connection.is_connected():
        print('Conexión exitosa a la base de datos MySQL')
        # Puedes ejecutar tus consultas aquí

except Error as e:
    print(f"Error al conectar con MySQL: {e}")

finally:
    # Cerrar la conexión si fue establecida
    if connection.is_connected():
        connection.close()
        print('Conexión MySQL cerrada')