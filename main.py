from multiprocessing import Process, cpu_count
from tkinter import *
from time import *
import pyfirmata as fir
from datetime import datetime
def wind():
    if 0 == 0:
        def click():
            global count
            count += 1
            global z
            z = 5
        def update():
            time_string = strftime("%H:%M:%S")
            time_label.config(text=time_string)
            window.after(1000, update)

        window = Tk()
        window.geometry("540x600")
        window.title("DOTS timer")
        icon = PhotoImage(file='icon.png')
        window.iconphoto(True,icon)
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

        #button = Button(window,
                        #command=click,
                        #font=("Comic Sans", 30),
                        #fg="#00FF00",
                        #bg="black",
                        #activeforeground="#00FF00",
                        #activebackground="black",
                        #state=ACTIVE,
                        #image=starb,
                        #compound='bottom')
        #button.pack()

        update()
        mainloop()
    else:
        print("fail")
def clok():
    if 0 == 0:
        now = datetime.now()
        current_time = now.strftime("%H%M")
        a = fir.Arduino('COM3')
        h = 0
        while 0 == 0:
            while now == now:
                p = current_time
                x = int(p[0])
                y = int(p[1])
                z = int(p[2])
                w = int(p[3])

                if x >= int(0):
                    if x == int(1):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(2):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(1)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(3):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(4):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(5):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(6):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(7):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(8):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    elif x == int(9):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                    else:
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[10].write(1)
                else:
                    print("hello world")
                a.digital[10].write(0)
                if y >= int(0):
                    if y == int(1):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(2):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(1)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(3):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(4):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(5):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(6):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(7):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(8):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    elif y == int(9):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                    else:
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[11].write(1)
                else:
                    print("hello world")
                a.digital[11].write(0)
                if z >= int(0):
                    if z == int(1):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(2):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(1)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(3):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(4):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(5):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(6):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(7):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(8):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    elif z == int(9):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                    else:
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                else:
                    print("hello world")
                a.digital[12].write(0)
                if w >= int(0):
                    if w == int(1):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(2):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(1)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(3):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(4):
                        a.digital[2].write(1)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(5):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(6):
                        a.digital[2].write(0)
                        a.digital[3].write(1)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(7):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(1)
                        a.digital[6].write(1)
                        a.digital[7].write(1)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(8):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    elif w == int(9):
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(1)
                        a.digital[7].write(0)
                        a.digital[8].write(0)
                        a.digital[9].write(1)
                        a.digital[13].write(1)
                    else:
                        a.digital[2].write(0)
                        a.digital[3].write(0)
                        a.digital[4].write(0)
                        a.digital[5].write(0)
                        a.digital[6].write(0)
                        a.digital[7].write(0)
                        a.digital[8].write(1)
                        a.digital[9].write(1)
                        a.digital[12].write(1)
                else:
                    print("hello world")
                a.digital[13].write(0)
                # if not now == datetime.now():
                # print(current_time)
                current_time = now.strftime("%H%M")
                now = datetime.now()

            else:
                print("end")
        else:
            print("endzz")
    else:
        print("fatal error")
    mainloop()

def main():

    print("cpu count:", cpu_count())

    a = Process(target=wind)
    b = Process(target=clok)

    a.start()
    b.start()


    print("processing...")

    a.join()
    b.join()

    print("Done!")



if __name__ == '__main__':
    main()