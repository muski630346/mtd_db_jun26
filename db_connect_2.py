import pymysql

def db_connect():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="Rijju@100", 
              database="muskan_db",  # change if needed
            port=3306,
            charset="utf8"
        )
        print("DB connected")
        return connection

    except Exception as e:
        print("DB connection failed:", e)
        return None


def db_disconnect(connection):
    try:
        if connection:
            connection.close()
            print("DB disconnected")
    except Exception as e:
        print("DB disconnection failed:", e)