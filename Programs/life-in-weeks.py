
age = input("What is your current age? ")

y = (90 - int(age))
d = (y - int(age)) * 365
w = (y - int(age)) * 52
m = (y - int(age)) * 12

message = f"You have {y} years, {d} days, {w} weeks, and {m} months left."

print(message)