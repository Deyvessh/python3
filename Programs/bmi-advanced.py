
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


bmi = weight / height ** 2
roundoff_bmi = round(bmi, 1)

print(f"Your BMI index is: {roundoff_bmi}")


if (roundoff_bmi <= 18.4):
    print("You are underweight")
elif (roundoff_bmi <= 24.9):
    print("You have normal weight")
elif (roundoff_bmi <= 29.9):
    print("You are slightly overweight")
elif (roundoff_bmi <= 34.9):
    print("You are obese")
else:
    print("You are clinically obese")










