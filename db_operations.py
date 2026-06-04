import db_connect_2 as dbc

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
        return

    cursor = connection.cursor()
    cursor.execute(query)

    connection.commit()
    cursor.close()
    dbc.db_disconnect(connection)

    print("Table created")
def insert_row():
    query = """
    INSERT INTO employee(name, salary, designation, phone_number)
    VALUES (%s, %s, %s, %s)
    """

    name = input("Enter name: ")
    salary = float(input("Enter salary: "))
    designation = input("Enter designation: ")
    phone_number = int(input("Enter phone number: "))

    data = (name, salary, designation, phone_number)

    connection = dbc.db_connect()
    if connection is None:
        return

    cursor = connection.cursor()
    cursor.execute(query, data)

    connection.commit()
    cursor.close()
    dbc.db_disconnect(connection)

    print("Row inserted")
def update_row():
    query = """
    UPDATE employee
    SET salary = %s
    WHERE id = %s
    """

    emp_id = int(input("Enter ID: "))
    salary = float(input("Enter new salary: "))

    data = (salary, emp_id)

    connection = dbc.db_connect()
    if connection is None:
        return

    cursor = connection.cursor()
    cursor.execute(query, data)

    connection.commit()
    cursor.close()
    dbc.db_disconnect(connection)

    print("Updated")
def delete_row():
    query = "DELETE FROM employee WHERE id = %s"

    emp_id = int(input("Enter ID: "))
    data = (emp_id,)

    connection = dbc.db_connect()
    if connection is None:
        return

    cursor = connection.cursor()
    cursor.execute(query, data)

    connection.commit()
    cursor.close()
    dbc.db_disconnect(connection)

    print("Deleted")
def select_rows():
    query = "SELECT * FROM employee"

    connection = dbc.db_connect()
    if connection is None:
        return

    cursor = connection.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    dbc.db_disconnect(connection)

    print("Displayed")
def main():
    print("DBMS Project Running...")

    while True:
        print("\n1. Create Table")
        print("2. Insert")
        print("3. Update")
        print("4. Delete")
        print("5. Select")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            create_table()
        elif choice == 2:
            insert_row()
        elif choice == 3:
            update_row()
        elif choice == 4:
            delete_row()
        elif choice == 5:
            select_rows()
        elif choice == 6:
            break
        else:
            print("Invalid choice")


main()    