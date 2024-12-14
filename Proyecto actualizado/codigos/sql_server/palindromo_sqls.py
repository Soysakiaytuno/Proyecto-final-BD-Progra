from tkinter import *
from tkinter import messagebox
import pyodbc
def encontrar_palindromo(palindromo):
    palabra = ""
    for extras in palindromo:
        if extras != "(" or extras != ")" or extras != ",":
             palabra += extras
    for espacio in palindromo:
        palabra = espacio.replace(' ', '')
    izquierda = 0 
    derecha = len(palabra) - 1
    palabra = palabra.lower()
    while izquierda < derecha:
        if palabra[izquierda] != palabra[derecha]:
            return "No es palindromo"
        else:
             izquierda += 1
             derecha -= 1
    return "Es palindromo"

def mostrar_nombre_palindromo(the_show,records):
    num = 1
    for record in records:              
        res = encontrar_palindromo(record)
        nombre = Label(the_show, text=record)
        nombre.grid(row=num, column=0)
        nombre = Label(the_show, text=res)
        nombre.grid(row=num, column=1)
        num += 1
def mostrar_apellido_palindromo(the_show,records):
    num = 1
    for record in records:              
        res = encontrar_palindromo(record)
        nombre = Label(the_show, text=record)
        nombre.grid(row=num, column=2)
        nombre = Label(the_show, text=res)
        nombre.grid(row=num, column=3)
        num += 1     
def palindromo(mydb):
        try:    
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT Nombre FROM Cliente;")
            records = mycursor.fetchall()
            the_show = Tk()
            the_show.title("Base de datos god")
            the_show.iconbitmap("codigos/assets/BDICON.ico")
            mycursor.execute(f"SELECT Apellido FROM Cliente;")
            apellidos = mycursor.fetchall()
            columna_n = Label(the_show, text="Nombres")
            columna_n.grid(row="0",column="0")
            columna_n = Label(the_show, text="Palindromo")
            columna_n.grid(row="0",column="1")
            columna_c = Label(the_show, text="Apellidos")
            columna_c.grid(row="0",column="2")
            columna_n = Label(the_show, text="Palindromo")
            columna_n.grid(row="0",column="3")
            mostrar_nombre_palindromo(the_show,records)
            mostrar_apellido_palindromo(the_show,apellidos)
            mainloop()
        except ex as ex:
            messagebox.showerror("Error", f"El error es \n{ex}")