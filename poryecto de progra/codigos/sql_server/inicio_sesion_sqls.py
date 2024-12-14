from tkinter import *
from tkinter import messagebox
import codigos.sql_server.BD_sql_server as BD_sql_server
import codigos.sql_server.menu_sql_server as menu_sql_server
from playsound import *
import codigos.musica as musica
global a
global b
kur = 1

def sonidito():
    global kur  # Asegurarnos de que x se refiera a la variable global
    if kur == 1:
        playsound("codigos/assets/Kururin_sound.wav")
        kur = 0
    else:
        playsound("codigos/assets/Kuru_kuru_sound.wav")
        kur = 1
def inicio_sesion(main_menu):
    def conectar(server, driver, database):
        try:
            BD_sql_server.conection(server, driver, database)  # Llamar a la función
        except Exception as ex:
            messagebox.showerror("ERROR", f"No se pudo conectar con la base de datos.\n{ex}")
    def hola():
        if driver.get() == '' or server.get() == '' or database.get() == '':
            messagebox.showwarning("ERROR", "Llena los datos antes de ingresar")
        else:
            a = driver.get()
            b = server.get()
            c = database.get()
            conectar(b,a,c)
            start_sqls.destroy()
            main_menu.destroy()
            musica.detenermusica()
            menu_sql_server.sqls()


    def cerrar():
        start_sqls.destroy()
    #raiz principal
    start_sqls = Toplevel()
    start_sqls.title("Iniciar sesion en SQLServer")
    start_sqls.iconbitmap("codigos/assets/BDICON.ico")
    start_sqls.config(bg="#7BBECB")
    x = 0
    #imagenSfrom playsound import playsound

# Definir una varfrom playsound import playsound

# Definir una variable global
    xd = PhotoImage(file="codigos/assets/padoru.png")
    label = Button(start_sqls ,image=xd, command=sonidito)
    label.place(x="300",y="100")
    label.config(cursor="hand2")

    #Ingresar datos
    titulo = Label(start_sqls, text="SQL SERVER", font=("Comic Sans SN", 10))
    titulo.grid(row="0",column="1", padx=10, pady=10)
    global driver
    driver = Entry(start_sqls)
    driver.grid(row="1",column="1", padx=10, pady=10)
    nombre_d = Label(start_sqls, text="Driver", font=("Comic Sans SN", 10))
    nombre_d.grid(row="1",column="0", padx=10, pady=10)
    global server
    server = Entry(start_sqls)
    server.grid(row="2",column="1", padx=10, pady=10)
    nombre_s = Label(start_sqls, text="Server", font=("Comic Sans SN", 10))
    nombre_s.grid(row="2",column="0", padx=10, pady=10)
    global database
    database = Entry(start_sqls)
    database.grid(row="3",column="1", padx=10, pady=10)
    nombre_d = Label(start_sqls, text="Database", font=("Comic Sans SN", 10))
    nombre_d.grid(row="3",column="0", padx=10, pady=10)

    #boton
    boton = Button(start_sqls, text="Confirmar", command=hola)
    boton.grid(row="4",column="0", padx=10, pady=10)
    salir = Button(start_sqls, text="Cerrar", command=cerrar)
    salir.grid(row="4",column="1", padx=10, pady=10)
    #main
    start_sqls.mainloop()