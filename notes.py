from tkinter import *
from tkinter import ttk
import tkinter


class Notes(tkinter.Tk):
    def __init__(self, tasks=None):
        super().__init__()
        self.bgColor = ["RoyalBlue","DarkSlateBlue", "DarkMagenta"]

        if not tasks:
            self.tasks = []
            task1 = tkinter.Label(self, text="Today's NOTES", bg="white", fg="tomato", pady=20, font=("Times",23))
            task1.pack(side=tkinter.TOP, fill=tkinter.X)
    
        self.taskCreate = tkinter.Text(self, height=3, bg="DarkCyan", fg="white")
        self.taskCreate.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.taskCreate.focus_set()
        
        self.bind('<Return>', self.addTask)

         
    def addTask(self, event=None):
        newText = self.taskCreate.get(1.0,tkinter.END).strip()
        
        if len(newText) > 0:
            newTask = tkinter.Label(self, text = newText, pady=20)
            doneButton = ttk.Button(newTask, text = "done",command = lambda:self.removeTask(doneButton))
            
            bgIdx = len(self.tasks)%len(self.bgColor)
            bgc = self.bgColor[bgIdx]
            
            newTask.configure(bg=bgc,fg="white",font=("Times",20))
            
            newTask.pack(side=tkinter.TOP, fill=tkinter.X)
            doneButton.pack(side=tkinter.RIGHT)
            
            self.tasks.append(newTask)
            
        self.taskCreate.delete(1.0, tkinter.END)
        
    def removeTask(self, done_button):
        done_button.pack_forget()
        done_button.master.pack_forget()
        self.tasks.remove(done_button.master)

    def closing(self):
        write = open("data.txt","w")
        for item in self.tasks:
            print(item.cget("text"),file=write)
        write.close()
        self.destroy()
    


if __name__ == "__main__":
    #saved tasks
    try:
        read = open("notes.txt","r")
    except FileNotFoundError:
        file = open("notes.txt","w")
        file.close()
        read=open("notes.txt","r")
        
    notes_lst=[]
    for line in readfile:
        line=line.strip()
        notes_lst.append(line)
    
    notes = Notes(notes_lst)
    notes.title("NOTES")
    notes.geometry("700x500")
    notes.protocol("WM_DELETE_WINDOW", notes.closing)
    notes.mainloop()
    


