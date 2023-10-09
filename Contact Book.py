from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from mysql.connector import connect, Error
import sqlite3
from tabulate import tabulate

#Will have to come back to this later. Not sure how to use the sql connector for now.

conn = sqlite3.connect('Contact Book.db')

def contact_menu():
    Menutable = [
    ['Option 1 - Add new contact records'],
    ['Option 2 - Search for contacts by name'],
    ['Option 3 - Display all contact records'],
    ['Option 4 - Delete contact records'],
    ['Option 5 - Modify contact records']
]
    head = ['Contact Menu:']
    print(tabulate(Menutable, headers=head, tablefmt='grid'))
contact_menu()

def contact_table():
    dbfile = 'C:\\Users\\findl\\OneDrive\\Documents\\Github\\Placement-Work\\Contact Book.db'
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    table_list = [a for a in cursor.execute("Select name FROM sqlite")]
contact_table()

def option1():
    name_input = input("Enter name: \n")
    address_input = input("Enter address: \n")
    phone_num = int(input("Enter phone number: \n"))
    email = input("Enter email: \n")
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO Contact(name, address, phone_number, email_address)
                   VALUES (?,?,?,?)
                   """, (name_input, address_input, phone_num, email))
    outputs = input("Show output? Y/N: \n")
    if outputs == "Y":
        rows = cursor.execute('SELECT name, address, phone_number, email_address FROM Contact').fetchall()
        print(rows)
    if outputs != "N":
        contact_menu()
        option()

def option2():
    target_name = input("Name of contact?: \n")
    cursor = conn.cursor
    search = cursor.execute(
        'SELECT name, address, phone_number, email_address FROM Contact WHERE name =?', (target_name,),
    ).fetchall()
    conn.commit()
    if search == None:
        print("Search not found.")
        contact_menu()
        option()
    else:
        print(search)

def option3():
    cursor = conn.cursor()
    rows = cursor.execute('SELECT name, address, phone_number, email_address FROM Contact').fetchall()
    print(rows)
    contact_menu()
    option()

def option():
    options = int(input('Please choose an option: \n'))
    if options == 1:
        option1()
    if options == 2:
        option2()
    if options == 3:
        option3()
option()

conn.close()