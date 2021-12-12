import random

player_card = []
computers_card = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playing = False
start = input("Do you want to start the game?y or n\n")
if start.lower() == "y":
    playing = True
else:
    playing = False
    print("Okay maybe play next time!")


def player_cards():
    for n in range(2):
        player_card.append(random.choice(cards))

    print(f"Your cards are {player_card}")
    return player_card


def computer_card():
    for n in range(2):
        computers_card.append(random.choice(cards))

    print(f"computers first card is {computers_card[0]}")
    return computers_card


while playing == True:

    player_card = []
    computers_card = []
    player_cards()
    computer_card()
    another_card = input("Type y to get another card and n to pass.")
    if another_card.lower() == "y":
        player_card.append(random.choice(cards))
        print(f"Your cards are {player_card}")
    print(f"computers cards are{computers_card}")
    player_total = 0
    computer_total = 0
    for card in player_card:
        player_total += card
    for cards in computers_card:
        computer_total += cards

    calculating_p = 21 - player_total
    calculating_c = 21 - computer_total
    win_lose = ""
    if calculating_p < 0:
        win_lose = "Dealer wins"
    elif calculating_p < calculating_c:
        win_lose = "You win"
    elif calculating_c < calculating_p:
        win_lose = "dealer wins"
    elif calculating_c == calculating_p:
        win_lose = "It is a tie"
    print(win_lose)
    playing = False