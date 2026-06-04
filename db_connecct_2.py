import pymysql#driver  for connecting python with mysql

def db_connect():
    connection=None
    try:
        connection=pymysql.connect(user='root',passwd='Rijju100',port=3306,database='pavan_db',charset='utf8',host='localhost')
        print("DB connected")
    except Exception as e:
        print("DB disconnected")
    return connection
def db_disconnect(connection):
    try:
        connection.close()
        print("DB disconnected")
    except Exception as e:
        print("DB disconnection failed")
connection=db_connect()
db_disconnect(connection)

