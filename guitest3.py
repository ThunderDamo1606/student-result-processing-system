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
    b1.place(x=50,y=50)
    b2.place(x=50,y=100 )
    b3.place(x=50,y=150 )
    b4.place(x=50,y=200)
    window.mainloop()
main()
