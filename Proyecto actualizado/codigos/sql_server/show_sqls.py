from tkinter import *
from tkinter import messagebox
import pyodbc

def confirmacion(select_show, table_var, mydb):
    table_name = table_var.get()
    select_show.destroy()
    final_show(mydb, table_name)

def final_show(mydb, table_name):
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM {table_name};")
    records = mycursor.fetchall()
    the_show = Toplevel()
    the_show.title("Base de datos god")
    the_show.iconbitmap("codigos/assets/BDICON.ico")
    
    mycursor.execute(f"""SELECT COLUMN_NAME 
                        FROM INFORMATION_SCHEMA.COLUMNS
                        WHERE TABLE_NAME = '{table_name}';
                        """)
    columns = [col[0] for col in mycursor.fetchall()]
    columnas = Label(the_show, text=', '.join(columns))
    columnas.pack()
    
    for record in records:
        datos = Label(the_show, text=record)
        datos.pack()

def show(mydb): 
    try:
        select_show = Toplevel()
        select_show.title("Base de datos god")
        select_show.iconbitmap("codigos/assets/BDICON.ico")
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
        tables = [table[0] for table in mycursor.fetchall() if 'sysdiagrams' not in table[0].lower()]
        
        if not tables:
            messagebox.showerror("ERROR", "No hay tablas disponibles.")
            return
        
        table_var = StringVar()
        table_var.set(tables[0])  # Set default value
        
        for table in tables:
            Radiobutton(select_show, text=table, variable=table_var, value=table).pack(anchor=W)
        
        connfirmar = Button(select_show, text="Confirmar", command=lambda: confirmacion(select_show, table_var, mydb))
        connfirmar.pack()
    
    except Exception as ex:
        messagebox.showerror("ERROR", f"El error es: \n{ex}")