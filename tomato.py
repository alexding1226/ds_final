from calendar import month
from re import T
import time
import datetime
from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import Calendar
class Task():
    def __init__(self,name,duration,importance,date,type = "study",successive = False) :
        self.name = name
        self.duration = duration
        self.importance = importance
        #self.deadline = deadline
        self.type = type
        self.successive = successive
        self.date = date
        self.whentodo = None #[month,day,period] #period = 1~48
        self.finished = False
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
        elif type == "duration":
            self.tasks = sorted(self.tasks,key= lambda task:task.duration,reverse = (rev))
            return self.tasks
        elif type == "name":
            self.tasks = sorted(self.tasks,key= lambda task:task.name,reverse = not (rev))
            return self.tasks
        elif type == "deadline":
            self.tasks = sorted(self.tasks,key= lambda task:task.date,reverse = not (rev))
            return self.tasks
    def algorithm(self):
        self.nextsixdays = [[self.tasks[2]],[],[],[],[],[]]
        self.today = [Task("a",0.5,3,[7,20]),Task("b",2,2,[8,30])]
        self.today[0].whentodo = [7,1,0]
        self.today[1].whentodo = [7,1,21]
    def delete(self,task):
        self.tasks.remove(task)
    def finished(self,task):
        task_in_all = list(filter(lambda x: (x.name  == task.name and x.importance == task.importance and x.type == task.type), self.tasks))
        if task_in_all[0].duration == task.duration:
            self.delete(task_in_all[0])
            self.data.finishtasks.add(self.task)
            self.task.finished = True
        else:
            task_in_all[0].duration -= task.duration


class Data():
    def __init__(self,all) :
        self.clock_time = 25
        self.alltasks = all
        self.alltasks.algorithm()
        self.types = ["study","exercise","homework"]
        #self.today = [self.alltasks.tasks[0],self.alltasks.tasks[1]]
        self.today = self.alltasks.today
        self.typecolor = {"study":["deep sky blue","light sky blue"],"exercise":"purple","homework":"green"}
        self.finishtasks = AllTasks([])


class main(Tk):
    def __init__(self,data) :
        super().__init__()
        self._frame = None
        self.geometry("1000x700")
        self.duration = 50
        self.remaintime = self.duration
        self.counting = False
        change_frame = Frame(self)
        change_frame.pack(side="left",fill="y")
        Button(change_frame,text="config",command=lambda:self.switch_frame(StartPage,data)).grid(column=0,row=0,pady=15,padx=15,sticky=N)
        Button(change_frame,text="tomato clock",command=lambda:self.switch_frame(Tomato,data)).grid(column=0,row=1,pady=15,padx=15,sticky=N)
        Button(change_frame,text="all tasks",command=lambda:self.switch_frame(AllTasksPage,data)).grid(column=0,row=2,pady=15,padx=15,sticky=N)
        Button(change_frame,text="today",command=lambda:self.switch_frame(TodayPage,data)).grid(column=0,row=3,pady=15,padx=15,sticky=N)
        self.switch_frame(StartPage,data)
    def switch_frame(self, frame_class,data):
        new_frame = frame_class(self,data)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(side = "left",fill = "both")
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

