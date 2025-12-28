import tkinter 
def main():
    w=tkinter.Tk(className="Gui Application")
    w["bg"]="yellow" # changing background color
    w.geometry("400x400") # size of the window
    l1=tkinter.Label(w,text="This is Label",bg="pink",fg="cyan",font=("Arial",20))
    l1.place(x=50,y=50)
    l2=tkinter.Label(w,text="This is Label",font=("Arial",20))
    l2.pack() # layout
main()
