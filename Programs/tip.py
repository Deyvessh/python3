
bill = input("What was the total bill: $")
tip = input("What percentage tip would you like to give? 10, 12 or 15?: ")
people = input("how many people to split the bill: ")

float_bill = float(bill)
int_tip = int(tip)
int_people = int(people)

tip_perc = (int_tip / 100) * float_bill
total_bill = float_bill + tip_perc
split = total_bill / int_people

# round_off = str(round(split, 2))
round_off = "{:.2f}".format(split) # another method to precision round off a number by 2 decimal points


print(f"Each person should pay: ${round_off}")


