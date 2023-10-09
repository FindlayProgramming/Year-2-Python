from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import mysql.connector
from mysql.connector import Error
import sqlite3

#Will have to come back to this later. Not sure how to use the sql connector for now.

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Contact_Book',
                                         user='Rus',
                                         password='G245')
    SQL_Contact_Table = """CREATE TABLE Laptop (
                      Id int(11) NOT NULL,
                      Name varchar(250) NOT NULL,
                      Price float NOT NULL,
                      Purchase_date Date NOT NULL,
                      PRIMARY KEY (Id))"""
    cursor = connection.cursor()
    result = cursor.execute(SQL_Contact_Table)
    print('Laptop Table created successfully')

except mysql.connector.Error as error:
    print('Error to create table in MySQL: {}'.format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('SQL DB connection closed')
