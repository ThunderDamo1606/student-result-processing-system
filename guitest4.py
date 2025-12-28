import tkinter
def main():
    window=tkinter.Tk()
    window.title("Button Example")
    window.geometry("300x300")
    def red():
        window.config(bg="red")
    def green():
        window.config(bg="green")
    def blue():
        window.config(bg="blue")
    def cyan():
        window.config(bg="cyan")
    b1=tkinter.Button(window,text="Red",command=red,width=10,height=2,bg="yellow",fg="red",font=("Arial",10))
    b2=tkinter.Button(window,text="Green",command=green,width=10,height=2,bg="yellow",fg="red")
    b3=tkinter.Button(window,text="Blue",command=blue,width=10,height=2,bg="yellow",fg="red")
    b4=tkinter.Button(window,text="Cyan",command=cyan,width=10,height=2,bg="yellow",fg="red")
    b1.grid(row=1,column=1)
    b2.grid(row=1,column=2 )
    b3.grid(row=1,column=3 )
    b4.grid(row=1,column=4)
    window.mainloop()
main()
