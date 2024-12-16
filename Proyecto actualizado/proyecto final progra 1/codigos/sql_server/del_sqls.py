from tkinter import *
from tkinter import messagebox
import pyodbc
from codigos.sql_server.obtener_nombres_columnas import obtener_nombres_columnas

# Función para eliminar un registro
def eliminar_fila(var, table_name, id_column, mydb, the_show):
    #Guardamos en una variable la id proporcionada por el Usuario de la linea de datos a borrar
    fila_id = var.get()
    #creamos una condicional la cual en caso de no encontrar la id dada por el usuario pare le programa
    if fila_id is not None:
        #Utilizamos el try para en caso de tener un error parar la ejecucion y mostrar un ventana emergente que informe al ususario del error
        try:
            cursor = mydb.cursor()
            #Por medio del cursor ejecutamos un quary que elimine los datos de la linea del id proveido por el usuario
            query = f"DELETE FROM {table_name} WHERE [{id_column}] = ?"
            cursor.execute(query, fila_id)
            #Por medio del cursor le confirmamos de los cambios a la base de datos para que los realize
            mydb.commit()
            #Abrimos una ventana emergente que informa del ejecucion exitosa de la operacion
            messagebox.showinfo("Éxito", "Registro eliminado exitosamente")
            #Cerramos la ventana en la cual la operacion se estaba realizando
            the_show.destroy()
        except Exception as ex:
            messagebox.showerror("ERROR", f"El error es: \n{ex}")
    else:
        messagebox.showerror("ERROR", "Seleccione una fila para eliminar")

# Función para mostrar la ventana y eliminar un registro
def eliminacion(mydb, table_name):
    cursor = mydb.cursor()
    #Utilizando el cursor ejecutamos un quary para obtener los datos de la tabla selecionada y los guardamos en una variable
    cursor.execute(f"SELECT * FROM {table_name};")
    records = cursor.fetchall()
    #Creamos una variable en la cual guardamos el nombre de las columnas de la tabla seleccionada
    columnas = obtener_nombres_columnas(mydb, table_name)
    
    # Asumimos que la primera columna es el identificador
    id_column = columnas[0]
     #Creamos una ventana emergente en la cual mostramos los datos a eliminar
    the_show = Toplevel()
    the_show.title(f"Eliminar datos de {table_name}")
    the_show.iconbitmap("codigos/assets/BDICON.ico")
    
    # Crear Canvas y Scrollbar
    canvas = Canvas(the_show)
    scrollbar = Scrollbar(the_show, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Colocar el Canvas y la Scrollbar en la ventana
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Mostrar columnas como encabezado
    encabezado = ', '.join(columnas)
    Label(scrollable_frame, text=encabezado, font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
    
    # Mostrar registros con Radiobutton para seleccionar la fila a eliminar
    var = IntVar()
    for i, record in enumerate(records, start=1):
        Radiobutton(scrollable_frame, text=record, variable=var, value=record[0]).grid(row=i, column=0, pady=5)
    
    # Botón para confirmar la eliminación
    Button(scrollable_frame, text="Eliminar", command=lambda: eliminar_fila(var, table_name, id_column, mydb, the_show)).grid(row=len(records)+1, column=0, pady=10)
    Button(scrollable_frame, text="Cancelar", command=the_show.destroy).grid(row=len(records)+1, column=1, ipadx=55, pady=10)

# Función para confirmar la selección de la tabla
def confirmacion(select_show, table_var, mydb):
    table_name = table_var.get()
    select_show.destroy()
    eliminacion(mydb, table_name)

# Función principal para eliminar registro
def delete(mydb): 
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
        Button(select_show, text="Confirmar", command=lambda: confirmacion(select_show, table_var, mydb)).pack()
        
    except Exception as ex:
        messagebox.showerror("ERROR", f"El error es: \n{ex}")
