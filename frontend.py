"""
Store Name, Date, Amount

User can:
View All Records
Search a specific record
add 
edit
delete
set spending limit
see remaining limit
quit
"""

from tkinter import *


window=Tk()

lstore=Label(window,text="Store")
lstore.grid(row=0,column=0)

ldate=Label(window, text="Date(mm/dd/yy)")
ldate.grid(row=0,column=2)

lamount=Label(window,text="Amount ($)")
lamount.grid(row=0,column=4)

store=StringVar()
estore = Entry(window,textvariable=store)
estore.grid(row=0,column=1)

dates=StringVar()
edate = Entry(window,textvariable=dates)
edate.grid(row=0,column=3)

amount=StringVar()
eamount = Entry(window,textvariable=amount)
eamount.grid(row=0,column=5)


window.mainloop()