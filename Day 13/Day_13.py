import game_data
import random

right = True
score = 0
while right:
    if score > 0:
        print(f"Your score is {score}")
    first = random.randint(0, 49)
    first_data = game_data.data[first]
    print("A:" + first_data["name"] + "," + first_data["description"] + "," + first_data["country"])
    second = random.randint(0, 49)
    second_data = game_data.data[second]
    print("B:" + second_data["name"] + "," + second_data["description"] + "," + second_data["country"])
    answer = input("Who has more followers?'A' 'or' 'B'").lower()
    if answer == "a":
        if first_data["follower_count"] > second_data["follower_count"]:
            right = True
            score += 1
        else:
            right = False
    elif answer == "b":
        if first_data["follower_count"] < second_data["follower_count"]:
            right = True
            score += 1
        else:
            right = False

print(f"You lost,Your final score is {score}")
