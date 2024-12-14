from tkinter import *
import codigos.sql_server.inicio_sesion_sqls as inicio_sesion_sqls
import codigos.my_sql.inicio_sesion_mysql as inicio_sesion_mysql
from playsound import playsound


#abrir el inicio de sesion
def abrir_sqls(main_menu):
    playsound("codigos/assets/Select.wav")
    inicio_sesion_sqls.inicio_sesion(main_menu)

def abrir_mysql(main_menu):
    playsound("codigos/assets/Select.wav")
    inicio_sesion_mysql.inicio_sesion(main_menu)

#inicio menu
def menu_inicio():
    main_menu = Tk()
    main_menu.title("Base de datos god")
    main_menu.iconbitmap("codigos/assets/BDICON.ico")
    main_menu.geometry("1280x720")
    main_menu.config(bg="#7BBECB")
    
    titulo = PhotoImage(file="codigos/assets/titulo.png")
    titulo_label = Label(main_menu, image=titulo)
    titulo_label.pack(side="top")
    titulo_label.config(cursor="hand2")


    sqls = Button(main_menu, text="SQL Server", font=("Arial", 30), width=10, height=2, command=lambda: abrir_sqls(main_menu))
    sqls.pack(side="top", padx=10, pady=50)
    sqls.config(cursor="hand2")

    mysql = Button(main_menu, text="MySQL", font=("Arial", 30), width=10, height=2, command=lambda: abrir_mysql(main_menu))
    mysql.pack(side="top", padx=10, pady=10)
    mysql.config(cursor="hand2")

    main_menu.mainloop()

