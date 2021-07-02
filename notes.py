from tkinter import *
from tkinter import Scrollbar
import tkinter

class Notes(Frame):
    def __init__(self,master):
        super(Notes, self).__init__(master)
        self.allFrame()
        self.firstTime = True
        self.counts = 0
        
    def addTitle(self):
        self.resultT = simpledialog.askstring(title = '獲取資訊',prompt='請輸入姓名：',initialvalue = '可以設定初始值')
        self.titleT = Label(self.col, textvariable=self.resultT, bg="white", fg="pink", font=('Arial', 18))
        self.titleT.grid(row=0, column=0)
        self.counts += 1
    def addContent(self):
        self.resultC = simpledialog.askstring(title = '獲取資訊',prompt='請輸入內容：',initialvalue = '可以設定初始值')
        self.titleC = Label(self.col, textvariable=self.resultT, bg="white", fg="pink", font=('Arial', 18))
        self.titleC.grid(row=self.count, column=1)
        self.counts += 1

    def allFrame(self):
        self.firstFrame = Frame(self)
        self.col = Frame(self.firstFrame)
        if self.firstTime == False:
            self.counts += 1
        self.addTitleBtn = Button(self,text = '添加任務',command = self.addTitle)
        self.addTitleBtn.grid(row=2, column=2)
        
        
        if self.counts >= 1:
            self.addTitleBtn = Button(self.col,text = '添加清單',command = self.addContent)
            self.addTitleBtn.grid(row=1, column=1)
        
        self.firstFrame.grid(row=0, column=0)
        
        
        
        
        
        
    
if __name__ == '__main__':
    root = Tk()
    root.title("Notes")
    root.resizable(0,0)
    app = Notes(root)
    app.configure(background="white")
    root.mainloop()




