import copy
import heapq

'''
# from Alex's work
class Task():
    def __init__(self, name, duration, importance,deadline,min_length = 1,
            type = "study", non_consecutive_type = []) :
        self.name = name # str
        self.duration = duration # int, every 30 min or 10 min 
        self.importance = importance # int 1~5, 5 is the most important
        self.deadline = deadline # int, how many hours left
        self.type = type # str
        self.min_length = min_length # int, every 30 min or 10 min 
        self.non_consecutive_type = non_consecutive_type # list of types that can't take place right after this task
#


class algo_task:
    def __init__(self,description): # the discription is an object of class Task
        self.name = discription.name
        self.duration = discription.duration
        self.priority = self.CalculatePriority(discription.importance, discription.deadline)
        self.type = discription.type
        self.min_length = discription.min_length
        self.non_consecutive_type = discription.non_consecutive_type

    def CalculatePriority(importance, remaining_time):
        k = 1 # TBD
        return (k*importance - remaining_time)

class algo_period:
    def __init__(self,date,begin_time,end_time):
        self.date = date
        self.begin_time = begin_time
        self.end_time = end_time
        self.length = end_time - begin_time

class algo_task_scheduling:
    def __init__(self,items,available): # items is a list of Task objects, time for available sections
        self.task = heapq()
        for i in items:
            self.task.heappush(i)
        self.time = heapq()
        for i in items:
            self.time.heappush(i)
        # need modification, to avoid affect the original data
'''


# Pseudo version: 
# total time insufficient warning should take plasce @ task adding section
# that deals with the case that the sum of time of the first n task exceed the sum of time 
# ... add up to the deadline of the n'th task

# so maybe I shoud try not split the task if possible
# the config. of split or not split 
# 先拆大的，窮舉？
