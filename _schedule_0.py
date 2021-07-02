#import algorithm.py
import heapq as hp

## data structure dependent : 

# priority (DL), importance, duration, name, type, min_length
task_list = [(2,1,3,"B","exercise",1),(2,2,3,"C","academy",1),(1,1,3,"A","academy",1)]
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

def t_GetDuration(task_item):
    return task_item[2]

def t_GetName(task_item):
    return task_item[3]

def t_GetMinLength(task_item):
    return task_item[5]

## Algorithm, abstractized : 
# 試著處理 min_length, not done yet

schedule = [[]] # name, begin time, end time ### separated by date
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
        
if __name__ == "__main__": # testing
    print(schedule)
