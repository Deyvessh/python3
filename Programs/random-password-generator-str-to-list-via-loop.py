import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


nr_letters = int(input("How many letters you want in your password: "))
nr_numbers = int(input("How many numbers you want in your password: "))
nr_symbols = int(input("How many symbols you want in your password: "))

password = []

for char in range(1, nr_letters + 1):
    char_password = random.choice(letters)
    password += char_password
    
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

# print(password)

random.shuffle(password)

# print(password)

password_final = ""

for char in password:
    password_final += char

print(f"You password is: {password_final}")
    