#from https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame
class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent,height, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,height=height,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
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
        self.alltasks = data.alltasks
        self.frame_config = Frame(self)
        self.frame_config.grid(row=0,column=0,sticky=W)
        self.frame_tasks = VerticalScrolledFrame(self,425)
        self.frame_tasks["height"] = 500
        self.frame_tasks["width"] = 1000
        self.frame_tasks.grid_propagate(0)
        self.frame_tasks.grid(row=1,column=0,rowspan=10,pady = 15)
        taskrow = 0
        for task in self.alltasks.tasks:
            task_frame =Frame(self.frame_tasks.interior)
            task_frame.grid(row = taskrow,column = 0, pady=5,sticky=W)
            name_label=Label(task_frame,text=task.name,width=20)
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
            imp_l = Label(task_frame,text="*" * task.importance,width=5)
            imp_l.grid_propagate(0)
            imp_l.grid(row=0,column=1,padx=20,sticky=W)
            du_l = Label(task_frame,text=str(task.duration)+"hrs",width=5)
            du_l.grid(row=0,column=2,padx=20)
            du_l.grid_propagate(0)
            date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20)
            date_l.grid_propagate(0)
            date_l.grid(row=0,column=3,padx=20,sticky=W)
            type_l = Label(task_frame,text=task.type,width = 10)
            type_l.grid(row=0,column=4,padx = 30,sticky=E)
            type_l.grid_propagate(0)
            task_button = TaskChangeButton(self.frame_tasks.interior,task,taskrow,task_frame,self.data)
            task_button.grid(row = taskrow,column = 1)
            taskrow += 1
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
            task_frame =Frame(self.finished_frame)
            task_frame.grid(row = finished_row,column = 0, pady=5,sticky=W)
            name_label=Label(task_frame,text=task.name,width=20)
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
            imp_l = Label(task_frame,text="*" * task.importance,width=5)
            imp_l.grid_propagate(0)
            imp_l.grid(row=0,column=1,padx=20,sticky=W)
            du_l = Label(task_frame,text=str(task.duration)+"hrs",width=5)
            du_l.grid(row=0,column=2,padx=20)
            du_l.grid_propagate(0)
            date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20)
            date_l.grid_propagate(0)
            date_l.grid(row=0,column=3,padx=20,sticky=W)
            type_l = Label(task_frame,text=task.type,width = 10)
            type_l.grid(row=0,column=4,padx = 30,sticky=E)
            type_l.grid_propagate(0)
            finished_row += 1
        self.add_task_button = Button(self,text="+",command=self.add_task)
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
        Label(self,text="duration").place(x=280,y=40)
        Label(self,text="deadline").place(x=410,y=40)
        Label(self,text="type").place(x=585,y=40)

    def sort(self,type,rev):
        self.frame_tasks.destroy()
        self.frame_tasks = VerticalScrolledFrame(self,425)
        self.frame_tasks.grid(row=1,column=0,pady=15)
        self.alltasks.tasks = self.data.alltasks.sort(type,not rev)
        taskrow = 0
        for task in self.alltasks.tasks:
            task_frame =Frame(self.frame_tasks.interior)
            task_frame.grid(row = taskrow,column = 0, pady=5,sticky=W)
            name_label=Label(task_frame,text=task.name,width=20)
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
            imp_l = Label(task_frame,text="*" * task.importance,width=5)
            imp_l.grid_propagate(0)
            imp_l.grid(row=0,column=1,padx=20,sticky=W)
            du_l = Label(task_frame,text=str(task.duration)+"hrs",width=5)
            du_l.grid(row=0,column=2,padx=20)
            du_l.grid_propagate(0)
            date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20)
            date_l.grid_propagate(0)
            date_l.grid(row=0,column=3,padx=20,sticky=W)
            type_l = Label(task_frame,text=task.type,width = 10)
            type_l.grid(row=0,column=4,padx = 30,sticky=E)
            type_l.grid_propagate(0)
            task_button = TaskChangeButton(self.frame_tasks.interior,task,taskrow,task_frame,self.data)
            task_button.grid(row = taskrow,column = 1)
            taskrow += 1
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
            task_frame =Frame(self.finished_frame)
            task_frame.grid(row = finished_row,column = 0, pady=5,sticky=W)
            name_label=Label(task_frame,text=task.name,width=20)
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
            imp_l = Label(task_frame,text="*" * task.importance,width=5)
            imp_l.grid_propagate(0)
            imp_l.grid(row=0,column=1,padx=20,sticky=W)
            du_l = Label(task_frame,text=str(task.duration)+"hrs",width=5)
            du_l.grid(row=0,column=2,padx=20)
            du_l.grid_propagate(0)
            date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20)
            date_l.grid_propagate(0)
            date_l.grid(row=0,column=3,padx=20,sticky=W)
            type_l = Label(task_frame,text=task.type,width = 10)
            type_l.grid(row=0,column=4,padx = 30,sticky=E)
            type_l.grid_propagate(0)
            finished_row += 1
        self.add_task_button = Button(self,text="+",command=self.add_task)
        self.add_task_button.grid(row=30,column=0,pady=30)
        Label(self,text="Name").place(x=68,y=40)
        Label(self,text="importance").place(x=170,y=40)
        Label(self,text="duration").place(x=280,y=40)
        Label(self,text="deadline").place(x=410,y=40)
        Label(self,text="type").place(x=585,y=40)
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
        Label(frame_addtask,text="hrs").grid(row=0,column=3)
        now = datetime.datetime.now()
        cal = Calendar(frame_addtask,selectmode = "day",year = now.year,month = now.month,day = now.day)
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
        task = Task(name.get(),int(dur.get()),imp.get(),[int(ymd[1]),int(ymd[2])],type.get())
        self.data.alltasks.add(task)
        if type.get() not in self.data.types:
            self.data.types.append(type.get())
        frame.destroy()
        self.confirm_button.destroy()
        self.add_task_button = Button(self,text="+",command=self.add_task)
        self.add_task_button.grid(row=30,column=0,pady=30)
        task_frame =Frame(self.frame_tasks.interior)
        task_frame.grid(row = len(self.data.alltasks.tasks)-1,column = 0, pady=5,sticky=W)
        name_label=Label(task_frame,text=task.name,width=20)
        name_label.grid(row = 0,column=0,padx=20,sticky=W)
        name_label.grid_propagate(0)
        imp_l = Label(task_frame,text="*" * task.importance,width=5)
        imp_l.grid_propagate(0)
        imp_l.grid(row=0,column=1,padx=20,sticky=W)
        du_l = Label(task_frame,text=str(task.duration)+"hrs",width=5)
        du_l.grid(row=0,column=2,padx=20)
        du_l.grid_propagate(0)
        type_l = Label(task_frame,text=task.type,width = 10)
        type_l.grid(row=0,column=4,padx = 30,sticky=E)
        type_l.grid_propagate(0)
        date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20)
        date_l.grid_propagate(0)
        date_l.grid(row=0,column=3,padx=20,sticky=W)
        task_button = TaskChangeButton(self.frame_tasks.interior,task,len(self.data.alltasks.tasks)-1,task_frame,self.data)
        task_button.grid(row = len(self.data.alltasks.tasks)-1,column = 1)
        taskrow = len(self.data.alltasks.tasks)
        self.finished_frame.destroy()
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
            task_frame =Frame(self.finished_frame)
            task_frame.grid(row = finished_row,column = 0, pady=5,sticky=W)
            name_label=Label(task_frame,text=task.name,width=20)
            name_label.grid(row = 0,column=0,padx=20,sticky=W)
            name_label.grid_propagate(0)
            imp_l = Label(task_frame,text="*" * task.importance,width=5)
            imp_l.grid_propagate(0)
            imp_l.grid(row=0,column=1,padx=20,sticky=W)
            du_l = Label(task_frame,text=str(task.duration)+"hrs",width=5)
            du_l.grid(row=0,column=2,padx=20)
            du_l.grid_propagate(0)
            date_l = Label(task_frame,text="%d/%d"%(task.date[0],task.date[1]),width=20)
            date_l.grid_propagate(0)
            date_l.grid(row=0,column=3,padx=20,sticky=W)
            type_l = Label(task_frame,text=task.type,width = 10)
            type_l.grid(row=0,column=4,padx = 30,sticky=E)
            type_l.grid_propagate(0)
            finished_row += 1

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
        change_frame.grid(column=0,row = self.taskrow)
        e_name = Entry(change_frame,width=20)
        e_name.insert(0,self.task.name)
        e_name.grid(column=0,row=0,rowspan=2,padx=10)
        scale_importance = Scale(change_frame,from_= 1 ,to=5,orient=HORIZONTAL,length=50)
        scale_importance.set(self.task.importance)
        scale_importance.grid(column=1,row=0,padx=20)
        e_duration = Entry(change_frame,width=5)
        e_duration.insert(0,self.task.duration)
        e_duration.grid(column=2,row=0,rowspan=2,padx=10)
        Label(change_frame,text="hrs").grid(column=3,row=0,rowspan=2)
        now = datetime.datetime.now()
        cal = Calendar(change_frame,selectmode = "day",year = now.year,month = self.task.date[0],day = self.task.date[1])
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
        self.task.name = self.name.get()
        self.task.importance = self.importance.get()
        self.task.duration = int(self.duration.get())
        self.task.type = self.type.get()
        if self.task.type not in self.data.types:
            self.data.types.append(self.task.type)
        ymd = self.cal.get_date().split("/")
        self.task.date = [int(ymd[1]),int(ymd[2])]
        self.frame.destroy()
        task_frame =Frame(self.root)
        task_frame.grid(row = self.taskrow,column = 0, pady=5,sticky=W)
        name_label=Label(task_frame,text=self.task.name,width=20)
        name_label.grid(row = 0,column=0,padx=20,sticky=W)
        name_label.grid_propagate(0)
        imp_l = Label(task_frame,text="*" * self.task.importance,width=5)
        imp_l.grid_propagate(0)
        imp_l.grid(row=0,column=1,padx=20,sticky=W)
        du_l = Label(task_frame,text=str(self.task.duration)+"hrs",width=5)
        du_l.grid(row=0,column=2,padx=20)
        du_l.grid_propagate(0)
        date_l =Label(task_frame,text="%d/%d"%(self.task.date[0],self.task.date[1]),width=20)
        date_l.grid(row=0,column=3,padx=20,sticky=W)
        date_l.grid_propagate(0)
        type_l = Label(task_frame,text=self.task.type,width = 10)
        type_l.grid(row=0,column=4,padx = 30,sticky=E)
        type_l.grid_propagate(0)
        self["text"] = "change"
        self["command"] = self.change

