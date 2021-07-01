from tkinter import *
import tkinter

class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.pack(anchor=CENTER,expand=1,fill=BOTH)
        self.createWidgets()
        self.timer = None
        self.conti = 0
        self._paused = False



    def createWidgets(self):

        self.timerVariable = StringVar()
        self.timerVariable.set(None)
    
        self.firstButtonFrame = Frame(self)

        self.time = Scale(self.firstButtonFrame, label='Time-period', from_=25, to=55, orient=HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=1)
        self.time.grid(row=1, column=0)
        self.b1=Button(self.firstButtonFrame,text='Set',command=self.set1)
        self.b1.grid(row=1, column=1)
    
        
        self.firstButtonFrame.grid(row=0, column=0)
        
        self.timerLabel = Label(self,text="00:00",font=("Cantrell",70),bg="white")
        self.timerLabel.grid(row=2, column=0)

        self.secondButtonFrame = Frame(self,bg="white")
        self.startButton = Button(self.secondButtonFrame,text="Start",fg="RED",activebackground="green",activeforeground="white",width="8",height="2",font=('Arial',11),command=self.startTime)
        self.startButton.grid(row=3, column=1)

        self.stopButton = Button(self.secondButtonFrame,text="Stop",fg="yellow",bg="red",width="8",height="2",activebackground=,activeforeground="white",font=('Arial',11),command=self.stopTime)
        self.stopButton.grid(row=3, column=2)

        self.resetButton = Button(self.secondButtonFrame,text="Reset",fg="black",width="8",height="2",font=('Arial',11),command=self.resetTime)
        self.resetButton.grid(row=3, column=3)
        self.secondButtonFrame.grid(row=3, column=0)

    
    def set1(self):
        self.timerToStart = self.time.get()
        
    def startClock(self):
        
        if self.timer is not None:
            self.master.after_cancel(self.timer)
        self._paused = False
        self.countdown(timerToStart * 60)


    def startTime(self):
        self._paused = False
        if self.timer is None:
            self.countdown(self.timerToStart*60)

    def stopTime(self):
        if self.timer is not None:
            self._paused = True
            
    def resetTime(self):
        self.master.after_cancel(self.timer)
        self.timer = None
        self._paused = False
        if self.conti%2 == 0:
            self.timerToStart = self.time.get()
        else:
            self.timerToStart = int(0.1*(self.time.get()))
        self.countdown(self.timerToStart*60)
        self._paused = True

    def countdown(self,timeInSeconds, start=True):
    
        if timeInSeconds >= 0:
            if start:
                self._starttime = timeInSeconds
            if self._paused:
                self.timer = self.master.after(1000,self.countdown,timeInSeconds,False)
            else:
                mins,secs = divmod(timeInSeconds,60)
                timeformat = "{0:02d}:{1:02d}".format(mins,secs)
                app.timerLabel.configure(text=timeformat)
                self.timer = self.master.after(1000,self.countdown,timeInSeconds-1,False)
        else:
            self.conti += 1
            self.resetTime()
            self.startTime()

if __name__ == '__main__':
    root = Tk()
    root.title("Pomodoro Timer")
    root.resizable(0,0)
    app = Application(root)
    app.configure(background="white")
    root.mainloop()
