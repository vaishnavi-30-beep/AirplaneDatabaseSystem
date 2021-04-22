from tkinter import *
import databaseConnection as dc

cur = dc.mydb.cursor()

root = Tk()
root.geometry("1000x900")
root.configure(bg='white')

frame = Frame(root)
frame.configure(bg='white')
frame.pack()

table_name = Label(frame, text="Traffic Controller Table", fg='brown', bg='white', padx=5, pady=5)
table_name.pack()
table_name.configure(font=("Helvetica", 16, "bold"))

date_label = Label(frame, text="Enter Date Of Exam: ", bg='white', fg="red", padx=5, pady=5)
date_label.pack()

entry1 = Text(frame, height=1, width=20, padx=5, pady=5)
entry1.pack()
entry1.configure(font=("Helvetica", 16))

faa_label = Label(frame, text="Enter FAA number: ", bg='white', fg="red", padx=5, pady=5)
faa_label.pack()

entry2 = Text(frame, height=1, width=20, padx=5, pady=5)
entry2.pack()
entry2.configure(font=("Helvetica", 16))

reg_label = Label(frame, text="Enter Registration number Of Airplane: ", bg='white', fg="red", padx=5, pady=5)
reg_label.pack()

entry3 = Text(frame, height=1, width=20, padx=5, pady=5)
entry3.pack()
entry3.configure(font=("Helvetica", 16))

mem_label = Label(frame, text="Enter Membership number: ", bg='white', fg="red", padx=5, pady=5)
mem_label.pack()

entry4 = Text(frame, height=1, width=20, padx=5, pady=5)
entry4.pack()
entry4.configure(font=("Helvetica", 16))

class TrafficController:

    def clear(self):
        entry1.delete('1.0', END)
        entry2.delete('1.0', END)

    def insert(self):
        insert_query = """INSERT INTO Traffic_Controller(date_of_exam, faa_no, reg_no, mem_no) VALUES(%s, %s, %s, %s)"""
        date_of_exam = entry1.get(1.0, 'end-1c')
        faa_no = entry2.get(1.0, 'end-1c')
        reg_no = entry3.get(1.0, 'end-1c')
        mem_no = entry4.get(1.0, 'end-1c')
        val = (date_of_exam, faa_no, reg_no, mem_no)
        if date_of_exam != "" and reg_no != "" and mem_no != "" and faa_no != "":
            cur.execute(insert_query, val)
            dc.mydb.commit()

    def delete(self):
        delete_query = """DELETE FROM Traffic_Controller WHERE mem_no = %s"""
        mem_no = entry1.get(1.0, 'end-1c')
        cur.execute(delete_query, (mem_no,))
        dc.mydb.commit()

    def display(self):
        cur.execute("SELECT *FROM Traffic_Controller")
        Rows = cur.fetchall()
        for Row in Rows:
            print_label = Label(frame, text=Row, bg='white', fg="blue", padx=5, pady=5)
            print_label.pack()
            print_label.configure(font=("Helvetica", 16))
            print(Row)

    def update(self):
        update_query = """update Traffic_Controller set date_of_exam = %s, faa_no= %s, reg_no = %s where mem_no = %s"""
        date_of_exam = entry1.get(1.0, 'end-1c')
        faa_no = entry2.get(1.0, 'end-1c')
        reg_no = entry3.get(1.0, 'end-1c')
        mem_no = entry4.get(1.0, 'end-1c')

        val = (date_of_exam, faa_no, reg_no, mem_no)
        cur.execute(update_query, val)
        dc.mydb.commit()


    def back(self):
        root.destroy()
        import UI

obj = TrafficController()
blank = Label(frame, bg='white', padx=15, pady=15)
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
blank = Label(frame, bg='white', padx=15, pady=15)
blank.pack()
root.mainloop()

