#!/usr/bin/python

import psycopg2

#Estoy experimentando la orientacion a objetos de python,
#realmente no era necesario hacer funciones :B viene todo en el "basic module usage" de psycopg2

class Conector(object):

        def __init__(self):
                self.conn = psycopg2.connect("dbname = TESTDB user = chepe")
                self.cur = self.conn.cursor()

	#Ejecutamos algo :3
	def ejecucion(self):
		cur.execute("CREATE TABLE test2 (id serial PRIMARY KEY, numero integer, datos text);")
		#Metemos algo en la tabla 
		cur.execute("INSERT INTO test2 (numero, datos) VALUES (%s, %s)",(100, "abc'def"))
		cur.execute("SELECT * FROM  prueba;")
		cur.fetchall()

 	#Hacer los cambios
	def cambiar(self):
		conn.commit()

	#Cerrar la conn
	def cerrar(self):
		cur.close()
		conn.close()

	
#Hola :)
variable = Conector()

variable.ejecucion()
variable.cambiar()
variable.cerrar()	
