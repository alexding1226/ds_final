
class task_item():
    def __init__(self, name, duration, importance, deadline_date, deadline_time, min_length = 1,
            type = "None", non_consecutive_type = []) :
        self.name = name # str
        self.duration = duration # int, every 30 min or 10 min 
        self.importance = importance # int 1~5, 5 is the most important
        self.deadline_date = deadline_date # int
        self.deadline_time = deadline_time # int 
        self.type = type # str
        self.min_length = min_length # int, every 30 min or 10 min 
        self.non_consecutive_type = non_consecutive_type # list of types that can't take place right after this task
        #self.partition_num = [1,duration//min_length]
        self.partition = [duration]
        #for i in range():
        #    self.partition.append(min_length)

    def copy(self):
        copy = task_item(self.name,self.duration, self.importance, self.deadline_date, self.deadline_time,
            self.min_length, self.type, self.non_consecutive_type)
        return copy

class period_item:
    def __init__(self,date,begin_time,end_time):
        self.date = date
        self.begin = begin_time
        self.end = end_time

    def copy(self):
        copy = period_item(self.date, self.begin, self.end)
        return copy

class list(): ## 可以廢掉
    def __init__(self, list_of_tasks):
        self.list = list_of_tasks
    
    def add(self, task_item):
        self.list.append(task_item)
    
    def delete(self, task_item):
        self.list.remove(task_item)

    def sort(self, type = "deadline", rev = True):
        if type == "deadline":
            self.list = sorted(self.list,key= lambda task_item:(task_item.deadline_date, task_item.deadline_time,
                task_item.importance), reverse = not (rev))
        elif type == "time":
            self.list = sorted(self.list,key= lambda period_item:(period_item.date, period_item.begin), reverse = not (rev))
        return self.list
    
    def delete(self,task):
        self.list.remove(task)

    def pop(self,index):
        self.list.pop(index)

    def RemoveMin(self):
        self.list.pop(0)

    def Swap(self):
        if len(self.list) > 1:
            temp = self.list[0]
            self.list[0] = self.list[1] 
            self.list[1] = temp
            return True
        return False
    
    def Peek(self):
        return self.list[0]

    def len(self):
        return len(self.list)

    def index(self,task_item):
        return self.list.index(task_item)
    
    def get(self,index):
        return self.list[index]

if __name__ == "__main__": #testing
    
    # date, begin time, endd time
    general_period_list = [(1,9,12),(2,13,19),(3,12,15)]

    t1 = task_item("B",3,1,2,24,1,"exercise",["academy"])
    t4 = task_item("A",3,1,1,24,1,"academy",[])
    t3 = task_item("C",3,2,3,24,1,"academy",[])
    t2 = task_item("D",1,1,4,24,1,"exercise",[])
    T = list([t1,t2,t3,t4])
    
