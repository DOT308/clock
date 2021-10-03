from tkinter import *
from time import *
import time
import one as one
import pyfirmata as fir
from datetime import datetime

count = 0


def click():
    global count
    count += 1


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    window.after(1000, update)


window = Tk()
window.geometry("540x840")
window.title("DOTS timer")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
window.config(background='black')  # hex colour picker
photo = PhotoImage(file='time.png')
starb = PhotoImage(file='starb.png')
label = Label(window,
              text="The time has come",
              font=("Arial", 32, "bold"),
              fg="orange",
              bg="black",
              # relief=RAISED,
              # bd=10,
              padx=4,
              pady=4,
              image=photo,
              compound='bottom')

label.pack()
time_label = Label(window,
                   font=("Arial", 30),
                   fg="orange",
                   bg="black",
                   padx=4,
                   pady=4)
time_label.pack()

button = Button(window,
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=starb,
                compound='bottom')
button.pack()

update()
mainloop()
