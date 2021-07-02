
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
            self.list.sort(self.list,key= lambda task_item:(task_item.deadline_date, task_item.deadline_time,
                task_item.importance), reverse = not (rev))
            return self.tasks
    
    def delete(self,task):
        self.tasks.remove(task)

class test():
    def __init__(self,list):
        test = list

if __name__ == "__main__": #testing
    t1 = test([1,2])
    t2 = test([3,4])
    T = [t1,t2]
    print(T.sort())