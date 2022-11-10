import psycopg2

try:
    Connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456',
        database='mastergoal'
    )

    print("Conexion Exitosa ")
    cursor=Connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)

    cursor.execute("SELECT *FROM usuario")
    rows=cursor.fetchall()

    for row in rows:
        print(row)
        
except Exception as ex:
    print(ex)
finally:
    Connection.close()
    print("Conexion finalizada")