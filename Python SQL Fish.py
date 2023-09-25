import sqlite3

target_name = 'Sammy'

conn = sqlite3.connect('aquarium.db')

cursor = conn.cursor()
cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")
cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
rows = cursor.execute(
    "SELECT name, species, tank_number FROM fish WHERE name =?", (target_name,),
                      ).fetchall()
cursor.close()
print(rows)
