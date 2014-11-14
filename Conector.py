#!/usr/bin/python

import psycopg2

#Estoy experimentando la orientación a objetos de python,
#realmente no era necesario hacer funciones :B viene todo en el "basic module usage" de psycopg2

class Conector(object):

	#Conectamos a la base de datos con su nombre y el dueño 
	def conexion(self):
		self.conn = psycopg2.connect("dbname = TESTDB user = carlos")


	#No sé por qué le llaman cursor, pero es para ejecutar query's a la base
	def cursor2(self):
		self.cur = self.conn.cursor()

	#Ejecutamos algo :3
	def ejecucion(self):

		self.cur.execute("CREATE TABLE prueba (id serial PRIMARY KEY, numero integer, datos text);")
		#Metemos algo en la tabla 
		self.cur.execute("INSERT INTO prueba (numero, datos) VALUES (%s, %s)",(100, "abc'def"))
		self.cur.execute("SELECT * FROM  prueba;")
		self.cur.fetchall()

 	#Hacer los cambios
	def cambiar(self):
		self.conn.commit()

	#Cerrar la conn
	def cerrar(self):
		self.cur.close()
		self.conn.close()

	
#Hola :)
variable = Conector()
variable.conexion()
variable.cursor2()
variable.ejecucion()
variable.cambiar()
variable.cerrar()	
