# test_connection.py
import mysql.connector
from mysql.connector import Error

def test_connection():
    try:
        # Conexión a la base de datos
        connection = mysql.connector.connect(
            host='localhost',
            database='familytree',
            user='root',
            password='admin'
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        else:
            print("Conexión fallida.")
    except Error as e:
        print("Error de conexión: ", e)
    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")

# Llamada a la función de prueba
test_connection()
