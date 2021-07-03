#import algorithm.py
import heapq as hp
import DataFormat as data

# Pseudo version: 
# total time insufficient warning should take plasce @ task adding section
# that deals with the case that the sum of time of the first n task exceed the sum of time 
# ... add up to the deadline of the n'th task

# so maybe I shoud try not split the task if possible
# the config. of split or not split 
# 先拆大的，窮舉？

# try : 讓user自訂長度，tail獨立出來或是併進去

# Input data : 
t1 = data.task_item("B",3,1,2,24,1,"exercise",["academy"])
#name, duration, importance, deadline_date, deadline_time, min_length, type, non_consecutive_type
t3 = data.task_item("A",3,1,1,24,1,"academy",[])
t2 = data.task_item("C",5,2,2,24,1,"academy",[])
#t4 = data.task_item("D",1,1,4,24,1,"exercise",[])
T = data.list([t1,t2,t3])


# date, begin time, endd time
p1 = data.period_item(1,9,12)
p4 = data.period_item(1,13,15)
p2 = data.period_item(2,9,12)
p5 = data.period_item(2,13,16)
p3 = data.period_item(3,10,15)
P = data.list([p1,p2,p3,p4,p5])

## Algorithm, abstractized : 
# 試著處理 min_length, not done yet

# insufficient time detection : 
def Detect():
    amount_task = 0
    amount_period = 0
    task_list = list(T.sort(type = "deadline"))
    period_list = list(P.sort(type = "time"))
    current_task = 1
    current_period = 1
    while current_task <= len(task_list):    
        
        current_date = task_list[current_task-1].deadline_date
        ##print("date",current_date)
        amount_task = amount_task + task_list[current_task-1].duration
        ##print("amout of tasks",amount_task)
        while(True):
            if (current_period>len(period_list)) or (period_list[current_period-1].date > current_date): # which day ?
                break
            amount_period = amount_period + period_list[current_period-1].end - period_list[current_period-1].begin
            current_period = current_period +1
        ##print("amount of periods",amount_period)
        if amount_task > amount_period:
            print("too much task on day",current_date)
            return -1
        
        current_task = current_task + 1
        
    print("the amount of tasks is okay")
    return 0

def t_is_split(task_item):
    if len(task_item) >7:
        return True
    return False

class schedule_2:
    
    def __init__(self):
        self.task_list = data.list([t1,t2,t3,t4])
        self.period_list = data.list([p1,p2,p3])
        self.flag = []
        #hp.heapify(self.task_list) ###
        self.task_list.sort(type = "deadline")
        self.period_list.sort(type = "time")
        

    def CheckExpire(self,task_deadline_date, task_deadline_time, current_date, current_time):
        if current_date < task_deadline_date:
            return False
        elif current_date == task_deadline_date:
            if current_time <= task_deadline_time:
                return False
        return True
    
    def ExpirationHandling(self,task_item_with_problem):
        S_new = schedule_2()
        index = S_new.task_list.index(task_item_with_problem)
        if index >= 1:
            S_new.task_list.get(index).type = "special" ## WATCHOUT
            return S_new.Schedule()

        else :
            print("index < 1 @ expiration handling")
            return -1
    
    
    def Schedule(self):
        
        schedule = [[]] # name, begin time, end time ### separated by date
        # deadline date, deadline time, importance, duration, name, type, min_length
        current_time = self.period_list.Peek().begin
        current_progress = 0
        current_date = self.period_list.Peek().date
        current_non_consecutive = [] # new
        while self.task_list.len() != 0:
            p_duration = self.period_list.Peek().end - current_time
            t_duration = self.task_list.Peek().duration - current_progress

            if p_duration == 0:
                self.period_list.RemoveMin()
                current_time = self.period_list.Peek().begin
                p_duration = self.period_list.Peek().end - current_time
        
            if t_duration == 0:
                self.task_list.RemoveMin()
                current_progress = 0
                t_duration = self.task_list.Peek().duration

            if self.period_list.Peek().date != current_date:
                schedule.append([]) 
                current_date = current_date +1

            if self.task_list.Peek().type in current_non_consecutive:
                if self.task_list.Swap():
                    t_duration = self.task_list.Peek().duration
                else:
                    print("can't skip this, no other task left")
                    current_non_consecutive = []


            if p_duration >= t_duration: 
                schedule[current_date-1].append((self.task_list.Peek().name, current_time, current_time + t_duration))
                current_time = current_time + t_duration
                if self.CheckExpire(self.task_list.Peek().deadline_date, self.task_list.Peek().deadline_time, current_date, current_time):
                    print("task", self.task_list.Peek().name,"expires at day", current_date)
                    print("old schedule current state :",schedule)
                    return self.ExpirationHandling(self.task_list.Peek())
                current_progress = 0
                current_non_consecutive = self.task_list.Peek().non_consecutive_type
                self.task_list.RemoveMin()
                
            else: # modified here
                # if p_duration >= t_GetMinLength() # don't care about whether the "tail" exceeds min_length
                schedule[current_date-1].append((self.task_list.Peek().name, current_time, current_time + p_duration))
                current_progress = current_progress + p_duration
                current_non_consecutive = self.task_list.Peek().non_consecutive_type
                current_time = current_time + p_duration
                if self.CheckExpire(self.task_list.Peek().deadline_date, self.task_list.Peek().deadline_time, current_date, current_time):
                    print("task",self.task_list.Peek().name,"expires at day", current_date)
                    print("old schedule current state :",schedule)
                    return self.ExpirationHandling(self.task_list.Peek())
                self.period_list.RemoveMin()
                current_time = self.period_list.Peek().begin
        return schedule

