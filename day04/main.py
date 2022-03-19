# Rock Paper Scissors

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

game_choices = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

player_choices = int(input())
print(game_choices[player_choices])

computer_choices = random.randint(0, 2)
print('Computer choice: ')
print(game_choices[computer_choices])

if player_choices == computer_choices:
    print("It's a tie.")

elif (player_choices == 0 and computer_choices == 2) or (player_choices == 1 and computer_choices == 0) or (player_choices == 2 and computer_choices == 1):
    print("You win.")
else:
    print("You lose.")
