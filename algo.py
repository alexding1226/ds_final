import DataFormat as data

# total time insufficient warning should take plasce @ task adding section
# that deals with the case that the sum of time of the first n task exceed the sum of time 
# ... add up to the deadline of the n'th task
# 現在版本 : 先試著不切，照non_consecutive排。if 不行,type豁免。if 再不行，切最後一個，填進去前面的空檔
# 兩種 items 都會被 modified，所以需要 deepcopy

class schedule_3:
    
    def __init__(self,data_task_list,data_period_list): 
        self.data_task_list = data_task_list
        self.data_task_list.sort()
        self.data_period_list = data_period_list
        self.data_period_list.sort()
        
        self.task_list = data.my_list(data_task_list)
        self.period_list = data.my_list([])
        for i in data_period_list:
            self.period_list.append(i.copy())
        
        self.flag = 0 # 先試忽略type，再試忽略min_length
        self.task_list.sort()
        self.period_list.sort()

    def Detect(self): # insufficient time detection : # using built-in list
        amount_task = 0
        amount_period = 0
        task_list = self.data_task_list
        period_list = self.data_period_list
        task_list.sort()
        period_list.sort()
        current_task = 1
        current_period = 1
        while current_task <= len(task_list):    
            
            current_date = task_list[current_task-1].deadline_date
            ##print("date",current_date)
            amount_task = amount_task + task_list[current_task-1].duration
            ##print("amout of tasks",amount_task)
            while(True):
                if (current_period > len(period_list)) or (period_list[current_period-1].date > current_date): # which day ?
                    break
                amount_period = amount_period + period_list[current_period-1].end - period_list[current_period-1].begin
                current_period = current_period +1
            ##print("amount of periods",amount_period)
            if amount_task > amount_period:
                ##print("too much task on day",current_date)
                return current_date
            
            current_task = current_task + 1
            
        ##print("the amount of tasks is okay")
        return 0
        
    def CheckExpire(self,task_deadline_date, task_deadline_time, current_date, current_time):
        if current_date < task_deadline_date:
            return False
        elif current_date == task_deadline_date:
            if current_time <= task_deadline_time:
                return False
        return True
    
    def ExpirationHandling(self,task_item_with_problem):
        S_new = schedule_3(self.data_task_list,self.data_period_list)
        index = S_new.task_list.index(task_item_with_problem)
        if self.flag == 1: # type
            S_new.flag = 1
            if index >= 1:
                S_new.data_task_list[index].type = "special"
                S_new.task_list[index].type = "special" ## WATCHOUT
                return S_new.Schedule()
            else :
                self.flag = self.flag +1
                ##print("index < 1 @ expiration handling")
                ##return -1
        
        if self.flag == 2: # min_length
            S_new.flag = 0
            empty_period = []
            for i in range(len(self.period_list)):
                p = self.period_list[i]
                if (p.date < task_item_with_problem.deadline_date):
                    empty_period.append(p)
                elif p.date == task_item_with_problem.deadline_date:
                    if p.begin < task_item_with_problem.deadline_time:
                        if p.end <= task_item_with_problem.deadline_time:
                            empty_period.append(p)
                        else:
                            empty_period.append(data.period_item(p.date,p.begin,task_item_with_problem.deadline_time))
                else:
                    break
            # 找出前面空著的時間，把那項分拆
            #S_new.task_list.delete(task_item_with_problem)
            self.data_task_list.remove(task_item_with_problem)
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
                        #S_new.task_list.add(t.copy())
                        self.data_task_list.append(t.copy())
                        current_duration_left = current_duration_left - p_duration
                    else:
                        t.duration = current_duration_left
                        #S_new.task_list.add(t)
                        self.data_task_list.append(t)
                        current_duration_left = 0
                else:
                    break
            S_new.task_list = data.my_list(self.data_task_list)
            S_new.task_list.sort()
            return S_new.Schedule()

        else:
            print("flag > 2")
            return -1
    
    def Schedule(self):
        
        schedule = [[]] # name, begin time, end time ### separated by date
        current_period =  1 
        current_date = self.period_list.Peek().date
        current_time = self.period_list.Peek().begin
        current_progress = 0
        current_non_consecutive = []
        p_duration = self.period_list.Peek().end - current_time 
        t_duration = self.task_list.Peek().duration - current_progress

        while len(self.task_list) != 0:
          
            if len(schedule) < current_date:
                schedule.append([]) 
                
            if self.task_list.Peek().type in current_non_consecutive: ## 可優化，變成試試看從下一天排起
                if self.task_list.Swap():
                    t_duration = self.task_list.Peek().duration
                else:
                    ##print("can't skip this, no other task left")
                    current_non_consecutive = []

            if current_period > len(self.period_list):
                ##print("task", self.task_list.Peek().name,"expires at day", current_date,"due to delay")
                ##print("old schedule current state :",schedule)
                self.flag = self.flag + 1
                return self.ExpirationHandling(self.task_list.Peek())

            if p_duration >= t_duration: 
                schedule[current_date-1].append((self.task_list.Peek().name, current_time, current_time + t_duration))
                ##print(schedule)
                current_time = current_time + t_duration
                self.period_list[current_period-1].begin = current_time
                if self.CheckExpire(self.task_list.Peek().deadline_date, self.task_list.Peek().deadline_time, current_date, current_time):
                    ##print("task", self.task_list.Peek().name,"expires at day", current_date)
                    ##print("old schedule current state :",schedule)
                    self.flag = self.flag + 1
                    return self.ExpirationHandling(self.task_list.Peek())
                current_progress = 0
                current_non_consecutive = self.task_list.Peek().non_consecutive_type
                self.task_list.RemoveMin()

                if current_time == self.period_list[current_period-1].end:
                    self.period_list.pop(current_period-1)
                else:
                    self.period_list[current_period-1].begin = current_time
                
                current_period = 1
                if len(self.task_list) != 0:
                    t_duration = self.task_list.Peek().duration - current_progress
                else:
                    break
                
            else: 
                current_period = current_period +1
            
            if current_period <= len(self.period_list):
                current_date = self.period_list[current_period-1].date
                current_time = self.period_list[current_period-1].begin
                p_duration = self.period_list[current_period-1].end - current_time 

        return schedule