class schedule_3: # 先delay，expire就把min_lentgh刪掉
    
    def __init__(self): 
        self.task_list = data.list([t1,t2,t3])
        self.period_list = data.list([p1,p2,p3,p4,p5])
        self.flag = 0 # 先試忽略type，再試忽略min_length
        #hp.heapify(self.task_list) ###
        self.task_list.sort(type = "deadline")
        self.period_list.sort(type = "time")
        

    def CheckExpire(self,task_deadline_date, task_deadline_time, current_date, current_time):
        if current_date < task_deadline_date:
            return False
        elif current_date == task_deadline_date:
            if current_time <= task_deadline_time:
                return False
        return True
    
    def ExpirationHandling(self,task_item_with_problem):
        S_new = schedule_3()
        index = S_new.task_list.index(task_item_with_problem)
        if self.flag == 1: # type
            S_new.flag = 1
            if index >= 1:
                S_new.task_list.get(index).type = "special" ## WATCHOUT
                return S_new.Schedule()
            else :
                print("index < 1 @ expiration handling")
                return -1
        
        elif self.flag == 2: # min_length
            S_new.flag = 2
            empty_period = []
            for i in range(self.period_list.len()):
                p = self.period_list.get(i)
                if (p.date < task_item_with_problem.deadline_date):
                    empty_period.append(p)
                elif p.date == task_item_with_problem.deadline_date:
                    if p.begin < task_item_with_problem.deadline_time:
                        empty_period.append(data.period_item(p.date,p.begin,task_item_with_problem.deadline_time))
                else:
                    break
            # 找出前面空著的時間，把那項塞進去
            S_new.task_list.delete(task_item_with_problem)
            t = task_item_with_problem.copy()
            t.min_length = 0
            t.type = "special2" ################################################################################################
            current_duration_left = t.duration
            for p in empty_period:
                if current_duration_left != 0:
                    p_duration = p.end - p.begin
                    t.importance = t.importance + 0.001
                    if p_duration  <= current_duration_left:
                        t.duration = p_duration
                        S_new.task_list.add(t)
                        current_duration_left = current_duration_left - p_duration
                    else:
                        t.duration = current_duration_left
                        S_new.task_list.add(t)
                        current_duration_left = 0
                else:
                    break
            return S_new.Schedule()
                
    
    
    def Schedule(self):
        
        schedule = [[]] # name, begin time, end time ### separated by date
        # deadline date, deadline time, importance, duration, name, type, min_length
        current_time = self.period_list.Peek().begin
        current_progress = 0
        current_date = self.period_list.Peek().date
        current_non_consecutive = []
        current_period =  1 # new
        while self.task_list.len() != 0:
            p_duration = self.period_list.get(current_period-1).end - current_time 
            t_duration = self.task_list.Peek().duration - current_progress

            if p_duration == 0:
                self.period_list.pop(current_period-1)
                current_period = 1
                current_time = self.period_list.get(current_period-1).begin
                p_duration = self.period_list.get(current_period-1).end - current_time
        
            if t_duration == 0:
                self.task_list.RemoveMin()
                current_progress = 0
                t_duration = self.task_list.Peek().duration

            if self.period_list.Peek().date != current_date:
                schedule.append([]) 
                current_date = current_date +1

            if self.task_list.Peek().type in current_non_consecutive:
                if self.task_list.Swap():
                    t_duration = self.task_list.Peek().duration
                else:
                    print("can't skip this, no other task left")
                    current_non_consecutive = []


            if p_duration >= t_duration: 
                schedule[current_date-1].append((self.task_list.Peek().name, current_time, current_time + t_duration))
                print(schedule)
                current_time = current_time + t_duration
                if self.CheckExpire(self.task_list.Peek().deadline_date, self.task_list.Peek().deadline_time, current_date, current_time):
                    print("task", self.task_list.Peek().name,"expires at day", current_date)
                    print("old schedule current state :",schedule)
                    self.flag = self.flag + 1
                    return self.ExpirationHandling(self.task_list.Peek())
                current_progress = 0
                current_non_consecutive = self.task_list.Peek().non_consecutive_type
                self.task_list.RemoveMin()
                
            else: # modified here
                '''
                #if p_duration >= self.task_list.Peek().min_length # don't care about whether the "tail" exceeds min_length
                schedule[current_date-1].append((self.task_list.Peek().name, current_time, current_time + p_duration))
                current_progress = current_progress + p_duration
                current_non_consecutive = self.task_list.Peek().non_consecutive_type
                current_time = current_time + p_duration
                if self.CheckExpire(self.task_list.Peek().deadline_date, self.task_list.Peek().deadline_time, current_date, current_time):
                    print("task",self.task_list.Peek().name,"expires at day", current_date)
                    print("old schedule current state :",schedule)
                    return self.ExpirationHandling(self.task_list.Peek(),"type")
                self.period_list.RemoveMin()
                current_time = self.period_list.Peek().begin
                '''
                current_period = current_period +1

            if current_period > self.period_list.len():
                print("task", self.task_list.Peek().name,"expires at day", current_date,"due to delay")
                print("old schedule current state :",schedule)
                self.flag = self.flag + 1
                return self.ExpirationHandling(self.task_list.Peek())



        return schedule

if __name__ == "__main__": # testing
    S = schedule_3()
    print(Detect())
    print(S.Schedule())

