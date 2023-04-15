
print("Welcome to the Love Calculator!\n")
name1 = input("What is your name?: ")
name2 = input("What is their name?: ")

combined_string = name1 + name2

lower_case_combined_string = combined_string.lower()

t = lower_case_combined_string.count("t")
r = lower_case_combined_string.count("r")
u = lower_case_combined_string.count("u")
e = lower_case_combined_string.count("e")


first = t+r+u+e
first_str = str(first)

l = lower_case_combined_string.count("l")
o = lower_case_combined_string.count("o")
v = lower_case_combined_string.count("v")
e = lower_case_combined_string.count("e")

second = l+o+v+e
second_str = str(second)

score = int(first_str + second_str)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together")
    
else:
    print(f"Your score is {score}")









