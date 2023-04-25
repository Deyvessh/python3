import random

letter = ['a', 'b', 'c', 'd']
number = ['1', '2', '3', '4']
symbol = ['!', '#', '$', '%']

nr_le = int(input("how many letters: "))
nr_nu = int(input("how many numbers: "))
nr_sy = int(input("how many symbols: "))


password = ""

for char in range(0, nr_le):
    random_char = random.choice(letter)
    password += random_char
    
for char in range(0, nr_nu):
    random_char = random.choice(number)
    password += random_char
    
for char in range(0, nr_sy):
    random_char = random.choice(symbol)
    password += random_char

print(password)



