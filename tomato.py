import time
import datetime
from tkinter import *
import tkinter.ttk as ttk
class Task():
    def __init__(self,name,duration,importance,deadline,type = "study",successive = False) :
        self.name = name
        self.duration = duration
        self.importance = importance
        self.deadline = deadline
        self.type = type
        self.successive = successive

class AllTasks():
    def __init__(self,tasks) :
        self.tasks = tasks
    def add(self,task):
        self.tasks.append(task)
    def sort(self ,type, rev = True):
        if type == "type":
            self.tasks = sorted(self.tasks,key= lambda task:task.type,reverse = not (rev))
            return self.tasks
        elif type == "importance":
            self.tasks = sorted(self.tasks,key= lambda task:task.importance,reverse = (rev))
            return self.tasks
        elif type == "deadline":
            self.tasks = sorted(self.tasks,key= lambda task:task.deadline,reverse = (rev))
            return self.tasks
        elif type == "duration":
            self.tasks = sorted(self.tasks,key= lambda task:task.duration,reverse = (rev))
            return self.tasks
        elif type == "name":
            self.tasks = sorted(self.tasks,key= lambda task:task.name,reverse = not (rev))
            return self.tasks
class Data():
    def __init__(self) :
        self.clock_time = 25
        self.alltasks = AllTasks([])


class main(Tk):
    def __init__(self,data) :
        super().__init__()
        self._frame = None
        self.geometry("500x500")
        self.duration = 50
        self.remaintime = self.duration
        self.counting = False
        self.switch_frame(StartPage,data)
        Button(text="config",command=lambda:self.switch_frame(StartPage,data)).grid(column=0,row=0)
        Button(text="tomato clock",command=lambda:self.switch_frame(Tomato,data)).grid(column=0,row=1)
        Button(text="all tasks",command=lambda:self.switch_frame(AllTasksPage,data)).grid(column=0,row=2)
    def switch_frame(self, frame_class,data):
        new_frame = frame_class(self,data)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(column = 1,row = 0,columnspan =5)
    def count_down(self):
        self.counting = True
        self.remaintime -= 1
        if self.remaintime >0:
            self.after(1000,self.count_down)
        else:
            self.remaintime = self.duration
            self.counting = False
        pass

class StartPage(Frame):
    def __init__(self, master,data):
        Frame.__init__(self, master)
        Label(self, text="config", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        self.e_duration = Entry(self,width= 50 )
        self.e_duration.insert(0,master.duration)
        self.e_duration.pack()
        self.confirm_button = Button(self,text="confirm",command=self.confirm_duration)
        self.confirm_button.pack()
    def confirm_duration(self):
        self.master.duration = int(self.e_duration.get())
        self.master.remaintime = int(self.e_duration.get())



class Tomato(Frame):
    def __init__(self,master,data):
        Frame.__init__(self, master)
        Label(self, text="tomato clock", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        self.remaintime = Label(self,text=str(master.remaintime))
        self.remaintime.pack()
        self.remaintime.after(1000,self.update)
        self.start_button = Button(self,text="start",command=self.count_down)
        if master.counting:
            self.start_button["state"] = DISABLED
        self.start_button.pack()
    def update(self) :
        self.remaintime["text"]=str(self.master.remaintime)
        self.remaintime.after(1000,self.update)
    def count_down(self):
        self.start_button["state"] = DISABLED
        self.master.count_down()

class AllTasksPage(Frame):
    def __init__(self,master,data):
        Frame.__init__(self, master)
        self.data = data
        self.alltasks = data.alltasks
        self.frame_config = Frame(self)
        self.frame_config.grid(row=0,column=0)
        self.frame_tasks = Frame(self)
        self.frame_tasks.grid(row=1,column=0)
        for task in self.alltasks.tasks:
            task_label =Label(self.frame_tasks, font=('Helvetica', 18, "bold"))
            task_label["text"] = task.name + "  " + task.importance * "*" + "  "+str(task.duration) + "hrs"
            task_label.pack(side="top", fill="x", pady=5)
        sort_combobox = ttk.Combobox(self.frame_config,values=["name","importance","duration"],state="readonly")
        sort_combobox.current(0)
        sort_combobox.grid(row=0,column=0)
        Button(self.frame_config,text="confirm",command = lambda: self.sort(sort_combobox.get())).grid(column=1,row=0)


    def sort(self,type):
        self.frame_tasks.destroy()
        self.frame_tasks = Frame(self)
        self.frame_tasks.grid(row=1,column=0)
        self.alltasks.tasks = data.alltasks.sort(type)
        for task in self.alltasks.tasks:
            task_label =Label(self.frame_tasks, font=('Helvetica', 18, "bold"))
            task_label["text"] = task.name + "  " + task.importance * "*" + "  "+str(task.duration) + "hrs"
            task_label.pack(side="top", fill="x", pady=5)

t1 = Task("a",5,3,20)
t2 = Task("b",2,2,29)
t3 = Task("c",3,4,29)
all = AllTasks([t1,t2,t3])
data = Data()
data.alltasks = all

app = main(data)
app.mainloop()