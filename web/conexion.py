import mysql.connector
import os
import time

# Obtener variables de entorno
db_host = os.getenv('DATABASE_HOST', 'db')
db_user = os.getenv('DATABASE_USER', 'user')
db_password = os.getenv('DATABASE_PASSWORD', 'userpassword')
db_name = os.getenv('DATABASE_NAME', 'mydatabase')

# Intentar conectarse a la base de datos con reintentos
for attempt in range(5):
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            break
    except mysql.connector.Error as err:
        print(f"Intento {attempt + 1}: No se pudo conectar a la base de datos. Error: {err}")
        time.sleep(5)  # Esperar 5 segundos antes de reintentar
else:
    print("Error: No se pudo establecer la conexión después de varios intentos")

# Cerrar la conexión si está abierta
if connection.is_connected():
    connection.close()
    print("Conexión cerrada")