from tkinter import *
from tkinter import messagebox
import mysql.connector
from codigos.my_sql.obtener_nombres_columnas import obtener_nombres_columnas

# Función para insertar un registro
def insertar_registro(entries, columnas, table_name, mydb, the_show):
    valores = [entry.get() for entry in entries.values()]
    columnas_str = ", ".join([f"`{columna}`" for columna in columnas] + ["`ModifiedDate`"])
    valores_placeholder = ", ".join(["%s" for _ in range(len(valores) + 1)])  # Placeholder for each value including ModifiedDate
    
    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT CURDATE()")
        current_date = cursor.fetchone()[0]  # Get the current date
        valores.append(current_date)
        query = f"INSERT INTO `{table_name}` ({columnas_str}) VALUES ({valores_placeholder})"
        cursor.execute(query, tuple(valores))
        mydb.commit()
        messagebox.showinfo("Éxito", "Registro añadido exitosamente")
        the_show.destroy()
    except Exception as ex:
        messagebox.showerror("ERROR", f"El error es: \n{ex}")

# Función para cancelar y cerrar la ventana
def cancelar(the_show):
    the_show.destroy()

# Función para mostrar la ventana y añadir un registro
def agregar(mydb, table_name):
    columnas = obtener_nombres_columnas(mydb, table_name)
    the_show = Toplevel()
    the_show.title(f"Añadir datos a {table_name}")
    the_show.iconbitmap("codigos/assets/BDICON.ico")
    entries = {}
    for i, columna in enumerate(columnas):
        label = Label(the_show, text=columna)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = Entry(the_show)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[columna] = entry

    boton_insertar = Button(the_show, text="Insertar", command=lambda: insertar_registro(entries, columnas, table_name, mydb, the_show))
    boton_insertar.grid(row=len(columnas), column=0, pady=10)
    boton_cancelar = Button(the_show, text="Cancelar", command=lambda: cancelar(the_show))
    boton_cancelar.grid(row=len(columnas), column=1, pady=10)

# Función para confirmar la selección de la tabla
def confirmacion(select_show, table_var, mydb):
    table_name = table_var.get()
    select_show.destroy()
    agregar(mydb, table_name)

# Función principal para añadir registro
def add(mydb):
    try:
        select_show = Toplevel()
        select_show.title("Seleccion de tabla")
        select_show.iconbitmap("codigos/assets/BDICON.ico")
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = DATABASE() AND TABLE_TYPE = 'BASE TABLE';")
        tables = [table[0] for table in mycursor.fetchall()]

        if not tables:
            messagebox.showerror("ERROR", "No hay tablas disponibles.")
            return

        table_var = StringVar()
        table_var.set(tables[0])  # Set default value

        for table in tables:
            Radiobutton(select_show, text=table, variable=table_var, value=table).pack(anchor=W)

        connfi = Button(select_show, text="Confirmar", command=lambda: confirmacion(select_show, table_var, mydb))
        connfi.pack()
    
    except Exception as ex:
        messagebox.showerror("ERROR", f"El error es: \n{ex}")
