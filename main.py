from calendar import month
from enum import Flag
from re import T, split
import time
import datetime
from datetime import date
from tkinter import *
from tkinter import font
from tkinter.font import ITALIC
import tkinter.ttk as ttk
from typing import Pattern
from tkcalendar import Calendar
from tkinter import messagebox
#import red_black_tree as rbt
import random
import string
import application
import notes
import schedule  as sch
import DataFormat

class Task():
    def __init__(self,name,duration,importance,date,type = "work",time_finished = 0) :
        self.name = name
        self.duration = duration
        self.importance = importance
        self.type = type
        self.date = date
        self.time_finished = time_finished
class AllTasks():
    def __init__(self,tasks) :
        self.tasks = dict()
        for task in tasks:
            self.tasks[task.name] = task
        #self.rbt = rbt.RBTree()
        #for task in tasks:
        #    self.rbt.insert(key=task.name,data=task)
    def add(self,task):
        self.tasks[task.name] = task
        #self.rbt.insert(key=task.name,data = task)
    def sort(self ,type, rev = True):
        if type == "type":
            a = sorted(self.tasks.items(),key = lambda task:task[1].type ,reverse = not (rev))
            return a
        elif type == "importance":
            a = sorted(self.tasks.items(),key = lambda task:task[1].importance ,reverse = (rev))
            return a
        elif type == "duration":
            a = sorted(self.tasks.items(),key = lambda task:task[1].duration ,reverse =  (rev))
            return a
        elif type == "deadline":
            a = sorted(self.tasks.items(),key = lambda task:task[1].date ,reverse = not (rev))
            return a
        elif type == "name":
            a = sorted(self.tasks.keys(),reverse = not (rev))
            return a
    """
    def algorithm(self):
        self.today = [Task("a",0.5,3,[7,20]),Task("b",2,2,[8,30])]
        self.today[0].whentodo = [7,1,0]
        self.today[1].whentodo = [7,1,21]
    """
    def delete(self,task):
        del self.tasks[task.name]
        #self.rbt.delete(key=task.name)
class FinishedTasks():
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
        elif type == "duration":
            self.tasks = sorted(self.tasks,key= lambda task:task.duration,reverse =  (rev))
            return self.tasks
        elif type == "name":
            self.tasks = sorted(self.tasks,key= lambda task:task.name,reverse = not (rev))
            return self.tasks
        elif type == "deadline":
            self.tasks = sorted(self.tasks,key= lambda task:task.date,reverse = not (rev))
            return self.tasks
    def delete(self,task):
        self.tasks.remove(task)
