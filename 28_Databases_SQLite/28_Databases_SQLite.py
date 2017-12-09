import sqlite3

# There are 5 steps to interact with a Database
# 1. Connect to the database
# 2. Create a cursor object (Pointer to access rows from database tables)
# 3. Write SQL query
# 4. Commit changes to the database
# 5. Close the connection to the database


def create_table():
    # Create the connection to the SQLite database
    # The connect function requires the database file
    # If the filename specified does not exist, the file will be created automatically
    # If the database already exists, there will be created a connection with it

    conn = sqlite3.connect("lite.db")

    # Create the cursor
    cur = conn.cursor()

    # Execute a SQL code on the current cursor
    # Our database is currently empty, so we create a table
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    # Commit changes to the database
    conn.commit()

    # Close the connection with the database
    conn.close()

    # If we execute the program for the first time, it will create the database lite.db


def insert_data(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    # WARNING: Be sure to use single quotes ' for inserting a TEXT, otherwise you'll confuse Python
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def remove_data(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()


def update_data(item, quantity):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=? WHERE item = ?", (quantity, item))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


print(view())


# remove_data("Xbox One X")
#insert_data("Xbox One X", 10, 499.99)
#update_data("Xbox One X", 9)
