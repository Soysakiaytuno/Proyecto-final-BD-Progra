from tkinter import *
from tkinter import messagebox
import pyodbc
import mysql.connector
from codigos.sql_server.prueba_migracion import prueba_migracion


# Conexión a MySQL
def connect_to_mysql_without_database(host, user, password):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

def connect_to_mysql_with_database(host, database, user, password):
    return mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
