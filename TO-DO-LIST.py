from tkinter import *
from tkinter import messagebox
def addTask():
    task = my_entry.get()
    if task != "":
        listbox.insert(END,task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning","Please enter some task.")
def deleteTask():
    listbox.delete(ANCHOR)
root = Tk()
root.geometry("600x400+500+500")
root.config(bg="grey")
root.title("TO-DO-LIST")
root.resizable(width=False,height=False)
frame=Frame(root)
frame.pack(pady=10)
listbox = Listbox(frame,width=35,height=8,font="Times 18 bold",bd=0,foreground="red",selectbackground='#a6a6a6',activestyle="none")
listbox.pack(side = LEFT, fill = BOTH)
task_list=[]
for items in task_list:
    listbox.insert(END, items)
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)
my_entry=Entry(root,font="times 14 bold")
my_entry.pack(pady = 20)
my_entry.pack(pady=20)
button_frame=Frame(root)
button_frame.pack(pady=20)

addTask_btn = Button(button_frame,text="Add Task",font="times 14 bold",bg="#c5f776",padx=20,pady=10,command=addTask)
addTask_btn.pack(fill=BOTH,expand=True,side=LEFT)
delTask_btn= Button(button_frame,text="Delete Task",font="times 14 bold",bg='#ff8b61',padx=20,pady=10,command=deleteTask)
delTask_btn.pack(fill=BOTH,expand=True,side=LEFT)









root.mainloop()