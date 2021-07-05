from typing import List

class task_item:
    def __init__(self, name, duration, importance, deadline_date, deadline_time, id, min_length = 1,
            type = "None", non_consecutive_type = []) :
        self.name = name # str
        self.duration = duration # int, every 30 min or 10 min 
        self.importance = importance # int 1~5, 5 is the most important
        self.deadline_date = deadline_date # int
        self.deadline_time = deadline_time # int 
        self.type = type # str
        self.min_length = min_length # int, every 30 min or 10 min 
        self.non_consecutive_type = non_consecutive_type # list of types that can't take place right after this task
        self.id = id # to identify tasks with same properties (e.g. splitted tasks)
        ##self.partition_num = [1,duration//min_length]
        ##self.partition = [duration]
        ##for i in range():
        ##    self.partition.append(min_length)

    def copy(self):
        copy = task_item(self.name,self.duration, self.importance, self.deadline_date, self.deadline_time,
            self.min_length, self.type, self.non_consecutive_type)
        return copy

    def __gt__(self,other):
        if (self.deadline_date, self.deadline_time, self.importance) > (other.deadline_date, other.deadline_time, other.importance):
            return True
        else:
            return False

    def __eq__(self, other: object) -> bool:
        if (self.deadline_date, self.deadline_time, self.importance, self.name, self.id) == \
                (other.deadline_date, other.deadline_time, other.importance, other.name, other.id):
            return True
        else:
            return False

    def __lt__(self,other):
        if (self.deadline_date, self.deadline_time, self.importance) < (other.deadline_date, other.deadline_time, other.importance):
            return True
        else:
            return False

    def __ge__(self,other):
        if (self.deadline_date, self.deadline_time, self.importance) >= (other.deadline_date, other.deadline_time, other.importance):
            return True
        else:
            return False

    def __le__(self,other):
        if (self.deadline_date, self.deadline_time, self.importance) <= (other.deadline_date, other.deadline_time, other.importance):
            return True
        else:
            return False
    
class period_item:
    def __init__(self,date,begin_time,end_time):
        self.date = date
        self.begin = begin_time
        self.end = end_time

    def copy(self):
        copy = period_item(self.date, self.begin, self.end)
        return copy

    def __gt__(self,other):
        if (self.date, self.begin, self.end) > (other.date, other.begin, other.end):
            return True
        else:
            return False

    def __eq__(self, other: object) -> bool:
        if (self.date, self.begin, self.end) == (other.date, other.begin, other.end):
            return True
        else:
            return False

    def __lt__(self,other):
        if (self.date, self.begin, self.end) < (other.date, other.begin, other.end):
            return True
        else:
            return False

    def __ge__(self,other):
        if (self.date, self.begin, self.end) >= (other.date, other.begin, other.end):
            return True
        else:
            return False

    def __le__(self,other):
        if (self.date, self.begin, self.end) <= (other.date, other.begin, other.end):
            return True
        else:
            return False

class my_list(List): 
    def __init__(self, list_item):
        super().__init__(list_item)
    
    def RemoveMin(self):
        super().pop(0)
        
    def Swap(self):
        if len(self) > 1:
            temp = self[0]
            self[0] = self[1] 
            self[1] = temp
            return True
        return False
    
    def Peek(self):
        return self[0]

if __name__ == "__main__": #testing
    
    # date, begin time, endd time
    general_period_list = [(1,9,12),(2,13,19),(3,12,15)]

    t1 = task_item("B",3,1,2,24,1,"exercise",["academy"])
    t4 = task_item("A",3,1,1,24,1,"academy",[])
    #t3 = task_item("C",3,2,3,24,1,"academy",[])
    #t2 = task_item("D",1,1,4,24,1,"exercise",[])
    #T = list([t1,t2,t3,t4])
    print(t1,t4)
    T = list([t1,t4])
    print(sorted(T))
