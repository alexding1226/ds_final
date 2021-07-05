from tkinter import *
from tkinter import ttk
from tkinter import Button
import tkinter


class NotesPage(Frame):
    def __init__(self,master,data, task=None):
        super().__init__(master)
        self.bgColor = ["RoyalBlue","DarkSlateBlue", "DarkMagenta", "Teal", "Indigo", "PaleVioletRed", "Crimson", "FireBrick","IndianRed", "Peru", "DarkGoldenRod", "OliveDrab", "LightSeaGreen", "CornflowerBlue", "DarkBlue", "DarkSlateBlue"]
        self["height"] = 500
        self["width"] = 800
        self.pack_propagate(0)
        self.data =data
        
        if not task:
            self.tasks = []
            task1 = Label(self, text="NOTES", bg="white", fg="tomato", pady=20, font=("Times",23))
            task1.pack(side=TOP, fill=X)
    
        self.taskCreate = Text(self, height=1, bg="DarkCyan", fg="white")
        self.taskCreate.pack(side=BOTTOM, fill=X)
        self.taskCreate.focus_set()
        self.instru = Label(self, text="Fill your note below and press ENTER. (Maximum 40 words, 16 notes)", fg="black")
        self.instru.pack(side=BOTTOM)
        self.taskCreate.bind('<Return>', self.addTask)
        

    def addTask(self, event):
        self.newText = self.taskCreate.get(1.0,END).strip()
    
        if len(self.newText) > 0:
            self.newTask = Label(self, text = self.newText, pady=20)
            self.tasks.append(self.newTask)
            #self.doneButton = Button(self.newTask, text = "done",command = lambda:self.tasks.remove(self.doneButton.master))
            #print(self.newText)
            self.bgIdx = len(self.tasks)%len(self.bgColor)
            self.bgc = self.bgColor[self.bgIdx]
            self.newTask.configure(bg=self.bgc,fg="white",font=("Times",20))
            self.newTask.pack(side=TOP, fill=X)
            doneButton = Button(self.newTask, text = "done",command = lambda:self.removeTask(doneButton))
            doneButton.pack(side=RIGHT)
   
        self.taskCreate.delete(1.0, END)
        
    def removeTask(self, doneButton):
        doneButton.pack_forget()
        doneButton.master.pack_forget()
        self.tasks.remove(doneButton.master)



if __name__ == "__main__":

    root = Tk()
    root.geometry ("1050x700")
    notes = NotesPage(root)
    notes.pack()
    root.mainloop()