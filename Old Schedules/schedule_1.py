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
                h_RemoveMin(self.period_list)
                current_time = p_GetBegin(Peek(self.period_list))
                p_duration = p_GetEnd(Peek(self.period_list)) - current_time
        
            if t_duration == 0:
                h_RemoveMin(self.task_list)
                current_progress = 0
                t_duration = t_GetDuration(Peek(self.task_list))

            if p_GetDate(Peek(self.period_list)) != current_date:
                schedule.append([]) 
                current_date = current_date +1

            if p_duration >= t_duration: 
                schedule[current_date-1].append((t_GetName(Peek(self.task_list)), current_time, current_time + t_duration))
                current_time = current_time + t_duration
                current_progress = 0
                h_RemoveMin(self.task_list)
        
            else: # modified here
                # if p_duration >= t_GetMinLength() # don't care about whether the "tail" exceeds min_length
                schedule[current_date-1].append((t_GetName(Peek(self.task_list)), current_time, current_time + p_duration))
                current_progress = current_progress + p_duration
                h_RemoveMin(self.period_list)
                current_time = p_GetBegin(Peek(self.period_list))
        return schedule


#import algorithm.py
import heapq as hp

## data structure dependent : 

# Input data : 
# deadline date, deadline time, importance, duration, name, type, min_length, non_consecutive
task_list = [[2,24,1,3,"B","exercise",1,["academy"]],[2,24,2,3,"C","academy",1,[]],[1,24,1,3,"A","academy",1,[]], [4,24,1,1,"D","Exercise",1,[]]]
# date, begin time, endd time
period_list = [(1,9,12),(2,13,19),(3,12,15)]

def Peek(heap):
    return heap[0]

def h_RemoveMin(heap):
    #hp.heappop(heap) ###
    heap.pop(0)

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


if __name__ == "__main__": # testing
    S = schedule_1()
    print(S.Schedule())