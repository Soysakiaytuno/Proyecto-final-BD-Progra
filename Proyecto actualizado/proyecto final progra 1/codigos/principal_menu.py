from tkinter import *
import codigos.sql_server.inicio_sesion_sqls as inicio_sesion_sqls
import codigos.my_sql.inicio_sesion_mysql as inicio_sesion_mysql
from playsound import playsound

#Hacemos una funcion que nos conencta con el SQL Server en la Computadora que se esta ejecutando el programa
def abrir_sqls(main_menu):
    playsound("codigos/assets/Select.wav")
    inicio_sesion_sqls.inicio_sesion(main_menu)
#Hacemos una funcion que nos conencta con MySQL en la Computadora que se esta ejecutando el programa
def abrir_mysql(main_menu):
    playsound("codigos/assets/Select.wav")
    inicio_sesion_mysql.inicio_sesion(main_menu)

#Creamos una ventana con dos votones uno para conectarse a SQL server y otro para conectarse con MySQL
def menu_inicio():
    #Creamos una ventana emergente en la cual trabajaremos
    main_menu = Tk()
    main_menu.title("Base de datos god")
    main_menu.iconbitmap("codigos/assets/BDICON.ico")
    main_menu.geometry("1280x720")
    main_menu.config(bg="#7BBECB")
    #Dentro de la ventana creada anterior mente ponemos el sigiente texto y archivos multimedia
    titulo = PhotoImage(file="codigos/assets/titulo.png")
    titulo_label = Label(main_menu, image=titulo)
    titulo_label.pack(side="top")
    titulo_label.config(cursor="hand2")

    #Aqui Creamos el boton el cual al ser presionado nos conecta con SQL Server
    sqls = Button(main_menu, text="SQL Server", font=("Arial", 30), width=10, height=2, command=lambda: abrir_sqls(main_menu))
    sqls.pack(side="top", padx=10, pady=50)
    sqls.config(cursor="hand2")
    #Aqui Creamos el boton el cual al ser presionado nos conecta con MySQL
    mysql = Button(main_menu, text="MySQL", font=("Arial", 30), width=10, height=2, command=lambda: abrir_mysql(main_menu))
    mysql.pack(side="top", padx=10, pady=10)
    mysql.config(cursor="hand2")

    main_menu.mainloop()

