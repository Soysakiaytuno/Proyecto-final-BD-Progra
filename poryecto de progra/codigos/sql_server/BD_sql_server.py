from tkinter import *
from tkinter import messagebox
import pyodbc
import codigos.sql_server.show_sqls as show_sqls
import codigos.sql_server.add_sqls as add_sqls
import codigos.sql_server.del_sqls as del_sqls
import codigos.sql_server.modificar_sqls as modificar_sqls
import codigos.sql_server.migrar_sqls_to_mysql as migrar_sqls_to_mysql
from playsound import *
# 1. Crear conexion SQL Server
def exit():
    mydb.close()
mydb = None
def conection(server, driver, database): 
    try:
        global mydb
        mydb = pyodbc.connect(f"Driver={driver};"
        f"Server={server};"
        f"Database={database};"
        "Trusted_Connection=yes;"
        )
        messagebox.showinfo("Conexion", "Se ha conectado exitosamente!")
    except Exception as ex:
        messagebox.showerror("ERROR", f"El error es: \n{ex}")

def show():
    playsound("codigos/assets/Select.wav")
    show_sqls.show(mydb)
def delete():
    playsound("codigos/assets/Select.wav")
    del_sqls.delete(mydb)
def add():
    playsound("codigos/assets/Select.wav")
    add_sqls.add(mydb)
def update():
    playsound("codigos/assets/Select.wav")
    modificar_sqls.modify(mydb)
def sqls_to_mysql():
    playsound("codigos/assets/Select.wav")
    migrar_sqls_to_mysql.migrar()  
