from tkinter import *
import tkinter
#import notify2 as notification
#from playsound import playsound

class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.pack(anchor=CENTER,expand=1,fill=BOTH)
        self.createWidgets()
        self.timer = None
        self._paused = False



    def createWidgets(self):

        self.timerVariable = StringVar()
        self.timerVariable.set(None)
    
        self.firstButtonFrame = Frame(self)

        self.time = Scale(self.firstButtonFrame, label='Time-period', from_=25, to=55, orient=HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=1)
        self.time.pack(side=LEFT,padx='0')
        self.b1=Button(self.firstButtonFrame,text='Set',command=self.set1)
        self.b1.pack(side=LEFT,padx='0')
        #self.timerToStart = self.timerVariable.get()
        
        self.firstButtonFrame.pack(side=TOP)
        
        self.timerLabel = Label(self,text="00:00",font=("Cantrell",70),bg="white")
        self.timerLabel.pack(side=TOP,pady="5")

        self.secondButtonFrame = Frame(self,bg="white")
        self.startButton = Button(self.secondButtonFrame,text="Start",fg="RED",bg="#5da423",activebackground="green",activeforeground="white",width="8",height="2",font=('Arial',11),command=self.startTime)
        self.startButton.pack(side=LEFT,padx='5')

        self.stopButton = Button(self.secondButtonFrame,text="Stop",fg="yellow",bg="red",width="8",height="2",activebackground="#c60f13",activeforeground="white",font=('Arial',11),command=self.stopTime)
        self.stopButton.pack(side=LEFT,padx='5')

        self.resetButton = Button(self.secondButtonFrame,text="Reset",fg="black",width="8",height="2",font=('Arial',11),command=self.resetTime)
        self.resetButton.pack(side=LEFT,padx='5')
        self.secondButtonFrame.pack(side=TOP,pady="5")

    
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
            self.countdown(self.timerToStart)

    def stopTime(self):
        if self.timer is not None:
            self._paused = True

    # I have to work on the reset method more cos it's not working as I expect
    def resetTime(self):
        self.master.after_cancel(self.timer)
        self.timer = None
        self._paused = False
        self.countdown(self.timerToStart)
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
            self.resetTime()
            self.startTime()
            #self.startTime()

if __name__ == '__main__':
    root = Tk()
    root.title("Pomodoro Timer")
    root.resizable(0,0)
    app = Application(root)
    app.configure(background="white")
    root.mainloop()
