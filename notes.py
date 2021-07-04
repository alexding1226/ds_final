from tkinter import *
from tkinter import ttk
import tkinter


class NotesPage(Frame):
    def __init__(self,master,data, tasks=None):
        super().__init__(master)
        self.bgColor = ["RoyalBlue","DarkSlateBlue", "DarkMagenta", "Teal", "Indigo", "PaleVioletRed", "Crimson", "FireBrick","IndianRed", "Peru", "DarkGoldenRod", "OliveDrab", "LightSeaGreen", "CornflowerBlue", "DarkBlue", "DarkSlateBlue"]
        self.data = data
        if not tasks:
            self.tasks = []
            task1 = tkinter.Label(self, text="NOTES", bg="white", fg="tomato", pady=20, font=("Times",23))
            task1.pack(side=tkinter.TOP, fill=tkinter.X)
    
        self.taskCreate = tkinter.Text(self, height=1, bg="DarkCyan", fg="white")
        self.taskCreate.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.taskCreate.focus_set()
        self.instru = tkinter.Label(self, text="Fill your note below and press ENTER. (Maximum 40 words, 16 notes)", fg="black")
        self.instru.pack(side=tkinter.BOTTOM)
        
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
"""
    def closing(self):
        write = open("data.txt","w")
        for item in self.tasks:
            print(item.cget("text"),file=write)
        write.close()
        self.destroy()
"""


if __name__ == "__main__":
    # Saved tasks in local

#    try:
#        read = open("notes.txt","r")
#    except FileNotFoundError:
#        file = open("notes.txt","w")
#        file.close()
#        read=open("notes.txt","r")
#        
    notes_lst=[]
#    for line in read:
#        line=line.strip()
#        notes_lst.append(line)
    root =Tk()
    root.geometry = "750x1000"
    notes = NotesPage(root,notes_lst)
    notes.pack()
    # Please modify the windows size
#    root.protocol("WM_DELETE_WINDOW", notes.closing)
    root.mainloop()