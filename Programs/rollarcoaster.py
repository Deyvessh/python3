
height = input("Please, Enter your height in cm: ")

int_height = int(height)

if (int_height >= 120):
    print("You can ride")
    age = input("Please, Enter your age: ")
    int_age = int(age)
    if (int_age >= 18):
        print("Please, get a ticket of $12 from the counter")
    elif (int_age > 12):
        print("Please, get a ticker of $7 from the counter")
    else:
        print("Please, get a ticket of $5 from the counter")        
else:
    print("Sorry, you can't ride")