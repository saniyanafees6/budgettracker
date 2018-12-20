from tkinter import*
import backend


def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
    except IndexError:
        pass

def clear_entry():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
    backend.view()
    t2.delete(1.0,END)
    t2.insert(END, round(backend.total_spent(),2))
    t1.delete(1.0,END)
    t1.insert(END, round(backend.ewvi()-backend.total_spent(),2))

def search_command():
    list1.delete(0,END)
    for row in backend.search(date_text.get(),store_text.get(),bill_text.get()):
        list1.insert(END,row)
    clear_entry()
    view_command()

def add_command():
    backend.insert(date_text.get(),store_text.get(),bill_text.get())
    list1.delete(0,END)
    list1.insert(END,(date_text.get(),store_text.get(),bill_text.get()))
    clear_entry()
    view_command()

def edit_command():
    backend.update(selected_tuple[0],date_text.get(),store_text.get(),bill_text.get())
    clear_entry()
    view_command()

def delete_command():
    t2.insert(END, backend.total_spent())
    backend.delete(selected_tuple[0])
    clear_entry()
    view_command()
    
def update_command():
    backend.dateup(esl_text.get())
    view_command()

def add_entry():
    e4.delete(0,END)
    e4.insert(END,backend.ewvi())



#------------------------------------------------------------------------------------------------------

root=Tk()
root.title("Budget Tracker")

Top=Frame(root, width = 1600, height = 50)
Top.pack(side=TOP)

Rt=Frame(root, width = 300, height = 700,)
Rt.pack(side=RIGHT)

Lt=Frame(root, width = 800, height = 700)
Lt.pack(side=LEFT)

#------------------------------------------------------------------------------------------------------

l1=Label(Top,text="Date [MM-DD-YYYY]: ").grid(row=0,column=0)

l2=Label(Top, text="Store: ").grid(row=0,column = 2)

l3=Label(Top, text="Bill Amount: $").grid(row=0,column=4)

date_text=StringVar()
e1=Entry(Top,textvariable=date_text)
e1.grid(row=0,column=1)

store_text=StringVar()
e2=Entry(Top,textvariable=store_text)
e2.grid(row=0,column=3)

bill_text = StringVar()
e3=Entry(Top,textvariable=bill_text)
e3.grid(row=0,column=5)

b1=Button(Top,text="Add",width=20,command=add_command)
b1.grid(row=1,column=0,columnspan=2)

b2=Button(Top, text="Edit",width=20, command=edit_command)
b2.grid(row=1,column=2,columnspan=2)

b3=Button(Top, text="Delete",width=20,command=delete_command)
b3.grid(row=1,column=4,columnspan=2)

#------------------------------------------------------------------------------------------------------

b4=Button(Rt, text="Show All", width = 40,command=view_command)
b4.grid(row=0,column=0, columnspan=2)

b5=Button(Rt, text="Search", width = 40, command=search_command)
b5.grid(row=1,column=0, columnspan=2)

b6=Button(Rt, text="Update Limit", width=40,command=update_command)
b6.grid(row=3,column=0, columnspan=2)

b7=Button(Rt, text="Quit", width=40,command=root.destroy)
b7.grid(row=4,column=0,columnspan=2)

esl_text=StringVar()
e4=Entry(Rt,textvariable=esl_text,width=40)
e4.grid(row=2,column=0,columnspan=2)

l5=Label(Rt,text="Remaining Balance $", pady=10).grid(row=5,column=0)



t1=Text(Rt, height=1, width=6, relief=RIDGE)
t1.grid(row=5, column=1)

#------------------------------------------------------------------------------------------------------

list1=Listbox(Lt, height=8,width=50)
list1.grid(row=0,column=0,columnspan=3)

# sb1=Scrollbar(Lt)
# sb1.grid(row=1,column=1)

# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

l4=Label(Lt,text="Total Spent $").grid(row=1,column=0)

t2=Text(Lt, height=1, width=10, relief=RIDGE)
# t2.insert(END, backend.total_spent())

t2.grid(row=1, column=1)

view_command()
add_entry()

#------------------------------------------------------------------------------------------------------

root.mainloop()