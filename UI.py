from tkinter import *

root = Tk(className="Airline Management")
root.geometry("1000x500")
root.configure(bg='white')
root.title("Airline Management System")
frame = Frame(root)
frame.configure(bg='white')
frame.pack()
blank = Label(frame, bg='white', padx=1, pady=1)
blank.pack()
title = Label(frame, text="Welcome To Airline Database Management System", bg='white', fg="brown", padx=1, pady=1)
title.pack()
title.configure(font=("Helvetica", 18, "bold"))


def pg1():
    root.destroy()
    import pages.pg1


def pg2():
    root.destroy()
    import pages.pg2


def pg3():
    root.destroy()
    import pages.pg3


def pg4():
    root.destroy()
    import pages.pg4


def pg5():
    root.destroy()
    import pages.pg5


def pg6():
    root.destroy()
    import pages.pg6


blank = Label(frame, bg='white', padx=1, pady=1)
blank.pack()
b1 = Button(frame, height=2, width=25, text='Airplane', command=pg1, bg='black', fg='white', padx=5, pady=5)
b1.pack()
blank = Label(frame, bg='white', padx=1, pady=1)
blank.pack()
b2 = Button(frame, height=2, width=25, text='Model', command=pg2, bg='black', fg='white', padx=5, pady=5)
b2.pack()
blank = Label(frame, bg='white', padx=1, pady=1)
blank.pack()
b3 = Button(frame, height=2, width=25, text='Employee', command=pg3, bg='black', fg='white', padx=5, pady=5)
b3.pack()
blank = Label(frame, bg='white', padx=1, pady=1)
blank.pack()
b4 = Button(frame, height=2, width=25, text='Technician', command=pg4, bg='black', fg='white', padx=5, pady=5)
b4.pack()
blank = Label(frame, bg='white', padx=1, pady=1)
blank.pack()
b5 = Button(frame, height=2, width=25, text='Traffic Controller', command=pg5, bg='black', fg='white', padx=5, pady=5)
b5.pack()
blank = Label(frame, bg='white', padx=1, pady=1)
blank.pack()
b6 = Button(frame, height=2, width=25, text='Test', command=pg6, bg='black', fg='white', padx=5, pady=5)
b6.pack()

root.mainloop()
