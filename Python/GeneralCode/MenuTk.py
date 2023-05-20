from tkinter import *

root = Tk()
root.title("Mi Menú")

menubar = Menu(root)
root.config(menu=menubar)  # Tenemos que guardarlo

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Save")
filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help me")
helpmenu.add_separator()
helpmenu.add_command(label="About me")



menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.mainloop()
