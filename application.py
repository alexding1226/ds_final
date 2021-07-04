from tkinter import *
import tkinter
from PIL import Image, ImageTk

class PomodoroPage(Frame):
    def __init__(self,master,data):
        super().__init__(master)
        self.createWidgets()
        self.pack(side=TOP)
        
        self.timer = None
        self.conti = 0
        self._paused = False
        self.timerToStart = 25
        
    def createWidgets(self):

        self.timerVariable = StringVar()
        self.timerVariable.set(None)
        self.canvas = Canvas(bg="#ffbc92", highlightthickness=0)
        
        self.tomatoImg = PhotoImage(file="2tomato.png")
        # Here need to be revise for the windows xy
        self.canvas.create_image(145, 114, image=self.tomatoImg)
        # Here need to be revise for windows y+11
        self.timerLabel = self.canvas.create_text(145, 125, text="00:00", fill="white", font=('Arial', 112))
        
        self.type = Label(self, text="Work", bg="#ffbc92", fg="sienna", font=('Arial', 40))
        self.type.grid(row=0, column=0, sticky="ewns")
        
        self.canvas.pack(side=TOP)
        
        self.frame1 = Frame(self,bg="#ffbc92")
        
        self.time = Scale(self.frame1, label='Time-period', from_=25, to=55, orient=HORIZONTAL, length=200, showvalue=0,tickinterval=10, resolution=1, bg="#ffbc92")
        self.time.grid(row=2, column=0)
        self.b1=Button(self.frame1,text='Set',command=self.set1, bg="#ffbc92")
        self.b1.grid(row=2, column=1)
        
        
        self.frame1.grid(sticky="ewns")
        
        

        self.frame2 = Frame(self,bg="#ffbc92")
        self.startButton = Button(self.frame2,text="Start",fg="RED",activeforeground="BlanchedAlmond",width="8",height="2",font=('Arial',11),command=self.startTime)
        self.startButton.grid(row=4, column=1, sticky="ewns")

        self.stopButton = Button(self.frame2,text="Stop",fg="green",background = 'BlanchedAlmond',width="8",height="2",activebackground="#ffbc92",activeforeground="#ffbc92",font=('Arial',11),command=self.stopTime)
        self.stopButton.grid(row=4, column=2, sticky="ewns")

        self.resetButton = Button(self.frame2,text="Reset",fg="black",width="8",height="2",font=('Arial',11),command=self.resetTime)
        self.resetButton.grid(row=4, column=3, sticky="ewns")
        self.frame2.grid(columnspan=5)

    
    def set1(self):
        self.timerToStart = self.time.get()


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
            self.type.config(text="Work")
            self.type.grid(row=0, column=0)
            self.timerToStart = self.time.get()
        else:
            self.type.config(text="Break")
            self.type.grid(row=0, column=0)
            self.timerToStart = int(0.1*(self.time.get()))
        self.countdown(self.timerToStart * 60)
        self._paused = True

    def countdown(self,timeInSeconds, start=True):
    
        if timeInSeconds >= 0:
            if start:
                self._starttime = timeInSeconds
            if self._paused:
                self.timer = self.master.after(1000,self.countdown,timeInSeconds,False)
            else:
                mins,secs = divmod(timeInSeconds,60)
                self.canvas.itemconfig(self.timerLabel, text=f"{mins}:{secs}")
                self.timer = self.master.after(1000,self.countdown,timeInSeconds-1,False)
        else:
            self.conti += 1
            self.resetTime()
            self.startTime()

if __name__ == '__main__':
    root = Tk()
    root.title("Pomodoro Timer")
    # Here need to be revise for the windows size
    root.geometry("700x500")
    root.configure(bg="#ffbc92")
    app =PomodoroPage(root,None)
    app.configure(background="#ffbc92")
    root.mainloop()
