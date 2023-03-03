from tkinter import *
a=Tk()
a.minsize(width=280,height=300)
a.maxsize(width=300,height=320)
a.title("Lambda Function Test")
b=""
var=StringVar()
def btn(txt):
    global b
    b=b+str(txt)
    var.set(b)
e1=Entry(a,font=2,textvariable=var)
e1.place(x=25,y=25)
b1=Button(a,text="Click Ok",font=8,command=lambda:btn(":-)"))
b1.place(x=25,y=70)
a.mainloop()