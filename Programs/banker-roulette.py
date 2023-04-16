
import random

name_string = input("Give me everybody's names, separated by a comma. ")

names = name_string.split(", ")

names_random = random.randrange(len(names))
 
names_random_final = names[names_random]

print(f"{names_random_final} is going to buy the meal today!")