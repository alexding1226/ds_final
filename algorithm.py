from datetime import date
from datetime import datetime
from functools import total_ordering

@total_ordering
class Task():
    def __init__(self,name,duration,importance,date,type = "study",successive = False) :
        self.name = name
        self.duration = duration
        self.importance = importance
        #self.deadline = deadline
        self.type = type
        self.successive = successive
        self.date = date 
        self.whentodo = None #[month,day,period] #period = 1,1.5,2,....,24
        self.finished = False
        self.remainday = None
        self.time_finished = 0
    def __eq__(self, other) -> bool:
        return (self.remainday,self.importance) == (other.remainday,other.importance)
    def __lt__(self,other):
        return (self.remainday,self.importance) < (other.remainday,other.importance)
class AllTasks():
    def __init__(self,tasks) :
        self.tasks = dict()
        for task in tasks:
            self.tasks[task.name] = task
    def add(self,task):
        self.tasks[task.name] = task
    def sort(self ,type, rev = True):
        pass
    def delete(self,task):
        del self.tasks[task.name]
class Period():
    def __init__(self,period) : #period : [[[begin,end],[begin,end]...]*7]
        self.period = period
class algorithm():
    def __init__(self,tasks,period):
        now = datetime.today().date()
        self.tasks = tasks
        for task in tasks:
            deadline = date(2021,task.date[0],task.date[1])
            task.remainday = (deadline - now).days
        self.sortedtasks = self.sort()
    def sort(self):
        return sorted(self.tasks.items(),key = lambda task:(task[1].remainday,task[1].importance))
t1 = Task("a",5,3,[7,5])
t2 = Task("b",3,1,[7,5])
t3 = Task("c",4,4,[7,6])
