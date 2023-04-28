import pyodbc
try:
    connection=pyodbc.connect('DRIVER={SQL Server};SERVER=ADRIANAVASQUEZ\SQLEXPRESS;DATABASE=FarmaApp;UID=adriana;PWD=Mirus')
    print("Conexion Exitosa")
    cursor=connection.cursor()
    #mostrar la version del sql
    cursor.execute("Select @@version;")
    row=cursor.fetchone()
    print(row)
    #mostar los registros de una tabla
    cursor.execute("select * from farmacia")
    rows=cursor.fetchall()
    for fila in rows:
        print(fila)
except Exception as EX:
    print(EX)
