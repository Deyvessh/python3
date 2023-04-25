
# Do not run here
# Reeborg's World Hurdles
# URL : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Hurdle 1

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def phase():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
phase()
phase()
phase()
phase()
phase()
phase()

# and to use for loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def phase():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    phase()
    

# to use while loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def phase():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
number_of_hurdles = 6           # loop will run total 6 times
while number_of_hurdles > 0:
    phase()
    number_of_hurdles -= 1      # when function phase() is run and completed then decrease the number_of_hurdles by 1 then
                                # in the first time the loop would run more 5 times


# Hurdle 2


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def phase():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6
while number_of_hurdles > 0:
    phase()
    if at_goal():      # when the condition met 'at_goal()' then break
        break          # that is 'if' with 'while'
 
 
# with while only


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def phase():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
    phase()
    
# or

while not at_goal():
    phase()
 



