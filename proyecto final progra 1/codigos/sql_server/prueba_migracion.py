import pyodbc
import mysql.connector

def prueba_migracion(sql_server_conn, mysql_conn, table_name):
    sql_server_cursor = sql_server_conn.cursor()
    mysql_cursor = mysql_conn.cursor()

    sql_server_cursor.execute(f"SELECT COUNT(*) FROM [{table_name}]")
    sql_server_count = sql_server_cursor.fetchone()[0]

    mysql_cursor.execute(f"SELECT COUNT(*) FROM `{table_name}`")
    mysql_count = mysql_cursor.fetchone()[0]

    sql_server_cursor.close()
    mysql_cursor.close()

    return sql_server_count == mysql_count
