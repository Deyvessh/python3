
int_height = int(input("Please, Enter your height in CM: "))


if (int_height >= 120):
    print("Congratulations! You can ride")
    int_age = int(input("Please, Enter your age: "))
    
    if (int_age >= 18):
        photo = input("Do you want you photo clicked while riding? (Yes or No) - Extra $3 will be added to ticket: ")
        if photo.capitalize() == 'Yes':
            print("You final ticket for Ride + Photo is: $15")
        else:
            print("You final ticket for Ride is: $12")

    elif (int_age >= 12 and int_age <= 17):
        photo = input("Do you want you photo clicked while riding? (Yes or No) - Extra $3 will be added to ticket: ")
        if photo.capitalize() == 'Yes':
            print("You final ticket for Ride + Photo is: $10")
        else:
            print("You final ticket for Ride is: $7")
    else:
        photo = input("Do you want you photo clicked while riding? (Yes or No) - Extra $3 will be added to ticket: ")
        if photo.capitalize() == 'Yes':
            print("You final ticket for Ride + Photo is: $8")
        else:
            print("You final ticket for Ride is: $5")    
else:
    print("Sorry, you can't ride (You should be atleast 120 CM in height)")
    
    
    
    