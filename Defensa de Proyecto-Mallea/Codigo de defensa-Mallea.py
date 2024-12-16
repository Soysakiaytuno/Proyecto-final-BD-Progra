import pyodbc
#Problemas planteado
#Insertar en una nueva columna de la tabla cliente los datos de la columna Apellido pero cambiados de la siguiente manera
# Marco -> Funcion -> (M(a(r)c)o)
#Esta funcion debe utilizar la recursion y mostrar los cambios en la base de datos
# Hacemos la conexion a el Sql server
mydb = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "SERVER=MSI\\MSSQLSERVER01;"
    "DATABASE=Proyecto_Zoologico;"
    "Trusted_Connection=Yes;"
)

# 2. Creo un cursor
mycursor = mydb.cursor()
# El cursor es el que ejectura las sentencias
mycursor.execute(f"select Apellido from Cliente;")

def Obtencion_Datos_Columna(cursor):
    columns = [column[0] for column in cursor.description]
    Apellidos = cursor.fetchall()
    character_to_eliminate=['(',')',',','\'',' ']
    Lista_Apellidos=[]
    #Por medio de un loop guardamos en una variable los datos de la columna Apellido y la tabla cliente
    for var1 in range(len(Apellidos)):
        Apellido =''
        Apellido1 = Apellidos[var1]
        for var2 in range(len(Apellido1)):
            for var3 in range(len(Apellido1[var2] )):
                a= Apellido1[var2] 
                if a[var3] != character_to_eliminate:
                    if a[var3] == ' ':
                        break 
                    Apellido += a[var3]
        Lista_Apellidos.append(Apellido)
    return Lista_Apellidos
def Parentesis_Recursivo(cadena:str, z:int):
    if z == len(cadena):
        return ')'   
    if z == 0:
        return '('+cadena[z] + Parentesis_Recursivo(cadena, z+1)
    elif z < len(cadena)/2:
        return '('+cadena[z] + Parentesis_Recursivo(cadena, z+1)
    elif z > len(cadena)/2:
        return ')'+cadena[z] + Parentesis_Recursivo(cadena, z+1)
    elif z == len(cadena)/2:
        return '()'+cadena[z] + Parentesis_Recursivo(cadena, z+1)
def colum_parentesis(cursor, tabla, nueva_columna):
    #Obtenemos los nombres de las columnas de la tabla selecionada
    columns = [column[0] for column in cursor.description]
    columns = [col.replace('.', '') for col in columns]
    #Obtenenmos los datos de la columna seleccionada
    Apellidos = Obtencion_Datos_Columna(cursor)
    Columna_nue = []
    #Guardamos en una variable la lista de nuevos datos ahora con los parentesis
    for var1 in range(len(Apellidos)):
        Columna_nue.append(Parentesis_Recursivo(Apellidos[var1], 0))
    #Ejecutamos diferentes quarys que anaden una nueva columna a la tabla y insertan los datos con parentesis en la misma
    cursor.execute(f"""
    ALTER TABLE {tabla}
    ADD {nueva_columna} VARCHAR(20) NULL;""")
    cursor.commit()
    cursor.execute(f"select * from {tabla};")
    columns = [column[0] for column in cursor.description]
    query1 = (f""" UPDATE {tabla}
                  SET {nueva_columna} = \'{Columna_nue[0]}\'
                  WHERE {columns[2]} = \'{Apellidos[0]}\';""")
    cursor.execute(query1)
    #Confirmamos los cambios a la base de datos para que se realizen
    cursor.commit()
colum_parentesis(mycursor, "Cliente", "Parentesis")
