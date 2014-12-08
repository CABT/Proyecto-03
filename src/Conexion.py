import psycopg2

class Conexion:

    def consulta(self, sql):
        conn = psycopg2.connect("dbname='sangobemoledor' user='postgres' password='root'")

        cur = conn.cursor()

        cur.execute(sql)
        rows= cur.fetchall()

        conn.close()
        cur.close()

        return rows
    
    def actualizar(self, sql):
        conn=psycopg2.connect("dbname='sangobemoledor' user='postgres' password='root' host='localhost'")
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()

        conn.close()
        cur.close()


class Usuario:
    conn=Conexion()
    print str(conn.actualizar("insert into usuario values (3,'sde','der','fre','1991-12-22','correo','dfret','xxx')"))

