from tkinter import *
from timeit import default_timer as timer
import random
import requests
r = requests.get(
    "https://random-word-api.herokuapp.com/word?number=10")
# print(r.json())
# creating window using gui
window = Tk()
print(r.text)
# the size of the window is defined
window.geometry("450x200")

x = 0


# defining the function for the test
def game():
    global x

    # loop for destroying the window
    # after on test
    if x == 0:
        window.destroy()
        x = x + 1

    # defining function for results of test
    def check_result():
        correct = 0
        end = timer()
        typed_words = entry.get().split()
        print(typed_words)
        for num in range(len(typed_words)):
            if typed_words[num] == words[num].strip():
                # print(words[num])
                # print(typed_words[num])
                correct += 1
        accuracy = correct*100/len(words)
        print(f"Accuracy: {accuracy}%, ")

    words = r.json()
    random_word = words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5] + " " + words[6] + " " + words[7] + " " + words[8] + " " + words[9]
    print(random_word)

    # Give random words for testing the speed of user
    word = random.randint(0, (len(words) - 1))

    # start timer using timeit function
    start = timer()
    windows = Tk()
    windows.geometry("1980x200")

    # use label method of tkinter for labeling in window
    x2 = Label(windows, text=random_word, font="times 20")

    # place of labeling in window
    x2.place(x=150, y=10)
    x3 = Label(windows, text="Start Typing", font="times 20")
    x3.place(x=10, y=50)

    entry = Entry(windows, width=len(random_word))
    entry.place(x=280, y=55)

    # buttons to submit output and check results
    b2 = Button(windows, text="Done",
                command=check_result, width=12, bg='grey')
    b2.place(x=150, y=100)

    b3 = Button(windows, text="Try Again",
                command=game, width=12, bg='grey')
    b3.place(x=250, y=100)
    windows.mainloop()


x1 = Label(window, text="Lets start playing..", font="times 20")
x1.place(x=10, y=50)

b1 = Button(window, text="Go", command=game, width=12, bg='grey')
b1.place(x=150, y=100)



# calling window
window.mainloop()