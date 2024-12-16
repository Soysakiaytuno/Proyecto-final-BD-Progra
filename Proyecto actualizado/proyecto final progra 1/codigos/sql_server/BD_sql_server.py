from tkinter import *
from tkinter import messagebox
import pyodbc
import codigos.sql_server.show_sqls as show_sqls
import codigos.sql_server.add_sqls as add_sqls
import codigos.sql_server.del_sqls as del_sqls
import codigos.sql_server.modificar_sqls as modificar_sqls
import codigos.sql_server.migrar_sqls_to_mysql as migrar_sqls_to_mysql
import codigos.sql_server.palindromo_sqls as palindromo_sqls
from playsound import *

class DatabaseManager:
    def __init__(self):
        self.mydb = None

    def exit(self):
        if self.mydb:
            self.mydb.close()


    def conection(self, server, driver, database):
        try:
            self.mydb = pyodbc.connect(f"Driver={driver};"
                                       f"Server={server};"
                                       f"Database={database};"
                                       "Trusted_Connection=yes;"
                                      )
            messagebox.showinfo("Conexion", "Se ha conectado exitosamente!")
        except Exception as ex:
            messagebox.showerror("ERROR", f"El error es: \n{ex}")

    def show(self):
        playsound("codigos/assets/Select.wav")
        show_sqls.show(self.mydb)

    def delete(self):
        playsound("codigos/assets/Select.wav")
        del_sqls.delete(self.mydb)

    def add(self):
        playsound("codigos/assets/Select.wav")
        add_sqls.add(self.mydb)

    def update(self):
        playsound("codigos/assets/Select.wav")
        modificar_sqls.modify(self.mydb)

    def sqls_to_mysql(self):
        playsound("codigos/assets/Select.wav")
        migrar_sqls_to_mysql.migrar(self)


    def palindromo(self):
        playsound("codigos/assets/Select.wav")
        palindromo_sqls.palindromo(self.mydb)

# Crear una instancia de la clase DatabaseManager
db_manager = DatabaseManager()


