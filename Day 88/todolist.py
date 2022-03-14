import tkinter

wn = tkinter.Tk()
wn.minsize(1920, 1080)
wn.configure(bg="#FF6363")

Welcome = tkinter.Label(text="Ready to Make your day more Productive?", font=("Arial", 24, "bold"), bg="#FF6363")
Welcome.place(x=600, y=0)

new_goal = tkinter.Entry(width=50, font=("Arial", 18))
new_goal.place(x=575, y=100)
x = 1
checkboxes = []


def new_todo():
    global x

    def checkbutton_used():
        # Prints 1 if On button checked, otherwise 0.
        if checked_state.get() == 1:
            new_label.destroy()
            new_label_check.destroy()

    new_label = tkinter.Label(text=new_goal.get(), font=("Arial", 19), width=10, bg="#9AD0EC",padx=960 )
    new_label.place(x=0, y=x*40+100, )

    checked_state = tkinter.IntVar()
    new_label_check = tkinter.Checkbutton(text="", variable=checked_state, command=checkbutton_used, font=("Arial", 15), bg="#9AD0EC")
    checked_state.get()
    new_label_check.place(x=1800, y=x * 40 + 100)
    checkboxes.append(new_label_check)
    x += 1





create = tkinter.Button(text="Create", command=new_todo, width=10, font=("Arial", 12))
create.place(x=1309, y=101)
wn.mainloop()
