import mysql.connector
import tkinter
from tkinter import messagebox
def student():
    swindow=tkinter.Tk()
    swindow.title("Student Information")
    swindow.geometry("300x300")
    l1=tkinter.Label(swindow,text="Rollno",font=("Arial",20))
    l2=tkinter.Label(swindow,text="Name",font=("Arial",20))
    l3=tkinter.Label(swindow,text="Course",font=("Arial",20))
    e1=tkinter.Entry(swindow,width=10,font=("Arial",20))
    e2=tkinter.Entry(swindow,width=10,font=("Arial",20))
    e3=tkinter.Entry(swindow,width=10,font=("Arial",20))
    def add():
        cn=mysql.connector.connect(user="root",password="root",database="studentdb")
        c=cn.cursor()
        cmd="insert into student values(%s,%s,%s)"
        c.execute(cmd,params=[int(e1.get()),e2.get(),e3.get()])
        k=c.rowcount
        if k>0:
            messagebox.showinfo("info","Student Added")
            cn.commit()
            e1.delete(0,tkinter.END)
            e2.delete(0,tkinter.END)
            e3.delete(0,tkinter.END)

    def close():
        swindow.destroy()
                  
    b1=tkinter.Button(swindow,text="Add",font=("Arial",20),command=add)
    b2=tkinter.Button(swindow,text="Close",font=("Arial",20),command=close)

    l1.grid(row=1,column=1)
    e1.grid(row=1,column=2)
    l2.grid(row=2,column=1)
    e2.grid(row=2,column=2)
    l3.grid(row=3,column=1)
    e3.grid(row=3,column=2)
    b1.grid(row=4,column=1)
    b2.grid(row=4,column=2)



def marks():
    swindow=tkinter.Tk()
    swindow.title("Marks Information")
    swindow.geometry("300x300")
    l1=tkinter.Label(swindow,text="Rollno",font=("Arial",20))
    l2=tkinter.Label(swindow,text="Subject1",font=("Arial",20))
    l3=tkinter.Label(swindow,text="Subject2",font=("Arial",20))
    l4=tkinter.Label(swindow,text="Subject3",font=("Arial",20))
    e1=tkinter.Entry(swindow,width=10,font=("Arial",20))
    e2=tkinter.Entry(swindow,width=10,font=("Arial",20))
    e3=tkinter.Entry(swindow,width=10,font=("Arial",20))
    e4=tkinter.Entry(swindow,width=10,font=("Arial",20))
    def add():
        cn=mysql.connector.connect(user="root",password="root",database="studentdb")
        c=cn.cursor()
        cmd="insert into marks values(%s,%s,%s,%s)"
        c.execute(cmd,params=[int(e1.get()),int(e2.get()),int(e3.get()),int(e4.get())])
        k=c.rowcount
        if k>0:
            messagebox.showinfo("info","Marks Added")
            cn.commit()
            e1.delete(0,tkinter.END)
            e2.delete(0,tkinter.END)
            e3.delete(0,tkinter.END)
            e4.delete(0,tkinter.END)
    def close():
        swindow.destroy()
                  
    b1=tkinter.Button(swindow,text="Add",font=("Arial",20),command=add)
    b2=tkinter.Button(swindow,text="Close",font=("Arial",20),command=close)

    l1.grid(row=1,column=1)
    e1.grid(row=1,column=2)
    l2.grid(row=2,column=1)
    e2.grid(row=2,column=2)
    l3.grid(row=3,column=1)
    e3.grid(row=3,column=2)
    l4.grid(row=4,column=1)
    e4.grid(row=4,column=2)
    b1.grid(row=5,column=1)
    b2.grid(row=5,column=2)

