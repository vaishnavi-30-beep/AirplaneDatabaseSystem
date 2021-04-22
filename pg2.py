from tkinter import *
import databaseConnection as dc

cur = dc.mydb.cursor()

root = Tk()
root.title("Model table")
root.geometry("1000x900")
root.configure(bg='white')

frame = Frame(root)
frame.configure(bg='white')
frame.pack()

table_name = Label(frame, text="Model Table", fg='brown', bg='white', padx=5, pady=5)
table_name.pack()
table_name.configure(font=("Helvetica", 16, "bold"))

model_label = Label(frame, text="Enter model number: ", bg='white', fg="red", padx=5, pady=5)
model_label.pack()

entry1 = Text(frame, height=1, width=20, padx=5, pady=5)
entry1.pack()
entry1.configure(font=("Helvetica", 16))


capacity_label = Label(frame, text="Enter capacity of the plane : ", bg='white', fg="red", padx=5, pady=5)
capacity_label.pack()

entry2 = Text(frame, height=1, width=20, padx=5, pady=5)
entry2.pack()
entry2.configure(font=("Helvetica", 16))

weight_label = Label(frame, text="Enter weight of the plane : ", bg='white', fg="red", padx=5, pady=5)
weight_label.pack()

entry3 = Text(frame, height=1, width=20, padx=5, pady=5)
entry3.pack()
entry3.configure(font=("Helvetica", 16))


class Model:

    def clear(self):
        entry1.delete('1.0', END)
        entry2.delete('1.0', END)
        entry3.delete('1.0',END)

    def insert(self):
        insert_query = """INSERT INTO model(model_no,capacity,weight) VALUES(%s, %s, %s)"""
        model_no = entry1.get(1.0, 'end-1c')
        capacity = entry2.get(1.0,'end-1c')
        weight = entry3.get(1.0,'end-1c')
        val = (model_no,capacity,weight)
        if model_no != "" and capacity != "" and weight != "":
            cur.execute(insert_query, val)
            dc.mydb.commit()

    def delete(self):
        delete_query = """DELETE FROM model WHERE model_no = %s"""
        model_no = entry1.get(1.0, 'end-1c')
        cur.execute(delete_query, (model_no))
        dc.mydb.commit()

    def display(self):
        cur.execute("SELECT *FROM model")
        Rows = cur.fetchall()
        for Row in Rows:
            print_label = Label(frame, text=Row, bg='white', fg="blue", padx=5, pady=5)
            print_label.pack()
            print_label.configure(font=("Helvetica", 16))
            print(Row)

    def update(self):
        model_no = entry1.get(1.0, 'end-1c')
        capacity = entry2.get(1.0,'end-1c')
        update_query = """update model set capacity = %s, weight = %s where model_no = %s"""
        val = (capacity,weight, model_no)
        cur.execute(update_query,val)
        dc.mydb.commit()


    def back(self):
        root.destroy()
        import UI

obj = Model()
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
blank = Label(frame, bg='white', padx=15, pady=15)
blank.pack()
root.mainloop()
