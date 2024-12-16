from tkinter import *
from tkinter import messagebox
import mysql.connector
from codigos.my_sql.obtener_nombres_columnas import obtener_nombres_columnas

# Función para eliminar un registro
def eliminar_fila(var, table_name, id_column, mydb, the_show):
    fila_id = var.get()
    if fila_id is not None:
        try:
            cursor = mydb.cursor()
            query = f"DELETE FROM `{table_name}` WHERE `{id_column}` = %s"
            cursor.execute(query, (fila_id,))
            mydb.commit()
            messagebox.showinfo("Éxito", "Registro eliminado exitosamente")
            the_show.destroy()
        except Exception as ex:
            messagebox.showerror("ERROR", f"El error es: \n{ex}")
    else:
        messagebox.showerror("ERROR", "Seleccione una fila para eliminar")

# Función para mostrar la ventana y eliminar un registro
def eliminar(mydb, table_name):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM `{table_name}`;")
    records = cursor.fetchall()
    columnas = obtener_nombres_columnas(mydb, table_name)
    
    # Asumimos que la primera columna es el identificador
    id_column = columnas[0]

    the_show = Toplevel()
    the_show.title(f"Eliminar datos de {table_name}")
    the_show.iconbitmap("codigos/assets/BDICON.ico")
    
    # Se crea una barra de scroll y se la asocia con el canvas para que pueda estar en toda la pantalla
    canvas = Canvas(the_show)
    scrollbar = Scrollbar(the_show, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)
    
    # Se configura la barra de scroll para que utilice toda la pantalla
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
    
    # Mostrar los datos para poder seleccionarlos
    encabezado = ', '.join(columnas)
    Label(scrollable_frame, text=encabezado, font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
    
    # Mostrar registros con Radiobutton para seleccionar la fila a eliminar
    var = IntVar()
    for i, record in enumerate(records, start=1):
        Radiobutton(scrollable_frame, text=', '.join(map(str, record)), variable=var, value=record[0]).grid(row=i, column=0, pady=5)
    
    # Botón para confirmar la eliminación
    Button(scrollable_frame, text="Eliminar", command=lambda: eliminar_fila(var, table_name, id_column, mydb, the_show)).grid(row=len(records)+1, column=0, pady=10)
    Button(scrollable_frame, text="Cancelar", command=the_show.destroy).grid(row=len(records)+1, column=1, ipadx=55, pady=10)

# Función para confirmar la selección de la tabla
def confirmacion(select_show, table_var, mydb):
    table_name = table_var.get()
    select_show.destroy()
    eliminar(mydb, table_name)

# Función principal para eliminar registro
def delete(mydb): 
    try:
        select_show = Toplevel()
        select_show.title("Base de datos god")
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
        
        Button(select_show, text="Confirmar", command=lambda: confirmacion(select_show, table_var, mydb)).pack()
    
    except Exception as ex:
        messagebox.showerror("ERROR", f"El error es: \n{ex}")
