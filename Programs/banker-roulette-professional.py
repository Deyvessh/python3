
import random

name_string = input("Give me everybody's names, separated by a comma. ")

names = name_string.split(", ")


length_names = len(names)

random_choice = random.randint(0, length_names - 1)

random_name = names[random_choice]

print(f"{random_name} is going to buy the meal today!")