import sqlite3 #Import module (standard to python since 2.5)

target_name = 'John Smith' #Will search Name

conn = sqlite3.connect("sales.db") #Connecting to db (Database)
cursor = conn.cursor() #Connect the cursor instance to use methods from sqlite such as fetching data from the result sets of queries.

def search_my_data(sales_id, name, city, commission):
    cursor.execute('CREATE TABLE salesman(salesman_id n(5), name char (30), city char (35), commission decimal(7,2));') #Creates table along with columns.
    cursor.execute("INSERT INTO salesman VALUES (4, 'Sammy', 'shark', 1)")
    cursor.execute("""
                   INSERT INTO salesman(salesman_id, name, city, commission)
                   VALUES (?,?,?,?)
                   """, (sales_id, name, city, commission)) #Inserts new data (the parameters) into the table.
    rows = cursor.execute("SELECT salesman_id, name, city, commission FROM salesman").fetchall()
    search = cursor.execute(
        'SELECT salesman_id, name, city, commission FROM salesman WHERE name =?',(target_name,), #Selects specific name stored.
        ).fetchall() #Selects the columns from the salesman table and fetches them all.
    conn.commit() #Commits to changes.
    print('Data entered...')
    conn.close() #Closes connection to DB.
    print(rows)
    print(search)
    if (conn):
        conn.close()
        print('\nDatabase closed...') #If the connection is closed it will print this message.
search_my_data(5, 'John Smith', 'New York', 5) #Inputs data through parameters to table.

