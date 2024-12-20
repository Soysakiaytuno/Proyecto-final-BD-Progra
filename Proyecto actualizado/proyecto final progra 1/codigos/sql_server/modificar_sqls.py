from tkinter import *
from tkinter import messagebox
import pyodbc
from codigo.sql_server.obtener_nombres_columnas import obtener_nombres_columnas
from codigo.sql_server.obtener_registros_Modificar import obtener_registros
from codigo.sql_server.actualizar_fila import actualizar_fila
from codigo.sql_server.conectar_mysql import *
# Función para mostrar detalles en Entry widgets
def mostrar_detalles(record, columnas, entries, scrollable_frame, records):
    for i, col in enumerate(columnas, start=1):
        if col not in entries:
            label = Label(scrollable_frame, text=col)
            label.grid(row=len(records) + i, column=0, padx=10, pady=5)
            entry = Entry(scrollable_frame)
            entry.grid(row=len(records) + i, column=1, padx=10, pady=5)
            entries[col] = entry
        entries[col].delete(0, END)
        entries[col].insert(0, record[i-1])

# Función para mostrar la ventana y actualizar un registro
def modificar(mydb, table_name):
    records, columnas = obtener_registros(mydb, table_name)
    
    # Asumimos que la primera columna es el identificador
    id_column = columnas[0]

    the_show = Toplevel()
    the_show.title(f"Actualizar datos de {table_name}")
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
    Label(scrollable_frame, text=encabezado, font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, padx=10, pady=5)
    
    # Mostrar registros con Radiobutton para seleccionar la fila a actualizar
    var = IntVar()
    entries = {}

    for i, record in enumerate(records, start=1):
        Radiobutton(scrollable_frame, text=record, variable=var, value=record[0], command=lambda r=record: mostrar_detalles(r, columnas, entries, scrollable_frame, records)).grid(row=i, column=0, padx=10, pady=5)

    # Botón para confirmar la actualización
    Button(scrollable_frame, text="Actualizar", command=lambda: actualizar_fila(var, entries, columnas, table_name, id_column, mydb, the_show)).grid(row=len(records)+len(columnas)+1, column=0, padx=10, pady=10)
    Button(scrollable_frame, text="Cancelar", command=the_show.destroy).grid(row=len(records)+len(columnas)+1, column=1, padx=10, pady=10)

def confirmacion(select_show, table_var, mydb):
    table_name = table_var.get()
    select_show.destroy()
    modificar(mydb, table_name)

# Función principal para modificar registro
def modify(mydb): 
    try:
        select_show = Toplevel()
        select_show.title("Base de datos god")
        select_show.iconbitmap("codigos/assets/BDICON.ico")
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_NAME != 'sysdiagrams';")
        tables = [table[0] for table in mycursor.fetchall()]

        if not tables:
            messagebox.showerror("ERROR", "No hay tablas disponibles.")
            return

        table_var = StringVar()
        table_var.set(tables[0])  # Set default value

        for table in tables:
            Radiobutton(select_show, text=table, variable=table_var, value=table).pack(anchor=W)
        
        Button(select_show, text="Confirmar", command=lambda: confirmacion(select_show, table_var, mydb)).pack()
    
    except Exception as ex:
        messagebox.showerror("ERROR", f"El error es: \n{ex}")
