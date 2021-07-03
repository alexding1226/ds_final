from datetime import date
from datetime import datetime
from functools import total_ordering
import heapq as hq
import time
import copy 
import random
import string
@total_ordering
class Task():
    def __init__(self,name,duration,importance,length,date,type = "study",successive = False) :
        self.name = name
        self.duration = duration
        self.importance = importance
        #self.deadline = deadline
        self.length = length
        self.type = type
        self.successive = successive
        self.date = date 
        #self.length = length
        self.whentodo = None #[month,day,period] #period = 1,1.5,2,....,24
        self.finished = False
        self.remainday = None
        self.time_finished = 0
        self.time_scheduled = 0
    def __eq__(self, other):
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
        self.tasks = list(tasks.tasks.values())
        for task in self.tasks:
            deadline = date(2021,task.date[0],task.date[1])
            task.remainday = (deadline - now).days
            task.time_scheduled = 0
        self.heap = self.tasks[:]
        hq.heapify(self.heap)
        self.sortedtasks = self.sort()
        self.period = period
        self.result1 = []
        self.result2 = []
        self.day = []
        start = time.process_time()
        self.main1()
        end = time.process_time()
        print("heap: %f"%(end - start))
        start = time.process_time()
        #self.main2()
        end = time.process_time()
        print("list: %f"%(end - start))
    def sort(self):
        return sorted(self.tasks)
    def main1(self):
        heap = self.heap
        self.day = []
        period = copy.deepcopy(self.period)
        while len(self.heap) > 0:
            most_important = heap[0]
            nearest_day = period[0]
            nearest_period = nearest_day[0]
            if most_important.duration - most_important.time_scheduled > nearest_period[1]-nearest_period[0]:
                self.day.append([most_important.name,nearest_period[0],nearest_period[1]])
                most_important.time_scheduled += nearest_period[1]-nearest_period[0]
                nearest_day.pop(0)
            elif most_important.duration - most_important.time_scheduled == nearest_period[1]-nearest_period[0]:
                self.day.append([most_important.name,nearest_period[0],nearest_period[1]])
                most_important.time_scheduled += nearest_period[1]-nearest_period[0]
                nearest_day.pop(0)
                hq.heappop(heap)
            else:
                self.day.append([most_important.name,nearest_period[0],nearest_period[0]+most_important.duration - most_important.time_scheduled])
                period[0][0][0] = period[0][0][0] + most_important.duration - most_important.time_scheduled
                hq.heappop(heap)
            while len(nearest_day) == 0:
                try:
                    period.pop(0)
                    nearest_day = period[0]
                    self.result1.append(self.day)
                    self.day = []
                except:
                    break
        #print(self.result1)
    def main2(self):
        heap = self.sort()
        self.day = []
        period = copy.deepcopy(self.period)
        while len(heap) > 0:
            most_important = heap[0]
            nearest_day = period[0]
            nearest_period = nearest_day[0]
            if most_important.duration - most_important.time_scheduled > nearest_period[1]-nearest_period[0]:
                self.day.append([most_important.name,nearest_period[0],nearest_period[1]])
                most_important.time_scheduled += nearest_period[1]-nearest_period[0]
                nearest_day.pop(0)
            elif most_important.duration - most_important.time_scheduled == nearest_period[1]-nearest_period[0]:
                self.day.append([most_important.name,nearest_period[0],nearest_period[1]])
                most_important.time_scheduled += nearest_period[1]-nearest_period[0]
                nearest_day.pop(0)
                heap.pop(0)
            else:
                self.day.append([most_important.name,nearest_period[0],nearest_period[0]+most_important.duration - most_important.time_scheduled])
                period[0][0][0] = period[0][0][0] + most_important.duration - most_important.time_scheduled
                heap.pop(0)
            while len(nearest_day) == 0:
                try:
                    period.pop(0)
                    nearest_day = period[0]
                    self.result2.append(self.day)
                    self.day = []
                except:
                    break
        #print(self.result2)
t1 = Task("a",5,3,2,[7,5])
t2 = Task("b",3,1,1,[7,5])
t3 = Task("c",4,4,2,[7,6])
t4 = Task("d",5,2,2,[7,9])
t5 = Task("e",1,2,1,[7,4])
t6 = Task("f",1,2,1,[7,3])
t7 = Task("g",5,2,2,[7,9])
t8 = Task("h",5,2,2,[7,9])
t9 = Task("i",5,2,2,[7,9])
t10 = Task("j",5,2,2,[7,9])
period = [[[10,15],[17,20]],[[4,7],[8,9]],[[10,13],[15,18]],[[5,8],[9,15],[16,20]],[[9,15],[17,24]],[[4,15],[16,24]],[[0,12],[15,20]],[[3,10],[15,24]]]

for _ in range(100000):
    period.append([[10,15],[16,20]])
all = AllTasks([t1,t2,t3,t4,t5,t6,t7,t8,t9,t10])
for _ in range(100000):
    t = Task("".join(random.choices(string.ascii_uppercase,k=200)),5,2,4,[8,1])
    all.add(t)

#all = AllTasks([t1,t2,t3,t4,t5,t6,t7,t8,t9,t10])
al = algorithm(all,period)
