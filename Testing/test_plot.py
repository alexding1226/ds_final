import algo
import algo_Exp
import DataFormat_Exp as data
import timeit
import matplotlib.pyplot as mat
import math

'''
t1 = data.task_item("B",3,1,2,24,1,"exercise",["academy"])
t3 = data.task_item("A",3,1,1,24,1,"academy",[])
t2 = data.task_item("C",5,2,2,24,1,"academy",[])
#t4 = data.task_item("D",1,1,4,24,1,"exercise",[])
T = [t1,t2,t3]

p1 = data.period_item(1,9,12)
p4 = data.period_item(1,13,15)
p2 = data.period_item(2,9,12)
p5 = data.period_item(2,13,16)
p3 = data.period_item(3,10,15)
P = [p1,p2,p3,p4,p5]
'''




'''
T =[]
T.append(data.task_item("C",1,1,2,12,0,1,"exercise",["exercise"]))
T.append(data.task_item("C",1,1,2,24,1,1,"exercise",["exercise"]))
T.append(data.task_item("C",1,1,3,12,2,1,"exercise",["exercise"]))
T.append(data.task_item("A",2,1,1,12,0,1,"academy",[]))
T.append(data.task_item("A",2,1,1,24,1,1,"academy",[]))
T.append(data.task_item("A",1,1,2,24,2,1,"academy",[]))
T.append(data.task_item("D",2,1,4,24,0,1,"academy",[]))

P =[]
p1 = data.period_item(1,9,12)
p4 = data.period_item(1,13,14)
p2 = data.period_item(2,9,13)
p5 = data.period_item(2,15,16)
p3 = data.period_item(3,10,15)
P = [p1,p2,p3,p5,p4]
'''

'''#言鼎
t1 = data.task_item("B",3,1,3,24,1,"exercise",["academy"])
t3 = data.task_item("A",3,1,1,24,1,"academy",[])
t2 = data.task_item("C",3,2,2,24,1,"academy",[])
#t4 = data.task_item("D",1,1,4,24,1,"exercise",[])
T = [t1,t2,t3]

p1 = data.period_item(1,7,9)
p4 = data.period_item(1,10,11)
p6 = data.period_item(1,13,15)
p2 = data.period_item(2,9,10)
p5 = data.period_item(2,13,13)
p3 = data.period_item(3,10,13)
P = [p1,p2,p3,p4,p5,p6]
'''

def test():
    S = algo.schedule_3(T,P)
    print(S.Detect())
    #print(S.Schedule())
    S.Schedule()

def test2():
    S = algo_Exp.schedule_3(T,P)
    print(S.Detect())
    S.Schedule()
    
''''''

T =[]
P =[]

def DataGenerating(k):
    for i in range(2,k+50,2):
        T.append(data.task_item(chr(65+(i%26)),3,1,500,24,0,1,"test",[""]))

    
    for i in range(0,k+50):
        P.append(data.period_item(i,9,11))
    k = k + 50
    return k
    
''''''

if __name__ == "__main__": # testing
    #x = [50,100,150,200,250,300,350,400,450,500]
    #y = [0.0277,0.1136,0.2372,0.5006,0.9424,
    #        1.57,2.3888,3.3416,4.788,6.39]
    x = []
    y = []
    k = 0
    
    for i in range(0,10):
        k = DataGenerating(k)
        print(k,":")
        t = timeit.timeit(stmt="test()", setup="from __main__ import test", number= 100)
        print("test",k, ":", "pop(0) :",t)
        x.append(k)
        y.append(t)
    
    mat.plot(x,y)
    
    a = []
    b = []
    for i in range(50,500,50):
        a.append(i)
        #b.append(y[0]*((i//50)^2)*math.log(i)/math.log(50))
        b.append(y[0]*((i//50)^3))
    mat.plot(a,b) 
    
    mat.show()
    
'''
t2, p2, 30000
pop(0) : 2.1528013
pop()  : 2.0687255999999996

t laborous :300
pop(0) : 1.0091413 
1000 : 超過 max recursion depth
pop(0) : 2.2455588 for 450
'''