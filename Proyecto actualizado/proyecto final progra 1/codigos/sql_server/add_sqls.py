from tkinter import *
from tkinter import messagebox
import pyodbc
from codigos.sql_server.obtener_nombres_columnas import obtener_nombres_columnas

# Función para insertar un registro
def insertar_registro(entries, columnas, table_name, mydb, the_show):
    #Guardamos los datos introducidos por el usuario en una variable
    valores = [entry.get() for entry in entries.values()]
    #Guardamos en una variable los nombre de las columnas mas la columna de la fecha de modificacion
    columnas_str = ", ".join([f"[{columna}]" for columna in columnas] + ["[ModifiedDate]"])
    valores_placeholder = ", ".join(["?" for _ in range(len(valores) + 1)])  # Placeholder for each value including ModifiedDate
    #Utilizamos el try para en caso de tener un error parar la ejecucion y mostrar un ventana emergente que informe al ususario del error
    try:
        cursor = mydb.cursor()
        #Por medio del cursor ejecutamos un quary que insert aen la tabla los valores nuevos junto al de la fecha de modificacion 
        query = f"INSERT INTO {table_name} ({columnas_str}) VALUES ({valores_placeholder})"
        valores.append(cursor.execute("SELECT CAST(GETDATE() AS date)").fetchval())  # Add current date to values
        cursor.execute(query, valores)
        #Por medio del cursor le confirmamos de los cambios a la base de datos para que los realize
        mydb.commit()
        #Abrimos una ventana emergente que informa del ejecucion exitosa de la operacion
        messagebox.showinfo("Éxito", "Registro añadido exitosamente")
        #Cerramos la ventana en la cual la operacion se estaba realizando
        the_show.destroy()
    except Exception as ex:
        messagebox.showerror("ERROR", f"El error es: \n{ex}")

# Función para cancelar y cerrar la ventana
def cancelar(the_show):
    the_show.destroy()

# Función para mostrar la ventana y añadir un registro
def añadiendo(mydb, table_name):
    #Obtenemos los nombre de las columnas y lo guardamos dentro una variable
    columnas = obtener_nombres_columnas(mydb, table_name)
    #Creamos una ventana emergente en la cual mostramos donde introducir los datos
    the_show = Toplevel()
    the_show.title(f"Añadir datos a {table_name}")
    the_show.iconbitmap("codigos/assets/BDICON.ico")
    entries = {}
    #Dentro de la anterior ventana creamos cuadrado de texto en la cual el usuario pode poder los datos que quierre introducir a la base de datos
    for i, columna in enumerate(columnas):
        label = Label(the_show, text=columna)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = Entry(the_show)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[columna] = entry
    #Creamos dos botones para cancelar o confirmar la operacion
    boton_insertar = Button(the_show, text="Insertar", command=lambda: insertar_registro(entries, columnas, table_name, mydb, the_show))
    boton_insertar.grid(row=len(columnas), column=0, pady=10)
    boton_cancelar = Button(the_show, text="Cancelar", command=lambda: cancelar(the_show))
    boton_cancelar.grid(row=len(columnas), column=1, pady=10)

# Función para confirmar la selección de la tabla
def confirmacion(select_show, table_var, mydb):
    table_name = table_var.get()
    select_show.destroy()
    añadiendo(mydb, table_name)

# Función principal para añadir registro
def add(mydb): 
    #Utilizamos el try para en caso de tener un error parar la ejecucion y mostrar un ventana emergente que informe al ususario del error
    try:
        #Creamos una ventana emergente en la cual trabajar
        select_show = Toplevel()
        select_show.title("Base de datos god")
        select_show.iconbitmap("codigos/assets/BDICON.ico")
        #Por medio del cursor ejecutamos un quary para obtenenr el nombre de las tablas de la base de datos seleccionada
        mycursor = mydb.cursor()
        mycursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
        tables = [table[0] for table in mycursor.fetchall() if 'sysdiagram' not in table[0].lower()]
        #Creamso una condicional que pararia el programa en caso de que no se encuentren tablas dentro de la base de datos selccionada
        if not tables:
            messagebox.showerror("ERROR", "No hay tablas disponibles que no sean sysdiagrams.")
            return
        
        table_var = StringVar()
        table_var.set(tables[0])  # Set default value
        #Mostramos en la venta los nombre de la tabla a selecionar junto a un boton para elegir a lado del nombre
        for table in tables:
            Radiobutton(select_show, text=table, variable=table_var, value=table).pack(anchor=W)
        #Creamos un boton para confirmar la selecion de la tabla
        connfi = Button(select_show, text="Confirmar", command=lambda: confirmacion(select_show, table_var, mydb))
        connfi.pack()
    
    except Exception as ex:
        messagebox.showerror("ERROR", f"El error es: \n{ex}")
