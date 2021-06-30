# Page1
from tkinter import ttk
import tkinter as tk
i = 0

def topFrame():
    
    global i
    l1 = tk.Label(window, text='Task', bg='yellow', font=('Arial', 12))
    l1.grid(row=0+2*i, column=0)
    e1 = tk.Entry(window, show = None, font = ('Arial', 14))
    e1.grid(row=0+2*i, column=1)
    l2 = tk.Label(window, text='Duration', bg='yellow', font=('Arial', 12))
    l2.grid(row=0+2*i, column=2)
    e2 = tk.Entry(window, show = None, font = ('Arial', 14))
    e2.grid(row=0+2*i, column=3)
    l3 = tk.Label(window, text='Deadline', bg='yellow', font=('Arial', 12))
    l3.grid(row=0+2*i, column=4)
    e3 = tk.Entry(window, show = None, font = ('Arial', 14))
    e3.grid(row=0+2*i, column=5, columnspan = 5)

    l4 = tk.Label(window, text='Type', bg='yellow', font=('Arial', 12))
    l4.grid(row=1+2*i, column=0)
    w1 = ttk.Combobox(window, values=["A", "B", "C", "D", "E"])
    w1.grid(row=1+2*i, column=1)


    l5 = tk.Label(window, text='Importancy', bg='yellow', font=('Arial', 12))
    l5.grid(row=1+2*i, column=2)
    s5 = tk.Scale(window, label='       ', from_=1, to=5, orient=tk.HORIZONTAL, showvalue=0,tickinterval=2, resolution=1)
    s5.grid(row=1+2*i, column=3)

    l6 = tk.Label(window, text='Successive', bg='yellow', font=('Arial', 12))
    l6.grid(row=1+2*i, column=4)
    varA = tk.IntVar()  # 定義varA整型變數用來存放選擇行為返回值
    varB = tk.IntVar()
    varC = tk.IntVar()
    varD = tk.IntVar()
    varE = tk.IntVar()

    c1 = tk.Checkbutton(window, text='A',variable=varA, onvalue=1, offvalue=0)    # 傳值原理類似於radiobutton部件
    c1.grid(row=1+2*i, column=5)
    c2 = tk.Checkbutton(window, text='B',variable=varB, onvalue=1, offvalue=0)
    c2.grid(row=1+2*i, column=6)
    c3 = tk.Checkbutton(window, text='C',variable=varC, onvalue=1, offvalue=0)
    c3.grid(row=1+2*i, column=7)
    c4 = tk.Checkbutton(window, text='D',variable=varD, onvalue=1, offvalue=0)
    c4.grid(row=1+2*i, column=8)
    c5 = tk.Checkbutton(window, text='E',variable=varE, onvalue=1, offvalue=0)
    c5.grid(row=1+2*i, column=9)
    
    i += 1
    
    
window = tk.Tk()
window.title('My Window')
window.geometry('800x500')


topFrame()

bt_addTask = tk.Button(window, text="Add Task", command=topFrame())
bt_addTask.grid(row=2+2*i, column=9)


window.mainloop()
