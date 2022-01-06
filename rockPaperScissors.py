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

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose ? Typ 0 for ROCK, 1 for PAPERr, 2 for SCISSORS\n"))

# check if the user doesn't insert number except 0,1,2 
if user_choice >= 3 or user_choice < 0:
    print("🟪 printed an invalid number , you lose")  
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("computer chose :")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0  and user_choice == 2:
        print("You Lose !")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print('You Win !!')
    elif computer_choice == user_choice:
        print("It's a draw")
