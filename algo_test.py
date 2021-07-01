#import algorithm.py
import heapq as hp

## data structure dependent : 

# deadline date, deadline time, importance, duration, name, type, min_length
task_list = [(2,24,1,3,"B","exercise",1),(3,24,2,3,"C","academy",1),(1,24,1,3,"A","academy",1)]
# date, begin time, endd time
period_list = [(1,9,14),(2,13,16),(3,12,15)]
hp.heapify(task_list)
hp.heapify(period_list)

def Peek(heap):
    return heap[0]

def RemoveMin(heap):
    hp.heappop(heap)

def p_GetDate(period_item):
    return period_item[0]

def p_GetBegin(period_item):
    return period_item[1]

def p_GetEnd(period_item):
    return period_item[2]

def t_GetDate(task_item):
    return task_item[0]

def t_GetDuration(task_item):
    return task_item[3]

def t_GetName(task_item):
    return task_item[4]

def t_GetMinLength(task_item):
    return task_item[6]

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
    


def Schedule():
    schedule = [[]] # name, begin time, end time ### separated by date
    # deadline date, deadline time, importance, duration, name, type, min_length
    current_time = p_GetBegin(Peek(period_list))
    current_progress = 0
    current_date = p_GetDate(Peek(period_list))
    while len(task_list) != 0:
        p_duration = p_GetEnd(Peek(period_list)) - current_time
        t_duration = t_GetDuration(Peek(task_list)) - current_progress
    
        if p_duration == 0:
            RemoveMin(period_list)
            current_time = p_GetBegin(Peek(period_list))
            p_duration = p_GetEnd(Peek(period_list)) - current_time
        
        if t_duration == 0:
            RemoveMin(task_list)
            current_progress = 0
            t_duration = t_GetDuration(Peek(task_list))

        if period_list[0][0] != current_date:
            schedule.append([]) 
            current_date = current_date +1

        if p_duration >= t_duration: 
            schedule[current_date-1].append((t_GetName(Peek(task_list)), current_time, current_time + t_duration))
            current_time = current_time + t_duration
            current_progress = 0
            RemoveMin(task_list)
    
        else: # modified here
            # if p_duration >= t_GetMinLength() # don't care about whether the "tail" exceeds min_length
            schedule[current_date-1].append((t_GetName(Peek(task_list)), current_time, current_time + p_duration))
            current_progress = current_progress + p_duration
            RemoveMin(period_list)
            current_time = p_GetBegin(Peek(period_list))
    return schedule

if __name__ == "__main__": # testing
    #print(Schedule())
    print(Detect())
