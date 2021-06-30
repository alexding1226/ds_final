#import algorithm.py
import heapq as hp

# 先做一個可以work的演算法出來，先不要管 min_length & consecutive

# priority (DL), importance, duration, name, type
task_list = [(2,1,3,"B","exercise"),(2,2,3,"C","academy"),(1,1,3,"A","academy")]
# date, begin time, endd time
period_list = [(1,9,14),(2,13,16),(3,12,15)]

hp.heapify(task_list)
hp.heapify(period_list)
schedule = [[]] # name, begin time, end time ### separated by date

current_time = period_list[0][1] # first begin time ## new list for new date
current_progress = 0
current_date = period_list[0][0]
while len(task_list) != 0:
    p_duration = period_list[0][2] - current_time
    t_duration = task_list[0][2] - current_progress
    
    
    if p_duration == 0:
        hp.heappop(period_list)
        current_time = period_list[0][1]
        p_duration = period_list[0][2] - current_time
        
    if t_duration == 0:
        hp.heappop(task_list)
        current_progress = 0
        t_duration = task_list[0][2]

    if period_list[0][0] != current_date:
        schedule.append([]) 
        current_date = current_date +1

    if p_duration >= t_duration: 
        schedule[current_date-1].append((task_list[0][3], current_time, current_time + t_duration))
        current_time = current_time + t_duration
        current_progress = 0
        hp.heappop(task_list)
    
    else:
        schedule[current_date-1].append((task_list[0][3], current_time, current_time + p_duration))
        current_progress = current_progress + p_duration
        hp.heappop(period_list)
        current_time = period_list[0][1]
        
if __name__ == "__main__": # testing
    print(schedule)
