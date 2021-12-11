import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

end_game = False
correct = 0
incorrect = 0
incorrects = False
while not end_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
            correct += 1

    if correct == 0:
        incorrects = True
    correct = 0

    if incorrects == True:

        incorrect += 1
        if incorrect == 1:
            print("_____\n  |  |\n     |\n     |\n     |")
        elif incorrect == 2:
            print("_____\n  |  |\n  O  |\n     |\n     |")
        elif incorrect == 3:
            print("_____\n  |  |\n  O  |\n  |  |\n     |")
        elif incorrect == 4:
            print("_____\n  |  |\n  O  |\n/ |  |\n     |")
        elif incorrect == 5:
            print("_____\n  |  |\n  O  |\n/ | \|\n     |")
        elif incorrect == 6:
            print("_____\n  |  |\n  O  |\n/ | \|\n /   |")
        elif incorrect == 7:
            print("_____\n  |  |\n  O  |\n/ | \|\n / \ |")
        else:
            print("Game Over!")
            end_game = True
        incorrects = False
    print(display)
    if "_" not in display:
        end_game = True
        print("You win")