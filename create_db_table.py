import db_connect_2 as dbc

def create_db():
    query = "CREATE DATABASE IF NOT EXISTS muskan_db"

    connection = dbc.db_connect()
    if connection is None:
        print("DB connection failed")
        return

    cursor = connection.cursor()
    cursor.execute(query)

    connection.commit()
    cursor.close()
    dbc.db_disconnect(connection)

    print("Database created successfully")


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS employee(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(20) NOT NULL,
        salary FLOAT,
        designation VARCHAR(20),
        phone_number BIGINT UNIQUE
    )
    """

    connection = dbc.db_connect()
    if connection is None:
        print("DB connection failed")
        return

    cursor = connection.cursor()
    cursor.execute(query)

    connection.commit()
    cursor.close()
    dbc.db_disconnect(connection)

    print("Table created successfully")


create_db()
create_table()