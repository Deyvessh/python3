print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
          |                   |                  |                     |
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")


choose1 = input("What do you choose? To go right or left (right/left): ").lower()
if choose1 == 'left':
    print("Your choice was correct to go left\n")
    choose2 = input("What do you choose? To wait for a boat or swim across the ocean? (wait/swim): ").lower()
    if choose2 == 'wait':
        print("Your choice was correct to wait\n")
        choose3 = input(
            "There are three doors (red, yellow and blue), which door you open (red or yellow or blue): "
        ).lower()
        if choose3 == 'yellow':
            print("Congratulations!!! You won the treasure bucket full of GOLD")
        elif choose3 == 'red':
            print('Sorry! You lose, There was a Giant Standing behind "RED DOOR".')
        else:
            print('Sorry! You lose, There was a Lion Sitting behind the "BLUE DOOR"')
    else:
        # here, you can see i have put '\' in the middle you\'re so in print it should look 'You've'
        print('Sorry! You lose, You\'re eaten by a "CROCODILE"')
      
else:
    print('Sorry! You lose, You fell into a hole. You shouldn\'t have gone right.')

