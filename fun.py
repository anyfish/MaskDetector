import mysql.connector
class fun(object):
	def conbd():
		try:
			mydb=mysql.connector.connect(
				host="us-cdbr-east-05.cleardb.net",
				user="b9a31ee20178d5",
				password="82c83d73",
				database="heroku_59960be04ed6f4c"
				)
			mycursor=mydb.cursor()
			print("Conectado...")
		except Exception as e:
			print("Error:" + str(e))
	def insertuser(name,ap,tel,ema,contr):
		try:
			mydb=mysql.connector.connect(
				host="us-cdbr-east-05.cleardb.net",
				user="b9a31ee20178d5",
				password="82c83d73",
				database="heroku_59960be04ed6f4c"
				)
			mycursor=mydb.cursor()
			sql="INSERT INTO `usuarios` (`id`, `nombre`, `apellido`, `telefono`, `correo`, `contra`) VALUES (%s,%s,%s,%s,%s,%s);"
			val=(1,name,ap,tel,ema,contr)
			mycursor.execute(sql,val)
			mydb.commit()
			print("Insertado")
		except Exception as e:
			print("Error:" + str(e))
	