from tkinter import *
import math

window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20, bg="yellow")

#NOTE ------ ------------------------- COUNTDOWN SYSTEM

seconds = 1 * 1000
timer = Label(text="00:00")
timer.pack()


reset_btn = Button(text="Reset")
reset_btn.pack()

def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60


    timer.config(text=f"{count_min}:{'00'if count_sec == 0 else count_sec}")

    if count > 0:
        window.after(seconds, countdown, count - 1)

def start_timer(): 
    countdown(5 * 60)

start_btn = Button(text="Start", command=start_timer)
start_btn.pack()


window.mainloop()