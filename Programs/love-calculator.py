
print("Welcome to the Love Calculator!\n")
name1 = input("What is your name?: ")
name2 = input("What is their name?: ")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

t = lower_case_name1.count("t")
r = lower_case_name1.count("r")
u = lower_case_name1.count("u")
e = lower_case_name1.count("e")

t2 = lower_case_name2.count("t")
r2 = lower_case_name2.count("r")
u2 = lower_case_name2.count("u")
e2 = lower_case_name2.count("e")

first = t+r+u+e+t2+r2+u2+e2
first_str = str(first)

l = lower_case_name1.count("l")
o = lower_case_name1.count("o")
v = lower_case_name1.count("v")
e = lower_case_name1.count("e")

l2 = lower_case_name2.count("l")
o2 = lower_case_name2.count("o")
v2 = lower_case_name2.count("v")
e2 = lower_case_name2.count("e")

second = l+o+v+e+l2+o2+v2+e2
second_str = str(second)

score = int(first_str + second_str)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together")
    
else:
    print(f"Your score is {score}")









