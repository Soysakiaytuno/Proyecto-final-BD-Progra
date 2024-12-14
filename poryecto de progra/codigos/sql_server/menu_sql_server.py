from tkinter import *
import codigos.sql_server.BD_sql_server as BD_sql_server 
import codigos.musica as musica
def sqls():
    main = Tk()
    musica.music("codigos/assets/sqlserver.ogg")
    main.title("Base de datos god")
    main.iconbitmap("codigos/assets/BDICON.ico")
    main.geometry("1280x720")
    main.config(bg="#F18A69")
    agregar = Button(main, text="Agregar", font=("Arial", 30), width=0, height=2, command=BD_sql_server.add)
    agregar.grid(row="0",column="0", padx=150, pady=50)
    modificar = Button(main, text="Modificar", font=("Arial", 30), width=0, height=2, command=BD_sql_server.update)
    modificar.grid(row="0",column="2", padx=100, pady=50)
    migrar = Button(main, text="Migrar a Mysql", font=("Arial", 30), width=0, height=2, command=BD_sql_server.sqls_to_mysql)
    migrar.grid(row="1",column="1", padx="0")
    eliminar = Button(main,text="Eliminar", font=("Arial", 30), width=0, height=2, command=BD_sql_server.delete)
    eliminar.grid(row="2",column="0", padx=110, pady=100)
    mostrar = Button(main, text="Mostrar", font=("Arial", 30), width=0, height=2, command=BD_sql_server.show)
    mostrar.grid(row="2",column="2", padx=110, pady=50)
    main.mainloop()
    musica.detenermusica()
    BD_sql_server.exit()
