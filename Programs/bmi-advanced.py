
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


bmi = weight / height ** 2
roundoff_bmi = round(bmi, 1)


if (roundoff_bmi <= 18.4):
    print(f"Your BMI is {roundoff_bmi} and You are underweight")
elif (roundoff_bmi <= 24.9):
    print(f"Your BMI is {roundoff_bmi} and You have normal weight")
elif (roundoff_bmi <= 29.9):
    print(f"Your BMI is {roundoff_bmi} and You are slightly overweight")
elif (roundoff_bmi <= 34.9):
    print(f"Your BMI is {roundoff_bmi} and You are obese")
else:
    print(f"Your BMI is {roundoff_bmi} and You are clinically obese")










