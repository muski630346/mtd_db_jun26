import pymysql#driver  for connecting python with mysql
import db_connect_2 as dbc

def create_db():
    query='create database  if not exists muskan_db'
    try:
        connection=dbc.db_connect()
        cursor=connection.cursor()
        result=cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc.db_disconnect(connection)
        if result==1:
            print("DB created")
        else:    
            print("DB already exists")
    except Exception as e:
        print("error in creating db:e",e)
    
def create_table():
    query='create table if not exists employee(id int primary key auto_increment,name varchar(20) not null,salary float,designation varchar(20),phone_number bigint unique)'
    try:
        connection=dbc.db_connect()
        cursor=connection.cursor()
        result=cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc.db_disconnect(connection)
        if result==1:
            print("table created")
        else:    
            print("table already exists")
    except Exception as e:
        print("error in creating table:e",e)
create_db()
create_table()

