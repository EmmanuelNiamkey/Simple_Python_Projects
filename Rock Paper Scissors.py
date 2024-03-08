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
import random

game_images = [rock, paper, scissors]


print("Welcome to the game")

# Making Computer List and player's list
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 Scissors. \n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")

else:
    print(game_images[user_choice])

    machine_choice = random.randint(0, 2)
    print("Computer chose :")
    print(game_images[machine_choice])

    # Game logic

    if user_choice == 0 and machine_choice == 2:
        print("You win!")
    elif machine_choice == 0 and user_choice == 2:
        print("You lose!")
    elif machine_choice > user_choice:
        print("You lose!")
    elif user_choice > machine_choice:
        print("You win!")
    elif machine_choice == user_choice:
        print("it's a draw!")




