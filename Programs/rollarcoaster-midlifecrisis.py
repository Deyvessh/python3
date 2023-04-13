
height = int(input("Enter your height in centimeters: "))

ticket = 0

if height >= 120:
    
    age = int(input("Enter your age: "))
    
    if age <= 11:
        ticket += 5
    elif age >= 12 and age <=18:
        ticket += 7
    elif age >= 19 and age <= 44:
        ticket += 12
    elif age >= 45 and age <=55:
        ticket += 0
    else:
        ticket += 12
        
        
    photo = input("You want your photo to be taken while the ride? (Y/N): ")
    if photo == 'Y' and age > 0:
        if age >= 45 and age <=55: 
            ticket += 0
        else:
            ticket += 3
        
    else:
        ticket += 0
        
    print(f"Your ticket price is: {ticket}")

else:
    print("Sorry, You can't ride.")
    
    
