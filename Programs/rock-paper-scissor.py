import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Rock - Paper - Scissor \n")

play = int(input("What do you choose? (0 - Rock) (1 - Paper) (2 - Scissor)? "))
print("\n")

if play == 0:
    print("You chose Rock")
    print(rock)
    
elif play == 1:
    print("You chose Paper")
    print(paper)
    
elif play == 2:
    print("You chose Scissors")
    print(scissors)
    
else:
    print("Wrong Input")

print("\n")

game_list = ["rock", "paper", "scissors"]
game_list_random = random.choice(game_list)

if game_list_random == "rock":
    print("Computer's choice is Rock \n")
    print(rock)

elif game_list_random == "paper":
    print("Computer's choice is Paper \n")
    print(paper)
    
else:
    game_list_random == "scissors"
    print("Computer's choice is Scissors \n")
    print(scissors)
    
    

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

print("\n")

if play == 0 and game_list_random == "scissors":
    print("You win")

elif play == 0 and game_list_random == "paper":
    print("You lose")
    
elif play == 0 and game_list_random == "rock":
    print("Match draw")
    
elif play == 1 and game_list_random == "rock":
    print("You lose")
    
elif play == 1 and game_list_random == "scissors":
    print("You win")
    
elif play == 1 and game_list_random == "paper":
    print("Match draw")
    
elif play == 2 and game_list_random== "rock":
    print("You lose")
    
elif play == 2 and game_list_random == "paper":
    print("You win")

elif play == 2 and game_list_random == "scissors":
    print("Match draw")
    
else:
    print("Wrong Input")







