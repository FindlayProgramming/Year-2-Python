from tabulate import tabulate
import csv

def menu():
    Menutable = [
    ['Option 1 - Input new customer information'],
    ['Option 2 - Search for customers via name'],
    ['Option 3 - Search for customers via car model']
]
    head = ['Sales Menu:']
    print(tabulate(Menutable, headers=head, tablefmt='grid')) #Outputs a menu through the use of the tabulate library.

menu()

options = int(input('Choose an option:\n')) #Here the user will decide which options to choose from the menu.

def option_results():
    if options == 1: #For option 1, the user will be given a series of inputs that will then be saved as new customer data and be transferred to an existing csv file.
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
    elif options == 2: #For option 2, the user will be able to search for existing customers by inputting their name. The program will then return the message "Name in file" however, the program was originally meant to output the full information of the customer if found. This could not happen due to other aspects having to be covered.
        search = input('Search by name:')
        with open('C:\\Users\\findl\\OneDrive\\Desktop\\T-Level Year 2\\Mark\\Customers.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                for field in row:
                    if field == search:
                        print('Name in file.')
    if options == 3: #Lastly, for option 3 the user will be given the option to search for existing customers by inputting the car model that the customer either wants to buy or owns. Originally, the program was meant to output the customer's information but will now output "car model found in file" if found. This is due to there being other aspects that have to be covered.
        search_car_model = input('Search customer via car model')
        with open('C:\\Users\\findl\\OneDrive\\Desktop\\T-Level Year 2\\Mark\\Customers.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                for field in row:
                    if field == search_car_model:
                        print('Car model found in file.')
option_results()