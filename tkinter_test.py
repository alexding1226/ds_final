from tkinter import *

root = Tk()

e = Entry(root,width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    #e.delete(0, END)
    #e.insert(0, str(current) + str(number))
    e.insert(END,number)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
root.mainloop()