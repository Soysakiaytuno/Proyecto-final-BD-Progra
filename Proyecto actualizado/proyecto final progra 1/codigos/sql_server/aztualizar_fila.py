from tkinter import *
from tkinter import messagebox
import pyodbc
from codigo.sql_server.obtener_nombres_columnas import obtener_nombres_columnas
from codigo.sql_server.obtener_registros_Modificar import obtener_registros

# Función para actualizar un registro
def actualizar_fila(var, entries, columnas, table_name, id_column, mydb, the_show):
    fila_id = var.get()
    if fila_id is not None:
        try:
            valores = [entries[col].get() for col in columnas]
            set_clause = ', '.join([f"[{col}] = ?" for col in columnas] + ["[ModifiedDate] = CAST(GETDATE() AS date)"])
            query = f"UPDATE {table_name} SET {set_clause} WHERE [{id_column}] = ?"
            valores.append(fila_id)
            cursor = mydb.cursor()
            cursor.execute(query, valores)
            mydb.commit()
            messagebox.showinfo("Éxito", "Registro actualizado exitosamente")
            the_show.destroy()
        except Exception as ex:
            messagebox.showerror("ERROR", f"El error es: \n{ex}")
    else:
        messagebox.showerror("ERROR", "Seleccione una fila para actualizar")
