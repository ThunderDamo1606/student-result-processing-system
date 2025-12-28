import tkinter
def main():
    win=tkinter.Tk()
    win.title("Welcome")
    win.geometry("400x400")
    win.config(bg="cyan")
    l1=tkinter.Label(win,text="Banking Application",fg="Blue",bg="pink",font=("Arial",18))
    l1.place(x=100,y=10)
    win.mainloop()
main()
