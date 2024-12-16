from tkinter import *
from tkinter import messagebox
import codigos.sql_server.BD_sql_server as BD_sql_server
import codigos.sql_server.menu_sql_server as menu_sql_server
from playsound import playsound
import codigos.musica as musica

sonido = 1
def sonidito():
    #Definimos la variable global para que cada que llame a la funcion intercambie de sonido
    global sonido 
    if sonido == 1:
        playsound("codigos/assets/Kururin_sound.wav")
        sonido = 0
    else:
        playsound("codigos/assets/Kuru_kuru_sound.wav")
        sonido = 1

def conectar(server, driver, database):
    try:
        BD_sql_server.db_manager.conection(server, driver, database)  # Llamar a la función
    except Exception as ex:
        messagebox.showerror("ERROR", f"No se pudo conectar con la base de datos.\n{ex}")

def ingresar(main_menu, driver, server, database, start_sqls):
    if driver.get() == '' or server.get() == '' or database.get() == '':
        messagebox.showwarning("ERROR", "Llena los datos antes de ingresar")
    else:
        str_driver = driver.get()
        str_server = server.get()
        str_database = database.get()
        conectar(str_server, str_driver, str_database)
        start_sqls.destroy()
        main_menu.destroy()
        musica.detenermusica()
        menu_sql_server.sqls()

def cerrar(start_sqls):
    start_sqls.destroy()

def inicio_sesion(main_menu):
    #raiz principal
    start_sqls = Toplevel()
    start_sqls.title("Iniciar sesion en SQLServer")
    start_sqls.iconbitmap("codigos/assets/BDICON.ico")
    start_sqls.config(bg="#7BBECB")

    #boton extra
    foto = PhotoImage(file="codigos/assets/padoru.png")
    label = Button(start_sqls, image=foto, command=sonidito)
    label.place(x="300", y="100")
    label.config(cursor="hand2")

    # Ingresar datos
    titulo = Label(start_sqls, text="SQL SERVER", font=("Comic Sans SN", 10))
    titulo.grid(row="0", column="1", padx=10, pady=10)
    
    driver = Entry(start_sqls)
    driver.grid(row="1", column="1", padx=10, pady=10)
    nombre_d = Label(start_sqls, text="Driver", font=("Comic Sans SN", 10))
    nombre_d.grid(row="1", column="0", padx=10, pady=10)

    server = Entry(start_sqls)
    server.grid(row="2", column="1", padx=10, pady=10)
    nombre_s = Label(start_sqls, text="Server", font=("Comic Sans SN", 10))
    nombre_s.grid(row="2", column="0", padx=10, pady=10)

    database = Entry(start_sqls)
    database.grid(row="3", column="1", padx=10, pady=10)
    nombre_d = Label(start_sqls, text="Database", font=("Comic Sans SN", 10))
    nombre_d.grid(row="3", column="0", padx=10, pady=10)

    # Botón
    boton = Button(start_sqls, text="Confirmar", command=lambda: ingresar(main_menu, driver, server, database, start_sqls))
    boton.grid(row="4", column="0", padx=10, pady=10)
    salir = Button(start_sqls, text="Cerrar", command=lambda: cerrar(start_sqls))
    salir.grid(row="4", column="1", padx=10, pady=10)
    
    # Main
    start_sqls.mainloop()
