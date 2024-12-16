from tkinter import *
from tkinter import messagebox
import pyodbc
from codigo.sql_server.obtener_nombres_columnas import obtener_nombres_columnas

# Función para obtener registros de la tabla, excluyendo ModifiedDate
def obtener_registros(mydb, table_name):
    cursor = mydb.cursor()
    #Guardamos el nombre de las columans obtenidos con la funcion "obtener_nombres_columnas" dentro de una variable vacia
    columnas = obtener_nombres_columnas(mydb, table_name)
    columnas_str = ', '.join([f"[{columna}]" for columna in columnas])
    cursor.execute(f"SELECT {columnas_str} FROM {table_name};")
    #Obtenemos los datos de la tabla selecionada y los guardamos en una variable
    registros = cursor.fetchall()
    return registros, columnas