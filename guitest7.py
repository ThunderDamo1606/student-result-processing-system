import tkinter
import mysql.connector
import student
import tkinter.messagebox
def main():
    window=tkinter.Tk()
    window.title("Student Result Processing")
    window.geometry("400x400")
    window.config(bg="cyan")
    def admin():
        awindow=tkinter.Tk()
        awindow.title("Admin Operations")
        awindow.geometry("300x300")
        b1=tkinter.Button(awindow,text="Add Student",font=("Arial",20),command=student.student)
        b2=tkinter.Button(awindow,text="Add Marks",font=("Arial",20),command=student.marks)
        b1.grid(row=1,column=1)
        b2.grid(row=2,column=1)
        awindow.mainloop()
    def stud():
        swindow=tkinter.Tk()
        swindow.title("Result")
        swindow.geometry("200x200")
        l1=tkinter.Label(swindow,text="Rollno",font=("arial",20))
        e1=tkinter.Entry(swindow,width=10,font=("Arial",20))
        def find():
            cn=mysql.connector.connect(database="studentdb",user="root",password="root")
            c=cn.cursor()
            cmd="select * from marks where rollno=%s"
            c.execute(cmd,params=[int(e1.get())])
            row=c.fetchone()
            if row!=None:
                if row[1]>40 and row[2]>40 and row[3]>40:
                    tkinter.messagebox.showinfo("Result",f"{row[1]},{row[2]},{row[3]} Result is Pass")
                else:
                    tkinter.messagebox.showinfo("Result","Result is Fail")
            else:
                tkinter.messagebox.showinfo("info","invalid rollno")
                
            
        b1=tkinter.Button(swindow,text="Find",font=("Arial",20),command=find)
        l1.grid(row=1,column=1)
        e1.grid(row=1,column=2)
        b1.grid(row=2,column=1)
        swindow.mainloop()
        
        
    b1=tkinter.Button(window,text="Admin",font=("Arial",20),width=15,height=2,command=admin)
    b2=tkinter.Button(window,text="Student",font=("Arial",20),width=15,height=2,command=stud)
    b1.place(x=25,y=100)
    b2.place(x=25,y=200)
    
    window.mainloop()


main()
