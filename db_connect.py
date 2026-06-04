import pymysql

connection=pymysql.connect(user='root',passwd='Rijju@100',port=3306,database='pavan_db',charset='utf8',host='localhost')
print("DB connected")
connection.close()
print("DB disconnected")
