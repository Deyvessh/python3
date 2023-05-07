import math

def paint_calc(height, width, cover):
    cans = math.ceil((height * width) / cover) # importing ceil (roundup) class from math function
    print(f"You'll need {cans} cans of paint.")  # ceil class from math function is differenct from round class
  

# Calculation codebase,

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

# function is called here,

paint_calc(height=test_h, width=test_w, cover=coverage)

