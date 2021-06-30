import math
import tkinter
from tkinter import ttk
from tkinter import StringVar
from PIL import Image, ImageTk


reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    tick.config(text="")


def start_timer(work):
    global reps
    reps += 1
    work_sec = work * 60
    short_break_sec = (work%10) * 60
    

    if reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work")


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = " "
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✓"
        tick.config(text=mark)



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



title = Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1,row=0)

img = Image.open('tomato.jpg')
photo = ImageTk.PhotoImage(img)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(103, 138, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)
var = 0
value = StringVar()
 
def getVal():
    global var
    if value.get() == "25":
        var = 25
    elif value.get() == "40":
        var = 40
    else:
        var = 55
    
value = StringVar()
ls1 = ttk.Combobox(window, textvariable = value, values=["25", "40", "55"], postcommand = getVal)
ls1.grid(column=5, row=5)


def select():
    start_timer(var)
    
start_button = Button(text="Start", highlightthickness=0, command=select)
start_button.grid(column=0,row=2)
                     
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

tick = Label(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
tick.grid(column=1,row=3)

#
window.mainloop()
