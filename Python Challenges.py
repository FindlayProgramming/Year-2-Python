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
print(triarea(5, 10))

def area(base, height):
    Area = base * height
    print('The area is:', Area)
print(area(5, 10))

def circuit_power(voltage, current):
    calculated_power = voltage * current
    print('The calculated voltage', calculated_power)
print(circuit_power(500, 4))

# ---Previous code.---
#def sum_of_two(num1, num2):
    #total = num1, num2
    #print('The total:', total)
#print(sum_of_two(5, 7))

def sum_of_two(num1, num2):
    total = num1, num2
    print('The total:', total)
print(sum_of_two(5, 7))

def divide_multiply(num1, num2):
    multiples_of_seven = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
    multiples_of_eleven = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
    if num1 in multiples_of_seven:
        print(num1 / num2)
    if num2 in multiples_of_eleven:
        print(num1 * num2)
    elif num1 and num2 in multiples_of_seven or multiples_of_eleven:
        print('Try again.')
print(divide_multiply(4, 5))
    

def convert_age_to_days():
    birthday = datetime.date(2005, 5, 6)
    now = datetime.date.today()
    delta = now - birthday
    print(delta.days)
convert_age_to_days()

def encrypt(msg):
    cipher = ''
    

def Encode_Morse(msg):
    morse = char_to_dots
    msg = morse
print(Encode_Morse('Hi, how are you?'))