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
player_score = 0
computer_score = 0
import random

for score in range(1, 12):
    computers_move = random.randint(1, 3)
    players_move = input("What you want to do?\n 1 for rock,2 for paper,3 for scissors. ")
    if int(players_move) == 1:
        print(rock)
    elif int(players_move) == 2:
        print(paper)
    elif int(players_move) == 3:
        print(scissors)
    if computers_move == 1:
        move = rock
    elif computers_move == 2:
        move = paper
    elif computers_move == 3:
        move = scissors
    player_move = int(players_move)
    print(f"The computer chose{move}")
    if player_move == 1 and computers_move == 2:
        computer_score += 1

    elif player_move == 2 and computers_move == 3:
        computer_score += 1
    elif player_move == 3 and computers_move == 1:
        computer_score += 1
    elif computers_move == player_move:
        pass
    elif player_move == 1 and computers_move == 3:
        player_score += 1
    elif player_move == 2 and computers_move == 1:
        player_score += 1
    elif player_move == 3 and computers_move == 2:
        player_score += 1
    print(f"computer has {computer_score} points\nYour have {player_score} points")

if player_score == computer_score:
    print("It an Draw")
elif player_score > computer_score:
    print("You won")
elif player_score < computer_score:
    print("You lose")