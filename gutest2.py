import tkinter
def main():
    window=tkinter.Tk()
    window.title("Button Example")
    window.geometry("300x200")
    def red():
        window.config(bg="red")
    def green():
        window.config(bg="green")
    def blue():
        window.config(bg="blue")
    def cyan():
        window.config(bg="cyan")
    b1=tkinter.Button(window,text="Red",command=red)
    b2=tkinter.Button(window,text="Green",command=green)
    b3=tkinter.Button(window,text="Blue",command=blue)
    b4=tkinter.Button(window,text="Cyan",command=cyan)
    b1.pack(side=tkinter.LEFT)
    b2.pack(side=tkinter.RIGHT)
    b3.pack(side=tkinter.TOP)
    b4.pack(side=tkinter.BOTTOM)
    window.mainloop()
main()
