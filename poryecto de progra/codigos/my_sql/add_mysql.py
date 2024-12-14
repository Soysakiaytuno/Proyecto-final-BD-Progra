from tkinter import *
from tkinter import messagebox
import mysql.connector

def add(mydb):
    #mostrar opciones para escoger la tabla donde quieres agregar informacion 
    try:
        select_show = Toplevel()
        select_show.title("Seleccion de tabla")
        select_show.iconbitmap("codigos/assets/BDICON.ico")
    #confirmar que esa tabla queremos agregar datos
        def confirmacion():
            table_name = table_var.get()
            select_show.destroy()
            final_show(mydb, table_name)
    #obtener nombres de las tablas 
        mycursor = mydb.cursor()
        mycursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = DATABASE() AND TABLE_TYPE = 'BASE TABLE';")
    #agregar las tablas a una lista    
        tables = [table[0] for table in mycursor.fetchall()]

        if not tables:
            messagebox.showerror("ERROR", "No hay tablas disponibles.")
            return
    #Aqui se almacena la tabla seleccionada
        table_var = StringVar()
        table_var.set(tables[0])
    #Enlista todas las tablas para su seleccion
        for table in tables:
            Radiobutton(select_show, text=table, variable=table_var, value=table).pack(anchor=W)
    #Se crea un boton de confirmacion, para poder mandar la variable
        connfi = Button(select_show, text="Confirmar", command=confirmacion)
        connfi.pack()
    #Una vez seleccionada la tabla, ahora se obtiene las columnas de esta misma y se guardan en una lista
        def obtener_nombres_columnas(table_name):
            cursor = mydb.cursor()
            cursor.execute(f"""SELECT COLUMN_NAME 
                        FROM INFORMATION_SCHEMA.COLUMNS
                        WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = '{table_name}';
                        """)
            columnas = cursor.fetchall()
            nombres_columnas = [columna[0] for columna in columnas]
            return nombres_columnas
    #aqui se obtine la lista de columnas y se crea una nueva ventana
        def final_show(mydb, table_name):
            columnas = obtener_nombres_columnas(table_name)
            the_show = Toplevel()
            the_show.title(f"Añadir datos a {table_name}")
            the_show.iconbitmap("codigos/assets/BDICON.ico")
    #se crea un diccionario donde se guarda los valores agregados y posteriormente se muestra en un
            entries = {}
            for i, columna in enumerate(columnas):
                label = Label(the_show, text=columna)
                label.grid(row=i, column=0, padx=10, pady=5)
                entry = Entry(the_show)
                entry.grid(row=i, column=1, padx=10, pady=5)
                entries[columna] = entry
    #Se almacena las columnas y los valores en listas y se los vuelve en una string, con sus respectivas comas y espacios
            def insertar_registro():
                valores = [entry.get() for entry in entries.values()]
                columnas_str = ", ".join([f"`{columna}`" for columna in columnas])
                valores_str = ", ".join([f"{valor}" if valor.isdigit() else f"'{valor}'" for valor in valores])
    #se usa un query para agregar los valores obtenidos en el programa            
                try:
                    cursor = mydb.cursor()
                    cursor.execute(f"INSERT INTO `{table_name}` ({columnas_str}) VALUES ({valores_str})")
                    mydb.commit()
                    messagebox.showinfo("Éxito", "Registro añadido exitosamente")
                    the_show.destroy()
                except Exception as ex:
                    messagebox.showerror("ERROR", f"El error es: \n{ex}")
    #en caso de que no queramos agregar valores 
            def cancelar():
                the_show.destroy()
    #se crean los botones ya sea para confirmar la entrada de los valores en la tabla, o cancelar
            boton_insertar = Button(the_show, text="Insertar", command=insertar_registro)
            boton_insertar.grid(row=len(columnas), column=0, pady=10)
            boton_cancelar = Button(the_show, text="Cancelar", command=cancelar)
            boton_cancelar.grid(row=len(columnas), column=1, pady=10)

    except Exception as ex:
        messagebox.showerror("ERROR", f"El error es: \n{ex}")
