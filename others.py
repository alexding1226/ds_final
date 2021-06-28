import time
import datetime
from tkinter import *

root = Tk()

class Task():
    def __init__(self,name,duration,importance,deadline,type = "study",successive = False) :
        self.name = name
        self.duration = duration
        self.importance = importance
        self.deadline = deadline
        self.type = type
        self.succesive = successive
class TomatoClock():
    def __init__(self,duration) :
        self.duration = duration
    def countdown(self):
        target =  datetime.datetime.now()
        one_second_later = datetime.timedelta(seconds=1)
        for remaining in range(self.duration, 0, -1):
            target += one_second_later
            self.remain_time = datetime.timedelta(seconds=remaining)
            time.sleep((target -  datetime.datetime.now()).total_seconds())
class AllTasks():
    def __init__(self,tasks) :
        self.tasks = tasks
    def add(self,task):
        self.tasks.append(task)
    def sort(self ,type, rev = True):
        if type == "type":
            return sorted(self.tasks,key= lambda task:task.type,reverse = not (rev))
        elif type == "importance":
            return sorted(self.tasks,key= lambda task:task.importance,reverse = (rev))
        elif type == "deadline":
            return sorted(self.tasks,key= lambda task:task.deadline,reverse = (rev))
        elif type == "duration":
            return sorted(self.tasks,key= lambda task:task.duration,reverse = (rev))