class TodayPage(VerticalScrolledFrame):
    def __init__(self,master,data):
        VerticalScrolledFrame.__init__(self, master,700)
        self.data = data
        self.master = master
        self.tasks = sorted(data.today,key= lambda task:task.whentodo)
        now = datetime.datetime.now()
        self.now = now
        self.now_hm = [now.hour,now.minute]
        endtime = self.tasks[0].whentodo[2]
        for task in self.tasks:
            if task.whentodo[2] != endtime:
                rest_time = task.whentodo[2] - endtime
                rest_frame = RestFrame(self.interior,data,rest_time,endtime)
                rest_frame.pack()
            task_frame = TaskFrame(self.interior,data,task)
            task_frame.pack()
            endtime = task.whentodo[2] + task.duration
class TaskFrame(Frame):
    def __init__(self,master,data,task):
        Frame.__init__(self,master)
        self.data = data
        self.master = master
        len_hour = 50
        self.task = task
        if task.whentodo[2]%1 == 0.5:
            starttime_min = 3
        else:
            starttime_min = 0
        starttime_hour = task.whentodo[2]//1
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
            endtime = task.whentodo[2]+task.duration
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
            color = data.typecolor[task.type][1]
        else:
            color = data.typecolor[task.type][0]
        starttime = "%d:%d0"%(starttime_hour,starttime_min)
        time_frame = Frame(self)
        time_frame.grid(row=0,column=0,sticky=N)
        Label(time_frame,text=starttime).pack(side="top")
        task_canvas = Canvas(self,bg = color,width=300,height=task.duration*len_hour)
        task_canvas.grid(row=0,column =1)
        label_task = Label(task_canvas,text=task.name,bg=color,font=('Helvetica', 22, "bold"),width=20,height=20)
        label_task.place(anchor="c",relx = .5,rely = .5)
        if doing:
            passtime = ((now_hour*60 + now_minute)-(starttime_hour*60+starttime_min*10))/60
            y = passtime * len_hour
            task_canvas.create_line(50,y,400,y)
            now_label = Label(task_canvas,text="now",bg = color)
            now_label.place(x=10,y=y-10,in_=task_canvas)
        self.var = IntVar
        check_done = Checkbutton(self,text="finished",command=self.finished,variable=self.var)
        check_done.grid(row=0,column=2)
        if self.task.finished :
            check_done.select()
            check_done.config(state=DISABLED)
        else:
            check_done.deselect()
        self.check_done = check_done
    def finished(self):
        self.check_done.config(state=DISABLED)
        self.data.alltasks.finished(self.task)
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
            task_canvas.create_line(50,y,400,y)
            now_label = Label(task_canvas,text="now")
            now_label.place(x=10,y=y,in_=task_canvas)
        pad_frame = Frame(self,width=71,highlightbackground="black",highlightthickness=5)
        pad_frame.grid(row = 0,column=2)
        






t1 = Task("a",2.5,3,[7,20])
t2 = Task("b",2,2,[8,30])
t3 = Task("c",2,2,[7,21])
all = AllTasks([t1,t2,t3])
data = Data(all)


app = main(data)
app.mainloop()