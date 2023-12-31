import datetime

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


def triarea(base, height):
    Area = base * height / 2
    print('The area is:', Area)
triarea(5, 10)

def area(base, height):
    Area = base * height
    print('The area is:', Area)
area(5, 10)

def circuit_power(voltage, current):
    calculated_power = voltage * current
    print('The calculated voltage', calculated_power)
circuit_power(500, 4)

# ---Previous code.---
#def sum_of_two(num1, num2):
    #total = num1, num2
    #print('The total:', total)
#sum_of_two(5, 7)

def sum_of_two(num1, num2):
    total = num1, num2
    print('The total:', total)
sum_of_two(5, 7)

def divide_multiply(num1, num2):
    for i in range (num1, num2):
        if (i % 7 ==0):
            print(num1 / num2)
        if (i % 11 == 0):
            print(num1 * num2)
        elif (i % 7 ==0) or (i % 11 == 0):
            print('Try again.')
divide_multiply(4, 5)
    

def convert_age_to_days():
    birthday = datetime.date(2005, 5, 6)
    now = datetime.date.today()
    delta = now - birthday
    print(delta.days)
convert_age_to_days()

def encrypt(msg):
    cipher = ''
    for letter in msg:
        if letter != '':
            cipher += char_to_dots[letter] + ''
        else:
            cipher += ''
    return cipher

def Encode_Morse(msg):
    result = encrypt(msg.upper())
    print(result)
Encode_Morse('Hi, how are you?')

def profit_calculation(cost, sell, inventory):
    sell_price = sell - cost
    if sell - cost:
        inventory - 1
    total = str(round(sell_price, 2))
    print(total)
    print(inventory)
    full_sell = sell * inventory
    full_cost = cost * inventory
    full_profit = full_sell - full_cost
    full = str(round(full_profit, 2))
    print(full)
profit_calculation(32.67, 45, 1200)

