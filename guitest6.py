import tkinter
def main():
    window=tkinter.Tk()
    window.title("Calculator")
    window.geometry("300x300")
    l1=tkinter.Label(window,text="Number",font=("Arial",14))
    l2=tkinter.Label(window,text="Number",font=("Arial",14))
    l3=tkinter.Label(window,text="Result",font=("Arial",14))
    e1=tkinter.Entry(window,width=10,font=("Arial",14))
    e2=tkinter.Entry(window,width=10,font=("Arial",14))
    e3=tkinter.Entry(window,width=10,font=("Arial",14))
    def add():
        n1=int(e1.get())
        n2=int(e2.get())
        n3=n1+n2
        e3.delete(0,tkinter.END)
        e3.insert(0,str(n3))
    def sub():
        n1 = int(e1.get())
        n2 = int(e2.get())
        n3 = n1 - n2
        e3.delete(0, tkinter.END)
        e3.insert(0, str(n3))
    def multiply():
        n1 = int(e1.get())
        n2 = int(e2.get())
        n3 = n1 * n2
        e3.delete(0, tkinter.END)
        e3.insert(0, str(n3))
    def div():
        n1 = int(e1.get())
        n2 = int(e2.get())
        n3 = n1 / n2
        e3.delete(0, tkinter.END)
        e3.insert(0, str(n3))

    b1=tkinter.Button(window,text="Add",font=("Arial",14),command=add)
    b2=tkinter.Button(window, text="Sub", font=("Arial", 14),command=sub)
    b3=tkinter.Button(window, text="Multiply", font=("Arial", 14),command=multiply)
    b4=tkinter.Button(window, text="Division", font=("Arial", 14),command=div)
    l1.grid(row=0,column=0)
    l2.grid(row=1,column=0)
    l3.grid(row=2,column=0)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    b1.grid(row=3,column=0)
    b2.grid(row=3,column=1)
    b3.grid(row=4,column=0)
    b4.grid(row=4,column=1)

    window.mainloop()
main()