class Data():
    def __init__(self,all,finished) :
        self.alltasks = all
        self.types = ["work","exercise","life"]
        self.all_color = [["deep sky blue","light sky blue"],["deep pink","pink"],["green2","palegreen1"],
                            ["yellow","#FFFF99"],["#9966CC","#CC99CC"],["#2376bd","#99c2e4"]]
        self.cand_color = [["yellow","#FFFF99"],["#9966CC","#CC99CC"],["#2376bd","#99c2e4"]]
        self.typecolor = {"work":["deep sky blue","light sky blue"],"exercise":["deep pink","pink"],"life":["green2","palegreen1"]}
        self.finishtasks =finished
        self.schedule = []
        self.period = {"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[],"Sunday":[]}
        t = open("data/tasks.txt")
        tasks = t.read().splitlines()
        for task in tasks:
            task_items = task.split("/")
            name = task_items[0]
            duration = float(task_items[1])
            importance = int(task_items[2])
            type = task_items[3]
            time_finished = float(task_items[4])
            date = task_items[5].split(",")
            date[0] = int(date[0])
            date[1] = int(date[1])
            ta = Task(name,duration,importance,date,type,time_finished)
            self.add(ta)
        f = open("data/finished_tasks.txt")
        tasks = f.read().splitlines()
        for task in tasks:
            task_items = task.split("/")
            name = task_items[0]
            duration = float(task_items[1])
            importance = int(task_items[2])
            type = task_items[3]
            time_finished = float(task_items[4])
            date = task_items[5].split(",")
            date[0] = int(date[0])
            date[1] = int(date[1])
            ta = Task(name,duration,importance,date,type,time_finished)
            self.finishtasks.add(ta)
        ty = open("data/type.txt")
        types = ty.read().splitlines()
        for type in types:
            type_items = type.split("/")
            self.types.append(type_items[0])
            self.typecolor[type_items[0]] = [type_items[1],type_items[2]]
        p = open("data/period.txt")
        days = p.read().splitlines()
        for day in days:
            day_items = day.split("/")
            day_items.pop()
            day_name = day_items[0]
            for day_period in day_items[1:]:
                day_period = day_period.split(",")
                day_period[0] = float(day_period[0])
                day_period[1] = float(day_period[1])
                self.period[day_name].append(day_period)
        s = open("data/schedule.txt")
        days = s.read().splitlines()
        for day in days:
            day_result = []
            periods = day.split("/")
            periods.pop()
            for period in periods:
                period_items = period.split(",")
                period_items.pop()
                period_items[1] = float(period_items[1])
                period_items[2] = float(period_items[2])
                period_items = tuple(period_items)
                day_result.append(period_items)
            self.schedule.append(day_result)
        
    def finished(self,task):
        self.alltasks.delete(task)
        self.finishtasks.add(task)
    def finished_part(self,task):
        task_in_all = self.alltasks.tasks[task[0]]
        if task_in_all.time_finished + task[2] - task[1] >= task_in_all.duration:
            self.alltasks.delete(task_in_all)
            self.finishtasks.add(task_in_all)
        else:
            task_in_all.time_finished += task[2] - task[1]        
    def add(self,task):
        self.alltasks.add(task)

    def scheduling(self):
        if len(self.alltasks.tasks)>0:
            days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
            today_weekday = days[datetime.datetime.today().weekday()]
            now =  datetime.datetime.now()
            now_hour = now.hour
            now_minute = now.minute
            taskslist = list(self.alltasks.tasks.values())
            today = datetime.datetime.today().date()
            toalgo_task = []
            for task in taskslist:
                deadline = date(2021,task.date[0],task.date[1])
                remainday = (deadline - today).days
                new_type_task = DataFormat.task_item(task.name,task.duration-task.time_finished,task.importance,remainday+1,24,1,task.type)
                toalgo_task.append(new_type_task)
            toalgo_period = []
            temp = 0
            today_period = self.period[today_weekday]
            period_amount = len(today_period)
            while temp < period_amount:
                if today_period[temp][0] > now_hour:
                    toalgo_period.append(DataFormat.period_item(1,today_period[temp][0],today_period[temp][1]))
                elif today_period[temp][0]//1 == now_hour:
                    if today_period[temp][0]%1 == 0.5 and now_minute < 30:
                        toalgo_period.append(DataFormat.period_item(1,today_period[temp][0],today_period[temp][1]))
                temp += 1
            temp = datetime.datetime.today().weekday()
            for i in range(1,10):
                index = int((temp+i)%7)
                for period in self.period[days[index]]:
                    toalgo_period.append(DataFormat.period_item(i+1,period[0],period[1]))
            algo =sch.schedule(toalgo_task,toalgo_period)
            if algo.Detect() == 0:
                schedule = algo.Schedule()
                for s in schedule:
                    s.sort(key = lambda task:task[1])
                self.schedule = schedule
            else:
                self.schedule = ["expire",algo.Detect()]
        else:
            self.schedule = ["no task"]
    def addtype(self,type):
        self.types.append(type)
        type_color_index = random.randint(0,len(self.cand_color)-1)
        type_color = self.cand_color.pop(type_color_index)
        self.typecolor[type] = type_color
        if len(self.cand_color) == 0:
            self.cand_color = self.all_color
    def save(self):
        type = open("data/type.txt","w")
        for key,value in self.typecolor.items():
            if key == "work" or key == "exercise" or key == "life":
                pass
            else:
                type.write(key + "/")
                type.write(value[0] + "/")
                type.write(value[1]  + "\n")
        type.close()
        t = open("data/tasks.txt","w")
        for task in self.alltasks.tasks.values():
            name = task.name + "/"
            duration = str(task.duration) + "/"
            type = task.type + "/"
            importance = str(task.importance) + "/"
            finishedtime = str(task.time_finished) + "/"
            deadline = str(task.date[0]) + "," + str(task.date[1]) + "\n"
            t.write(name + duration  + importance + type + finishedtime + deadline)
        t.close()
        p = open("data/period.txt","w")
        for day,periods in self.period.items():
            p.write(day + "/")
            for period in periods:
                p.write(str(period[0]) + "," + str(period[1]) + "/")
            p.write("\n")
        p.close()
        s = open("data/schedule.txt","w")
        if len(self.schedule)>0:
            if self.schedule == ["no task"]:
                s.write("no task")
            elif self.schedule[0] == "expire":
                s.write("expire/" + str(self.schedule[1]))
            else:
                for day in self.schedule:
                    for period in day:
                        for item in period:
                            item = str(item)
                            s.write(item + ",")
                        s.write("/")
                    s.write("\n")
        else:
            for a in self.schedule:
                s.write(a)
        s.close()
        f = open("data/finished_tasks.txt","w")
        for task in self.finishtasks.tasks:
            name = task.name + "/"
            duration = str(task.duration) + "/"
            type = task.type + "/"
            importance = str(task.importance) + "/"
            finishedtime = str(task.time_finished) + "/"
            deadline = str(task.date[0]) + "," + str(task.date[1]) + "\n"
            f.write(name + duration  + importance + type + finishedtime + deadline)
        f.close()

            







class main(Tk):
    def __init__(self,data) :
        super().__init__()
        self._frame = None
        self.geometry("1050x700")
        self.duration = 50
        self.data = data
        change_frame = Frame(self)
        change_frame.pack(side="left",fill="y")
        self.protocol("WM_DELETE_WINDOW",self.save)
        Button(change_frame,text="all tasks",command=lambda:self.switch_frame(AllTasksPage,data)).grid(column=0,row=2,pady=15,padx=15,sticky=N)
        Button(change_frame,text="schedule",command=lambda:self.switch_frame(SchedulePage,data)).grid(column=0,row=3,pady=15,padx=15,sticky=N)
        Button(change_frame,text = "set period",command=lambda:self.switch_frame(PeriodPage,data)).grid(column=0,row=4,pady=15,padx=15,sticky=N)
        Button(change_frame,text="pomodoro",command=pomodoro).grid(column=0,row=5,pady=15,sticky=N)
        Button(change_frame,text="notes",command=lambda:self.switch_frame(notes.NotesPage,data)).grid(column=0,row=6,pady=15,sticky=N)
        Button(change_frame,text="為你安排行程!",command= self.scheduling).grid(column=0,row = 7,pady=15,sticky=N)
        self.switch_frame(AllTasksPage,data)
    
    def switch_frame(self, frame_class,data):
        new_frame = frame_class(self,data)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(side = "left",fill = "both")
    def scheduling(self):
        self.data.scheduling()
        if self.data.schedule[0] == "expire":
            today = datetime.datetime.today()
            days = datetime.timedelta(days=self.data.schedule[1]-1)
            expireday = today + days
            expiredate = [expireday.month,expireday.day]
            messagebox.showwarning("expire","task expire at day %d/%d"%(expiredate[0],expiredate[1]))
        elif self.data.schedule[0] == "no task":
            messagebox.showinfo("no task","add a task first")
    def save(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.data.save()
            self.destroy()
def pomodoro():
    global pomodoro_frame
    top = Toplevel()
    top.title("pomodoro")
    top.geometry("500x500")
    top.configure(bg="#ffbc92")
    pomodoro_frame = application.PomodoroPage(top)
    pomodoro_frame.pack()

#from https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame
class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    """
    def __init__(self, parent,height,width=None, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            
        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,height=height,
                        yscrollcommand=vscrollbar.set)
        if width:
            canvas["width"] = width
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        canvas.pack_propagate(0)
        vscrollbar.config(command=canvas.yview)
        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        self.interior["width"] = 1000
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)
        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)
        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)
class AllTasksPage(Frame):
    def __init__(self,master,data):
        Frame.__init__(self, master)
        self.data = data
        self.master = master
        self.alltasks = data.alltasks
        self.frame_config = Frame(self)
        self.frame_config.grid(row=0,column=0,sticky=W)
        self.frame_tasks = VerticalScrolledFrame(self,425)
        self.frame_tasks["height"] = 500
        self.frame_tasks["width"] = 1000
        self.frame_tasks.grid_propagate(0)
        self.frame_tasks.grid(row=1,column=0,rowspan=10,pady = 15)
        taskrow = 0
        if len(self.alltasks.tasks) == 0:
            no_task_frame = Frame(self.frame_tasks.interior,width=800,height=25)
            no_task_frame.grid(row=0,column=0,pady=5,sticky=W)
            no_task_frame.grid_propagate(0)
            no_task_label = Label(no_task_frame,text="there is no unfinished task, add one below")
            no_task_label.place(anchor="c",relx=.5,rely=.5)
            taskrow = 1
        for task in self.alltasks.tasks.values():
            color = self.data.typecolor[task.type][0]
            task_frame =Frame(self.frame_tasks.interior,bg=color)
            task_frame.grid(row = taskrow,column = 0, pady=5,sticky=W)
            name_label=Label(task_frame,text=task.name,width=20,bg=color)
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
            imp_l = Label(task_frame,text="*" * task.importance,width=5,bg=color)
            imp_l.grid_propagate(0)
            imp_l.grid(row=0,column=1,padx=20,sticky=W)
            du_l = Label(task_frame,text=str(task.time_finished) +"/" + str(task.duration)+"hrs",width=8,bg=color)
            du_l.grid(row=0,column=2,padx=20)
            du_l.grid_propagate(0)
            date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20,bg=color)
            date_l.grid_propagate(0)
            date_l.grid(row=0,column=3,padx=20,sticky=W)
            type_l = Label(task_frame,text=task.type,width = 10,bg=color)
            type_l.grid(row=0,column=4,padx = 30,sticky=E)
            type_l.grid_propagate(0)
            task_button = TaskChangeButton(self.frame_tasks.interior,task,taskrow,task_frame,self.data)
            task_button.grid(row = taskrow,column = 1)
            finished_button = FinishButton(task_frame,task,self.data,self,master)
            finished_button["bg"] = color
            finished_button.grid(row=0,column=5)
            delete_button = Delete_notfinishButton(task_frame,task,self.data,self.master)
            delete_button["bg"] = color
            delete_button.grid(row =0,column=6,padx=10)
            taskrow += 1
        self.finished_frame = Frame()
        if len(self.data.finishtasks.tasks)>0:
            self.finished_frame = Frame(self.frame_tasks.interior)
            self.finished_frame.grid(row=taskrow,column=0)
            task_frame =Frame(self.finished_frame)
            task_frame.grid(row = 0,column = 0, pady=30,sticky=W)
            name_label=Label(task_frame,text="finished tasks:")
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
        finished_row = 1
        for task in self.data.finishtasks.tasks:
            color = self.data.typecolor[task.type][1]
            task_frame =Frame(self.finished_frame,width=800,height=25,bg=color)
            task_frame.grid(row = finished_row,column = 0, pady=5,sticky=W)
            task_frame.grid_propagate(0)
            name_label=Label(task_frame,text=task.name,width=20,bg=color)
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
            imp_l = Label(task_frame,text="*" * task.importance,width=5,bg=color)
            imp_l.grid_propagate(0)
            imp_l.grid(row=0,column=1,padx=20,sticky=W)
            du_l = Label(task_frame,text=str(task.duration)+"hrs",width=8,bg=color)
            du_l.grid(row=0,column=2,padx=20)
            du_l.grid_propagate(0)
            date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20,bg=color)
            date_l.grid_propagate(0)
            date_l.grid(row=0,column=3,padx=20,sticky=W)
            type_l = Label(task_frame,text=task.type,width = 10,bg=color)
            type_l.grid(row=0,column=4,padx = 30,sticky=W)
            type_l.grid_propagate(0)
            delete_button = Delete_finishButton(task_frame,task,self.data,self.master)
            delete_button["bg"] = color
            delete_button.grid(row =0,column=5,padx=10)
            finished_row += 1
        self.add_task_button = Button(self,text="add task",command=self.add_task,font=('Corbel',16))
        self.add_task_button.grid(row=30,column=0,pady=30)
        sort_combobox = ttk.Combobox(self.frame_config,values=["name","importance","duration","deadline","type"],state="readonly",width=10)
        sort_combobox.current(0)
        sort_combobox.grid(row=0,column=1,padx = 10,pady=10)
        Label(self.frame_config,text="sort by:").grid(row=0,column=0)
        rev = BooleanVar()
        check_reverse =  Checkbutton(self.frame_config,text="reverse",variable=rev,onvalue=True,offvalue=False)
        check_reverse.grid(column = 2,row = 0,padx=10,pady=10)
        Button(self.frame_config,text="confirm",command = lambda: self.sort(sort_combobox.get(),rev.get())).grid(column=3,row=0,padx=10,pady=10)
        Label(self,text="Name").place(x=68,y=40)
        Label(self,text="importance").place(x=170,y=40)
        Label(self,text="time").place(x=300,y=40)
        Label(self,text="deadline").place(x=430,y=40)
        Label(self,text="type").place(x=605,y=40)
    def sort(self,type,rev):
        self.frame_tasks.destroy()
        self.frame_tasks = VerticalScrolledFrame(self,425)
        self.frame_tasks.grid(row=1,column=0,pady=15)
        tasks = self.data.alltasks.sort(type,not rev)
        taskrow = 0
        if len(self.alltasks.tasks) == 0:
            no_task_frame = Frame(self.frame_tasks.interior,width=800,height=25)
            no_task_frame.grid(row=0,column=0,pady=5,sticky=W)
            no_task_frame.grid_propagate(0)
            no_task_label = Label(no_task_frame,text="there is no unfinished task, add one below")
            no_task_label.place(anchor="c",relx=.5,rely=.5)
            taskrow = 1
        for task in tasks:
            if type == "name":
                task = task
            else:
                task = task[1]
            color = self.data.typecolor[task.type][0]
            task_frame =Frame(self.frame_tasks.interior,bg=color)
            task_frame.grid(row = taskrow,column = 0, pady=5,sticky=W)
            name_label=Label(task_frame,text=task.name,width=20,bg=color)
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
            imp_l = Label(task_frame,text="*" * task.importance,width=5,bg=color)
            imp_l.grid_propagate(0)
            imp_l.grid(row=0,column=1,padx=20,sticky=W)
            du_l = Label(task_frame,text=str(task.time_finished) +"/" + str(task.duration)+"hrs",width=8,bg=color)
            du_l.grid(row=0,column=2,padx=20)
            du_l.grid_propagate(0)
            date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20,bg=color)
            date_l.grid_propagate(0)
            date_l.grid(row=0,column=3,padx=20,sticky=W)
            type_l = Label(task_frame,text=task.type,width = 10,bg=color)
            type_l.grid(row=0,column=4,padx = 30,sticky=E)
            type_l.grid_propagate(0)
            task_button = TaskChangeButton(self.frame_tasks.interior,task,taskrow,task_frame,self.data)
            task_button.grid(row = taskrow,column = 1)
            finished_button = FinishButton(task_frame,task,self.data,self,self.master)
            finished_button["bg"] = color
            finished_button.grid(row=0,column=5)
            delete_button = Delete_notfinishButton(task_frame,task,self.data,self.master)
            delete_button.grid(row =0,column=6,padx=10)
            taskrow += 1
        self.finished_frame = Frame()
        if len(self.data.finishtasks.tasks)>0:
            self.finished_frame = Frame(self.frame_tasks.interior)
            self.finished_frame.grid(row=taskrow,column=0)
            task_frame =Frame(self.finished_frame)
            task_frame.grid(row = 0,column = 0, pady=30,sticky=W)
            name_label=Label(task_frame,text="finished tasks:")
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
        finished_row = 1
        for task in self.data.finishtasks.sort(type,not rev):
            color = self.data.typecolor[task.type][1]
            task_frame =Frame(self.finished_frame,width=800,height=25,bg=color)
            task_frame.grid(row = finished_row,column = 0, pady=5,sticky=W)
            task_frame.grid_propagate(0)
            name_label=Label(task_frame,text=task.name,width=20,bg=color)
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
            imp_l = Label(task_frame,text="*" * task.importance,width=5,bg=color)
            imp_l.grid_propagate(0)
            imp_l.grid(row=0,column=1,padx=20,sticky=W)
            du_l = Label(task_frame,text=str(task.duration)+"hrs",width=8,bg=color)
            du_l.grid(row=0,column=2,padx=20)
            du_l.grid_propagate(0)
            date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20,bg=color)
            date_l.grid_propagate(0)
            date_l.grid(row=0,column=3,padx=20,sticky=W)
            type_l = Label(task_frame,text=task.type,width = 10,bg=color)
            type_l.grid(row=0,column=4,padx = 30,sticky=W)
            type_l.grid_propagate(0)
            delete_button = Delete_finishButton(task_frame,task,self.data,self.master)
            delete_button["bg"] = color
            delete_button.grid(row =0,column=5,padx=10)
            finished_row += 1
        self.add_task_button = Button(self,text="add task",command=self.add_task)
        self.add_task_button.grid(row=30,column=0,pady=30)
        Label(self,text="Name").place(x=68,y=40)
        Label(self,text="importance").place(x=170,y=40)
        Label(self,text="time").place(x=300,y=40)
        Label(self,text="deadline").place(x=430,y=40)
        Label(self,text="type").place(x=605,y=40)
    def add_task(self):
        self.add_task_button.destroy()
        frame_addtask = Frame(self)
        frame_addtask.grid(row=30,column=0,pady=30,sticky=W)
        e_name = Entry(frame_addtask,width=20)
        e_name.insert(0,"Name")
        e_name.grid(column=0,row=0,padx=10)
        scale_importance = Scale(frame_addtask,from_= 1 ,to=5,orient=HORIZONTAL,length=50,width=10)
        scale_importance.grid(column=1,row=0,padx=20)
        e_duration = Entry(frame_addtask,width=3)
        e_duration.insert(0,1)
        e_duration.grid(column=2,row=0,padx=10)
        Label(frame_addtask,text="*30min").grid(row=0,column=3)
        now = datetime.datetime.now()
        cal = Calendar(frame_addtask,selectmode = "day",year = now.year,month = now.month,day = now.day,date_pattern = "yyyy/MM/dd")
        cal.grid(row = 0,column = 4,padx = 20)
        types=self.data.types[:]
        types.append("new")
        combo_type = ttk.Combobox(frame_addtask,values=types,width=10)
        combo_type.current(0)
        combo_type.grid(column=5,row=0,padx=10)
        confirm_button = Button(self,text="confirm"
                                ,command=lambda: self.add_confirm(frame_addtask,e_name,scale_importance,e_duration,cal,combo_type))
        confirm_button.grid(row=30,column=1,pady=30,sticky=W)
        self.confirm_button = confirm_button
    def add_confirm(self,frame,name,imp,dur,cal,type):
        ymd = cal.get_date().split("/")
        if name.get() not in self.data.alltasks.tasks:
            task = Task(name.get(),int(dur.get())/2,imp.get(),[int(ymd[1]),int(ymd[2])],type.get())
            self.data.alltasks.add(task)
            if type.get() not in self.data.types:
                self.data.addtype(type.get())
            color = self.data.typecolor[task.type][0]
            frame.destroy()
            self.confirm_button.destroy()
            self.add_task_button = Button(self,text="add task",command=self.add_task,font=('Corbel',16))
            self.add_task_button.grid(row=30,column=0,pady=30)
            task_frame =Frame(self.frame_tasks.interior,bg=color)
            task_frame.grid(row = len(self.data.alltasks.tasks)-1,column = 0, pady=5,sticky=W)
            name_label=Label(task_frame,text=task.name,width=20,bg=color)
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
            imp_l = Label(task_frame,text="*" * task.importance,width=5,bg=color)
            imp_l.grid_propagate(0)
            imp_l.grid(row=0,column=1,padx=20,sticky=W)
            du_l = Label(task_frame,text=str(task.time_finished) +"/" + str(task.duration)+"hrs",width=8,bg=color)
            du_l.grid(row=0,column=2,padx=20)
            du_l.grid_propagate(0)
            type_l = Label(task_frame,text=task.type,width = 10,bg=color)
            type_l.grid(row=0,column=4,padx = 30,sticky=E)
            type_l.grid_propagate(0)
            date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20,bg=color)
            date_l.grid_propagate(0)
            date_l.grid(row=0,column=3,padx=20,sticky=W)
            task_button = TaskChangeButton(self.frame_tasks.interior,task,len(self.data.alltasks.tasks)-1,task_frame,self.data)
            task_button.grid(row = len(self.data.alltasks.tasks)-1,column = 1)
            finished_button = FinishButton(task_frame,task,self.data,self,self.master)
            finished_button.grid(row=0,column=5)
            finished_button["bg"] = color
            delete_button = Delete_notfinishButton(task_frame,task,self.data,self.master)
            delete_button.grid(row =0,column=6,padx=10)
            delete_button["bg"] = color
            taskrow = len(self.data.alltasks.tasks)
            self.finished_frame.destroy()
            if len(self.data.finishtasks.tasks)>0:
                self.finished_frame = Frame(self.frame_tasks.interior)
                self.finished_frame.grid(row=taskrow,column=0,sticky=W)
                task_frame =Frame(self.finished_frame)
                task_frame.grid(row = 0,column = 0, pady=30,sticky=W)
                name_label=Label(task_frame,text="finished tasks:")
                name_label.grid(row = 0,column=0,padx=20,sticky=W)
                name_label.grid_propagate(0)
            finished_row = 1
            for task in self.data.finishtasks.tasks:
                color = self.data.typecolor[task.type][1]
                task_frame =Frame(self.finished_frame,bg=color)
                task_frame.grid(row = finished_row,column = 0, pady=5,sticky=W)
                name_label=Label(task_frame,text=task.name,width=20,bg=color)
                name_label.grid(row = 0,column=0,padx=20,sticky=W)
                name_label.grid_propagate(0)
                imp_l = Label(task_frame,text="*" * task.importance,width=5,bg=color)
                imp_l.grid_propagate(0)
                imp_l.grid(row=0,column=1,padx=20,sticky=W)
                du_l = Label(task_frame,text=str(task.time_finished) +"/" + str(task.duration)+"hrs",width=8,bg=color)
                du_l.grid(row=0,column=2,padx=20)
                du_l.grid_propagate(0)
                date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20,bg=color)
                date_l.grid_propagate(0)
                date_l.grid(row=0,column=3,padx=20,sticky=W)
                type_l = Label(task_frame,text=task.type,width = 10,bg=color)
                type_l.grid(row=0,column=4,padx = 30,sticky=E)
                type_l.grid_propagate(0)
                delete_button = Delete_finishButton(task_frame,task,self.data,self.master)
                delete_button["bg"] = color
                delete_button.grid(row =0,column=5,padx=10)
                finished_row += 1
        else:
            name = name.get()
            frame.destroy()
            self.confirm_button.destroy()
            self.add_task_button = Button(self,text="add task",command=self.add_task,font=('Corbel',16))
            self.add_task_button.grid(row=30,column=0,pady=30)
            messagebox.showwarning("Error","Name \"" + name + "\" already exist")


class FinishButton(Button):
    def __init__(self,frame,task,data,master,grandmaster):
        super().__init__(frame)
        self.root = frame
        self.task = task
        self.data = data
        self["text"] = "finish"
        self["command"] = self.finish
        self.master = master
        self.grandmaster = grandmaster
    def finish(self):
        self.data.finished(self.task)
        self.grandmaster.switch_frame(AllTasksPage,self.data)



class Delete_notfinishButton(Button):
    def __init__(self,frame,task,data,grandmaster):
        super().__init__(frame)
        self.task = task
        self.data = data
        self["text"] = "delete"
        self["command"] = self.delete
        self.grandmaster = grandmaster
        self["bg"] = data.typecolor[task.type][0]
    def delete(self):
        self.data.alltasks.delete(self.task)
        self.grandmaster.switch_frame(AllTasksPage,self.data)




class Delete_finishButton(Button):
    def __init__(self,frame,task,data,grandmaster):
        super().__init__(frame)
        self.task = task
        self.data = data
        self["text"] = "delete"
        self["command"] = self.delete
        self.grandmaster = grandmaster
        self["bg"] = data.typecolor[task.type][0]
    def delete(self):
        self.data.finishtasks.delete(self.task)
        self.grandmaster.switch_frame(AllTasksPage,self.data)




class TaskChangeButton(Button):
    def __init__(self,frame,task,taskrow,task_frame,data):
        super().__init__(frame)
        self.root = frame
        self.task = task
        self.taskrow = taskrow
        self.task_frame = task_frame
        self.data = data
        self["command"] = self.change
        self["text"] = "change"
    def change(self):
        self["text"] = "confirm"
        self["command"] = self.confirm
        self.task_frame.destroy()
        change_frame = Frame(self.root)
        change_frame.grid(column=0,row = self.taskrow,sticky=W)
        e_name = Entry(change_frame,width=20)
        e_name.insert(0,self.task.name)
        e_name.grid(column=0,row=0,rowspan=2,padx=10)
        scale_importance = Scale(change_frame,from_= 1 ,to=5,orient=HORIZONTAL,length=50)
        scale_importance.set(self.task.importance)
        scale_importance.grid(column=1,row=0,padx=20)
        e_duration = Entry(change_frame,width=5)
        e_duration.insert(0,int(self.task.duration*2))
        e_duration.grid(column=2,row=0,rowspan=2,padx=10)
        Label(change_frame,text="*30mins").grid(column=3,row=0,rowspan=2)
        now = datetime.datetime.now()
        cal = Calendar(change_frame,selectmode = "day",year = now.year,month = self.task.date[0],day = self.task.date[1],date_pattern = "yyyy/MM/dd")
        cal.grid(column = 4,row = 0,padx = 10)
        types=self.data.types[:]
        types.append("new")
        current_type = types.index(self.task.type)
        combo_type = ttk.Combobox(change_frame,values=types,width=10)
        combo_type.current(current_type)
        combo_type.grid(column=5,row=0,padx=10)
        self.name = e_name
        self.importance = scale_importance
        self.duration = e_duration
        self.frame = change_frame
        self.cal = cal
        self.type = combo_type
    def confirm(self):
        name = self.name.get()
        old_name = self.task.name
        if name not in self.data.alltasks.tasks or name == old_name:
            self.data.alltasks.delete(self.task)
            self.task.name = name
            self.task.importance = self.importance.get()
            self.task.duration = int(self.duration.get())/2
            self.task.type = self.type.get()
            if self.task.type not in self.data.types:
                self.data.addtype(self.task.type)
            ymd = self.cal.get_date().split("/")
            self.task.date = [int(ymd[1]),int(ymd[2])]
            self.data.alltasks.add(self.task)
        else:
            messagebox.showwarning("Error","Name \"" + name + "\" already exist")
        self.frame.destroy()
        color = self.data.typecolor[self.task.type][0]
        task_frame =Frame(self.root,bg=color)
        self.task_frame = task_frame
        task_frame.grid(row = self.taskrow,column = 0, pady=5,sticky=W)
        name_label=Label(task_frame,text=self.task.name,width=20,bg=color)
        name_label.grid(row = 0,column=0,padx=20,sticky=W)
        name_label.grid_propagate(0)
        imp_l = Label(task_frame,text="*" * self.task.importance,width=5,bg=color)
        imp_l.grid_propagate(0)
        imp_l.grid(row=0,column=1,padx=20,sticky=W)
        du_l = Label(task_frame,text=str(self.task.time_finished) +"/" + str(self.task.duration)+"hrs",width=8,bg=color)
        du_l.grid(row=0,column=2,padx=20)
        du_l.grid_propagate(0)
        date_l =Label(task_frame,text="%d/%d"%(self.task.date[0],self.task.date[1]),width=20,bg=color)
        date_l.grid(row=0,column=3,padx=20,sticky=W)
        date_l.grid_propagate(0)
        type_l = Label(task_frame,text=self.task.type,width = 10,bg=color)
        type_l.grid(row=0,column=4,padx = 30,sticky=E)
        type_l.grid_propagate(0)
        finished_button = FinishButton(task_frame,self.task,self.data,self,self.master.master.master.master.master)
        finished_button["bg"] = color
        finished_button.grid(row=0,column=5)
        delete_button = Delete_notfinishButton(task_frame,self.task,self.data,self.master.master.master.master.master)
        delete_button["bg"] = color
        delete_button.grid(row =0,column=6,padx=10)
        self["text"] = "change"
        self["command"] = self.change
class SchedulePage(Frame):
    def __init__(self,master,data):
        Frame.__init__(self,master)
        self.data = data
        if self.data.schedule == [] :
            Label(self,text="push the buttom \"為你安排行程\" at left first").pack()
        else:
            todayframe = TodayFrame(self,data)
            todayframe.pack(side="left")
            scheduleframe = ScheduleFrame(self,data)
            scheduleframe.pack(side="left")
class TodayFrame(VerticalScrolledFrame):
    def __init__(self,master,data):
        VerticalScrolledFrame.__init__(self, master,700,500)
        self.data = data
        self.master = master
        self.tasks = data.schedule[0]
        now = datetime.datetime.now()
        self.now = now
        self.now_hm = [now.hour,now.minute]
        Label(self.interior,text="today:",font=('Helvetica', 20, ITALIC)).pack(side = "top",anchor=W,padx=30)
        if len(self.tasks) == 0:
            l = Label(self.interior,text="today has no work",width=50)
            l.pack_propagate(0)
            l.pack()
        if len(self.tasks)>0:
            endtime = self.tasks[0][1]
            for task in self.tasks:
                if task[1] != endtime:
                    rest_time = task[1] - endtime
                    rest_frame = RestFrame(self.interior,data,rest_time,endtime)
                    rest_frame.pack()
                task_frame = TaskFrame(self.interior,data,task)
                task_frame.pack(pady=1)
                endtime =task[2]
class TaskFrame(Frame):
    def __init__(self,master,data,task):
        Frame.__init__(self,master)
        self.data = data
        self.master = master
        len_hour = 50
        self.task = task
        if task[1]%1 == 0.5:
            starttime_min = 3
        else:
            starttime_min = 0
        starttime_hour = task[1]//1
        now =  datetime.datetime.now()
        now_hour = now.hour
        now_minute = now.minute
        if now_hour < starttime_hour:
            done = False
            doing = False
        elif now_hour == starttime_hour:
            if now_minute <30:
                if starttime_min == 3:
                    done = False
                    doing = False
                else:
                    done = False
                    doing = True
            else:
                if starttime_min == 3:
                    done = False
                    doing = True
                else:
                    if task.duration == 0.5:
                        done = True
                        doing = False
                    else:
                        done = False
                        doing = True
        else: #now_hour > starttime_hour
            endtime = task[2]
            endtime_hour = endtime//1
            if endtime%1 == 0.5:
                endtime_min = 30
            else:
                endtime_min = 0
            if now_hour < endtime_hour:
                done = False
                doing = True
            elif now_hour == endtime_hour:
                if now_minute < endtime_min:
                    done = False
                    doing = True
                else:
                    done = True
                    doing = False
            else:
                done = True
                doing = False
        if done:
            if len(task) == 3:
                color = data.typecolor[data.alltasks.tasks[task[0]].type][1]
            else:
                color = task[3]
        else:
            if len(task) == 3:
                color = data.typecolor[data.alltasks.tasks[task[0]].type][0]
            else:
                color = task[3]
        starttime = "%d:%d0"%(starttime_hour,starttime_min)
        time_frame = Frame(self)
        time_frame.grid(row=0,column=0,sticky=N)
        l = Label(time_frame,text=starttime,width=5,height=1)
        l.pack(side="top")
        l.pack_propagate(0)
        task_canvas = Canvas(self,bg = color,width=300,height=(task[2]-task[1])*len_hour)
        task_canvas.grid(row=0,column =1)
        label_task = Label(task_canvas,text=task[0],bg=color,font=('Helvetica', 22, "bold"),width=20,height=20)
        label_task.place(anchor="c",relx = .5,rely = .5)
        if doing:
            passtime = ((now_hour*60 + now_minute)-(starttime_hour*60+starttime_min*10))/60
            y = passtime * len_hour
            now_label = Label(task_canvas,text="now",bg = color)
            now_label.place(x=10,y=y-10,in_=task_canvas)
            task_canvas.create_line(50,y,400,y,width=3)
        self.var = IntVar
        #check_done = Checkbutton(self,text="finished",command=self.finished,variable=self.var)
        #check_done.grid(row=0,column=2)
        if done or task[0] == "a":
            self.check_done = Checkbutton(self,text="finished",command=self.finished,variable=self.var)
            self.check_done.grid(row=0,column=2)
            if len(task) == 4:
                self.check_done.select()
                self.check_done.config(state=DISABLED)
        else:
            pad_frame = Frame(self,width=71,highlightthickness=5)
            pad_frame.grid(row = 0,column=2)
        """
        if self.task.finished :
            check_done.select()
            check_done.config(state=DISABLED)
        else:
            check_done.deselect()
        """
    def finished(self):
        color = data.typecolor[data.alltasks.tasks[self.task[0]].type][1]
        temp = 0
        for task in self.data.schedule[0]:
            if task[1] == self.task[1]:
                task = task + (color,)
                self.data.schedule[0][temp] = task
                break
            temp += 1
        self.check_done.config(state=DISABLED)
        self.data.finished_part(self.task)
        self.master.master.master.master.master.switch_frame(SchedulePage,data)
class RestFrame(Frame):
    def __init__(self,master,data,duration,starttime):
        Frame.__init__(self,master)
        self.data = data
        len_hour = 50
        self.duration = duration 
        if starttime %1 == 0.5:
            starttime_min = 3
        else:
            starttime_min = 0
        starttime_hour = starttime // 1
        now =  datetime.datetime.now()
        now_hour = now.hour
        now_minute = now.minute
        if now_hour < starttime_hour:
            done = False
            doing = False
        elif now_hour == starttime_hour:
            if now_minute <30:
                if starttime_min == 3:
                    done = False
                    doing = False
                else:
                    done = False
                    doing = True
            else:
                if starttime_min == 3:
                    done = False
                    doing = True
                else:
                    if duration == 0.5:
                        done = True
                        doing = False
                    else:
                        done = False
                        doing = True
        else: #now_hour > starttime_hour
            endtime = starttime+duration
            endtime_hour = endtime//1
            if endtime%1 == 0.5:
                endtime_min = 30
            else:
                endtime_min = 0
            if now_hour < endtime_hour:
                done = False
                doing = True
            elif now_hour == endtime_hour:
                if now_minute < endtime_min:
                    done = False
                    doing = True
                else:
                    done = True
                    doing = False
            else:
                done = True
                doing = False
        starttime = "%d:%d0"%(starttime_hour,starttime_min)
        time_frame = Frame(self)
        time_frame.grid(row=0,column=0,sticky=N+W)
        Label(time_frame,text=starttime).pack(side="top")
        task_canvas = Canvas(self,width=300,height=duration*len_hour)
        task_canvas.grid(row=0,column =1,sticky=W)
        rest_label = Label(task_canvas,text="Rest",font=('Helvetica', 22, "bold"),width=20)
        rest_label.place(anchor="c",in_=task_canvas,relx=.5,rely = .5)
        if doing:
            passtime = ((now_hour*60 + now_minute)-(starttime_hour*60+starttime_min*10))/60
            y = passtime * len_hour
            task_canvas.create_line(50,y,400,y,width=3)
            now_label = Label(task_canvas,text="now")
            now_label.place(x=10,y=y-10,in_=task_canvas)
        pad_frame = Frame(self,width=71,highlightthickness=5)
        pad_frame.grid(row = 0,column=2)

class ScheduleFrame(VerticalScrolledFrame):
    def __init__(self,master,data):
        VerticalScrolledFrame.__init__(self, master,700)
        self.master = master
        self.data = data
        schedule = self.data.schedule
        Label(self.interior,text="all:",font=('Helvetica', 20, ITALIC)).pack(anchor=W,padx=25)
        date = datetime.date.today()
        one_day = datetime.timedelta(days=1)
        for day in schedule:
            if len(day) > 0:
                day_frame = DayFrame(self.interior,data,day,date)
                day_frame.pack(pady=20)
            date += one_day

class DayFrame(Frame):
    def __init__(self,master,data,tasks,date):
        Frame.__init__(self,master)
        self.master = master
        self.data = data
        if len(tasks)>0:
            date = "%d/%d"%(date.month,date.day)
            date_frame = Frame(self)
            date_frame.grid(row=0,column=0,sticky=N)
            Label(date_frame,text=date,font=('Helvetica', 13, "bold")).pack()
            tasks_frame = Frame(self)
            tasks_frame.grid(row=0,column=1)
            row = 0
            for task in tasks:
                starttime = task[1]
                start_hour = str(int(starttime//1))
                if starttime%1 == 0:
                    starttime_minute = "00"
                else:
                    starttime_minute = "30"
                endtime = task[2]
                endtime_hour = str(int(endtime//1))
                if endtime%1 == 0:
                    endtime_minute = "00"
                else:
                    endtime_minute = "30"
                time_label = Label(tasks_frame,text=start_hour+ ":" + starttime_minute + "~" + endtime_hour + ":" + endtime_minute)
                time_label.grid(row=row,column=0,sticky=W)
                if len(task) == 3:
                    color = self.data.typecolor[data.alltasks.tasks[task[0]].type][0]
                else:
                    color = task[3]
                task_name_frame = Frame(tasks_frame,bg=color,width=300,height=20)
                task_name_frame.grid(row=row,column=1,sticky=W)
                task_name_frame.grid_propagate(0)
                task_label = Label(task_name_frame,text=task[0],bg = color,font = ('Helvetica', 15, "bold"))
                task_label.place(anchor="c",relx = .5,rely = .5)
                row += 1
class PeriodPage(Frame):
    def __init__(self,master,data):
        Frame.__init__(self,master)
        self.data = data
        self.period = self.data.period
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        row = 0
        for day in days:
            day_frame = Frame(self)
            day_frame.grid(row=row,column=0,pady=25,sticky=W)
            day_label = Label(day_frame,text=day+":",font =('Microsoft Sans Serif',16),width=10)
            day_label.pack(side="left")
            day_label.pack_propagate(0)
            period_text = []
            if len(self.period[day])>0:
                for period in self.period[day]:
                    startime = period[0]
                    starthour =str(int(startime//1))
                    if startime%1 == 0.5:
                        startmin = "30"
                    else:
                        startmin = "00"
                    endtime = period[1]
                    endhour = str(int(endtime//1))
                    if endtime %1 == 0.5:
                        endmin = "30"
                    else:
                        endmin = "00"
                    period_text.append(starthour+":"+startmin + "~" + endhour + ":" + endmin)
            period_text = "     ".join(period_text)
            period_label = Label(day_frame,text=period_text,font = ('Microsoft Sans Serif',16),width=60,anchor=W)
            period_label.pack(side="left")
            period_label.pack_propagate(0)
            delete_button = DeletePeriodButton(day_frame,data,day)
            delete_button.pack(side="right")
            row += 1
        add_period_frame = Frame(self)
        add_period_frame.grid(row = row,column=0,sticky=W,pady=25)
        Label(add_period_frame,text="add period:",font= ('Microsoft Sans Serif',16),fg="red").grid(row = 0,column=0,sticky=W)
        day_combo = ttk.Combobox(add_period_frame,values=days,state="readonly",width=10)
        day_combo.current(0)
        day_combo.grid(row = 0,column=1,padx=10)
        hour_start_entry = Entry(add_period_frame,width=5)
        hour_end_entry = Entry(add_period_frame,width=5)
        min_start_combo = ttk.Combobox(add_period_frame,values = ["00","30"],state="readonly",width=5)
        min_start_combo.current(0)
        min_end_combo = ttk.Combobox(add_period_frame,values=["00","30"],state="readonly",width=5)
        min_end_combo.current(0)
        hour_start_entry.grid(row = 0,column=2)
        Label(add_period_frame,text=":").grid(row = 0,column=3)
        min_start_combo.grid(row = 0,column=4)
        Label(add_period_frame,text="~").grid(row=0,column=5)
        hour_end_entry.grid(row = 0,column=6)
        Label(add_period_frame,text=":").grid(row = 0,column= 7)
        min_end_combo.grid(row = 0,column=8)
        Button(add_period_frame,text="add",command=self.add).grid(row = 0,column=9)
        self.day = day_combo
        self.starthour = hour_start_entry
        self.startmin = min_start_combo
        self.endhour = hour_end_entry
        self.endmin = min_end_combo
    def add(self):
        day = self.day.get()
        try:
            starthour = int(self.starthour.get())
            endhour = int(self.endhour.get())
            if starthour > 24 or endhour > 24 or starthour < 0 or endhour < 0:
                messagebox.showwarning("Error","Please enter integer between 0 and 24")
                return
        except:
            messagebox.showwarning("Error","Please enter integer")
            return
        if self.startmin.get() == "00":
            starttime = starthour
        else:
            starttime = starthour+0.5
        if self.endmin.get() == "00":
            endtime = endhour
        else:
            endtime = endhour+0.5
        new = True
        for period in self.data.period[day]:
            p_start = period[0]
            p_end = period[1]
            if p_start <= starttime <= p_end:
                new = False
                if endtime > p_end:
                    period[1] = endtime
                else:
                    break
            elif p_start <= endtime <= p_end:
                new = False
                if starttime < p_start:
                    period[0] = starttime
                else:
                    break
        if len(self.data.period[day]) >= 2:
            former_period = self.data.period[day][0]
            for period in self.data.period[day][1:]:
                if former_period[1] >= period[0]:
                    former_period[1] = period[1]
                    self.data.period[day].remove(period)
                former_period = period
        if new:
            self.data.period[day].append([starttime,endtime])
            self.data.period[day].sort()
        self.master.switch_frame(PeriodPage,self.data)
class DeletePeriodButton(Button):
    def __init__(self,master,data,day):
        super().__init__(master)
        self["command"] = self.delete
        self["text"] = "delete"
        self.data = data
        self.day = day
    def delete(self):
        self.data.period[self.day] = []
        self.master.master.master.switch_frame(PeriodPage,self.data)

t1 = Task("錄資結影片",1,3,[7,5],"工作")
t2 = Task("複習DS",3,4,[7,6],"工作")
t3 = Task("跑步",0.5,2,[7,7],"運動")
t4 = Task("整理演算法",2,5,[7,5],"工作")
t5 = Task("全聯買東西",1,2,[7,12],"生活")
all = AllTasks([])
f = FinishedTasks([])
data = Data(all,f)

"""
now = time.process_time()
for i in range(100000):
    name = "".join(random.choice(string.ascii_letters + string.digits) for x in range(10))
    duration = random.randint(1,10000)
    t = Task(name,duration,1,[5,5])
    data.alltasks.add(t)
end = time.process_time()
print("add by dict:%f" %(end - now))

now = time.process_time()
data.alltasks.sort("name")
end = time.process_time()
print("sort by rbt:%f" %(end - now))
now = time.process_time()
data.alltasks.sort("duration")
end = time.process_time()
print("sort by dict:%f" %(end - now))
"""



app = main(data)
app.mainloop()