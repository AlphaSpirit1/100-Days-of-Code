import random
print("welcome to the number guess")
print("I'm thinking of a number between 1 to 100")
difficulty=input("What difficulty do you want to play on 'easy' or 'hard'?\n")
number_guess=random.randint(1,101)
if difficulty.lower()=="easy":
  number_of_guesses=10
if difficulty.lower()=="hard":
  number_of_guesses=5
while number_of_guesses>0:
  print(f"You have {number_of_guesses} left")
  guess=int(input("What is the number?"))
  if guess>number_guess:
    win=False
    print("The number you have guessed is too high.")
  elif guess<number_guess:
    win=False
    print("Your guess is too low")
  elif guess==number_guess:
    win=True
    print("You guessed the number")
    number_of_guesses=0
  number_of_guesses-=1
if win==False:
  print("You have no attempts left")
  print("You lose")
if win==True:
  print("You win")
