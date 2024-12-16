import mysql.connector
from tkinter import messagebox
from mysql.connector import Error
import codigos.my_sql.add_mysql as add_mysql 
import codigos.my_sql.del_mysql as del_mysql
import codigos.my_sql.modificar_mysql as modificar_mysql
import codigos.my_sql.show_mysql as show_mysql
import codigos.my_sql.migrar_mysql_to_sqls as migrar_mysql_to_sqls
from playsound import *

class MySQLManager:
    def __init__(self):
        self.mydb = None

    def exit(self):
        if self.mydb:
            self.mydb.close()

    def conexion(self, user, password, database):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user=user,
                password=password,
                database=database,
                port="3306"
            )
            messagebox.showinfo("Conexion Mysql", "Conexion exitosa!")
        except Error as e:
            messagebox.showerror("Error", f"El Error es: \n{e}")

    def add(self):
        playsound("codigos/assets/Select.wav")
        add_mysql.add(self.mydb)

    def show(self):
        playsound("codigos/assets/Select.wav")
        show_mysql.show(self.mydb)

    def delete(self):
        playsound("codigos/assets/Select.wav")
        del_mysql.delete(self.mydb)

    def mod(self):
        playsound("codigos/assets/Select.wav")
        modificar_mysql.modify(self.mydb)

    def mysql_to_sqls(self):
        playsound("codigos/assets/Select.wav")
        migrar_mysql_to_sqls.migrar()

# Crear una instancia de la clase MySQLManager
db_manager = MySQLManager()



