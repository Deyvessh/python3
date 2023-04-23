
# number divisible by 3 then print "Fizz"
# number divisible by 5 then print "Buzz"
# number divisibe by 3 and 5 then print "FizzBuzz"
# else print number

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)