from tabulate import tabulate
import csv

def menu():
    Menutable = [
    ['Option 1 - Input new customer information'],
    ['Option 2 - Search for customers via name'],
    ['Option 3 - Search for customers via car model']
]
    head = ['Sales Menu:']
    print(tabulate(Menutable, headers=head, tablefmt='grid'))

menu()

options = int(input('Choose an option:\n'))

def option_results():
    if options == 1:
        new_customer = str(input('What is the name of the new customer?\n'))
        make = str(input('What make?\n'))
        model = str(input('What model?\n'))
        colour = str(input('What colour?\n'))
        f = open('C:\\Users\\findl\\OneDrive\\Desktop\\T-Level Year 2\\Mark\\Customers.csv', 'a')
        f.write(new_customer )
        f.write(make )
        f.write(model )
        f.write(colour )
        f.close()
        f = open('C:\\Users\\findl\\OneDrive\\Desktop\\T-Level Year 2\\Mark\\Customers.csv', 'r')
        print(f.read())
    elif options == 2:
        search = input('Search by name:')
        with open('C:\\Users\\findl\\OneDrive\\Desktop\\T-Level Year 2\\Mark\\Customers.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                for field in row:
                    if field == search:
                        print('Name in file.')
    if options == 3:
        search_car_model = input('Search customer via car model')
        with open('C:\\Users\\findl\\OneDrive\\Desktop\\T-Level Year 2\\Mark\\Customers.csv', 'rt'):
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                for field in row:
                    if field == search:
                        print('Car model found in file.')
option_results()