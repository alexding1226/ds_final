
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

class task_list():
    def __init__(self, list_of_tasks):
        self.list = list_of_tasks
    
    def add(self, task_item):
        self.tasks.append(task_item)
    
    def delete(self, task_item):
        self.tasks.remove(task_item)

    def sort(self, type = "deadline", rev = True):
        if type == "deadline":
            self.list = sorted(self.list,key= lambda task_item:(task_item.deadline_date, task_item.deadline_time,
                task_item.importance), reverse = not (rev))
    
    def delete(self,task):
        self.tasks.remove(task)

    def 

if __name__ == "__main__": #testing
    general_task_list = [[2,24,1,3,"B","exercise",1,["academy"]],[2,24,2,3,"C","academy",1,[]],[1,24,1,3,"A","academy",1,[]], [4,24,1,1,"D","Exercise",1,[]]]
    
    # date, begin time, endd time
    general_period_list = [(1,9,12),(2,13,19),(3,12,15)]

    t1 = task_item("B",3,1,2,24,1,"exercise",["academy"])
    t4 = task_item("A",3,1,1,24,1,"academy",[])
    t3 = task_item("C",3,2,3,24,1,"academy",[])
    t2 = task_item("D",1,1,4,24,1,"exercise",[])
    T = task_list([t1,t2,t3,t4])
    T.sort()
    print(T)
