import mysql.connector
# Función para obtener nombres de columnas de la tabla, excluyendo ModifiedDate
def obtener_nombres_columnas(mydb, table_name):
    cursor = mydb.cursor()
    cursor.execute(f"""
        SELECT COLUMN_NAME 
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = '{table_name}' AND COLUMN_NAME != 'ModifiedDate';
    """)
    columnas = cursor.fetchall()
    nombres_columnas = [columna[0] for columna in columnas]
    return nombres_columnas