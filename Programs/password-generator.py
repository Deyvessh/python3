import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = input("How many letters would you like in your password?\n").split()
nr_symbols = input("How many symbols would you like?\n").split()
nr_numbers = input("How many numbers would you like?\n").split()

for n in range(0, len(nr_letters)):
    nr_letters[n] = int(nr_letters[n])
    
for n in range(0, len(nr_symbols)):
    nr_symbols[n] = int(nr_symbols[n])
    
for n in range(0, len(nr_numbers)):
    nr_numbers[n] = int(nr_numbers[n])

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letter_temp = 0
for l in nr_letters:
    l = random.randint(0, len(letters))
    l = letters
    letters = letter_temp
    
symbol_temp = 0
for s in nr_symbols:
    s = random.randint(0, len(symbols))
    symbol_temp = s
    
number_temp = 0
for n in nr_numbers:
    n = random.randint(0, len(numbers))
    number_temp = n
    

print(f"Here is your password: {letter_temp + symbol_temp + number_temp}")





#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P