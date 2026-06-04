import db_connect_2 as dbc

def insert_row():
    query = """
    INSERT INTO employee(name, salary, designation, phone_number)
    VALUES (%s, %s, %s, %s)
    """

    connection = dbc.db_connect()
    if connection is None:
        print("DB connection failed")
        return

    cursor = connection.cursor()

    name = input("Enter name: ")
    salary = float(input("Enter salary: "))
    designation = input("Enter designation: ")
    phone_number = int(input("Enter phone number: "))

    data = (name, salary, designation, phone_number)

    cursor.execute(query, data)

    connection.commit()
    cursor.close()
    dbc.db_disconnect(connection)

    print("Row inserted successfully")


insert_row()
