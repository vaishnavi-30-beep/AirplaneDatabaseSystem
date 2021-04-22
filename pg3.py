from tkinter import *
import databaseConnection as dc

cur = dc.mydb.cursor()

root = Tk()
root.geometry("1000x900")
root.configure(bg='white')

frame = Frame(root)
frame.configure(bg='white')
frame.pack()

table_name = Label(frame, text="Employee", fg='brown', bg='white', padx=5, pady=5)
table_name.pack()
table_name.configure(font=("Helvetica", 16, "bold"))

memNo_label = Label(frame, text="Enter Membership number: ", bg='white', fg="red", padx=5, pady=5)
memNo_label.pack()

entry1 = Text(frame, height=1, width=20, padx=5, pady=5)
entry1.pack()
entry1.configure(font=("Helvetica", 16))

salary_label = Label(frame, text="Enter Salary: ", bg='white', fg="red", padx=5, pady=5)
salary_label.pack()

entry2 = Text(frame, height=1, width=20, padx=5, pady=5)
entry2.pack()
entry2.configure(font=("Helvetica", 16))

phoneNo_label = Label(frame, text="Enter Phone number: ", bg='white', fg="red", padx=5, pady=5)
phoneNo_label.pack()

entry3 = Text(frame, height=1, width=20, padx=5, pady=5)
entry3.pack()
entry3.configure(font=("Helvetica", 16))

addr_label = Label(frame, text="Enter Address: ", bg='white', fg="red", padx=5, pady=5)
addr_label.pack()

entry4 = Text(frame, height=1, width=20, padx=5, pady=5)
entry4.pack()
entry4.configure(font=("Helvetica", 16))

fName_label = Label(frame, text="Enter First Name: ", bg='white', fg="red", padx=5, pady=5)
fName_label.pack()

entry5 = Text(frame, height=1, width=20, padx=5, pady=5)
entry5.pack()
entry5.configure(font=("Helvetica", 16))

lName_label = Label(frame, text="Enter Last Name: ", bg='white', fg="red", padx=5, pady=5)
lName_label.pack()

entry6 = Text(frame, height=1, width=20, padx=5, pady=5)
entry6.pack()
entry6.configure(font=("Helvetica", 16))

faaNo_label = Label(frame, text="Enter FAA number: ", bg='white', fg="red", padx=5, pady=5)
faaNo_label.pack()

entry7 = Text(frame, height=1, width=20, padx=5, pady=5)
entry7.pack()
entry7.configure(font=("Helvetica", 16))


class Employee:

    def clear(self):
        entry1.delete('1.0', END)
        entry2.delete('1.0', END)

    def insert(self):
        insert_query = """INSERT INTO Employee(Membership_no, Salary, Phone_no, Address, first_name, last_name, 
        faa_no) VALUES( %s, %s, %s, %s, %s, %s, %s) """
        mem_no = entry1.get(1.0, 'end-1c')
        salary = entry2.get(1.0, 'end-1c')
        phNo = entry3.get(1.0, 'end-1c')
        addr = entry4.get(1.0, 'end-1c')
        fName = entry5.get(1.0, 'end-1c')
        lName = entry6.get(1.0, 'end-1c')
        faaNo = entry7.get(1.0, 'end-1c')

        val = (mem_no, salary, phNo, addr, fName, lName, faaNo)
        if mem_no != "" and salary != "" and phNo != "" and addr != "" and fName != "" and lName != "" and faaNo != "":
            cur.execute(insert_query, val)
            dc.mydb.commit()

    def delete(self):
        delete_query = """DELETE FROM Employee WHERE Membership_no = %s"""
        mem_no = entry1.get(1.0, 'end-1c')
        cur.execute(delete_query, (mem_no,))
        dc.mydb.commit()
        # messagebox.showinfo("Information", "Data Deleted")

    def display(self):
        pass

    def update(self):
        update_query = """update Employee set salary = %s, Phone_no = %s, Address = %s, first_name = %s, last_name = 
        %s, faa_no = %s where Membership_no = %s """
        mem_no = entry1.get(1.0, 'end-1c')
        salary = entry2.get(1.0, 'end-1c')
        phNo = entry3.get(1.0, 'end-1c')
        addr = entry4.get(1.0, 'end-1c')
        fName = entry5.get(1.0, 'end-1c')
        lName = entry6.get(1.0, 'end-1c')
        faaNo = entry7.get(1.0, 'end-1c')

        val = (salary, phNo, addr, fName, lName, faaNo, mem_no)
        if mem_no != "" and salary != "" and phNo != "" and addr != "" and fName != "" and lName != "" and faaNo != "":
            cur.execute(update_query, val)
            dc.mydb.commit()

    def back(self):
        root.destroy()
        import UI


obj = Employee()
blank = Label(frame,bg='white', padx=15, pady=15)
blank.pack()
b1 = Button(frame, height=2, width=10, text='Insert', command=obj.insert, bg='black', fg='white',
            padx=5, pady=5)
b1.pack(side=LEFT)
b2 = Button(frame, text='Delete', height=2, width=10, command=obj.delete, bg='black', fg='white', padx=5, pady=5)
b2.pack(side=LEFT)
b3 = Button(frame, text='Display', height=2, width=10, command=obj.display, bg='black', fg='white', padx=5, pady=5)
b3.pack(side=LEFT)
b4 = Button(frame, text='Update', height=2, width=10, command=obj.update, bg='black', fg='white', padx=5, pady=5)
b4.pack(side=LEFT)
b5 = Button(frame, text='Clear', height=2, width=10, command=obj.clear, bg='black', fg='white', padx=5, pady=5)
b5.pack(side=LEFT)
back = Button(frame, text='Back', height=2, width=10, command=obj.back, bg='black', fg='white', padx=5, pady=5)
back.pack(side=LEFT)