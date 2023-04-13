
int_height = int(input("Enter your height in cm: "))

bill = 0 

if int_height >= 120:
    print("Congratulation! You can ride")
    
    int_age = int(input("Enter your age: "))
    if int_age <= 11:
        bill = 5
        print("Your ride cost is $5")
    elif int_age >=12 and int_age <=17:
        bill = 7
        print("Your ride cost is $7")
    else:
        bill = 12
        print("Your ride cost is $12")
        
    
    photo = input("Do you want your photo taken while riding? (Yes/No or Y/N): ")
    if photo.capitalize() == 'Yes' or 'Y':
        bill += 3
    
    print(f"You final bill is: ${bill}")
    
else:
    print("You can't ride!")