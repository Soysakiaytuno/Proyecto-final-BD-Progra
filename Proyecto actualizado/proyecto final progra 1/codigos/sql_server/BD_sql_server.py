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
#Creamos una clase en la cual guardaremos losdatos necesarios para la coneccion con las distintas bases de datos
class DatabaseManager:
    def __init__(self):
        self.mydb = None

    def exit(self):
        if self.mydb:
            self.mydb.close()

    #En este Metodo guardamos la informacion para conectarse a SQL Server
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
    #Con este metood mostramos la base de datos seleccionada
    def show(self):
        playsound("codigos/assets/Select.wav")
        show_sqls.show(self.mydb)
    #Con este metodo eliminamos datos de la base de datos seleccionada
    def delete(self):
        playsound("codigos/assets/Select.wav")
        del_sqls.delete(self.mydb)
    #Con este metodo agregamos datos a la base de datos seleccionada
    def add(self):
        playsound("codigos/assets/Select.wav")
        add_sqls.add(self.mydb)
    #Con este metodo hacemos o modificamos diferentes datos dentro de la base de datos seleccionada
    def update(self):
        playsound("codigos/assets/Select.wav")
        modificar_sqls.modify(self.mydb)
    #Con este metood Migrmaos la base datos seleccionada dentro de SQL Server a  MySQL
    def sqls_to_mysql(self):
        playsound("codigos/assets/Select.wav")
        migrar_sqls_to_mysql.migrar(self)


    def palindromo(self):
        playsound("codigos/assets/Select.wav")
        palindromo_sqls.palindromo(self.mydb)

# Crear una instancia de la clase DatabaseManager
db_manager = DatabaseManager()


