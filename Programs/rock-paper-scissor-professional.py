
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

user_choice = int(input("What do you choose? (0 - Rock) (1 - Paper) (2 - Scissor)? "))
print("\n")

game_choice = [rock, paper, scissors]

if user_choice >= 2 or user_choice < 0:
    print("You typed an invalid number, You lose!")
    
else:
    
    print(f"You chose: \n {game_choice[user_choice]}")

    computer_choice = random.randint(0, 2)
    print("\n")
    print(f"Computer chose: \n {game_choice[computer_choice]}")


    print("\n")

        
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
        
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")

    elif computer_choice > user_choice:
        print("You lose!")

    elif user_choice > computer_choice:
        print("You win!")

    elif user_choice == computer_choice:
        print("Match draw!")
        











