#import algorithm.py
import heapq as hp

## data structure dependent : 

# deadline date, deadline time, importance, duration, name, type, min_length, non_consecutive
task_list = [[2,24,1,3,"B","exercise",1,["academy"]],[3,24,2,3,"C","academy",1,[]],[1,24,1,3,"A","academy",1,[]], [3,24,1,1,"D","Exercise",1,[]]]
# date, begin time, endd time
period_list = [(1,9,14),(2,13,16),(3,12,15)]

def Peek(heap):
    return heap[0]

def h_RemoveMin(heap):
    hp.heappop(heap)

def l_RemoveMin(list):
    list.pop(0)

def p_GetDate(period_item):
    return period_item[0]

def p_GetBegin(period_item):
    return period_item[1]

def p_GetEnd(period_item):
    return period_item[2]

def t_GetDate(task_item):
    return task_item[0]

def t_GetTime(task_item):
    return task_item[1]

def t_GetDuration(task_item):
    return task_item[3]

def t_GetName(task_item):
    return task_item[4]

def t_GetType(task_item):
    return task_item[5]

def t_GetMinLength(task_item):
    return task_item[6]

def t_GetNonConsecutive(task_item):
    return task_item[7]

def Swap(list):
    if len(list)>1:
        temp = list[0]
        list[0] = list[1]
        list[1] = temp
        return True
    return False

## Algorithm, abstractized : 
# 試著處理 min_length, not done yet

# insufficient time detection : 
def Detect():
    amount_task = 0
    amount_period = 0
    _task_list = sorted(task_list)
    _period_list = sorted(period_list)
    current_task = 1
    current_period = 1
    while current_task <= len(_task_list):    
        
        current_date = t_GetDate(_task_list[current_task-1])
        print("date",current_date)
        amount_task = amount_task + t_GetDuration(_task_list[current_task-1])
        print("amout of tasks",amount_task)
        while(True):
            if (current_period>len(_period_list)) or (p_GetDate(_period_list[current_period-1]) > current_date): # which day ?
                break
            amount_period = amount_period + p_GetEnd(_period_list[current_period-1]) - p_GetBegin(_period_list[current_period-1])
            current_period = current_period +1
        print("amount of periods",amount_period)
        if amount_task > amount_period:
            print("too much task on day",current_date)
            return -1
        
        current_task = current_task + 1
        
    print("the amount of tasks is okay")
    return 0

class schedule_1:
    def __init__(self):
        self.task_list = task_list
        self.period_list = period_list

    def Schedule(self):
        hp.heapify(self.task_list)
        hp.heapify(self.period_list)
        schedule = [[]] # name, begin time, end time ### separated by date
        # deadline date, deadline time, importance, duration, name, type, min_length
        current_time = p_GetBegin(Peek(self.period_list))
        current_progress = 0
        current_date = p_GetDate(Peek(self.period_list))
        while len(self.task_list) != 0:
            p_duration = p_GetEnd(Peek(self.period_list)) - current_time
            t_duration = t_GetDuration(Peek(self.task_list)) - current_progress
    
            if p_duration == 0:
                RemoveMin(self.period_list)
                current_time = p_GetBegin(Peek(self.period_list))
                p_duration = p_GetEnd(Peek(self.period_list)) - current_time
        
            if t_duration == 0:
                RemoveMin(self.task_list)
                current_progress = 0
                t_duration = t_GetDuration(Peek(self.task_list))

            if p_GetDate(Peek(self.period_list)) != current_date:
                schedule.append([]) 
                current_date = current_date +1

            if p_duration >= t_duration: 
                schedule[current_date-1].append((t_GetName(Peek(self.task_list)), current_time, current_time + t_duration))
                current_time = current_time + t_duration
                current_progress = 0
                RemoveMin(self.task_list)
        
            else: # modified here
                # if p_duration >= t_GetMinLength() # don't care about whether the "tail" exceeds min_length
                schedule[current_date-1].append((t_GetName(Peek(self.task_list)), current_time, current_time + p_duration))
                current_progress = current_progress + p_duration
                RemoveMin(self.period_list)
                current_time = p_GetBegin(Peek(self.period_list))
        return schedule

def t_is_split(task_item):
    if len(task_item) >7:
        return True
    return False

class schedule_2:
    def __init__(self):
        self.task_list = task_list
        self.period_list = period_list

    def CheckExpire(self,task_deadline_date, task_deadline_time, current_date, current_time):
        if current_date < task_deadline_date:
            return False
        elif current_date == task_deadline_date:
            if current_time <= task_deadline_time:
                return False
        return True

    def Schedule(self):
        hp.heapify(self.task_list)
        self.period_list.sort()

        schedule = [[]] # name, begin time, end time ### separated by date
        # deadline date, deadline time, importance, duration, name, type, min_length
        current_time = p_GetBegin(Peek(self.period_list))
        current_progress = 0
        current_date = p_GetDate(Peek(self.period_list))
        current_non_consecutive = [] # new
        while len(self.task_list) != 0:
            p_duration = p_GetEnd(Peek(self.period_list)) - current_time
            t_duration = t_GetDuration(Peek(self.task_list)) - current_progress

            if p_duration == 0:
                l_RemoveMin(self.period_list)
                current_time = p_GetBegin(Peek(self.period_list))
                p_duration = p_GetEnd(Peek(self.period_list)) - current_time
        
            if t_duration == 0:
                h_RemoveMin(self.task_list)
                current_progress = 0
                t_duration = t_GetDuration(Peek(self.task_list))

            if p_GetDate(Peek(self.period_list)) != current_date:
                schedule.append([]) 
                current_date = current_date +1

            if t_GetType(Peek(self.task_list)) in current_non_consecutive:
                if Swap(self.task_list):
                    t_duration = t_GetDuration(Peek(self.task_list))
                else:
                    print("can't skip this, no other task left")
                    current_non_consecutive = []


            if p_duration >= t_duration: 
                schedule[current_date-1].append((t_GetName(Peek(self.task_list)), current_time, current_time + t_duration))
                current_time = current_time + t_duration
                if self.CheckExpire(t_GetDate(Peek(self.task_list)), t_GetTime(Peek(self.task_list)), current_date, current_time):
                    print("task",t_GetName(Peek(self.task_list)),"expires at day", current_date)
                    #break
                current_progress = 0
                current_non_consecutive = t_GetNonConsecutive(Peek(task_list))
                h_RemoveMin(self.task_list)
        
            else: # modified here
                # if p_duration >= t_GetMinLength() # don't care about whether the "tail" exceeds min_length
                schedule[current_date-1].append((t_GetName(Peek(self.task_list)), current_time, current_time + p_duration))
                current_progress = current_progress + p_duration
                current_non_consecutive = t_GetNonConsecutive(Peek(task_list))
                current_time = current_time + p_duration
                if self.CheckExpire(t_GetDate(Peek(self.task_list)), t_GetTime(Peek(self.task_list)), current_date, current_time):
                    print("task",t_GetName(Peek(self.task_list)),"expires at day", current_date)
                    #break
                l_RemoveMin(self.period_list)
                current_time = p_GetBegin(Peek(self.period_list))
        return schedule

if __name__ == "__main__": # testing
    S = schedule_2()
    print(S.Schedule())
    #print(Detect())
